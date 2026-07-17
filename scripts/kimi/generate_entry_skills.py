#!/usr/bin/env python3
"""生成 KIMI 领域入口技能（.agents/skills/legal-*/SKILL.md）。

每个入口技能是 KIMI 原生技能（name + description），正文包含：
1. 画像读取门禁（legal-profile/）
2. 工作流路由表（由各领域 skills/*/SKILL.md 的 frontmatter 描述自动生成）
3. KIMI 平台输出规则（检索插件、来源标注、律师审查门槛）

幂等：重跑会覆盖生成文件。上游同步后先跑 transform.py 再跑本脚本。
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".agents" / "skills"

DOMAINS = {
    "commercial-legal": {
        "skill": "legal-commercial", "display": "商事合同",
        "triggers": "合同审查、NDA、保密协议、供应商协议、SaaS/MSA、续约、合同利益方摘要、合同风险上报、商事法务",
    },
    "corporate-legal": {
        "skill": "legal-corporate", "display": "公司与并购",
        "triggers": "并购尽调、重大合同披露、董事会/股东会决议、交割清单、公司合规、投后整合、公司法",
    },
    "employment-legal": {
        "skill": "legal-employment", "display": "劳动用工",
        "triggers": "劳动合同解除、劳动关系认定、假期管理、员工调查、规章制度、工资工时、跨省用工、劳动法",
    },
    "privacy-legal": {
        "skill": "legal-privacy", "display": "数据合规与隐私",
        "triggers": "个人信息保护影响评估、PIA、PIPL、数据处理协议、DSAR、隐私政策、数据合规差距、数据出境和隐私合规",
    },
    "product-legal": {
        "skill": "legal-product", "display": "产品与营销合规",
        "triggers": "产品上线审查、营销文案审查、广告法、反不正当竞争、功能法律风险、业务法务快速咨询",
    },
    "regulatory-legal": {
        "skill": "legal-regulatory", "display": "监管合规",
        "triggers": "法规动态监控、监管简报、政策差异比对、合规差距、征求意见稿、监管政策重写、行政监管",
    },
    "ai-governance-legal": {
        "skill": "legal-ai-governance", "display": "AI 治理",
        "triggers": "AI 应用登记、算法安全评估、科技伦理审查、生成式 AI 合规、AI 供应商审查、AI 治理",
    },
    "ip-legal": {
        "skill": "legal-ip", "display": "知识产权",
        "triggers": "商标可注册性、FTO、侵权警告函、通知删除、开源许可证、知识产权条款、专利、著作权、商标",
    },
    "litigation-legal": {
        "skill": "legal-litigation", "display": "诉讼仲裁",
        "triggers": "案件登记、诉讼仲裁、律师函、要件分析、大事记、证据三性、庭前准备、保全、调查令、法律文书",
    },
    "legal-clinic": {
        "skill": "legal-clinic", "display": "法律诊所",
        "triggers": "法律诊所、学生案件接待、诊所备忘录、研究路线、结案移交、指导老师审阅、当事人沟通",
    },
    "law-student": {
        "skill": "legal-law-student", "display": "法学学习与法考",
        "triggers": "法考、案例摘要、IRAC、课堂提问、法学写作、记忆卡片、学习计划、主观题和客观题训练",
    },
}

BODY_TEMPLATE = """# {display}（KIMI 版）

中国法{display}工作流入口。本技能是路由层：实际工作流定义在 `{domain}/skills/` 下的各文件中，按需加载，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 读取共享公司画像 `legal-profile/company-profile.md` 和本领域画像 `legal-profile/{domain}.md`。
2. 如果任一文件不存在、或仍含 `[PLACEHOLDER]` 标记：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经用户同意后加载 `{domain}/skills/cold-start-interview/SKILL.md` 并执行。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 本领域共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `{domain}/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，加载对应文件并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动加载。

{table}

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件（yuandian_law）；企业征信查询使用天眼查插件（tianyancha）；北大法宝、威科先行等可通过 WebBridge 操作网页版。
- 通过检索插件获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；完全没有可用检索工具时，在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。
- 知识库交叉引用协议（如用户配置了本地知识库）：见 `references/knowledge-base-crossref.md`。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。
"""


def parse_skill(path: Path) -> tuple[str, str] | None:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    fm = m.group(1)
    desc_m = re.search(r"description:\s*>?\s*\n?(.*?)(?=\n[a-z-]+:|$)", fm, re.DOTALL)
    if not desc_m:
        return None
    desc = " ".join(desc_m.group(1).split())
    if "已弃用" in desc[:60]:
        return None
    return path.parent.name, desc


def intent_of(name: str, desc: str) -> str:
    d = desc
    for prefix in ("参考：", "Reference:", "参考资料："):
        if d.startswith(prefix):
            d = d[len(prefix):].strip()
            break
    cut = re.split(r"[。；]| 当| 在| 用于| 适用", d, maxsplit=1)
    intent = cut[0].strip(" ，,。：:")
    return intent[:48] + ("…" if len(intent) > 48 else "")


def is_reference(name: str, desc: str) -> bool:
    return desc.startswith(("参考", "Reference"))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for domain, meta in DOMAINS.items():
        skills_dir = ROOT / domain / "skills"
        rows, refs = [], []
        for sk in sorted(skills_dir.glob("*/SKILL.md")):
            parsed = parse_skill(sk)
            if not parsed:
                continue
            name, desc = parsed
            rel = f"{domain}/skills/{name}/SKILL.md"
            if name == "cold-start-interview":
                rows.append(("**首次使用：冷启动访谈（配置画像）**", rel))
                continue
            intent = intent_of(name, desc)
            if is_reference(name, desc):
                refs.append((f"{intent}（参考）", rel))
            else:
                rows.append((intent, rel))
        rows.extend(refs)
        table = "| 用户意图 | 加载文件 |\n|---|---|\n" + "\n".join(
            f"| {intent} | `{rel}` |" for intent, rel in rows
        )
        body = BODY_TEMPLATE.format(
            display=meta["display"], domain=domain, table=table)
        desc = (f"中国法{meta['display']}法律工作入口。{meta['triggers']}。"
                f"当用户提出{meta['display']}相关任务时使用本技能，"
                f"它将路由到 claude-for-legal-ZH（KIMI 版）仓库中对应的专业工作流文件。")
        out_dir = OUT / meta["skill"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "SKILL.md").write_text(
            f"---\nname: {meta['skill']}\ndescription: {desc}\n---\n\n{body}",
            encoding="utf-8",
        )
        print(f"wrote .agents/skills/{meta['skill']}/SKILL.md ({len(rows)} workflows)")


if __name__ == "__main__":
    main()

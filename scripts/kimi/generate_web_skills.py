#!/usr/bin/env python3
"""生成网页版 KIMI 技能文件（install/web-skills/legal-*.md）。

网页版 KIMI 无本地文件系统，但可以通过工具抓取 raw.githubusercontent.com 链接。
因此网页版技能 = 自包含 prompt：画像读写改为 KIMI 记忆，路由表改为 raw URL，
并要求把工作流文件中的相对路径引用一律解析为 raw URL 前缀。

输出文件供 skill-creator 读取后创建自定义技能。
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "install" / "web-skills"

# 仓库改名或换默认分支时，改这里并重跑
RAW_BASE = "https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main"
# Gitee 镜像（国内访问兜底），目录浏览用 Gitee tree 页面
GITEE_RAW_BASE = "https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main"
GITEE_TREE = "https://gitee.com/shoushou1106/kimi-for-legal-ZH/tree/main"

DOMAINS = {
    "commercial-legal": ("legal-commercial", "商事合同",
        "合同审查、NDA、保密协议、供应商协议、SaaS/MSA、续约、合同利益方摘要、合同风险上报、商事法务"),
    "corporate-legal": ("legal-corporate", "公司与并购",
        "并购尽调、重大合同披露、董事会/股东会决议、交割清单、公司合规、投后整合、公司法"),
    "employment-legal": ("legal-employment", "劳动用工",
        "劳动合同解除、劳动关系认定、假期管理、员工调查、规章制度、工资工时、跨省用工、劳动法"),
    "privacy-legal": ("legal-privacy", "数据合规与隐私",
        "个人信息保护影响评估、PIA、PIPL、数据处理协议、DSAR、隐私政策、数据合规差距、数据出境"),
    "product-legal": ("legal-product", "产品与营销合规",
        "产品上线审查、营销文案审查、广告法、反不正当竞争、功能法律风险、业务法务快速咨询"),
    "regulatory-legal": ("legal-regulatory", "监管合规",
        "法规动态监控、监管简报、政策差异比对、合规差距、征求意见稿、行政监管"),
    "ai-governance-legal": ("legal-ai-governance", "AI 治理",
        "AI 应用登记、算法安全评估、科技伦理审查、生成式 AI 合规、AI 供应商审查"),
    "ip-legal": ("legal-ip", "知识产权",
        "商标可注册性、FTO、侵权警告函、通知删除、开源许可证、知识产权条款、专利、著作权、商标"),
    "litigation-legal": ("legal-litigation", "诉讼仲裁",
        "案件登记、诉讼仲裁、律师函、要件分析、大事记、证据三性、庭前准备、保全、法律文书"),
    "legal-clinic": ("legal-clinic", "法律诊所",
        "法律诊所、学生案件接待、诊所备忘录、研究路线、结案移交、指导老师审阅、当事人沟通"),
    "law-student": ("legal-law-student", "法学学习与法考",
        "法考、案例摘要、IRAC、课堂提问、法学写作、记忆卡片、学习计划、主观题和客观题训练"),
}

TEMPLATE = """# KIMI 自定义技能定义：{skill}

> 本文件是一个 KIMI 自定义技能的完整定义，供 skill-creator 读取后创建技能。
> 技能名称：{skill}
> 技能说明（触发描述）：中国法{display}法律工作入口。{triggers}。当用户提出{display}相关任务时使用。

---

# {display}（KIMI 网页版）

中国法{display}工作流入口。本技能是路由层：实际工作流定义在 GitHub 仓库的 `{domain}/skills/` 目录下，按需读取，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 从 KIMI 记忆中读取你的画像：共享公司画像（company-profile）和本领域画像（{domain}）。
2. 如果记忆中没有画像或画像仍是占位符：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经同意后读取 `{RAW_BASE}/{domain}/skills/cold-start-interview/SKILL.md` 并执行；访谈结束后将画像全文写入 KIMI 记忆，**每条记忆以「kimi-for-legal-ZH 法律画像」开头标注来源，并注明仅在法律工作任务中适用**（KIMI 的记忆在所有会话中始终生效，标注是防止法律画像渗入无关对话）。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `{RAW_BASE}/{domain}/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，读取对应 URL 并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动读取。

{table}

## 相对路径解析规则

工作流文件中引用的所有相对路径（如 `{domain}/references/contract-law-core.md`、`references/knowledge-base-crossref.md`），一律加上前缀 `{RAW_BASE}/` 后作为 URL 读取。如果该地址无法访问（网络原因），改用 Gitee 镜像前缀 `{GITEE_RAW_BASE}/`。需要读取目录清单时，改用 GitHub 页面 `https://github.com/shoushou1106/kimi-for-legal-ZH/tree/main/<目录>` 或 Gitee 页面 `{GITEE_TREE}/<目录>` 查看文件列表。

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件；企业征信查询使用天眼查插件；其他数据库可通过 WebBridge 或联网搜索。
- 通过检索获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；无法检索时在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。
"""


def parse_skill(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    desc_m = re.search(r"description:\s*>?\s*\n?(.*?)(?=\n[a-z-]+:|$)", m.group(1), re.DOTALL)
    if not desc_m:
        return None
    desc = " ".join(desc_m.group(1).split())
    if "已弃用" in desc[:60]:
        return None
    return path.parent.name, desc


def intent_of(desc: str) -> str:
    d = desc
    for prefix in ("参考：", "Reference:", "参考资料："):
        if d.startswith(prefix):
            d = d[len(prefix):].strip()
            break
    intent = re.split(r"[。；]| 当| 在| 用于| 适用", d, maxsplit=1)[0].strip(" ，,。：:")
    return intent[:48] + ("…" if len(intent) > 48 else "")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for domain, (skill, display, triggers) in DOMAINS.items():
        rows, refs = [], []
        for sk in sorted((ROOT / domain / "skills").glob("*/SKILL.md")):
            parsed = parse_skill(sk)
            if not parsed:
                continue
            name, desc = parsed
            url = f"{RAW_BASE}/{domain}/skills/{name}/SKILL.md"
            if name == "cold-start-interview":
                rows.append(("**首次使用：冷启动访谈（配置画像）**", url))
                continue
            intent = intent_of(desc)
            (refs if desc.startswith(("参考", "Reference")) else rows).append(
                (intent + ("（参考）" if desc.startswith(("参考", "Reference")) else ""), url))
        rows.extend(refs)
        table = "| 用户意图 | 读取 URL |\n|---|---|\n" + "\n".join(
            f"| {i} | {u} |" for i, u in rows)
        (OUT / f"{skill}.md").write_text(
            TEMPLATE.format(skill=skill, display=display, triggers=triggers,
                            domain=domain, table=table, RAW_BASE=RAW_BASE,
                            GITEE_RAW_BASE=GITEE_RAW_BASE, GITEE_TREE=GITEE_TREE),
            encoding="utf-8")
        print(f"wrote install/web-skills/{skill}.md ({len(rows)} workflows)")


if __name__ == "__main__":
    main()

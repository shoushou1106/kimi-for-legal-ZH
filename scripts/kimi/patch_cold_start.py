#!/usr/bin/env python3
"""cold-start-interview 专项改写（KIMI 版）。

对 11 个领域的 cold-start-interview/SKILL.md：
1. 删除"项目范围安装检查"段落（Claude Code 专属概念，KIMI 无对应物）
2. 修复"不是你的领域？"引导语（原指向已删除的 builder-hub）
3. 统一缓存迁移说明为"从 Claude Code 版本迁移画像"
4. CLAUDE.md 残留指称 → 画像文件
5. 文末追加"写入 KIMI 记忆"步骤（KIMI 版新增）
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

MIGRATION_LINE = (
    "**迁移：** 如果用户之前安装过 Claude Code 版本"
    "（画像位于 `~/.claude/plugins/config/claude-for-legal-zh/`），"
    "将对应画像复制到 `legal-profile/` 下并保持原文件名，向用户展示迁移内容；否则跳过。"
)

REDIRECT = "不是你关注的领域？直接使用对应领域的入口技能即可（见仓库 `.agents/skills/` 目录）。"
REDIRECT_RE = re.compile(r"不是[你您]的?关?注?的?领域？[ `]*（该功能属于 Claude 技能市场生态，KIMI 版本已移除）`?。")

MEMORY_STEP = """

---

## 追加步骤：写入 KIMI 记忆（KIMI 版新增）

访谈完成、画像写入 `legal-profile/{domain}.md` 后：

1. 将画像**要点摘要**写入 KIMI 长期记忆，**每条记忆必须以「kimi-for-legal-ZH 法律画像」开头，标注来源与适用范围**。例如：「kimi-for-legal-ZH 法律画像（{domain}）：用户为企业法务，采购方立场，风险偏好中等……仅在处理法律工作任务时适用」。摘要内容包括：执业场景、使用者角色、所在领域、风险偏好、升级阈值，以及画像文件位置 `legal-profile/{domain}.md`。
2. KIMI 的记忆在所有会话中始终生效——标注"仅在法律工作任务中适用"是为了防止法律画像渗入无关对话（日常聊天、非法律工作）。
3. 详细审查指引以画像文件为唯一真实来源；记忆中只放摘要和文件指针，避免两处不一致。
4. 如果用户使用**网页版 KIMI**（无工作区文件系统），则将画像全文写入 KIMI 记忆（同样以「kimi-for-legal-ZH 法律画像」开头标注），并在后续法律会话开始时主动读取。
"""


def patch_paragraphs(text: str) -> str:
    """删除 Claude Code 安装范围检查的残留段落（连续非空行视为一个段落）。"""
    blocks = re.split(r"(\n\s*\n)", text)
    drop_markers = ["项目范围", "安装范围检查", "项目内部（非用户主目录）", "项目内部（而非用户主目录）"]
    out = []
    for block in blocks:
        if block.strip() and any(m in block for m in drop_markers):
            continue
        out.append(block)
    return "".join(out)


def patch_file(path: Path, domain: str) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    # 1. 删除项目范围检查段落
    text = patch_paragraphs(text)

    # 2. 修复领域引导语
    text = REDIRECT_RE.sub(REDIRECT, text)

    # 3. 统一缓存迁移行
    lines = []
    for ln in text.splitlines():
        if "缓存" in ln and ln.strip():
            m = re.match(r"^(\s*(?:\d+\.\s*)?[-*]?\s*)", ln)
            lines.append((m.group(1) if m else "") + MIGRATION_LINE)
        else:
            lines.append(ln)
    text = "\n".join(lines)

    # 4. CLAUDE.md 残留指称
    text = text.replace("${CLAUDE_PLUGIN_ROOT}/CLAUDE.md",
                        f"{domain}/profile-template.md")
    text = re.sub(r"(?<![\w/.-])CLAUDE\.md", "画像文件", text)

    # 5. 追加 KIMI 记忆步骤（幂等）
    if "## 追加步骤：写入 KIMI 记忆" not in text:
        text = text.rstrip() + "\n" + MEMORY_STEP.format(domain=domain)

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for sk in sorted(ROOT.glob("*/skills/cold-start-interview/SKILL.md")):
        domain = sk.relative_to(ROOT).parts[0]
        if patch_file(sk, domain):
            changed += 1
            print(f"patched {domain}")
    print(f"total patched: {changed}")

    # 残留检查
    for pat in ["项目范围", "缓存路径", r"\$\{CLAUDE_PLUGIN_ROOT\}"]:
        hits = []
        for sk in sorted(ROOT.glob("*/skills/cold-start-interview/SKILL.md")):
            for i, ln in enumerate(sk.read_text(encoding="utf-8").splitlines(), 1):
                if re.search(pat, ln):
                    hits.append(f"{sk}:{i}")
        print(f"LEFTOVER {pat}: {len(hits)}")
        for h in hits[:6]:
            print(f"  {h}")


if __name__ == "__main__":
    main()

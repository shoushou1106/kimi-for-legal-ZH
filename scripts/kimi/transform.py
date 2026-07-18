#!/usr/bin/env python3
"""KIMI 适配批量转换脚本 —— claude-for-legal-ZH → kimi-for-legal-ZH

在 kimi-adaptation 分支上原地转换：
1. 画像路径：~/.claude/plugins/config/... → legal-profile/...
2. 斜杠命令：/<plugin>:<skill> → 「<skill>」工作流（加载 <plugin>/skills/<skill>/SKILL.md）
3. frontmatter 清洗：删除 argument-hint / user-invocable 行
4. 连接器表述：MCP/连接器 → KIMI 插件表述
5. profile-template.md 头部注释块重写为 KIMI 版本

幂等：重复运行不会产生叠加替换。
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

PLUGINS = [
    "ai-governance-legal", "commercial-legal", "corporate-legal",
    "employment-legal", "ip-legal", "law-student", "legal-clinic",
    "litigation-legal", "privacy-legal", "product-legal", "regulatory-legal",
]

CMD_RE = re.compile(
    r"/(ai-governance-legal|commercial-legal|corporate-legal|employment-legal"
    r"|ip-legal|law-student|legal-clinic|litigation-legal|privacy-legal"
    r"|product-legal|regulatory-legal):([a-z0-9-]+)"
)
HUB_CMD_RE = re.compile(r"/legal-builder-hub:([a-z0-9-]+)")

# 顺序敏感：长的、具体的模式放前面
TEXT_REPLACEMENTS = [
    # 画像路径（具体优先）
    ("~/.claude/plugins/config/claude-for-legal-zh/company-profile.md",
     "legal-profile/company-profile.md"),
    *[(f"~/.claude/plugins/config/claude-for-legal-zh/{p}/CLAUDE.md",
       f"legal-profile/{p}.md") for p in PLUGINS],
    # 连接器与检索工具表述
    ("元典 yuandian MCP", "元典法律数据库"),
    ("元典MCP或官方网站", "元典法律数据库或官方网站"),
    ("元典MCP", "元典检索"),
    ("yuandian MCP", "元典检索"),
    ("yuandian（元典）MCP", "元典法律数据库"),
    ("（元典）MCP", "法律数据库"),
    ("企业信用信息 MCP 连接器", "企业信用查询插件（如天眼查）"),
    ("法律研究连接器", "法律检索插件"),
    ("研究连接器", "检索插件"),
    ("MCP 服务器", "KIMI 插件"),
    ("MCP 服务", "KIMI 插件"),
    ("MCP 连接器", "插件"),
    ("MCP连接器", "插件"),
    ("测试MCP连接", "检查检索插件是否可用"),
    ("MCP 连接", "插件连接"),
    ("MCP", "插件"),  # 兜底，放在最后
    ("[CNIPA]`或法律研究连接器的插件工具名", "[CNIPA]`或检索插件的工具名"),
]

HEADER_RE = re.compile(r"\A<!--.*?-->", re.DOTALL)

HEADER_TEMPLATE = """<!--
KIMI 版本画像说明

本领域用户的实务画像保存在工作区的 legal-profile/ 目录：

  legal-profile/{plugin}.md

规则：
1. 本领域所有技能从上述路径读取画像，而不是从本文件。
2. 如果该文件不存在或仍包含 [PLACEHOLDER] 标记，在进行实质工作前停下，
   引导用户先运行冷启动访谈（加载 {plugin}/skills/cold-start-interview/SKILL.md）。
3. 冷启动访谈将画像写入上述路径，可按需创建父目录。
4. 本文件是模板，随仓库分发。不要在此写入用户数据。

共享公司画像：公司级信息（主体身份、业务、经营地域、风险偏好、关键人员）保存在
legal-profile/company-profile.md，由全部 12 个领域共享，先读它再读本领域画像。
-->
"""


def transform_text(text: str) -> str:
    # 斜杠命令（builder-hub 单独处理，避免指向已删除目录）
    text = HUB_CMD_RE.sub(
        "（该功能属于 Claude 技能市场生态，KIMI 版本已移除）", text)
    text = CMD_RE.sub(
        lambda m: f"「{m.group(2)}」工作流（加载 {m.group(1)}/skills/{m.group(2)}/SKILL.md）",
        text,
    )
    for old, new in TEXT_REPLACEMENTS:
        text = text.replace(old, new)
    # 兜底路径规则（在具体替换之后）
    text = re.sub(
        r"~/.claude/plugins/config/claude-for-legal-zh/([a-z][a-z0-9-]*)/",
        r"legal-profile/\1/", text)
    text = re.sub(
        r"~/.claude/plugins/config/claude-for-legal-zh/?",
        "legal-profile/", text)
    text = re.sub(
        r"~/.claude/plugins/cache/\S*",
        "legal-profile/（旧版缓存路径，已废弃）", text)
    return text


def clean_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end == -1:
        return text
    head, body = text[:end], text[end:]
    lines = [
        ln for ln in head.splitlines()
        if not ln.startswith("argument-hint:") and not ln.startswith("user-invocable:")
    ]
    return "\n".join(lines) + body


def process_file(path: Path, stats: dict) -> None:
    text = path.read_text(encoding="utf-8")
    original = text
    if path.name == "SKILL.md":
        text = clean_frontmatter(text)
    text = transform_text(text)
    if path.name == "profile-template.md":
        plugin = path.parent.name
        if HEADER_RE.match(text):
            text = HEADER_RE.sub(HEADER_TEMPLATE.format(plugin=plugin), text, count=1)
    if text != original:
        path.write_text(text, encoding="utf-8")
        stats["changed"] += 1
    stats["seen"] += 1


def main() -> None:
    stats = {"seen": 0, "changed": 0}
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        process_file(md, stats)
    print(f"scanned={stats['seen']} changed={stats['changed']}")

    # 残留检查
    leftovers = []
    for pattern in [r"\.claude", r"mcp__", r"/[a-z-]+legal:[a-z-]+", r"argument-hint", r"user-invocable"]:
        hits = []
        for md in sorted(ROOT.rglob("*.md")):
            if ".git" in md.parts:
                continue
            for i, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
                if re.search(pattern, line):
                    hits.append(f"{md.relative_to(ROOT)}:{i}")
        leftovers.append((pattern, hits))
    for pattern, hits in leftovers:
        print(f"LEFTOVER {pattern}: {len(hits)}")
        for h in hits[:10]:
            print(f"  {h}")


if __name__ == "__main__":
    main()

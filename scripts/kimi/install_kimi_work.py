#!/usr/bin/env python3
"""KIMI Work 全局安装器。

把 11 个领域入口技能安装到 KIMI Work 的技能目录（daimon 托管 skills root），
并把技能正文中的仓库相对路径改写为本仓库的绝对路径——这样技能在任意
工作区中都能路由到本仓库的工作流文件。

用法：
    python3 scripts/kimi/install_kimi_work.py            # 安装
    python3 scripts/kimi/install_kimi_work.py --uninstall  # 卸载

注意：
- 安装后需要**开启新的 KIMI Work 会话**才能看到技能（索引在会话启动时构建）。
- 本仓库移动位置后需要重跑本脚本（绝对路径会写入技能文件）。
- KIMI 大版本更新可能重置托管技能目录，如技能消失重跑本脚本即可。
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILLS_ROOT = (
    Path.home()
    / "Library/Application Support/kimi-desktop/daimon-share/daimon/skills"
)

DOMAINS = [
    "ai-governance-legal", "commercial-legal", "corporate-legal",
    "employment-legal", "ip-legal", "law-student", "legal-clinic",
    "litigation-legal", "privacy-legal", "product-legal", "regulatory-legal",
]

ROOT_NOTE = (
    f"\n> **本仓库根目录：`{REPO_ROOT}`。** 本技能路由到的工作流文件、画像文件"
    f"（legal-profile/）与共享参考文件（references/）均位于该目录下；"
    f"正文中的相对路径引用一律相对于该根目录解析。\n"
)


def absolutize(text: str) -> str:
    """把入口技能正文中的仓库相对路径替换为绝对路径。"""
    repo = str(REPO_ROOT)
    # 画像目录与共享参考目录
    text = text.replace("`legal-profile/", f"`{repo}/legal-profile/")
    text = text.replace("`references/", f"`{repo}/references/")
    # 各领域目录（skills 文件、profile-template）
    for d in DOMAINS:
        text = text.replace(f"`{d}/", f"`{repo}/{d}/")
    # 在首段后插入仓库根目录说明（幂等）
    if "本仓库根目录：" not in text:
        marker = "按需加载，不要一次性全部读入。\n"
        if marker in text:
            text = text.replace(marker, marker + ROOT_NOTE, 1)
        else:
            text += ROOT_NOTE
    return text


def install() -> None:
    src_root = REPO_ROOT / ".agents" / "skills"
    if not src_root.is_dir():
        sys.exit("未找到 .agents/skills/，请先运行 scripts/kimi/generate_entry_skills.py")
    SKILLS_ROOT.mkdir(parents=True, exist_ok=True)
    count = 0
    for skill_dir in sorted(src_root.iterdir()):
        if not skill_dir.is_dir():
            continue
        dest = SKILLS_ROOT / skill_dir.name
        dest.mkdir(parents=True, exist_ok=True)
        text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        (dest / "SKILL.md").write_text(absolutize(text), encoding="utf-8")
        count += 1
        print(f"installed {skill_dir.name} -> {dest}")
    print(f"\n共安装 {count} 个技能到 {SKILLS_ROOT}")
    print("请开启新的 KIMI Work 会话使技能生效。")


def uninstall() -> None:
    src_root = REPO_ROOT / ".agents" / "skills"
    count = 0
    for skill_dir in sorted(src_root.iterdir()):
        dest = SKILLS_ROOT / skill_dir.name
        if dest.is_dir():
            shutil.rmtree(dest)
            count += 1
            print(f"removed {dest}")
    print(f"\n共卸载 {count} 个技能。请开启新的 KIMI Work 会话生效。")


if __name__ == "__main__":
    if "--uninstall" in sys.argv:
        uninstall()
    else:
        install()

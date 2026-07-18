#!/usr/bin/env python3
"""定时 Agent 蓝图改写（KIMI 版）。

对 */agents/*.md：
1. frontmatter 删除 model: / tools: 行（Claude 专属，tools 中含 mcp__ 工具名）
2. 文末追加"在 KIMI 中创建定时任务"指引（KIMI Work cron + 网页版定时任务）
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

AGENTS = {
    "commercial-legal/agents/renewal-watcher.md": {
        "when": "每周一 08:47", "cron": "47 8 * * 1",
        "task": "合同续约监控：读取续约登记册，输出未来 90 天续约/解约预警报告",
    },
    "commercial-legal/agents/deal-debrief.md": {
        "when": "每周五 17:52", "cron": "52 17 * * 5",
        "task": "签署合同复盘：汇总本周已签署协议中的审查指引偏离项",
    },
    "commercial-legal/agents/playbook-monitor.md": {
        "when": "每周三 09:23", "cron": "23 9 * * 3",
        "task": "审查指引监控：分析偏离日志，当条款持续偏移时提出审查指引更新建议",
    },
    "corporate-legal/agents/dataroom-watcher.md": {
        "when": "每日 08:17", "cron": "17 8 * * *",
        "task": "数据室监控：检查数据室新增文件，更新交割清单状态",
    },
    "employment-legal/agents/leave-tracker.md": {
        "when": "每周一 09:07", "cron": "7 9 * * 1",
        "task": "假期监控：检查在休假期（年休假/产假/病假）的审批、证明和到期截止日期预警",
    },
    "ip-legal/agents/ip-renewal-watcher.md": {
        "when": "每周一 08:23", "cron": "23 8 * * 1",
        "task": "知识产权续展监控：输出知识产权组合台账的截止日期报告",
    },
    "product-legal/agents/launch-watcher.md": {
        "when": "每周二、周四 09:13", "cron": "13 9 * * 2,4",
        "task": "产品上线雷达：监控上线追踪器中即将需要法务审查的产品",
    },
    "regulatory-legal/agents/reg-change-monitor.md": {
        "when": "每周一 07:43", "cron": "43 7 * * 1",
        "task": "法规动态监控：轮询法规信息源，生成周一晨会监管简报",
    },
    "litigation-legal/agents/docket-watcher.md": {
        "when": "每工作日 08:37", "cron": "37 8 * * 1-5",
        "task": "案件进度监控：监控在办案件进展和截止日期",
    },
}

SECTION = """

---

## 在 KIMI 中创建定时任务（KIMI 版）

**KIMI Work：** 对本文件说"按此蓝图创建定时任务"，或按以下参数创建定时任务（cron job）：

- 建议时间：{when}（cron `{cron}`，时区 Asia/Shanghai；可按需调整）
- 执行内容：读取 `legal-profile/{domain}.md` 获取配置，然后按上方工作流执行，报告输出到对话
- 可选：要求附加完成通知

**网页版 KIMI：** 在对话中说"创建定时任务：{task}，{when}执行"，或在定时任务表单中手动填写。画像以 KIMI 记忆为准。

**注意：** 原蓝图中的频道推送（Slack/飞书）在 KIMI 版中改为对话内输出或写入工作区文件；确需推送到 IM 时，可通过 WebBridge 操作网页版 IM 转发。
"""


def clean_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end == -1:
        return text
    head, body = text[:end], text[end:]
    lines = [ln for ln in head.splitlines()
             if not ln.startswith("model:") and not ln.startswith("tools:")]
    return "\n".join(lines) + body


def main() -> None:
    for rel, meta in AGENTS.items():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        original = text
        text = clean_frontmatter(text)
        if "## 在 KIMI 中创建定时任务" not in text:
            domain = rel.split("/")[0]
            text = text.rstrip() + SECTION.format(domain=domain, **meta)
        if text != original:
            path.write_text(text, encoding="utf-8")
            print(f"patched {rel}")
    # 残留检查
    hits = []
    for md in sorted(ROOT.glob("*/agents/*.md")):
        for i, ln in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if "mcp__" in ln or ln.startswith(("model:", "tools:")):
                hits.append(f"{md}:{i}")
    print(f"LEFTOVER mcp__/model/tools: {len(hits)}")
    for h in hits:
        print(f"  {h}")


if __name__ == "__main__":
    main()

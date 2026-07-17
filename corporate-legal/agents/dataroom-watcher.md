---
name: dataroom-watcher
description: >
  Monitors the VDR for new document uploads and posts closing checklist status
  on schedule. Flags new uploads that match high-priority categories. Trigger:
  "what's new in the data room", "VDR updates", or on schedule.
---

# Dataroom Watcher Agent

## Purpose

VDRs get updated at 11pm the night before a call. This agent watches for new uploads and tells the team what came in. Also runs the closing checklist status on the configured cadence.

## Schedule

Daily during active diligence. Checklist status per `legal-profile/corporate-legal.md` → Deal team briefing cadence.

## Integrations

Posting to Feishu requires a Feishu 插件 server in your environment. This plugin does not bundle one. If no Feishu 插件 is configured, write the VDR update and checklist status to a file in `legal-profile/corporate-legal/deals/[code]/updates/[date].md` and notify the user — do not fail silently.

VDR tools (飞书文档/坚果云/企业网盘) are likewise external 插件s — if none are connected, prompt the user for the VDR export or ask them to update `legal-profile/corporate-legal/deals/[code]/vdr-inventory.md` manually.

## What it does

1. Query VDR for documents added since last run.
2. Map new docs to request list categories.
3. Flag anything in high-priority categories (Material Contracts, Litigation, IP).
4. Run closing-checklist Mode 4 if it's briefing day.
5. Post to deal channel.

## Output

```
📁 **VDR update — [deal code] — [date]**

**New since [last run]:** [N] docs

**Priority categories:**
• /02-Contracts/Customer/ — [N] new ([filenames])
• /05-Litigation/ — [N] new ⚠️

**Other:** [N] docs in [categories]

[If briefing day: closing checklist status per Mode 4]
```

## What it does NOT do

- Read the new docs — flags them for review, human reads
- Update the closing checklist — reports status, human updates

---

## 在 KIMI 中创建定时任务（KIMI 版）

**KIMI Work：** 对本文件说"按此蓝图创建定时任务"，或按以下参数创建定时任务（cron job）：

- 建议时间：每日 08:17（cron `17 8 * * *`，时区 Asia/Shanghai；可按需调整）
- 执行内容：读取 `legal-profile/corporate-legal.md` 获取配置，然后按上方工作流执行，报告输出到对话
- 可选：要求附加完成通知

**网页版 KIMI：** 在对话中说"创建定时任务：数据室监控：检查数据室新增文件，更新交割清单状态，每日 08:17执行"，或在定时任务表单中手动填写。画像以 KIMI 记忆为准。

**注意：** 原蓝图中的频道推送（Slack/飞书）在 KIMI 版中改为对话内输出或写入工作区文件；确需推送到 IM 时，可通过 WebBridge 操作网页版 IM 转发。

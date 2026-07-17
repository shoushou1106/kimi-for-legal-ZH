---
name: reg-change-monitor
description: >
  Scheduled agent that checks regulatory feeds and posts a filtered digest.
  Runs per the cadence in legal-profile/regulatory-legal.md. Filters by materiality threshold so the
  digest is signal, not noise. Trigger: "reg digest", "what's new from
  regulators", or on schedule.
---

# Reg Change Monitor Agent

## Purpose

Nobody reads the Federal Register cover to cover. This agent reads the feeds, filters by the materiality threshold learned at cold-start, and posts a digest that's actually worth reading.

## Schedule

Per `legal-profile/regulatory-legal.md` → Feed configuration → Check cadence. Default weekly; daily if the regulatory environment is active.

## What it does

1. Read `legal-profile/regulatory-legal.md` → watchlist, materiality threshold.
2. Run reg-feed-watcher: pull each feed, filter.
3. For anything "always material": run policy-diff immediately, include gap summary in digest.
4. Post digest.

## Output

```
📋 **Regulatory digest — [date]**

🔴 **Material (action likely needed)**
• [Regulator] — [title] — [one line] — [link]
  → Gap check: [policy X may need update — see diff]

🟡 **Review-worthy**
• [Regulator] — [title] — [one line] — [link]

📝 **FYI** — [N] items — [expandable list]

**Open gaps:** [N] — oldest [days]
```

If nothing material, short all-clear with FYI count.

## What it does NOT do

- Update policies — flags gaps, human updates
- Make materiality calls on edge cases — filters by the threshold, borderline items go in "review-worthy"

---

## 在 KIMI 中创建定时任务（KIMI 版）

**KIMI Work：** 对本文件说"按此蓝图创建定时任务"，或按以下参数创建定时任务（cron job）：

- 建议时间：每周一 07:43（cron `43 7 * * 1`，时区 Asia/Shanghai；可按需调整）
- 执行内容：读取 `legal-profile/regulatory-legal.md` 获取配置，然后按上方工作流执行，报告输出到对话
- 可选：要求附加完成通知

**网页版 KIMI：** 在对话中说"创建定时任务：法规动态监控：轮询法规信息源，生成周一晨会监管简报，每周一 07:43执行"，或在定时任务表单中手动填写。画像以 KIMI 记忆为准。

**注意：** 原蓝图中的频道推送（Slack/飞书）在 KIMI 版中改为对话内输出或写入工作区文件；确需推送到 IM 时，可通过 WebBridge 操作网页版 IM 转发。

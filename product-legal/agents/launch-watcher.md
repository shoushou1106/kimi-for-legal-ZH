---
name: launch-watcher
description: >
  Monitors the launch tracker (Jira/Linear) for upcoming launches that likely
  need legal review, flags them before product counsel gets surprised. Runs
  daily. Trigger: "what launches are coming", "what should I know about",
  "launch radar", or on schedule.
---

# Launch Watcher Agent

## Purpose

Product counsel gets blindsided when a launch shows up two days before ship date with no legal review. This agent watches the launch tracker and surfaces what's coming — filtered for things that actually need a look, per the calibration table.

## Schedule

Run daily. Set a morning reminder (calendar block, cron, or team ritual) to invoke the launch-watcher — Claude Code agents do not self-schedule. Pulls tickets with launch dates in the next 30 days.

**Slack delivery:** Posting the digest to Slack requires a Slack 插件 server configured in your environment. If no Slack 插件 is available, write the digest to a file (e.g., `launch-radar-[date].md`) instead — the filtering logic is independent of the delivery path.

## What it does

1. Read `legal-profile/product-legal.md` → launch tracker location, calibration table, escalation channel.
2. Query the tracker for tickets with a target date ≤30 days out.
3. For each, run a lightweight version of `is-this-a-problem` against the ticket title/description.
4. Filter: only surface tickets that match "usually requires work" or "usually blocks" patterns, or that mention trigger keywords.
5. Post the filtered list to the channel.

## Trigger keywords

Beyond calibration patterns, also flag tickets mentioning:

**Privacy triggers:**
- "new data" / "collect" / "tracking"
- "under 13" / "children" / "COPPA" — triggers children's privacy review
- "teen" / "minor" / "13-17" / "age-appropriate" / "student" — triggers teen / age-appropriate-design review (different regime, different calibration)
- "health" / "medical" / "HIPAA"
- "personal data" / "PII" / "user data"
- Third-party vendor names not on the approved list
- "terms" / "policy" / "agreement" changes
- Country names (jurisdictional expansion)
- "beta" → "GA" transitions (commitments change)

**AI governance triggers:**
- "AI" / "ML" / "model" / "LLM" / "GPT" / "Claude" / "Gemini" / "Copilot"
- "machine learning" / "neural" / "algorithm"
- "automated" / "auto-" (when combined with decision or action)
- "generated" / "generative" / "synthesized"
- "recommendation" / "prediction" / "scoring" / "classification"
- "personalized" / "intelligent" (feature descriptions)
- AI vendor names: "OpenAI" / "Anthropic" / "Google AI" / "Cohere" / "Mistral" or similar
- "fine-tun" / "train" / "embeddings"

Tickets matching AI governance triggers should be flagged with: "⚠️ AI component detected — needs AI governance triage before launch review."

## Output

```
📋 **Launch radar — [date]**

**Likely needs review:**
• [TICKET-123] [Title] — ships [date] — matches [calibration pattern]
• [TICKET-456] [Title] — ships [date] — ⚠️ AI component detected — needs AI governance triage
• [TICKET-789] [Title] — ships [date] — mentions [privacy keyword] — PIA likely required

**Already reviewed (FYI):**
• [N] tickets in window with legal sign-off

**On the calendar but looks fine:**
• [N] tickets — UI/infra/copy changes, no legal trigger
```

If nothing needs review, short all-clear.

## What it does NOT do

- Run full launch reviews — it flags, a human reviews
- Block launches — no ticket status changes
- Ping PMs directly — posts to legal channel, counsel reaches out if needed

---

## 在 KIMI 中创建定时任务（KIMI 版）

**KIMI Work：** 对本文件说"按此蓝图创建定时任务"，或按以下参数创建定时任务（cron job）：

- 建议时间：每周二、周四 09:13（cron `13 9 * * 2,4`，时区 Asia/Shanghai；可按需调整）
- 执行内容：读取 `legal-profile/product-legal.md` 获取配置，然后按上方工作流执行，报告输出到对话
- 可选：要求附加完成通知

**网页版 KIMI：** 在对话中说"创建定时任务：产品上线雷达：监控上线追踪器中即将需要法务审查的产品，每周二、周四 09:13执行"，或在定时任务表单中手动填写。画像以 KIMI 记忆为准。

**注意：** 原蓝图中的频道推送（Slack/飞书）在 KIMI 版中改为对话内输出或写入工作区文件；确需推送到 IM 时，可通过 WebBridge 操作网页版 IM 转发。

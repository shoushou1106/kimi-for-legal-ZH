---
name: legal-regulatory
description: 中国法监管合规法律工作入口。法规动态监控、监管简报、政策差异比对、合规差距、征求意见稿、监管政策重写、行政监管。当用户提出监管合规相关任务时使用本技能，它将路由到 claude-for-legal-ZH（KIMI 版）仓库中对应的专业工作流文件。
---

# 监管合规（KIMI 版）

中国法监管合规工作流入口。本技能是路由层：实际工作流定义在 `regulatory-legal/skills/` 下的各文件中，按需加载，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 读取共享公司画像 `legal-profile/company-profile.md` 和本领域画像 `legal-profile/regulatory-legal.md`。
2. 如果任一文件不存在、或仍含 `[PLACEHOLDER]` 标记：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经用户同意后加载 `regulatory-legal/skills/cold-start-interview/SKILL.md` 并执行。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 本领域共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `regulatory-legal/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，加载对应文件并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动加载。

| 用户意图 | 加载文件 |
|---|---|
| **首次使用：冷启动访谈（配置画像）** | `regulatory-legal/skills/cold-start-interview/SKILL.md` |
| 审阅公开的征求意见期，记录决策，跟踪截止日期 | `regulatory-legal/skills/comments/SKILL.md` |
| 指导式定制监管实践配置——在不重新运行完整冷启动访谈的情况下对单项进行调整 | `regulatory-legal/skills/customize/SKILL.md` |
| 开放差距跟踪器——已标记但尚未关闭的事项 | `regulatory-legal/skills/gaps/SKILL.md` |
| 管理事务工作区——创建、列表、切换、关闭或解除活跃事务（实践层面） | `regulatory-legal/skills/matter-workspace/SKILL.md` |
| 将特定法规变化与已索引的政策库进行差异分析 | `regulatory-legal/skills/policy-diff/SKILL.md` |
| 产出关闭一个差距的政策修订建议稿（带标记版） | `regulatory-legal/skills/policy-redraft/SKILL.md` |
| 检查法规动态源，报告自上次检查以来的新事项，按重要度阈值过滤 | `regulatory-legal/skills/reg-feed-watcher/SKILL.md` |
| 支持 「gaps」工作流（加载 regulatory-legal/skills/gaps/SKI…（参考） | `regulatory-legal/skills/gap-surfacer/SKILL.md` |

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件（yuandian_law）；企业征信查询使用天眼查插件（tianyancha）；北大法宝、威科先行等可通过 WebBridge 操作网页版。
- 通过检索插件获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；完全没有可用检索工具时，在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。
- 知识库交叉引用协议（如用户配置了本地知识库）：见 `references/knowledge-base-crossref.md`。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。

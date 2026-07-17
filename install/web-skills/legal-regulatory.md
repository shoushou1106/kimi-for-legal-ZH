# KIMI 自定义技能定义：legal-regulatory

> 本文件是一个 KIMI 自定义技能的完整定义，供 skill-creator 读取后创建技能。
> 技能名称：legal-regulatory
> 技能说明（触发描述）：中国法监管合规法律工作入口。法规动态监控、监管简报、政策差异比对、合规差距、征求意见稿、行政监管。当用户提出监管合规相关任务时使用。

---

# 监管合规（KIMI 网页版）

中国法监管合规工作流入口。本技能是路由层：实际工作流定义在 GitHub 仓库的 `regulatory-legal/skills/` 目录下，按需读取，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 从 KIMI 记忆中读取你的画像：共享公司画像（company-profile）和本领域画像（regulatory-legal）。
2. 如果记忆中没有画像或画像仍是占位符：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经同意后读取 `https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/regulatory-legal/skills/cold-start-interview/SKILL.md` 并执行；访谈结束后将画像全文写入 KIMI 记忆，**每条记忆以「kimi-for-legal-ZH 法律画像」开头标注来源，并注明仅在法律工作任务中适用**（KIMI 的记忆在所有会话中始终生效，标注是防止法律画像渗入无关对话）。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/regulatory-legal/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，读取对应 URL 并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动读取。

| 用户意图 | 读取 URL |
|---|---|
| **首次使用：冷启动访谈（配置画像）** | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/regulatory-legal/skills/cold-start-interview/SKILL.md |
| 审阅公开的征求意见期，记录决策，跟踪截止日期 | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/regulatory-legal/skills/comments/SKILL.md |
| 指导式定制监管实践配置——在不重新运行完整冷启动访谈的情况下对单项进行调整 | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/regulatory-legal/skills/customize/SKILL.md |
| 开放差距跟踪器——已标记但尚未关闭的事项 | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/regulatory-legal/skills/gaps/SKILL.md |
| 管理事务工作区——创建、列表、切换、关闭或解除活跃事务（实践层面） | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/regulatory-legal/skills/matter-workspace/SKILL.md |
| 将特定法规变化与已索引的政策库进行差异分析 | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/regulatory-legal/skills/policy-diff/SKILL.md |
| 产出关闭一个差距的政策修订建议稿（带标记版） | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/regulatory-legal/skills/policy-redraft/SKILL.md |
| 检查法规动态源，报告自上次检查以来的新事项，按重要度阈值过滤 | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/regulatory-legal/skills/reg-feed-watcher/SKILL.md |
| 支持 「gaps」工作流（加载 regulatory-legal/skills/gaps/SKI…（参考） | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/regulatory-legal/skills/gap-surfacer/SKILL.md |

## 相对路径解析规则

工作流文件中引用的所有相对路径（如 `regulatory-legal/references/contract-law-core.md`、`references/knowledge-base-crossref.md`），一律加上前缀 `https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/` 后作为 URL 读取。如果该地址无法访问（网络原因），改用 Gitee 镜像前缀 `https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/`。需要读取目录清单时，改用 GitHub 页面 `https://github.com/shoushou1106/kimi-for-legal-ZH/tree/main/<目录>` 或 Gitee 页面 `https://gitee.com/shoushou1106/kimi-for-legal-ZH/tree/main/<目录>` 查看文件列表。

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件；企业征信查询使用天眼查插件；其他数据库可通过 WebBridge 或联网搜索。
- 通过检索获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；无法检索时在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。

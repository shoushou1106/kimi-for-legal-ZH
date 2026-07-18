# KIMI 自定义技能定义：legal-litigation

> 本文件是一个 KIMI 自定义技能的完整定义，供 skill-creator 读取后创建技能。
> 技能名称：legal-litigation
> 技能说明（触发描述）：中国法诉讼仲裁法律工作入口。案件登记、诉讼仲裁、律师函、要件分析、大事记、证据三性、庭前准备、保全、法律文书。当用户提出诉讼仲裁相关任务时使用。

---

# 诉讼仲裁（KIMI 网页版）

中国法诉讼仲裁工作流入口。本技能是路由层：实际工作流定义在 GitHub 仓库的 `litigation-legal/skills/` 目录下，按需读取，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 从 KIMI 记忆中读取你的画像：共享公司画像（company-profile）和本领域画像（litigation-legal）。
2. 如果记忆中没有画像或画像仍是占位符：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经同意后读取 `https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/cold-start-interview/SKILL.md` 并执行。**执行访谈时注意：网页版没有持久文件系统，访谈文件中所有写文件步骤（写入 legal-profile/ 等）一律跳过，画像内容直接记入记忆**（见该文件末尾「保存画像到 KIMI 记忆」一节）。访谈结束后**直接记住**画像内容——使用你自带的记忆功能即可，**不要通过命令行、终端或文件写入来操作记忆**（那样会陷入失败循环）。每条记忆以「kimi-for-legal-ZH 法律画像」开头标注来源，并注明仅在法律工作任务中适用（KIMI 的记忆在所有会话中始终生效，标注是防止法律画像渗入无关对话）。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，读取对应 URL 并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动读取。

| 用户意图 | 读取 URL |
|---|---|
| 按内部风格起草法律文书章节，与案件理论保持一致——每个事实有出处， 每个案例经核实，每个论点绑定… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/brief-section-drafter/SKILL.md |
| 从声明的文件来源和上传材料构建或更新大事记——提取带日期的事件、 去重，并按案件理论标记重要性 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/chronology/SKILL.md |
| 构建或审查要件分析表——专利权利要求对照表（侵权、无效或审查）或 民事构成要件分析表（任何诉讼请… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/claim-chart/SKILL.md |
| **首次使用：冷启动访谈（配置画像）** | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/cold-start-interview/SKILL.md |
| 引导式自定义你的诉讼实践画像——修改一项而不重新运行整个首次配置访谈 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/customize/SKILL.md |
| 从已完成的委托登记起草律师函——通过保密/自认风险/和解谈判姿态检查清单门禁， 输出 .docx… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/demand-draft/SKILL.md |
| 律师函起草前的委托背景收集——当事人、事实、依据、筹码、 最佳替代方案和保密过滤——写入结构化的… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/demand-intake/SKILL.md |
| 来函分流处理——提取关键字段、交叉检索案件组合、评估实质理由、 提出响应方案并附建议，必要时转交… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/demand-received/SKILL.md |
| 为证人构建庭前准备提纲——从案件材料中提取其相关文件， 围绕案件理论组织要点，并浮现质证材料 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/deposition-prep/SKILL.md |
| 发出、更新、解除或报告证据保全通知——将保全通知起草为 .docx， 更新案件日志中的保全字段，… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/legal-hold/SKILL.md |
| 单个案件深度简报——当前姿态、变化之处、下个节点、 待解决问题和风险重评估检查，适用于向法务负责… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/matter-briefing/SKILL.md |
| 结案——捕获结果、最终敞口和反思教训，从活跃案件组合中归档但不删除记录 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/matter-close/SKILL.md |
| 登记新案件——统一问题涵盖标识信息、利益冲突检索、来源、 风险分流、重要性、外聘律师、内部负责人… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/matter-intake/SKILL.md |
| 向案件历史文件追加带日期的事件记录并刷新日志行—— 捕获新进展、状态变化、风险重评估、期限变更和… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/matter-update/SKILL.md |
| 为多客户执业场景管理案件工作空间——创建、列表、切换、关闭或脱离活跃案件 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/matter-workspace/SKILL.md |
| 为活跃案件组合中的各外聘律师生成每周状态请求邮件草稿—— 每案一份 markdown | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/oc-status/SKILL.md |
| 从 _log.yaml 汇总案件组合——风险分布、即将到期的节点、 陈旧案件、重要性汇总、阶段分… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/portfolio-status/SKILL.md |
| 证据三性审查——对证据清单进行首轮审查，做出明显的 合法性/关联性判断并标记需要律师审查的疑难项… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/privilege-log-review/SKILL.md |
| 处理送达公司的法院调查令、行政机关协查通知或证人出庭通知—— 分类、分析范围/负担/保密、交叉检… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/litigation-legal/skills/subpoena-triage/SKILL.md |

## 相对路径解析规则

工作流文件中引用的所有相对路径（如 `litigation-legal/references/contract-law-core.md`、`references/knowledge-base-crossref.md`），一律加上前缀 `https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/` 后作为 URL 读取。如果该地址无法访问（Gitee 同步延迟或网络原因），改用 GitHub 前缀 `https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/`。需要读取目录清单时，用 Gitee 页面 `https://gitee.com/shoushou1106/kimi-for-legal-ZH/tree/main/<目录>` 或 GitHub 页面 `https://github.com/shoushou1106/kimi-for-legal-ZH/tree/main/<目录>` 查看文件列表。

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件；企业征信查询使用天眼查插件；其他数据库可通过 WebBridge 或联网搜索。
- 通过检索获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；无法检索时在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。

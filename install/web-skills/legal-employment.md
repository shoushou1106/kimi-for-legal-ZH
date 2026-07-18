# KIMI 自定义技能定义：legal-employment

> 本文件是一个 KIMI 自定义技能的完整定义，供 skill-creator 读取后创建技能。
> 技能名称：legal-employment
> 技能说明（触发描述）：中国法劳动用工法律工作入口。劳动合同解除、劳动关系认定、假期管理、员工调查、规章制度、工资工时、跨省用工、劳动法。当用户提出劳动用工相关任务时使用。

---

# 劳动用工（KIMI 网页版）

中国法劳动用工工作流入口。本技能是路由层：实际工作流定义在 GitHub 仓库的 `employment-legal/skills/` 目录下，按需读取，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 从 KIMI 记忆中读取你的画像：共享公司画像（company-profile）和本领域画像（employment-legal）。
2. 如果记忆中没有画像或画像仍是占位符：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经同意后读取 `https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/cold-start-interview/SKILL.md` 并执行；访谈结束后将画像全文写入 KIMI 记忆，**每条记忆以「kimi-for-legal-ZH 法律画像」开头标注来源，并注明仅在法律工作任务中适用**（KIMI 的记忆在所有会话中始终生效，标注是防止法律画像渗入无关对话）。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，读取对应 URL 并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动读取。

| 用户意图 | 读取 URL |
|---|---|
| **首次使用：冷启动访谈（配置画像）** | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/cold-start-interview/SKILL.md |
| 引导式自定义你的劳动法实践画像——修改一项内容 而不重新运行整个首次配置访谈 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/customize/SKILL.md |
| 启动在新省/直辖市或地域的用工扩张规划——收集基础信息，运行 劳务派遣 vs 业务外包 vs 直… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/expansion-kickoff/SKILL.md |
| 更新进行中的跨地域用工扩张项目状态——重新计算现已解封的项目， 标记任何逾期的项目，浮现下一优先… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/expansion-update/SKILL.md |
| 将拟议的规章制度变更与现行版本进行diff对比，标记连锁影响 和省级补充条款影响 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/handbook-updates/SKILL.md |
| 审查录用通知书及竞业限制/保密条款——含管辖地检查 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/hiring-review/SKILL.md |
| 向进行中的调查添加数据——文件、访谈记录或观察意见 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/investigation-add/SKILL.md |
| 从调查日志起草或更新调查备忘录 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/investigation-memo/SKILL.md |
| 开启新的内部调查事项——运行立案登记，生成证据来源清单， 并创建持续调查日志 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/investigation-open/SKILL.md |
| 对进行中的调查日志进行查询——证人说了什么、哪些地方陈述互相矛盾、 存在哪些证据缺口、每个问题上… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/investigation-query/SKILL.md |
| 从调查备忘录起草面向特定受众的摘要——HR版本、管理层版本或外部律师版本 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/investigation-summary/SKILL.md |
| 检查进行中的假期，获取截止日期预警和需要做出的决策 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/leave-tracker/SKILL.md |
| 向假期登记册添加新假期条目，录入开始追踪截止日期所需的最低信息 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/log-leave/SKILL.md |
| 管理案件工作空间——新建、列表、切换、关闭或解除（实务级） | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/matter-workspace/SKILL.md |
| 起草劳动规章制度/员工手册——含省级补充条款，在管辖范围内法律有差异时 生成地方版本 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/policy-drafting/SKILL.md |
| 劳动合同解除审查——高风险标记检测、经济补偿/赔偿金计算及最终工资支付时点 按管辖地（省/直辖市… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/termination-review/SKILL.md |
| 管辖地感知的劳动用工问答——工时制度分类、加班工资、最低工资、 年休假、产假、病假/医疗期、最终… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/wage-hour-qa/SKILL.md |
| 对拟议用工安排进行劳动关系认定——根据劳社部发〔2005〕12号三要素逐项分析， 区分劳动关系、… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/worker-classification/SKILL.md |
| shared framework for managing internal investiga…（参考） | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/internal-investigation/SKILL.md |
| implementation-planning framework for internatio…（参考） | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/employment-legal/skills/international-expansion/SKILL.md |

## 相对路径解析规则

工作流文件中引用的所有相对路径（如 `employment-legal/references/contract-law-core.md`、`references/knowledge-base-crossref.md`），一律加上前缀 `https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/` 后作为 URL 读取。如果该地址无法访问（Gitee 同步延迟或网络原因），改用 GitHub 前缀 `https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/`。需要读取目录清单时，用 Gitee 页面 `https://gitee.com/shoushou1106/kimi-for-legal-ZH/tree/main/<目录>` 或 GitHub 页面 `https://github.com/shoushou1106/kimi-for-legal-ZH/tree/main/<目录>` 查看文件列表。

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件；企业征信查询使用天眼查插件；其他数据库可通过 WebBridge 或联网搜索。
- 通过检索获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；无法检索时在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。

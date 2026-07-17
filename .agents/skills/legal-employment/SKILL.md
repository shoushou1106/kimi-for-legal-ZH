---
name: legal-employment
description: 中国法劳动用工法律工作入口。劳动合同解除、劳动关系认定、假期管理、员工调查、规章制度、工资工时、跨省用工、劳动法。当用户提出劳动用工相关任务时使用本技能，它将路由到 kimi-for-legal-ZH 仓库中对应的专业工作流文件。
---

# 劳动用工（KIMI 版）

中国法劳动用工工作流入口。本技能是路由层：实际工作流定义在 `employment-legal/skills/` 下的各文件中，按需加载，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 读取共享公司画像 `legal-profile/company-profile.md` 和本领域画像 `legal-profile/employment-legal.md`。
2. 如果任一文件不存在、或仍含 `[PLACEHOLDER]` 标记：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经用户同意后加载 `employment-legal/skills/cold-start-interview/SKILL.md` 并执行。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 本领域共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `employment-legal/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，加载对应文件并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动加载。

| 用户意图 | 加载文件 |
|---|---|
| **首次使用：冷启动访谈（配置画像）** | `employment-legal/skills/cold-start-interview/SKILL.md` |
| 引导式自定义你的劳动法实践画像——修改一项内容 而不重新运行整个首次配置访谈 | `employment-legal/skills/customize/SKILL.md` |
| 启动在新省/直辖市或地域的用工扩张规划——收集基础信息，运行 劳务派遣 vs 业务外包 vs 直… | `employment-legal/skills/expansion-kickoff/SKILL.md` |
| 更新进行中的跨地域用工扩张项目状态——重新计算现已解封的项目， 标记任何逾期的项目，浮现下一优先… | `employment-legal/skills/expansion-update/SKILL.md` |
| 将拟议的规章制度变更与现行版本进行diff对比，标记连锁影响 和省级补充条款影响 | `employment-legal/skills/handbook-updates/SKILL.md` |
| 审查录用通知书及竞业限制/保密条款——含管辖地检查 | `employment-legal/skills/hiring-review/SKILL.md` |
| 向进行中的调查添加数据——文件、访谈记录或观察意见 | `employment-legal/skills/investigation-add/SKILL.md` |
| 从调查日志起草或更新调查备忘录 | `employment-legal/skills/investigation-memo/SKILL.md` |
| 开启新的内部调查事项——运行立案登记，生成证据来源清单， 并创建持续调查日志 | `employment-legal/skills/investigation-open/SKILL.md` |
| 对进行中的调查日志进行查询——证人说了什么、哪些地方陈述互相矛盾、 存在哪些证据缺口、每个问题上… | `employment-legal/skills/investigation-query/SKILL.md` |
| 从调查备忘录起草面向特定受众的摘要——HR版本、管理层版本或外部律师版本 | `employment-legal/skills/investigation-summary/SKILL.md` |
| 检查进行中的假期，获取截止日期预警和需要做出的决策 | `employment-legal/skills/leave-tracker/SKILL.md` |
| 向假期登记册添加新假期条目，录入开始追踪截止日期所需的最低信息 | `employment-legal/skills/log-leave/SKILL.md` |
| 管理案件工作空间——新建、列表、切换、关闭或解除（实务级） | `employment-legal/skills/matter-workspace/SKILL.md` |
| 起草劳动规章制度/员工手册——含省级补充条款，在管辖范围内法律有差异时 生成地方版本 | `employment-legal/skills/policy-drafting/SKILL.md` |
| 劳动合同解除审查——高风险标记检测、经济补偿/赔偿金计算及最终工资支付时点 按管辖地（省/直辖市… | `employment-legal/skills/termination-review/SKILL.md` |
| 管辖地感知的劳动用工问答——工时制度分类、加班工资、最低工资、 年休假、产假、病假/医疗期、最终… | `employment-legal/skills/wage-hour-qa/SKILL.md` |
| 对拟议用工安排进行劳动关系认定——根据劳社部发〔2005〕12号三要素逐项分析， 区分劳动关系、… | `employment-legal/skills/worker-classification/SKILL.md` |
| shared framework for managing internal investiga…（参考） | `employment-legal/skills/internal-investigation/SKILL.md` |
| implementation-planning framework for internatio…（参考） | `employment-legal/skills/international-expansion/SKILL.md` |

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件（yuandian_law）；企业征信查询使用天眼查插件（tianyancha）；北大法宝、威科先行等可通过 WebBridge 操作网页版。
- 通过检索插件获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；完全没有可用检索工具时，在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。
- 知识库交叉引用协议（如用户配置了本地知识库）：见 `references/knowledge-base-crossref.md`。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。

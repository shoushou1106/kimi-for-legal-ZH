---
name: legal-commercial
description: 中国法商事合同法律工作入口。合同审查、NDA、保密协议、供应商协议、SaaS/MSA、续约、合同利益方摘要、合同风险上报、商事法务。当用户提出商事合同相关任务时使用本技能，它将路由到 claude-for-legal-ZH（KIMI 版）仓库中对应的专业工作流文件。
---

# 商事合同（KIMI 版）

中国法商事合同工作流入口。本技能是路由层：实际工作流定义在 `commercial-legal/skills/` 下的各文件中，按需加载，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 读取共享公司画像 `legal-profile/company-profile.md` 和本领域画像 `legal-profile/commercial-legal.md`。
2. 如果任一文件不存在、或仍含 `[PLACEHOLDER]` 标记：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经用户同意后加载 `commercial-legal/skills/cold-start-interview/SKILL.md` 并执行。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 本领域共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `commercial-legal/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，加载对应文件并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动加载。

| 用户意图 | 加载文件 |
|---|---|
| 追溯合同从基础协议到所有修订的变更轨迹——可以是所有变更的时间线摘要， 也可以是特定条款的追踪 | `commercial-legal/skills/amendment-history/SKILL.md` |
| **首次使用：冷启动访谈（配置画像）** | `commercial-legal/skills/cold-start-interview/SKILL.md` |
| 商事合同业务领域配置的引导式定制——修改一项配置而无需重新运行完整的冷启动访谈 | `commercial-legal/skills/customize/SKILL.md` |
| 根据审查指引中的上报矩阵将合同问题路由至合适的审批人，并起草上报说明 | `commercial-legal/skills/escalation-flagger/SKILL.md` |
| 管理事项工作区——新建、列出、切换、关闭或脱离（业务领域级） | `commercial-legal/skills/matter-workspace/SKILL.md` |
| 展示具有即将到来的取消截止日期的合同，在通知窗口关闭前发出预警， 基于维护的续约登记册运行 | `commercial-legal/skills/renewal-tracker/SKILL.md` |
| 根据审查指引审查供应商协议、保密协议或SaaS订阅 | `commercial-legal/skills/review/SKILL.md` |
| 审查并批准（或拒绝）来自审查指引监控代理的待处理更新建议，并将批准的变更 应用到业务领域配置中 | `commercial-legal/skills/review-proposals/SKILL.md` |
| 将合同审查转化为业务利益方实际会阅读的摘要 | `commercial-legal/skills/stakeholder-summary/SKILL.md` |
| 对接收方保密协议进行快速三色分类（绿/黄/红），使团队成员仅将律师时间投入 真正需要审查的协议（参考） | `commercial-legal/skills/nda-review/SKILL.md` |
| SaaS订阅协议审查，重点关注订阅交易中最关键的条款——自动续约机制、 价格调整、数据可迁移性、…（参考） | `commercial-legal/skills/saas-msa-review/SKILL.md` |
| 根据团队审查指引审查接收方供应商协议（参考） | `commercial-legal/skills/vendor-agreement-review/SKILL.md` |

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件（yuandian_law）；企业征信查询使用天眼查插件（tianyancha）；北大法宝、威科先行等可通过 WebBridge 操作网页版。
- 通过检索插件获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；完全没有可用检索工具时，在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。
- 知识库交叉引用协议（如用户配置了本地知识库）：见 `references/knowledge-base-crossref.md`。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。

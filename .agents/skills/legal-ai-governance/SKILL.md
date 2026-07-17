---
name: legal-ai-governance
description: 中国法AI 治理法律工作入口。AI 应用登记、算法安全评估、科技伦理审查、生成式 AI 合规、AI 供应商审查、AI 治理。当用户提出AI 治理相关任务时使用本技能，它将路由到 claude-for-legal-ZH（KIMI 版）仓库中对应的专业工作流文件。
---

# AI 治理（KIMI 版）

中国法AI 治理工作流入口。本技能是路由层：实际工作流定义在 `ai-governance-legal/skills/` 下的各文件中，按需加载，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 读取共享公司画像 `legal-profile/company-profile.md` 和本领域画像 `legal-profile/ai-governance-legal.md`。
2. 如果任一文件不存在、或仍含 `[PLACEHOLDER]` 标记：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经用户同意后加载 `ai-governance-legal/skills/cold-start-interview/SKILL.md` 并执行。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 本领域共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `ai-governance-legal/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，加载对应文件并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动加载。

| 用户意图 | 加载文件 |
|---|---|
| 按系统逐一定义AI角色、风险等级和监管义务——判定每个系统是 AI服务提供者还是使用者，分配风险… | `ai-governance-legal/skills/ai-inventory/SKILL.md` |
| 为AI系统或模型生成风险定级和合规概要评估——涵盖数据、公平性、 透明度、安全性和监管注册表 | `ai-governance-legal/skills/aia-generation/SKILL.md` |
| **首次使用：冷启动访谈（配置画像）** | `ai-governance-legal/skills/cold-start-interview/SKILL.md` |
| 在不重新运行完整冷启动访谈的情况下定制AI治理实践配置 | `ai-governance-legal/skills/customize/SKILL.md` |
| 管理事务工作区——创建、列表、切换、关闭或解除活跃事务 | `ai-governance-legal/skills/matter-workspace/SKILL.md` |
| 保持AI使用政策与当前实践一致 | `ai-governance-legal/skills/policy-monitor/SKILL.md` |
| 根据监管注册表和公司已有的实践位置，起草AI使用政策 | `ai-governance-legal/skills/policy-starter/SKILL.md` |
| 将新的或修订的AI法规与当前AI政策和实践进行差异分析—— 输出差距清单和整改计划，含负责人和日… | `ai-governance-legal/skills/reg-gap-analysis/SKILL.md` |
| 对提议的AI用例进行分类和风险排序：检索现有注册表、检查红线、 对残余风险进行分级 | `ai-governance-legal/skills/use-case-triage/SKILL.md` |
| 审查AI供应商条款——重点核查训练数据来源合规性、责任分配、 模型变更通知、合规义务向下传导 | `ai-governance-legal/skills/vendor-ai-review/SKILL.md` |

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件（yuandian_law）；企业征信查询使用天眼查插件（tianyancha）；北大法宝、威科先行等可通过 WebBridge 操作网页版。
- 通过检索插件获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；完全没有可用检索工具时，在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。
- 知识库交叉引用协议（如用户配置了本地知识库）：见 `references/knowledge-base-crossref.md`。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。

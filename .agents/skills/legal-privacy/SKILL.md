---
name: legal-privacy
description: 中国法数据合规与隐私法律工作入口。个人信息保护影响评估、PIA、PIPL、数据处理协议、DSAR、隐私政策、数据合规差距、数据出境和隐私合规。当用户提出数据合规与隐私相关任务时使用本技能，它将路由到 claude-for-legal-ZH（KIMI 版）仓库中对应的专业工作流文件。
---

# 数据合规与隐私（KIMI 版）

中国法数据合规与隐私工作流入口。本技能是路由层：实际工作流定义在 `privacy-legal/skills/` 下的各文件中，按需加载，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 读取共享公司画像 `legal-profile/company-profile.md` 和本领域画像 `legal-profile/privacy-legal.md`。
2. 如果任一文件不存在、或仍含 `[PLACEHOLDER]` 标记：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经用户同意后加载 `privacy-legal/skills/cold-start-interview/SKILL.md` 并执行。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 本领域共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `privacy-legal/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，加载对应文件并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动加载。

| 用户意图 | 加载文件 |
|---|---|
| **首次使用：冷启动访谈（配置画像）** | `privacy-legal/skills/cold-start-interview/SKILL.md` |
| Guided customization of your privacy practice pr… | `privacy-legal/skills/customize/SKILL.md` |
| 依据你的数据处理协议（DPA）操作手册审查一份DPA——自动检测你是受托处理者 还是处理者，并应… | `privacy-legal/skills/dpa-review/SKILL.md` |
| 处理个人信息主体权利请求（查阅、复制、删除、可携带、更正等）并起草回复——验证身份、 按系统逐一… | `privacy-legal/skills/dsar-response/SKILL.md` |
| 管理事项工作区——新建、列出、切换、关闭或脱离（实践级） | `privacy-legal/skills/matter-workspace/SKILL.md` |
| 生成符合内部格式的个人信息保护影响评估（PIA），适用于新功能、产品或处理活动， 使用从种子PI… | `privacy-legal/skills/pia-generation/SKILL.md` |
| 保持个人信息处理规则与实践一致 | `privacy-legal/skills/policy-monitor/SKILL.md` |
| 将新出台或变更的法规与现行个人信息处理规则及实践进行差异对比——输出差距清单和 附负责人和日期的… | `privacy-legal/skills/reg-gap-analysis/SKILL.md` |
| 快速判断某项处理活动是否需要个人信息保护影响评估、是否触发个保法第55条法定评估义务， 或可直接… | `privacy-legal/skills/use-case-triage/SKILL.md` |

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件（yuandian_law）；企业征信查询使用天眼查插件（tianyancha）；北大法宝、威科先行等可通过 WebBridge 操作网页版。
- 通过检索插件获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；完全没有可用检索工具时，在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。
- 知识库交叉引用协议（如用户配置了本地知识库）：见 `references/knowledge-base-crossref.md`。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。

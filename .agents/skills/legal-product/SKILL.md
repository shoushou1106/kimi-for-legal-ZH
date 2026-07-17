---
name: legal-product
description: 中国法产品与营销合规法律工作入口。产品上线审查、营销文案审查、广告法、反不正当竞争、功能法律风险、业务法务快速咨询。当用户提出产品与营销合规相关任务时使用本技能，它将路由到 claude-for-legal-ZH（KIMI 版）仓库中对应的专业工作流文件。
---

# 产品与营销合规（KIMI 版）

中国法产品与营销合规工作流入口。本技能是路由层：实际工作流定义在 `product-legal/skills/` 下的各文件中，按需加载，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 读取共享公司画像 `legal-profile/company-profile.md` 和本领域画像 `legal-profile/product-legal.md`。
2. 如果任一文件不存在、或仍含 `[PLACEHOLDER]` 标记：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经用户同意后加载 `product-legal/skills/cold-start-interview/SKILL.md` 并执行。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 本领域共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `product-legal/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，加载对应文件并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动加载。

| 用户意图 | 加载文件 |
|---|---|
| **首次使用：冷启动访谈（配置画像）** | `product-legal/skills/cold-start-interview/SKILL.md` |
| 对产品法务实务画像进行引导式定制——修改单项设置，无需重新运行完整冷启动访谈 | `product-legal/skills/customize/SKILL.md` |
| 对单个功能或产品领域进行更深入的风险评估，当上线审查发现某个议题需要 超出单行条目的深度分析时使… | `product-legal/skills/feature-risk-assessment/SKILL.md` |
| 对快速的飞书/钉钉问题给出"这有问题吗？"答复——对照您的校准进行模式匹配 | `product-legal/skills/is-this-a-problem/SKILL.md` |
| 对照您的框架和风险校准进行全面产品上线审查 | `product-legal/skills/launch-review/SKILL.md` |
| 审查营销文案中的宣传主张，识别哪些需要证实、改写或删除 | `product-legal/skills/marketing-claims-review/SKILL.md` |
| 管理事项工作空间——新建、列表、切换、关闭或脱钩（实务级） | `product-legal/skills/matter-workspace/SKILL.md` |

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件（yuandian_law）；企业征信查询使用天眼查插件（tianyancha）；北大法宝、威科先行等可通过 WebBridge 操作网页版。
- 通过检索插件获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；完全没有可用检索工具时，在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。
- 知识库交叉引用协议（如用户配置了本地知识库）：见 `references/knowledge-base-crossref.md`。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。

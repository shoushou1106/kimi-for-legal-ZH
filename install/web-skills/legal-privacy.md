# KIMI 自定义技能定义：legal-privacy

> 本文件是一个 KIMI 自定义技能的完整定义，供 skill-creator 读取后创建技能。
> 技能名称：legal-privacy
> 技能说明（触发描述）：中国法数据合规与隐私法律工作入口。个人信息保护影响评估、PIA、PIPL、数据处理协议、DSAR、隐私政策、数据合规差距、数据出境。当用户提出数据合规与隐私相关任务时使用。

---

# 数据合规与隐私（KIMI 网页版）

中国法数据合规与隐私工作流入口。本技能是路由层：实际工作流定义在 GitHub 仓库的 `privacy-legal/skills/` 目录下，按需读取，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 从 KIMI 记忆中读取你的画像：共享公司画像（company-profile）和本领域画像（privacy-legal）。
2. 如果记忆中没有画像或画像仍是占位符：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经同意后读取 `https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/privacy-legal/skills/cold-start-interview/SKILL.md` 并执行；访谈结束后将画像全文写入 KIMI 记忆，**每条记忆以「kimi-for-legal-ZH 法律画像」开头标注来源，并注明仅在法律工作任务中适用**（KIMI 的记忆在所有会话中始终生效，标注是防止法律画像渗入无关对话）。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/privacy-legal/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，读取对应 URL 并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动读取。

| 用户意图 | 读取 URL |
|---|---|
| **首次使用：冷启动访谈（配置画像）** | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/privacy-legal/skills/cold-start-interview/SKILL.md |
| Guided customization of your privacy practice pr… | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/privacy-legal/skills/customize/SKILL.md |
| 依据你的数据处理协议（DPA）操作手册审查一份DPA——自动检测你是受托处理者 还是处理者，并应… | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/privacy-legal/skills/dpa-review/SKILL.md |
| 处理个人信息主体权利请求（查阅、复制、删除、可携带、更正等）并起草回复——验证身份、 按系统逐一… | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/privacy-legal/skills/dsar-response/SKILL.md |
| 管理事项工作区——新建、列出、切换、关闭或脱离（实践级） | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/privacy-legal/skills/matter-workspace/SKILL.md |
| 生成符合内部格式的个人信息保护影响评估（PIA），适用于新功能、产品或处理活动， 使用从种子PI… | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/privacy-legal/skills/pia-generation/SKILL.md |
| 保持个人信息处理规则与实践一致 | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/privacy-legal/skills/policy-monitor/SKILL.md |
| 将新出台或变更的法规与现行个人信息处理规则及实践进行差异对比——输出差距清单和 附负责人和日期的… | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/privacy-legal/skills/reg-gap-analysis/SKILL.md |
| 快速判断某项处理活动是否需要个人信息保护影响评估、是否触发个保法第55条法定评估义务， 或可直接… | https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/privacy-legal/skills/use-case-triage/SKILL.md |

## 相对路径解析规则

工作流文件中引用的所有相对路径（如 `privacy-legal/references/contract-law-core.md`、`references/knowledge-base-crossref.md`），一律加上前缀 `https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/` 后作为 URL 读取。如果该地址无法访问（网络原因），改用 Gitee 镜像前缀 `https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/`。需要读取目录清单时，改用 GitHub 页面 `https://github.com/shoushou1106/kimi-for-legal-ZH/tree/main/<目录>` 或 Gitee 页面 `https://gitee.com/shoushou1106/kimi-for-legal-ZH/tree/main/<目录>` 查看文件列表。

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件；企业征信查询使用天眼查插件；其他数据库可通过 WebBridge 或联网搜索。
- 通过检索获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；无法检索时在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。

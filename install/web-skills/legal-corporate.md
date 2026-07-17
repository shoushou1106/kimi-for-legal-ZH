# KIMI 自定义技能定义：legal-corporate

> 本文件是一个 KIMI 自定义技能的完整定义，供 skill-creator 读取后创建技能。
> 技能名称：legal-corporate
> 技能说明（触发描述）：中国法公司与并购法律工作入口。并购尽调、重大合同披露、董事会/股东会决议、交割清单、公司合规、投后整合、公司法。当用户提出公司与并购相关任务时使用。

---

# 公司与并购（KIMI 网页版）

中国法公司与并购工作流入口。本技能是路由层：实际工作流定义在 GitHub 仓库的 `corporate-legal/skills/` 目录下，按需读取，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 从 KIMI 记忆中读取你的画像：共享公司画像（company-profile）和本领域画像（corporate-legal）。
2. 如果记忆中没有画像或画像仍是占位符：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经同意后读取 `https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/corporate-legal/skills/cold-start-interview/SKILL.md` 并执行；访谈结束后将画像全文写入 KIMI 记忆，**每条记忆以「kimi-for-legal-ZH 法律画像」开头标注来源，并注明仅在法律工作任务中适用**（KIMI 的记忆在所有会话中始终生效，标注是防止法律画像渗入无关对话）。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/corporate-legal/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，读取对应 URL 并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动读取。

| 用户意图 | 读取 URL |
|---|---|
| 检测 AI 辅助审查工具（如 Luminance、Kira 等）是否在使用中，将大批量条款提取 … | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/corporate-legal/skills/ai-tool-handoff/SKILL.md |
| 按你的内部格式起草董事会或专门委员会会议纪要 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/corporate-legal/skills/board-minutes/SKILL.md |
| 什么在阻碍交割——维护交割检查表，包含状态、关键路径和距交割天数 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/corporate-legal/skills/closing-checklist/SKILL.md |
| **首次使用：冷启动访谈（配置画像）** | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/corporate-legal/skills/cold-start-interview/SKILL.md |
| 公司业务实务画像的引导式定制——修改一项配置而无需重新运行完整的冷启动访谈 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/corporate-legal/skills/customize/SKILL.md |
| 将尽调发现汇总为适合受众层级的交易团队简报——面向领导层的执行摘要、面向团队的 工作摘要 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/corporate-legal/skills/deal-team-summary/SKILL.md |
| 读取数据室文件并按内部类别和重要性阈值提取问题，以内部备忘录格式产出发现 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/corporate-legal/skills/diligence-issue-extraction/SKILL.md |
| 主体合规追踪器——初始化、报告即将到来的截止日、更新状态、运行健康审计、 导出为 CSV | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/corporate-legal/skills/entity-compliance/SKILL.md |
| 交割后并购整合追踪器——分阶段工作计划、同意追踪、规模化合同转让、 每周状态报告 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/corporate-legal/skills/integration-management/SKILL.md |
| 从尽调发现构建重大合同披露清单，适用股权收购协议的重大合同定义，并按 协议清单格式排版 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/corporate-legal/skills/material-contract-schedule/SKILL.md |
| 管理事项工作区——创建、列出、切换、关闭或分离活跃事项，使多客户执业者将一个 客户的上下文与其他… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/corporate-legal/skills/matter-workspace/SKILL.md |
| 表格审查——一行一文件，一列一数据点，每个单元格标注来源 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/corporate-legal/skills/tabular-review/SKILL.md |
| 以内部格式起草董事会或专门委员会的一致书面决议，从决议存储库中检索先例 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/corporate-legal/skills/written-consent/SKILL.md |

## 相对路径解析规则

工作流文件中引用的所有相对路径（如 `corporate-legal/references/contract-law-core.md`、`references/knowledge-base-crossref.md`），一律加上前缀 `https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/` 后作为 URL 读取。如果该地址无法访问（Gitee 同步延迟或网络原因），改用 GitHub 前缀 `https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/`。需要读取目录清单时，用 Gitee 页面 `https://gitee.com/shoushou1106/kimi-for-legal-ZH/tree/main/<目录>` 或 GitHub 页面 `https://github.com/shoushou1106/kimi-for-legal-ZH/tree/main/<目录>` 查看文件列表。

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件；企业征信查询使用天眼查插件；其他数据库可通过 WebBridge 或联网搜索。
- 通过检索获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；无法检索时在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。

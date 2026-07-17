# KIMI 自定义技能定义：legal-law-student

> 本文件是一个 KIMI 自定义技能的完整定义，供 skill-creator 读取后创建技能。
> 技能名称：legal-law-student
> 技能说明（触发描述）：中国法法学学习与法考法律工作入口。法考、案例摘要、IRAC、课堂提问、法学写作、记忆卡片、学习计划、主观题和客观题训练。当用户提出法学学习与法考相关任务时使用。

---

# 法学学习与法考（KIMI 网页版）

中国法法学学习与法考工作流入口。本技能是路由层：实际工作流定义在 GitHub 仓库的 `law-student/skills/` 目录下，按需读取，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 从 KIMI 记忆中读取你的画像：共享公司画像（company-profile）和本领域画像（law-student）。
2. 如果记忆中没有画像或画像仍是占位符：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经同意后读取 `https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/law-student/skills/cold-start-interview/SKILL.md` 并执行；访谈结束后将画像全文写入 KIMI 记忆。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/law-student/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，读取对应 URL 并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动读取。

| 用户意图 | 读取 URL |
|---|---|
| 法考备考题目——客观题或主观题，针对你的薄弱科目和考试类型 | https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/law-student/skills/bar-prep-questions/SKILL.md |
| 按你偏好的格式撰写案例摘要 | https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/law-student/skills/case-brief/SKILL.md |
| 课堂提问准备——预测老师可能提问的问题并以苏格拉底式追问训练，标注你的薄弱 环节以便课前重温 | https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/law-student/skills/cold-call-prep/SKILL.md |
| **首次使用：冷启动访谈（配置画像）** | https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/law-student/skills/cold-start-interview/SKILL.md |
| 引导式自定义你的法学学习画像——无需重新运行完整的新手导入访谈即可修改单项设置 | https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/law-student/skills/customize/SKILL.md |
| 分析同一授课教师的历年考题以揭示模式——科目权重、反复出现的考点陷阱、 偏好的案例假设类型、政策… | https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/law-student/skills/exam-forecast/SKILL.md |
| 生成或训练法条概念记忆卡片——莱特纳式记忆桶，按科目的 Markdown 存储， 带自我评估的训… | https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/law-student/skills/flashcards/SKILL.md |
| 给 IRAC 论文评分——结构、考点识别、规则准确性、分析深度和组织 | https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/law-student/skills/irac-practice/SKILL.md |
| 对法律写作草稿（备忘录、代理词、论文、法考主观题答案）的结构性反馈—— 组织结构、分析深度、清晰… | https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/law-student/skills/legal-writing/SKILL.md |
| 按你的格式从课堂笔记和教材构建或扩展课程知识大纲 | https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/law-student/skills/outline-builder/SKILL.md |
| 在一个科目上运行一场集中的 N 题练习——客观题、主观题或记忆卡片 | https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/law-student/skills/session/SKILL.md |
| 苏格拉底式追问训练——我问，你答，我追问 | https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/law-student/skills/socratic-drill/SKILL.md |
| 构建或更新长期法考备考（或期末备考）学习计划——分阶段、按薄弱科目的权重分配、 每日练习安排，根… | https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/law-student/skills/study-plan/SKILL.md |

## 相对路径解析规则

工作流文件中引用的所有相对路径（如 `law-student/references/contract-law-core.md`、`references/knowledge-base-crossref.md`），一律加上前缀 `https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/` 后作为 URL 读取。需要读取目录清单时，改用 GitHub 页面 `https://github.com/shoushou1106/claude-for-legal-ZH/tree/main/<目录>` 查看文件列表。

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件；企业征信查询使用天眼查插件；其他数据库可通过 WebBridge 或联网搜索。
- 通过检索获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；无法检索时在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。

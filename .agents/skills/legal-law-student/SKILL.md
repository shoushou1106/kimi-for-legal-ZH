---
name: legal-law-student
description: 中国法法学学习与法考法律工作入口。法考、案例摘要、IRAC、课堂提问、法学写作、记忆卡片、学习计划、主观题和客观题训练。当用户提出法学学习与法考相关任务时使用本技能，它将路由到 claude-for-legal-ZH（KIMI 版）仓库中对应的专业工作流文件。
---

# 法学学习与法考（KIMI 版）

中国法法学学习与法考工作流入口。本技能是路由层：实际工作流定义在 `law-student/skills/` 下的各文件中，按需加载，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 读取共享公司画像 `legal-profile/company-profile.md` 和本领域画像 `legal-profile/law-student.md`。
2. 如果任一文件不存在、或仍含 `[PLACEHOLDER]` 标记：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经用户同意后加载 `law-student/skills/cold-start-interview/SKILL.md` 并执行。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 本领域共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `law-student/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，加载对应文件并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动加载。

| 用户意图 | 加载文件 |
|---|---|
| 法考备考题目——客观题或主观题，针对你的薄弱科目和考试类型 | `law-student/skills/bar-prep-questions/SKILL.md` |
| 按你偏好的格式撰写案例摘要 | `law-student/skills/case-brief/SKILL.md` |
| 课堂提问准备——预测老师可能提问的问题并以苏格拉底式追问训练，标注你的薄弱 环节以便课前重温 | `law-student/skills/cold-call-prep/SKILL.md` |
| **首次使用：冷启动访谈（配置画像）** | `law-student/skills/cold-start-interview/SKILL.md` |
| 引导式自定义你的法学学习画像——无需重新运行完整的新手导入访谈即可修改单项设置 | `law-student/skills/customize/SKILL.md` |
| 分析同一授课教师的历年考题以揭示模式——科目权重、反复出现的考点陷阱、 偏好的案例假设类型、政策… | `law-student/skills/exam-forecast/SKILL.md` |
| 生成或训练法条概念记忆卡片——莱特纳式记忆桶，按科目的 Markdown 存储， 带自我评估的训… | `law-student/skills/flashcards/SKILL.md` |
| 给 IRAC 论文评分——结构、考点识别、规则准确性、分析深度和组织 | `law-student/skills/irac-practice/SKILL.md` |
| 对法律写作草稿（备忘录、代理词、论文、法考主观题答案）的结构性反馈—— 组织结构、分析深度、清晰… | `law-student/skills/legal-writing/SKILL.md` |
| 按你的格式从课堂笔记和教材构建或扩展课程知识大纲 | `law-student/skills/outline-builder/SKILL.md` |
| 在一个科目上运行一场集中的 N 题练习——客观题、主观题或记忆卡片 | `law-student/skills/session/SKILL.md` |
| 苏格拉底式追问训练——我问，你答，我追问 | `law-student/skills/socratic-drill/SKILL.md` |
| 构建或更新长期法考备考（或期末备考）学习计划——分阶段、按薄弱科目的权重分配、 每日练习安排，根… | `law-student/skills/study-plan/SKILL.md` |

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件（yuandian_law）；企业征信查询使用天眼查插件（tianyancha）；北大法宝、威科先行等可通过 WebBridge 操作网页版。
- 通过检索插件获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；完全没有可用检索工具时，在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。
- 知识库交叉引用协议（如用户配置了本地知识库）：见 `references/knowledge-base-crossref.md`。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。

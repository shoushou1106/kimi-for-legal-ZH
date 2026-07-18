---
name: legal-clinic
description: 中国法法律诊所法律工作入口。法律诊所、学生案件接待、诊所备忘录、研究路线、结案移交、指导老师审阅、当事人沟通。当用户提出法律诊所相关任务时使用本技能，它将路由到 kimi-for-legal-ZH 仓库中对应的专业工作流文件。
---

# 法律诊所（KIMI 版）

中国法法律诊所工作流入口。本技能是路由层：实际工作流定义在 `legal-clinic/skills/` 下的各文件中，按需加载，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 读取共享公司画像 `legal-profile/company-profile.md` 和本领域画像 `legal-profile/legal-clinic.md`。
2. 如果任一文件不存在、或仍含 `[PLACEHOLDER]` 标记：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经用户同意后加载 `legal-clinic/skills/cold-start-interview/SKILL.md` 并执行。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 本领域共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `legal-clinic/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，加载对应文件并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动加载。

| 用户意图 | 加载文件 |
|---|---|
| 帮助诊所指导老师撰写实践领域指南，配置面向学生技能的行为——接待问题、 教学姿态（assist … | `legal-clinic/skills/build-guide/SKILL.md` |
| 记录当事人沟通——电话、邮件、短信、信函、面谈、语音留言 | `legal-clinic/skills/client-comms-log/SKILL.md` |
| 结构化接待——实践领域模板、跨领域考点识别、利益冲突标记、分流分类 | `legal-clinic/skills/client-intake/SKILL.md` |
| 基于模板的常规当事人信函——预约确认、文件索取、"已提交"简报 | `legal-clinic/skills/client-letter/SKILL.md` |
| **首次使用：冷启动访谈（配置画像）** | `legal-clinic/skills/cold-start-interview/SKILL.md` |
| 引导式定制你的法律诊所画像——无需重新运行整个冷启动访谈即可更改一项内容 | `legal-clinic/skills/customize/SKILL.md` |
| 追踪案件截止日期——添加、跨案汇总报告、更新、完成、关闭 | `legal-clinic/skills/deadlines/SKILL.md` |
| 常见诊所文件的初稿——实践领域模板（劳动争议仲裁申请书、离婚起诉状、 人身保护令申请书、律师函等… | `legal-clinic/skills/draft/SKILL.md` |
| IRAC 框架化的案件分析备忘录，标注检索缺口——提供框架结构而非分析结论 | `legal-clinic/skills/memo/SKILL.md` |
| 学生学期导入——诊所程序、工具导览、真实案件之前的实践练习 | `legal-clinic/skills/ramp/SKILL.md` |
| 法律问题的检索路线图——需查阅的法条、需调查的案例法领域、行政监管框架、 北大法宝/法信/元典检… | `legal-clinic/skills/research-start/SKILL.md` |
| 学期末案件交接备忘录——/ramp 的镜像 | `legal-clinic/skills/semester-handoff/SKILL.md` |
| 按受众的案件状态摘要——面向当事人（通俗语言）、面向内部（供指导老师）、 或面向法院（按本地规则… | `legal-clinic/skills/status/SKILL.md` |
| 指导老师审查队列——学生输出在此等待指导老师批准后才能发给当事人或法院 | `legal-clinic/skills/supervisor-review-queue/SKILL.md` |

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件（yuandian_law）；企业征信查询使用天眼查插件（tianyancha）；北大法宝、威科先行等可通过 WebBridge 操作网页版。
- 通过检索插件获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；完全没有可用检索工具时，在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。
- 知识库交叉引用协议（如用户配置了本地知识库）：见 `references/knowledge-base-crossref.md`。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。

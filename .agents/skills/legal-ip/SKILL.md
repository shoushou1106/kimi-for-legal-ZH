---
name: legal-ip
description: 中国法知识产权法律工作入口。商标可注册性、FTO、侵权警告函、通知删除、开源许可证、知识产权条款、专利、著作权、商标。当用户提出知识产权相关任务时使用本技能，它将路由到 kimi-for-legal-ZH 仓库中对应的专业工作流文件。
---

# 知识产权（KIMI 版）

中国法知识产权工作流入口。本技能是路由层：实际工作流定义在 `ip-legal/skills/` 下的各文件中，按需加载，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 读取共享公司画像 `legal-profile/company-profile.md` 和本领域画像 `legal-profile/ip-legal.md`。
2. 如果任一文件不存在、或仍含 `[PLACEHOLDER]` 标记：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经用户同意后加载 `ip-legal/skills/cold-start-interview/SKILL.md` 并执行。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 本领域共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `ip-legal/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，加载对应文件并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动加载。

| 用户意图 | 加载文件 |
|---|---|
| 起草侵权警告函（发送模式）或对收到的警告函进行分诊（接收模式） | `ip-legal/skills/cease-desist/SKILL.md` |
| 商标清除初步检索——排除性筛查+近似商标查询，产出标注清单而非清除法律意见 | `ip-legal/skills/clearance/SKILL.md` |
| **首次使用：冷启动访谈（配置画像）** | `ip-legal/skills/cold-start-interview/SKILL.md` |
| Guided customization of your IP practice profile… | `ip-legal/skills/customize/SKILL.md` |
| 自由实施（FTO）初检——对可能构成障碍的专利进行结构化初步审查，非FTO法律意见 | `ip-legal/skills/fto-triage/SKILL.md` |
| 知识产权侵权初步筛查——涵盖商标、著作权、专利和商业秘密的侵权因素清单， 标注各方有利/不利因素… | `ip-legal/skills/infringement-triage/SKILL.md` |
| 发明披露初步筛查——新颖性、创造性、可授权主题、公开日和 可检测性及战略价值 | `ip-legal/skills/invention-intake/SKILL.md` |
| 审查协议中的知识产权条款——权利归属、所有权、许可授予、 保证、赔偿 | `ip-legal/skills/ip-clause-review/SKILL.md` |
| 管理事项工作区——创建、列表、切换、关闭或解除（实务级） | `ip-legal/skills/matter-workspace/SKILL.md` |
| 开源许可证合规检查——对依赖列表、单个库或对外发布代码 | `ip-legal/skills/oss-review/SKILL.md` |
| 追踪知识产权组合——注册、续展、维持费和商标使用声明 | `ip-legal/skills/portfolio/SKILL.md` |
| 起草"通知-删除"通知（依信息网络传播权保护条例）、对收到的通知进行分诊或起草反通知 | `ip-legal/skills/takedown/SKILL.md` |

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件（yuandian_law）；企业征信查询使用天眼查插件（tianyancha）；北大法宝、威科先行等可通过 WebBridge 操作网页版。
- 通过检索插件获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；完全没有可用检索工具时，在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。
- 知识库交叉引用协议（如用户配置了本地知识库）：见 `references/knowledge-base-crossref.md`。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。

# KIMI 自定义技能定义：legal-ip

> 本文件是一个 KIMI 自定义技能的完整定义，供 skill-creator 读取后创建技能。
> 技能名称：legal-ip
> 技能说明（触发描述）：中国法知识产权法律工作入口。商标可注册性、FTO、侵权警告函、通知删除、开源许可证、知识产权条款、专利、著作权、商标。当用户提出知识产权相关任务时使用。

---

# 知识产权（KIMI 网页版）

中国法知识产权工作流入口。本技能是路由层：实际工作流定义在 GitHub 仓库的 `ip-legal/skills/` 目录下，按需读取，不要一次性全部读入。

## 开工前的画像门禁（每次必做）

1. 从 KIMI 记忆中读取你的画像：共享公司画像（company-profile）和本领域画像（ip-legal）。
2. 如果记忆中没有画像或画像仍是占位符：**停止实质工作**，告知用户需要先运行冷启动访谈（约 10–15 分钟），经同意后读取 `https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/ip-legal/skills/cold-start-interview/SKILL.md` 并执行；访谈结束后将画像全文写入 KIMI 记忆，**每条记忆以「kimi-for-legal-ZH 法律画像」开头标注来源，并注明仅在法律工作任务中适用**（KIMI 的记忆在所有会话中始终生效，标注是防止法律画像渗入无关对话）。用户也可选择"临时模式"——按通用默认值工作，每个输出标注 `[临时模式]`。
3. 共享安全规则（发送目的地检查、来源溯源标签、律师审查门槛）见 `https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/ip-legal/profile-template.md` 的「共享安全机制」段，所有输出适用。

## 工作流路由

根据用户意图选择一行，读取对应 URL 并严格遵循其工作流。标注"参考"的技能不直接调用，由主工作流在需要时自动读取。

| 用户意图 | 读取 URL |
|---|---|
| 起草侵权警告函（发送模式）或对收到的警告函进行分诊（接收模式） | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/ip-legal/skills/cease-desist/SKILL.md |
| 商标清除初步检索——排除性筛查+近似商标查询，产出标注清单而非清除法律意见 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/ip-legal/skills/clearance/SKILL.md |
| **首次使用：冷启动访谈（配置画像）** | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/ip-legal/skills/cold-start-interview/SKILL.md |
| Guided customization of your IP practice profile… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/ip-legal/skills/customize/SKILL.md |
| 自由实施（FTO）初检——对可能构成障碍的专利进行结构化初步审查，非FTO法律意见 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/ip-legal/skills/fto-triage/SKILL.md |
| 知识产权侵权初步筛查——涵盖商标、著作权、专利和商业秘密的侵权因素清单， 标注各方有利/不利因素… | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/ip-legal/skills/infringement-triage/SKILL.md |
| 发明披露初步筛查——新颖性、创造性、可授权主题、公开日和 可检测性及战略价值 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/ip-legal/skills/invention-intake/SKILL.md |
| 审查协议中的知识产权条款——权利归属、所有权、许可授予、 保证、赔偿 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/ip-legal/skills/ip-clause-review/SKILL.md |
| 管理事项工作区——创建、列表、切换、关闭或解除（实务级） | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/ip-legal/skills/matter-workspace/SKILL.md |
| 开源许可证合规检查——对依赖列表、单个库或对外发布代码 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/ip-legal/skills/oss-review/SKILL.md |
| 追踪知识产权组合——注册、续展、维持费和商标使用声明 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/ip-legal/skills/portfolio/SKILL.md |
| 起草"通知-删除"通知（依信息网络传播权保护条例）、对收到的通知进行分诊或起草反通知 | https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/ip-legal/skills/takedown/SKILL.md |

## 相对路径解析规则

工作流文件中引用的所有相对路径（如 `ip-legal/references/contract-law-core.md`、`references/knowledge-base-crossref.md`），一律加上前缀 `https://raw.giteeusercontent.com/shoushou1106/kimi-for-legal-ZH/raw/main/` 后作为 URL 读取。如果该地址无法访问（Gitee 同步延迟或网络原因），改用 GitHub 前缀 `https://raw.githubusercontent.com/shoushou1106/kimi-for-legal-ZH/main/`。需要读取目录清单时，用 Gitee 页面 `https://gitee.com/shoushou1106/kimi-for-legal-ZH/tree/main/<目录>` 或 GitHub 页面 `https://github.com/shoushou1106/kimi-for-legal-ZH/tree/main/<目录>` 查看文件列表。

## 检索与引用规则

- 法律法规、案例检索优先使用 KIMI 元典法律数据库插件；企业征信查询使用天眼查插件；其他数据库可通过 WebBridge 或联网搜索。
- 通过检索获取的引用标注来源标签（如 `[元典检索]`）；仅来自模型知识的标注 `[需验证]`；无法检索时在交付物顶部注明来源未经验证。
- 引用具体法条、司法解释、诉讼时效等时效性内容前，必须独立检索验证。

## 输出底线

- 所有输出为律师审查草稿——不是法律意见，不替代律师。涉主观法律判断默认保守处理，管辖权假设明示标注。
- 任何提交、发送或依赖前设明确门槛，由律师审查、核实并承担专业责任。

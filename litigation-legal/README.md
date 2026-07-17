> ⚠️ **KIMI 适配版说明**：本文件保留自上游仓库，其中 Claude Code 安装方式、斜杠命令与配置路径描述已不适用。KIMI 版的安装与使用以根目录 [README.md](../README.md) 和 [QUICKSTART.md](../QUICKSTART.md) 为准；本领域工作流内容仍然有效，经入口技能路由使用。

# 中国诉讼业务管理插件

中国企业/律所诉讼业务支持：管理案件组合、跟踪审理进度、起草诉讼文书。Cold-start 捕获你的风险校准、争议类型画像和文书风格——作为每个案件分流的基础框架。统一案件登记将新案件转化为结构化日志条目和逐案历史文件。组合概览和深度简报从日志中读取。

为同时管理多个案件的法务/律师设计，多数案件由外部律师代理。本插件是思维伙伴，不是案件管理系统。如果你已在使用律所管理软件（如 iCourt、无讼等），本插件不会替代它们——而是作为结构化推理层与之并行。

**每一份输出均为供律师审查的草案——附引用来源、标注风险、设审查门禁——不是法律结论。** 插件完成工作：读取文件，应用你的实务规则，发现问题，起草备忘录。律师审查、核实、决策。引用附来源标签，方便你判断哪些来自检索工具、哪些需要核实。保密标记谨慎适用，不因疏忽导致弃权。关键动作——提交立案、发送文书、签署——均设有显式确认门禁。

## 适用对象

| 角色 | 主要用途 |
|---|---|
| **企业诉讼律师/法务** | 全部——案件登记、分流、进度、历史、简报 |
| **法务副总监/总监** | 案件组合概览、向管理层/董事会报告 |
| **法务负责人/GC** | 快速了解案件组合状态、任一案件的深度分析 |

## 首次运行：cold-start

Cold-start 访谈编写*事务所/法务部*级别的实践画像——跨所有案件持续适用。三大支柱：

- **风险校准**——风险偏好、重大性阈值、准备金/披露触发条件、和解权限、保险覆盖、严重性-可能性矩阵
- **争议画像**——公司概况、经营地域、监管状态、争议模式、常见对手、外部律师库、内部利益相关方
- **文书风格**——向管理层/董事会的报告格式、准备金备忘录格式、外部律师指令风格、保密惯例、上报规范

每一步提供合理默认值（如 3x3 严重性-可能性矩阵），所有内容保持自由文本可编辑。

```
「cold-start-interview」工作流（加载 litigation-legal/skills/cold-start-interview/SKILL.md）
```

你的配置存储于 `legal-profile/litigation-legal.md`，不受插件更新影响。

## 命令

| 命令 | 功能 |
|---|---|
| `「cold-start-interview」工作流（加载 litigation-legal/skills/cold-start-interview/SKILL.md）` | Cold-start → 编写实践画像 |
| `「matter-intake」工作流（加载 litigation-legal/skills/matter-intake/SKILL.md）` | 统一案件登记 → 写入 `matters/[slug]/` + 追加至 `_log.yaml` |
| `「portfolio-status」工作流（加载 litigation-legal/skills/portfolio-status/SKILL.md）` | 案件组合概览——风险分布、即将到期的期限、停滞案件 |
| `「matter-briefing」工作流（加载 litigation-legal/skills/matter-briefing/SKILL.md） [slug]` | 单一案件深度简报——与法务负责人或外部律师沟通前的完整阅读 |
| `「matter-update」工作流（加载 litigation-legal/skills/matter-update/SKILL.md） [slug]` | 追加带日期的事件至案件历史；刷新日志的 `last_updated` |
| `「matter-close」工作流（加载 litigation-legal/skills/matter-close/SKILL.md） [slug]` | 将案件从活跃组合归档（保留，不删除） |
| `「demand-intake」工作流（加载 litigation-legal/skills/demand-intake/SKILL.md） [title]` | 律师函发送前的背景信息收集 |
| `「demand-draft」工作流（加载 litigation-legal/skills/demand-draft/SKILL.md） [slug]` | 基于收集信息起草律师函——经保密性审查，输出 `.docx`，附发送后核查清单 |
| `「demand-received」工作流（加载 litigation-legal/skills/demand-received/SKILL.md） [path]` | 收悉对方律师函——方案分析、案件组合交叉检索、转交至案件登记 |
| `「subpoena-triage」工作流（加载 litigation-legal/skills/subpoena-triage/SKILL.md） [path]` | 法院调查令/协查通知分类——范围/负担/保密性分析、异议框架、合规方案 |
| `「legal-hold」工作流（加载 litigation-legal/skills/legal-hold/SKILL.md） [slug] [--issue/--refresh/--release/--status]` | 证据保全通知的签发、更新、解除或状态报告 |
| `「chronology」工作流（加载 litigation-legal/skills/chronology/SKILL.md） [slug]` | 从已声明文件来源+上传材料构建或更新大事记/时间线——按案件理论标注重要性 |
| `「oc-status」工作流（加载 litigation-legal/skills/oc-status/SKILL.md）` | 起草周期性的外部律师案件进度询问函 |
| `「claim-chart」工作流（加载 litigation-legal/skills/claim-chart/SKILL.md）` | 构建或审查要件分析表——对任一请求权基础或抗辩事由进行构成要件逐项分析，附法条编号，检测证据缺口 |

## 技能

| 技能 | 用途 |
|---|---|
| **cold-start-interview** | 实践画像——风险校准、争议画像、文书风格 |
| **matter-intake** | 统一案件登记问题；写入案件文件+日志记录 |
| **portfolio-status** | 日志层面的组合概览——风险、期限、停滞 |
| **matter-briefing** | 从案件文件+历史中深度阅读一个案件 |
| **matter-update** | 结构化事件追加；更新日志中的 `last_updated` |
| **matter-close** | 归档语义；记录结果 |
| **demand-intake** | 律师函背景信息收集——当事人、事实、优势分析、保密过滤 |
| **demand-draft** | 保密性审查，起草 `.docx`，附 `[CITE:___]` 占位符；输出发送后核查清单；提供案件创建选项 |
| **demand-received** | 收悉对方函件——实体审查、方案分析、案件组合交叉检索 |
| **subpoena-triage** | 法院调查令分类、分析范围/负担/保密性，输出异议框架+合规方案 |
| **legal-hold** | 证据保全通知的签发/更新/解除/状态报告 |
| **chronology** | 从已声明文件来源+上传材料提取日期事件；去重；按案件理论标注重要性 |
| **oc-status** | 周期性的外部律师案件进度询问函起草 |
| **claim-chart** | 要件分析表——对任一请求权基础或抗辩事由进行构成要件逐项分析、逐项引用法条编号、证据缺口检测 |

## 交互式命令与定时代理人

上述命令由你主动调用——用于处理具体案件。以下代理人按计划自动运行——用于被动监控：

| 代理人 | 监控内容 | 默认频率 |
|---|---|---|
| **docket-watcher** | 活跃案件组合的审理进度——通过 yuan dian 或 人民法院案例库 拉取新进展、计算候选期限、交叉对照各案件的历史和交付物 | 每周 |

## 数据组织

```
litigation-legal/
├── CLAUDE.md                          # 实践画像——风险、画像、风格
├── matters/
│   ├── _log.yaml                      # 案件组合账本（每条记录一个案件）
│   └── [matter-slug]/
│       ├── matter.md                  # 案件级别的登记+诉讼理论+态势
│       ├── history.md                 # 仅追加的事件日志
│       ├── chronology.md              # 面向诉讼的大事记/时间线（按需生成）
│       └── legal-hold-v[N].docx       # 证据保全通知
├── demand-letters/                    # 发出律师函
│   └── [slug]/
│       ├── intake.md
│       ├── draft-v1.docx
│       └── checklist.md
├── inbound/                           # 收悉的律师函、调查令、监管函
│   └── [slug]/
│       ├── incoming.[ext]
│       ├── triage.md
│       └── response-v1.docx
└── oc-status/                         # 周期性外部律师进度询问函
    └── [YYYY-MM-DD]/
        ├── _summary.md
        └── [slug].md
```

## 检索工具与引用核验

**请先连接检索工具——引用保护机制依赖于此。** 无检索工具时，每条引用均标注 `[需核实]`，审查备注记录来源未经验证。通过 **yuan dian 插件**（案例语义检索、法规检索）、**聚法案例**或**人民法院案例库**检索获得的引用，标注来源并可追溯。来自模型知识或联网搜索的引用标注 `[需核实]` 或 `[需核实-精确引用]`，应在信赖前对照一手来源核验。插件对引用分层标注，使你的核实时间集中在最重要的地方。

## 内联标记惯例

三种标记出现在技能输出和草案中。它们不是免责声明——而是行动项目：

- `[引用: 需补充具体法条]` ——法律依据占位符。律师在发送前填写或确认。
- `[核实: 具体事实]` ——尚未确认来源的事实性陈述。律师在信赖前核实。
- `[SME核实: 具体专业判断]` ——需要执业律师专业判断的事项（实体审查、重要性标注、证据三性判断、保密性判断）。SME = 具有相关执业资格的律师。

含未解决标记的草案或分流分析不是最终稿，无论其文字多么完善。

## 注意事项

- 每个技能首先从 `legal-profile/litigation-legal.md` 读取配置。如果你的风险偏好变化或增加了新的外部律师，更新该文件——不要在个案中覆盖。
- `_log.yaml` 是案件组合状态的唯一事实来源。保持整洁。
- 案件历史仅追加。如果之前记录有误，以新条目记录更正——不修改既往记录。
- 已结案案件保留在 `_log.yaml` 中（可搜索历史）。`/portfolio-status` 默认过滤已结案案件。
- 所有输出中的法条引用均附来源溯源标签（`[法条原文]`/`[裁判文书]`/`[yuandian检索]`/`[模型知识 — 需验证]`等），律师应在信赖前核实。

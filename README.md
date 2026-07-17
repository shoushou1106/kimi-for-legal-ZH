# KIMI for Legal —— 中国法技能包

> 本仓库是 [CSlawyer1985/claude-for-legal-ZH](https://github.com/CSlawyer1985/claude-for-legal-ZH) 的 **KIMI 适配版**（其本身是 [Anthropic claude-for-legal](https://github.com/anthropics/claude-for-legal) 的中国法本地化版本）。
> 覆盖商事合同 · 隐私数据 · 产品合规 · 公司并购 · 劳动用工 · 争议解决 · 监管合规 · AI 治理 · 知识产权 · 法学教育 · 法律诊所。
> 原仓库的 Claude Code 插件市场、MCP 连接器、Codex 适配层已移除；法律知识、工作流方法论和安全机制完整保留。

## 两种安装方式

### 方式一：KIMI Work（推荐，完整能力）

```bash
git clone https://github.com/shoushou1106/claude-for-legal-ZH.git
cd claude-for-legal-ZH
python3 scripts/kimi/install_kimi_work.py
```

安装器会把 11 个领域入口技能复制到 KIMI Work 的技能目录，并把路由路径改写为本仓库的绝对路径。**开启新的 KIMI Work 会话**后技能即可用（KIMI Work 的技能索引在会话启动时构建）。

- 仓库请放在**固定位置**——技能中的路由使用绝对路径指向本仓库；移动仓库后重跑一次安装器即可。
- 卸载：`python3 scripts/kimi/install_kimi_work.py --uninstall`
- KIMI 大版本更新后若技能消失，重跑安装器即可恢复。

然后对 KIMI 说「运行商事合同冷启动访谈」（或你所在领域），完成 10–15 分钟的访谈，它会生成你的实务画像（`legal-profile/`），所有工作流从此按你的实务方式执行。

### 方式二：网页版 KIMI（轻量使用）

网页版 KIMI 通过对话创建技能，无本地文件系统。按照 **[install/INSTALL_KIMI_WEB.md](install/INSTALL_KIMI_WEB.md)** 操作——把一段预设文本粘贴给 skill-creator，它会从本仓库读取 11 个技能定义并批量创建；画像写入 KIMI 记忆。

## 仓库结构

```
.agents/skills/            # 11 个 KIMI 领域入口技能（源文件，经安装器部署到 KIMI Work）
  legal-commercial/        # 商事合同     legal-corporate/    # 公司与并购
  legal-employment/        # 劳动用工     legal-privacy/      # 数据合规与隐私
  legal-product/           # 产品合规     legal-regulatory/   # 监管合规
  legal-ai-governance/     # AI 治理      legal-ip/           # 知识产权
  legal-litigation/        # 诉讼仲裁     legal-clinic/       # 法律诊所
  legal-law-student/       # 法学学习与法考
<领域名>/                  # 11 个领域工作流库（约 150 个工作流文件）
  skills/<工作流>/SKILL.md  # 具体工作流，由入口技能按需路由加载
  references/              # 该领域中国法核心规则参考（法条原文级）
  agents/                  # 定时监控蓝图（KIMI Work 定时任务 / 网页版定时任务）
  profile-template.md      # 该领域实务画像模板
references/                # 跨领域共享工作流（知识库交叉引用、尽调、庭审准备、合同审核门禁等）
legal-profile/             # 你的实务画像（冷启动访谈写入，个人数据不入库）
install/                   # 网页版 KIMI 导入指南 + 网页版技能定义文件
scripts/kimi/              # KIMI 适配转换脚本（上游同步时重跑）
```

## 与 Claude 版本的机制对应

| Claude Code 概念 | KIMI 版本实现 |
|---|---|
| `~/.claude/plugins/config/.../CLAUDE.md` 实践画像 | `legal-profile/<领域>.md` + KIMI 长期记忆（摘要） |
| `company-profile.md` 共享公司画像 | `legal-profile/company-profile.md` + KIMI 长期记忆 |
| `/插件:技能` 斜杠命令 | 自然语言触发入口技能 → 路由加载工作流文件 |
| MCP 连接器（元典、北大法宝、e签宝等） | KIMI 自带插件：元典法律数据库（yuandian_law）、天眼查（tianyancha）；WebBridge 操作网页版数据库 |
| 定时 Agent（agents/） | KIMI Work 定时任务（cron job）/ 网页版 KIMI 定时任务，创建指引见各蓝图文件末尾 |
| Claude Managed Agents API 蓝图 | 已移除，定时能力由上述定时任务覆盖 |
| legal-builder-hub 社区技能市场 | 已移除（KIMI 无对应生态）；技能质量评估框架保留于 `references/skills-qa-workflow.md` |

## 使用示例

```text
审查这份供应商合同，重点看责任限制、解除、赔偿、数据处理和争议解决。
```

```text
我们准备上线一个用户画像推荐功能，判断是否需要个人信息保护影响评估。
```

```text
员工在上海，公司想协商解除劳动合同，帮我做解除审查和经济补偿测算。
```

```text
按 litigation-legal/agents/docket-watcher.md 蓝图创建定时任务，每工作日早上监控我的案件进展。
```

## 重要声明

- **所有输出均为律师审查草稿**——不是法律意见，不是法律结论，不替代律师。每条引用标注来源，涉主观法律判断默认保守处理，任何提交、发送或依赖前设有明确门槛。律师审查、核实并对所有对外产出承担专业责任。
- 无法从权威来源（元典法律数据库等）核实的引用会标注 `[需验证]`。
- 本适配版不代表 Anthropic、月之暗面（Moonshot AI）或原仓库作者的法律立场。

## 致谢与许可证

- 原仓库（中国法本地化）：**[CSlawyer1985/claude-for-legal-ZH](https://github.com/CSlawyer1985/claude-for-legal-ZH)**，作者**陈石律师**（浙江海泰律师事务所）
- 上游框架：**[Anthropic claude-for-legal](https://github.com/anthropics/claude-for-legal)**
- KIMI 适配：见本仓库提交历史
- 依据 [Apache License, Version 2.0](LICENSE) 许可，保留原版权声明

## 上游同步

本仓库与上游 `CSlawyer1985/claude-for-legal-ZH` 的同步流程：

```bash
git fetch upstream && git merge upstream/main
python3 scripts/kimi/transform.py            # 重新执行批量转换（幂等）
python3 scripts/kimi/patch_cold_start.py     # 冷启动专项改写（幂等）
python3 scripts/kimi/patch_agents.py         # 定时 Agent 改写（幂等）
python3 scripts/kimi/generate_entry_skills.py  # 重新生成入口技能
python3 scripts/kimi/generate_web_skills.py    # 重新生成网页版技能
python3 scripts/kimi/install_kimi_work.py      # 刷新 KIMI Work 中的全局技能副本
```

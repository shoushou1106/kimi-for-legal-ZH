# 网页版 KIMI 导入指南（一次性使用）

> 本指南帮助你在**网页版 KIMI** 中安装中国法律技能包。整个过程约 10 分钟，只需复制粘贴。
> 如果你使用 **KIMI Work**（桌面端），不需要本指南——直接 `git clone` 仓库并在 KIMI Work 中打开该目录即可，技能会被自动发现。

## 这个技能包是什么

11 个中国法律领域的 KIMI 自定义技能：商事合同、公司与并购、劳动用工、数据合规与隐私、产品与营销合规、监管合规、AI 治理、知识产权、诉讼仲裁、法律诊所、法学学习与法考。每个技能是路由入口，按需从 GitHub 仓库读取对应的专业工作流文件执行。

## 第一步：批量创建技能

1. 打开网页版 KIMI，进入 **侧边栏 → 插件 → 技能 Tab → 自定义技能 → 与 Kimi 对话创建技能**。
2. KIMI 会自动填入"请用 skill-creator 帮我创建技能，要求是："——在它后面**粘贴下面整段内容**：

```text
请依次读取以下 11 个链接，每个链接是一个自定义技能的完整定义（文件顶部标注了技能名称和触发描述，正文是技能内容）。请为每个文件创建一个自定义技能，共 11 个：

1. https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/install/web-skills/legal-commercial.md
2. https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/install/web-skills/legal-corporate.md
3. https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/install/web-skills/legal-employment.md
4. https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/install/web-skills/legal-privacy.md
5. https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/install/web-skills/legal-product.md
6. https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/install/web-skills/legal-regulatory.md
7. https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/install/web-skills/legal-ai-governance.md
8. https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/install/web-skills/legal-ip.md
9. https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/install/web-skills/legal-litigation.md
10. https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/install/web-skills/legal-clinic.md
11. https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/install/web-skills/legal-law-student.md

全部创建完成后，请告诉我"技能包安装完成"，并列出已创建的技能名称清单。
```

3. 等待 KIMI 逐个创建。如果中途中断或遗漏，把缺失的链接单独发给它补建。
4. 创建完成后，到 **插件 → 技能** 页面确认 11 个技能都在列表中。

> 也可以一次只创建一个：在 skill-creator 对话中发送单个链接，例如"请读取 <某个链接> 并按其定义创建技能"。

## 第二步：运行冷启动访谈（让技能真正懂你）

技能安装后还需要配置你的实务画像，否则输出是通用模板。对 KIMI 说：

```text
运行商事合同冷启动访谈
```

（或任何你常用的领域，如"运行劳动用工冷启动访谈"）。KIMI 会通过 10–15 分钟的访谈了解你的实务方式、审查指引和升级规则，并把画像写入 **KIMI 记忆**。每个领域只需做一次；公司层面的信息一次访谈、全领域共享。

## 第三步（可选）：安装定时监控任务

本技能包含 9 个定时监控蓝图（合同续约预警、法规动态简报、案件进度监控等）。网页版 KIMI 支持定时任务，以"合同续约监控"为例，对 KIMI 说：

```text
读取 https://raw.githubusercontent.com/shoushou1106/claude-for-legal-ZH/main/commercial-legal/agents/renewal-watcher.md ，按文件末尾「在 KIMI 中创建定时任务」一节为我创建定时任务
```

其他蓝图位于仓库各领域的 `agents/` 目录下（如 `litigation-legal/agents/docket-watcher.md` 案件进度监控、`regulatory-legal/agents/reg-change-monitor.md` 法规动态简报），同理创建。

## 使用时的注意事项

- **检索验证**：技能会优先调用元典法律数据库、天眼查等插件核实法条和案例；无法核实的引用会标注 `[需验证]`。所有输出是律师审查草稿，不替代律师判断。
- **读取速度**：工作流文件按需从 GitHub 读取，首次执行某个任务时会有几次链接抓取，属正常现象。
- **画像更新**：实务方式变化后，直接对 KIMI 说"更新我的画像"并说明要改的内容，或重新运行冷启动访谈。
- **完整功能**：网页版技能依赖在线读取工作流文件；如需本地知识库集成、事项工作区文件管理等完整能力，建议使用 KIMI Work 版本。

## 仓库地址

https://github.com/shoushou1106/claude-for-legal-ZH （KIMI 适配版，基于 CSlawyer1985/claude-for-legal-ZH）

# 快速上手（KIMI 版）

## KIMI Work 用户（60 秒）

1. `git clone https://github.com/shoushou1106/kimi-for-legal-ZH.git && cd kimi-for-legal-ZH`
2. `python3 scripts/kimi/install_kimi_work.py`（卸载加 `--uninstall`）
3. **开启新的 KIMI Work 会话**——11 个领域技能生效。
4. 对 KIMI 说：**「运行商事合同冷启动访谈」**（换成你的领域）。约 10–15 分钟，生成你的实务画像。
5. 开始工作，例如：「审查这份供应商合同」。

## 网页版 KIMI 用户（10 分钟）

打开 **[install/INSTALL_KIMI_WEB.md](install/INSTALL_KIMI_WEB.md)**，按指南把预设文本粘贴给 skill-creator，批量创建 11 个技能，然后运行冷启动访谈。

## 定时监控（可选）

9 个定时监控蓝图在各领域 `agents/` 目录下（续约预警、法规简报、案件监控等）。
- KIMI Work：对 KIMI 说「按 commercial-legal/agents/renewal-watcher.md 蓝图创建定时任务」。
- 网页版：在定时任务表单中创建，或让 KIMI 读取蓝图文件后代为创建。

## 最重要的一条

**先运行冷启动访谈再开始工作。** 所有工作流都从 `legal-profile/` 的实务画像读取配置——跳过访谈是输出泛化的最常见原因。所有输出为律师审查草稿，不替代律师。

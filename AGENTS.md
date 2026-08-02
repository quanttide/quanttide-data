# Agent Instructions

本文件为 AI Agent 提供本仓库的特殊文件索引。

## 关键文档

| 文档 | 用途 |
|------|------|
| [README.md](README.md) | 项目定位、子模块介绍、文档边界 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 贡献指南、提交规则、子模块提交流程 |
| [STATUS.md](STATUS.md) | 各子模块最新版本状态 |
| [CHANGELOG.md](CHANGELOG.md) | 版本变更记录 |
| [.gitmodules](.gitmodules) | 子模块注册与 URL 配置 |

## AI 技能

| 技能 | 位置 | 用途 |
|------|------|------|
| qtcloud-devops | `.agents/skills/qtcloud-devops/SKILL.md` | DevOps 流程：子模块管理、构建、测试、发布 |

## 经验教训

- **CI 对齐（qtcloud-data src/cli）**：重构/移动文件后先跑格式检查再提交（`cargo fmt --check`），并保持本地检查从严与 CI 一致（clippy `-D warnings`）——本地双绿（fmt + 严格 lint）约等于 CI 绿。CI 失败先查是 fmt 差异还是逻辑错误（历史上多次 CI 失败均为 fmt 未跑导致）

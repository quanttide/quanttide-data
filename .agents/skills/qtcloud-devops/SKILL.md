---
name: qtcloud-devops
description: 使用 qtcloud-devops CLI 执行本项目的 DevOps 流程：子模块管理、构建、测试、发布、规划审计。当用户要求提交、发布、检查状态、审计代码、或执行标准研发流程时使用。
---

# qtcloud-devops — 量潮 DevOps 工作流程

## 概述

`qtcloud-devops` 是量潮数据工程的 DevOps 命令行工具，覆盖从代码到发布的完整生命周期。

**核心流程：** `code → build → test → release`

## 全局命令

| 命令 | 用途 |
|---|---|
| `qtcloud-devops status` | 聚合查看 build / test / release / contract / plan 状态 |
| `qtcloud-devops audit` | 聚合执行 build / test / release 审计 |

## Stage 说明

### 1. code — 代码管理

在提交代码前运行审计，确保代码质量：

```sh
qtcloud-devops code status          # 查看子模块同步状态
qtcloud-devops code audit           # 审计：scope 目录、TODO/FIXME 密度、语法检查
```

### 2. build — 构建

```sh
qtcloud-devops build status         # 查看构建状态
qtcloud-devops build clean          # 清理构建产物（target/、dist/ 等）
qtcloud-devops build audit          # 审计：编译器配置、CI 工作流、依赖声明
```

### 3. test — 测试

```sh
qtcloud-devops test status          # 查看测试状态
qtcloud-devops test clean           # 清理测试产物（覆盖率报告等）
qtcloud-devops test audit           # 审计：测试覆盖率、错误变体覆盖、门禁达标
```

### 4. release — 发布

发布前必须完成 build 和 test 审计。发布流程：

```sh
qtcloud-devops release status       # 查看当前版本状态（版本号、标签、CHANGELOG）
qtcloud-devops release audit        # 发布预检：检查版本号、CHANGELOG、标签冲突
qtcloud-devops release publish      # 执行发布：更新 CHANGELOG → 打 tag → 推送 → 创建 GitHub Release
```

## 跨 Stage 命令

| 命令 | 用途 |
|---|---|
| `qtcloud-devops plan status` | 查看 ROADMAP 进度 |
| `qtcloud-devops plan audit` | 审计 ROADMAP 与 TODO 的一致性 |
| `qtcloud-devops plan doctor` | 修复 ROADMAP 和 TODO 格式 |
| `qtcloud-devops plan clean` | 删除 scope 已完成条目 |
| `qtcloud-devops source status` | 检查系统依赖（git、gh、python、rust 等） |

## 推荐工作流

### 日常开发

```sh
# 1. 检查环境
qtcloud-devops source status

# 2. 代码审计
qtcloud-devops code audit

# 3. 构建验证
qtcloud-devops build status

# 4. 测试
qtcloud-devops test status
```

### 发布新版本

```sh
# 1. 预检
qtcloud-devops release audit

# 2. 发布
qtcloud-devops release publish

# 3. 验证
qtcloud-devops release status
```

## 注意事项

- 发布前必须通过 `release audit` 预检，否则 `publish` 会拒绝执行
- `code audit` 应在每次提交前运行，确保子模块同步和代码质量
- `plan doctor` 可自动修复 ROADMAP.md 和 TODO.md 的格式问题
- 子模块路径变更后，请运行 `qtcloud-devops code status` 确认同步状态

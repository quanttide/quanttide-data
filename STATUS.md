# quanttide-data 状态报告

> 更新日期：2026-07-20
> 最新主仓库 commit：407c4d4

## 子模块引用状态

本次更新了以下子模块到最新：

| 子模块 | 更新前 | 更新后 | 版本 |
|--------|--------|--------|------|
| apps/qtcloud-data | 2669db9 | 2669db9 | cli/v0.1.0-alpha.1 (未变) |
| data/journal | 8fbd8c0 | 3302eb8 | heads/main |
| packages/quanttide-data-toolkit | fd857d5 | a6ccd67 | dart/v0.3.0-2-ga6ccd67 |
| apps/qtclass | — | 9eae6f7 | **新增** |

其余子模块已处于最新版本，无需更新。

## Apps 进度

### qtdata (`apps/qtdata`)

- **仓库**：`quanttide/qtdata`
- **最新版本**：v0.0.2 (2026-06-23)
- **最新 commit**：`70f0d38` (2026-07-11) — "docs: 引导引擎 → 叙事蓝图"
- **技术栈**：Rust CLI + Python FastAPI Provider + Flutter Studio

| 组件 | 状态 | 说明 |
|------|------|------|
| CLI (`src/cli`) | v0.0.2 已实现 | blueprint/scope/quotation/delivery 四命令；读 Markdown → LLM → 结构化输出 |
| Provider (`src/provider`) | v0.0.1 已实现 | FastAPI，Project/Task CRUD，内存存储 |
| Studio (`src/studio`) | v0.0.1 已实现 | Flutter 四列看板（需求→约定→执行→交付） |

**关键差距**（详见 `apps/qtdata/STATUS.md`）：CLI 是本地单用户工具，与 intention/journal 中的平台化战略目标（三方体系、供应链整合、跨业务联动）存在系统性差距。

### qtclass (`apps/qtclass`)

- **仓库**：`quanttide/qtclass`
- **最新版本**：v0.0.2 (2026-05-16)
- **最新 commit**：`9eae6f7` (2026-07-11) — "docs: 补充产品定位文档"
- **技术栈**：Flutter Studio

| 组件 | 状态 | 说明 |
|------|------|------|
| Studio (`src/studio`) | v0.0.2 已实现 | 课时详情页 + Lecture 数据模型；使用 `quanttide_course` 包 |

**注意**：qtclass 无 CLI、无 Provider，仅有 Flutter Studio 前端。相对于 qtdata 的三件套架构（CLI+Provider+Studio），qtclass 目前只有展示层。

### qtcloud-data (`apps/qtcloud-data`)

- **仓库**：`quanttide/qtcloud-data`
- **最新版本**：cli/v0.1.0-alpha.1
- **最新 commit**：`2669db9` — "release: cli v0.1.0-alpha.1 — Blueprint five-command set"

## quanttide-tech 个人工作空间进度

### qtdata-* 系列

| 仓库 | 最后活跃 | 进度 |
|------|---------|------|
| qtdata-zhangyang | 2026-07-12 | sec-credit-cleaner 持续更新 |
| qtdata-private | 2026-07-14 | Asset audit skill 迁移到 `.agents/skills/` |
| qtdata-enhe | 2026-07-07 | Python 项目初始化，客户文档 |
| qtdata-huangjian | 2026-07-03 | v0.1.0，uspto-entity-matcher |
| qtdata-wangtong | 2026-07-03 | 第二大脑个人工作空间 |
| qtdata-laiyunzu | 2026-07-03 | garment-factory-cleaner |
| qtdata-langdong | 2026-07-03 | 刚初始化 |
| qtdata-fenghan | 2026-07-03 | 刚初始化 |

### qtclass-* 系列

| 仓库 | 最后活跃 | 进度 |
|------|---------|------|
| qtclass-baoyuhang | 2026-07-15 | 咨询记录持续更新（最活跃） |
| qtclass-private | 2026-07-15 | 跟踪 qtclass-baoyuhang 子模块 |
| qtclass-zstu | 2026-07-13 | 文件上传 |
| qtclass-caihongzuo | 2026-07-13 | 业务目录 + 第二大脑升级 |

## 其他 scope 子模块

| Scope | 子模块 | 状态 |
|-------|--------|------|
| data/ | context, intention, insight, roadmap, profile, journal, archive, brochure, history, library, report | 全部 heads/main |
| docs/ | tutorial, handbook, specification, gallery, essay, bylaw | 全部 heads/main |
| packages/ | quanttide-data-toolkit, quanttide-toolkit, quanttide-agent-toolkit | 全部 heads/main |
| examples/ | default, company | 全部 heads/main |

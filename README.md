# 量潮数据工程 (`quanttide-data`)

量潮第二大脑的数据工程领域仓库。涵盖数据工程相关的文档、数据、应用与工具，采用 Git 子模块架构统一管理。

## 文档边界

本仓库涉及两类文档，分工不同：

| 类型 | 位置 | 角色 | 回答的问题 |
|---|---|---|---|
| **spec（规范）** | `docs/specification/` | 结构与格式 | 长什么样 |
| **bylaw（章程）** | `docs/bylaw/` | 规则与治理 | 必须做什么 |

- spec 定义目录结构、文件格式、字段定义、命名约定
- bylaw 定义流程要求、质量约束、变更规则、跨领域边界
- 两者不重复，各自回答不同层面的问题

## 子模块

### apps/ — 应用

| 子模块 | 说明 |
|--------|------|
| `qtcloud-data` | 数据云 CLI，封装数据需求文档（DRD）流程 |
| `qtdata` | 数据工程工具链：CLI + Provider + Studio |

### data/ — 数据仓库

| 子模块 | 说明 |
|--------|------|
| `archive` | 归档数据 |
| `brochure` | 宣介材料 |
| `context` | 上下文资料 |
| `history` | 历史记录 |
| `insight` | 洞察分析 |
| `intention` | 意图与规划 |
| `journal` | 工作日志 |
| `library` | 知识库 |
| `profile` | 画像档案 |
| `report` | 报告 |
| `roadmap` | 路线图 |

### docs/ — 文档

| 子模块 | 说明 |
|--------|------|
| `bylaw` | 数据工程章程（规则与治理） |
| `essay` | 数据工程随笔 |
| `gallery` | 数据工程案例库 |
| `handbook` | 数据工程手册 |
| `specification` | 数据工程规范（结构与格式） |
| `tutorial` | 数据工程教程 |

### examples/ — 实验室

| 子模块 | 说明 |
|--------|------|
| `company` | 商业实体实验室 |
| `default` | 实验室入口（实验性/原型项目） |

### packages/ — 工具包

| 子模块 | 说明 |
|--------|------|
| `quanttide-agent-toolkit` | AI Agent 工具包 |
| `quanttide-data-toolkit` | 数据工程工具包（Dart/Flutter SDK） |
| `quanttide-toolkit` | 通用工具包 |

## 相关链接

- [量潮第二大脑](https://github.com/quanttide/quanttide) — 根仓库
- [量潮数据工作手册](https://github.com/quanttide/quanttide-handbook-of-data-engineering) — 数据工程手册
- [量潮数据工程标准](https://github.com/quanttide/quanttide-specification-of-data-engineering) — 数据工程规范

## 许可证

[CC BY 4.0](LICENSE)

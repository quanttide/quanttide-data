# 量潮数据工程 (`quanttide-data`)

量潮第二大脑的数据工程领域仓库。涵盖数据工程相关的文档、数据、应用与工具，采用 Git 子模块架构统一管理。

## 范畴结构

本仓按量潮第二大脑范畴组织：20 个子范畴分处陈述型与程序型两个九宫格，Context 与 Archive 不入格。五个目录轴承载这些子范畴——`data/` 承载陈述型，`docs/`、`packages/`、`apps/`、`examples/` 按消费对象分层承载程序型。每个子范畴是独立子模块，命名与目录均以范畴定义为依据。

### 陈述型记忆（`data/`）——知道什么

| 位置 | 事件 | 语义 | 自我 |
|:--|:--|:--|:--|
| 过去 | `data/report` 报告 | `data/library` 图书馆 | `data/history` 历史 |
| 现在 | `data/journal` 日志 | `data/profile` 档案 | `data/brochure` 宣传册 |
| 未来 | `data/roadmap` 路线图 | `data/insight` 洞察 | `data/intention` 愿景 |

### 程序型记忆（`docs/` `packages/` `apps/` `examples/`）——怎么做事

| 位置 | 规则（`docs/`） | 建模（`docs/`） | 应用 |
|:--|:--|:--|:--|
| 宪法 | `docs/bylaw` 章程 | `docs/specification` 工程标准 | `packages/` 标准库 |
| 法律 | `docs/handbook` 手册 | `docs/gallery` 案例 | `apps/` 平台 |
| 法理 | `docs/tutorial` 教程 | `docs/essay` 论文 | `examples/quanttide-data-lab` 实验室 |

应用列的三个约束力层次分别落位：标准库在 `packages/`（`quanttide-data-toolkit`、`quanttide-agent-toolkit`），平台在 `apps/`（`qtdata` 工具链、`qtcloud-data` 数据云），实验室在 `examples/quanttide-data-lab`。

### 两端

- `data/context` 语境——入口：日常工作中未成形、未分类、跨域的内容先进这里，再向九宫格发散。当前已迁空，保留入口位置。
- `data/archive` 归档——出口：两个九宫格过时的内容归此，保存备查而非弃置。

## 主干流向

**Context（入口）→ 陈述型（知道什么）→ 程序型（怎么做事）→ Archive（出口）**

陈述型到程序型之间是提炼，不是移置——换个目录放不等于变成程序型。提炼走四步：从事件里认出模式，收敛成命题（进 insight），定成规范（进 bylaw、specification），写成做法付诸执行（进 handbook、tutorial、gallery，或可执行的 toolkit 与 platform）。

提炼是否成立的判据：照着程序型内容，换一个人或换一个 AI 能不能做出同样的结果。做不到，它仍只是陈述型套上了程序型的形式。

## 许可证

[CC BY 4.0](LICENSE)

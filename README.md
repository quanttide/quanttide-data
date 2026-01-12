# Quanttide Data

量潮数据工程知识库，包含数据工程相关的教程、手册和标准文档。

## 项目结构

```
quanttide-data/
├── docs/                    # 文档类项目
│   ├── tutorial/           # 数据工程教程
│   ├── handbook/           # 数据工程手册
│   └── specification/      # 数据工程标准
└── src/                     # 源代码类项目
    └── qtcloud-data/       # 数据云
```

## 子项目

- **docs/tutorial** - 数据工程教程
- **docs/handbook** - 数据工程手册
- **docs/specification** - 数据工程标准
- **src/qtcloud-data** - 数据云

## 快速开始

克隆此仓库时会自动包含所有子模块：

```bash
git clone --recurse-submodules https://github.com/quanttide/quanttide-data.git
```

如果已经克隆了仓库，可以单独获取子模块：

```bash
git submodule update --init --recursive
```

## 更新子模块

更新所有子模块到最新版本：

```bash
git submodule update --remote
```

更新特定子模块：

```bash
cd <submodule-path>
git pull origin main
cd ..
git add <submodule-path>
git commit -m "Update <submodule-path>"
```

# Quanttide Data

量潮数据工程知识库，包含数据工程相关的教程、手册和标准文档。

## 子项目

- **qtcloud-data** - 数据云
- **quanttide-tutorial-of-data-engineering** - 数据工程教程
- **quanttide-handbook-of-data-engineering** - 数据工程手册
- **quanttide-specification-of-data-engineering** - 数据工程标准

## 快速开始

克隆此仓库时会自动包含所有子模块：

```bash
git clone --recurse-submodules git@github.com:quanttide/quanttide-data.git
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
cd <submodule-name>
git pull origin main
cd ..
git add <submodule-name>
git commit -m "Update <submodule-name>"
```

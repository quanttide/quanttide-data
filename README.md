# 量潮数据工程(`quanttide-data`)

## 项目结构

```
quanttide-data/
├── docs/                    # 文档类项目
│   ├── tutorial/           # 数据工程教程
│   ├── handbook/           # 数据工程手册
│   ├── alternative/        # 数据工程竞品
│   ├── specification/      # 数据工程标准
│   └── profile/            # 数据工程档案
├── src/                     # 源代码类项目
│   ├── qtcloud-data/       # 数据云
│   └── toolkit/            # 数据工程工具箱
├── examples/                # 示例类项目
│   ├── quanttide-example-of-data-engineering/  # 数据工程示例
│   └── quanttide-example-of-big-data/         # 大数据示例
└── tests/                   # 测试类项目
    └── fixtures/           # 测试数据集
```

## 子项目

- **docs/tutorial** - 数据工程教程
- **docs/handbook** - 数据工程手册
- **docs/alternative** - 备选方案文档
- **docs/specification** - 数据工程标准
- **docs/profile** - 数据工程画像
- **src/qtcloud-data** - 数据云
- **src/toolkit** - 数据工具包（Python/Flutter/Django SDK）
- **examples/quanttide-example-of-data-engineering** - 数据工程示例
- **examples/quanttide-example-of-big-data** - 大数据示例
- **tests/fixtures** - 测试数据集

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

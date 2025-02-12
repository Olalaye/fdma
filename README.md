# File Description Management Assistant (FDMA)

FDMA 是一个文件描述管理助手，用于管理文件描述信息，方便您为不可编辑的文件添加描述信息，从而更好地管理文件的多个版本和依赖项。

## 功能和特点

- **添加文件描述**：记录文件的名称、MD5值、依赖项和描述信息。
- **可视化文件描述**：打印已有的文件描述信息，便于查看。


## 安装

您可以通过 `pip` 安装FDMA：

```sh
pip install fdma
```


## 使用说明

安装完成后，您可以通过 FDMA 命令来使用FDMA工具。以下是一些常用命令的示例：

### 添加文件描述

```
FDMA add <file_path> <dependencies> <description>
```
示例：
```
FDMA add test.so dummyLib1.so dummyLib2.so "这是一个测试文件"
```
该命令将添加文件 test.so 的描述信息，包括文件的依赖项和描述。

### 可视化文件描述

```
FDMA visualize
```
该命令将打印已有的文件描述信息，便于查看和管理。

保存和可视化的信息示例：
```
# 版本描述

Name: test.so
md5: 0qaea24q3q2axxx
Deps: dummyLib1.so, dummyLib2.so
Desc: 这是一个测试文件

----

Name: test.1.so
md5: 0q123sea24q3r2saxxx
Deps: dummyLib1.so, dummyLib2.so
Desc: 这是另一个测试文件

----

```

## 贡献指南

欢迎贡献！如果您有任何建议或发现了问题，请提交`Issue`或`Pull Request`。


## 提交Issue

1. 确保您的问题未在已有的`Issue`中提到。
2. 提供详细的信息和重现步骤。


## 提交Pull Request

1. `Fork`本仓库。
2. 创建一个新的分支 (`git checkout -b feature/YourFeature`)。
3. 提交您的修改 (`git commit -am 'Add some feature'`)。
4. 推送到分支 (`git push origin feature/YourFeature`)。
5. 提交一个`Pull Request`。


## 许可证

本项目基于MIT许可证开源，详情请参见`LICENSE`文件。
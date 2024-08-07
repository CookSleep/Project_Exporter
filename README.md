# 项目文件导出工具
![image](https://github.com/user-attachments/assets/4cf70ba3-1237-47e7-9028-4e975c072e08)

![image](https://github.com/user-attachments/assets/33fa68ad-629e-418c-85ec-b6caecdb87ce)


## 简介

这是一个使用PyQt5开发的项目文件导出工具。它允许用户通过拖拽或选择文件夹的方式将项目文件夹到工具窗口中，然后自动生成项目的文件结构和具体内容（可选）的文本文件。

该工具旨在方便开发者直接通过上下文向LLM传递项目的详细信息。

本项目的代码几乎完全由GPT-4o、Claude 3.5 Sonnet编写，我仅提供需求和建议。

## 功能特点

- 自动生成项目的文件结构树
- 提取每个文件的代码内容并写入输出文件（可选）
- 使用XML标签包裹文件内容，便于LLM更好地读取文件
- 将导出的文本文件放置在导入的项目文件目录中
- 实时显示导出状态和输出文件路径

## 使用方法

1. 前往 [Releases](https://github.com/CookSleep/Project_Exporter/releases) 页面
2. 下载最新版本的 `Project_Exporter.zip`。
3. 解压 `Project_Exporter.zip`。
4. 双击运行 `项目文件导出工具.exe`。
5. 将需要导入的项目文件夹拖入程序窗口/点击“选择文件夹”选择需要导出的文件夹。
6. 在输出完成后，前往刚刚选择的项目目录（在输出框也有显示）查找输出文件。
7. 复制粘贴全文到LLM的上下文窗口中，继续你和LLM的项目研究之旅。

## 贡献

如果您对本项目有任何建议或意见，欢迎提交Issue或Pull Request。

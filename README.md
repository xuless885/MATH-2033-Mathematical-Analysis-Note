# MATH 2033 & 3033 — Mathematical Analysis Notes

> HKUST Undergraduate Mathematical Analysis I & II — LaTeX 笔记与讲义

[![GitHub last commit](https://img.shields.io/github/last-commit/xuless885/MATH-2033-Mathematical-Analysis-Note)](https://github.com/xuless885/MATH-2033-Mathematical-Analysis-Note)

---

## 项目结构

```
MATH 2033+3033 Note/
├── .vscode/                  # VSCode 工作区配置
│   ├── settings.json         # 编辑器 + LaTeX Workshop 全局设置
│   ├── tasks.json            # 编译任务（完整编译 / 清理）
│   └── extensions.json       # 推荐扩展
├── MATH 2033 Analysis/       # 数学分析 (I) — Real Analysis
│   ├── .vscode/              # 项目级 LaTeX Workshop 配置
│   ├── Images/               # 插图资源
│   ├── LegrandOrangeBook.cls # 文档类（基于 Legrand Orange Book）
│   ├── indexstyle.ist        # 索引样式
│   ├── sample.bib            # 参考文献
│   ├── plot_sequence.py      # Python 绘图脚本
│   └── HKUST AnalysisI (UG).tex  # 主 TeX 源文件
├── MATH 3033 Analysis/       # 数学分析 (II) — Complex & Advanced
│   ├── .vscode/
│   ├── Images/
│   ├── LegrandOrangeBook.cls
│   ├── indexstyle.ist
│   ├── sample.bib
│   ├── plot_sequence.py
│   └── HKUST AnalysisII (UG).tex
├── .gitignore
├── .gitattributes
└── README.md
```

## 编译指南

### 环境要求

- **LaTeX 发行版**：TeX Live 2024+（含 `xelatex`、`biber`）
- **Python 3.11+**（可选，仅绘图脚本需要 `plot_sequence.py`）
- **字体**：需安装中英文字体（XeLaTeX 调用系统字体）

### VSCode 一键编译（推荐）

1. 安装推荐扩展（打开项目时会自动提示）：
   - **LaTeX Workshop** (James Yu)
   - LaTeX Utilities (tecosaur)
2. 打开 `.tex` 文件，保存即自动编译（`onSave`）。
3. 或按 `Ctrl+Shift+B` 选择编译任务。

### 命令行编译

```bash
# MATH 2033
cd "MATH 2033 Analysis"
xelatex -synctex=1 -interaction=nonstopmode -file-line-error \
        -output-directory=build "HKUST AnalysisI (UG).tex"
biber build/"HKUST AnalysisI (UG)"
xelatex -synctex=1 -interaction=nonstopmode -file-line-error \
        -output-directory=build "HKUST AnalysisI (UG).tex"
xelatex -synctex=1 -interaction=nonstopmode -file-line-error \
        -output-directory=build "HKUST AnalysisI (UG).tex"

# MATH 3033（同理）
cd "MATH 3033 Analysis"
# ...
```

### 获取 PDF

PDF 文件不直接纳入版本控制。请通过以下方式获取：

- 本地编译生成（推荐）
- [GitHub Releases](https://github.com/xuless885/MATH-2033-Mathematical-Analysis-Note/releases) 下载预编译版本

---

## 贡献

本项目为个人学习笔记，欢迎指出错误或提出改进建议（Issue / PR）。

## 许可

&copy; 2026 xuless885. All rights reserved.

---

_Last updated: 2026-06-18_

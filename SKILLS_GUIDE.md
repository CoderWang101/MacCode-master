# Trae Skills Guide

这份文档介绍了当前工作区已安装的 Skills 及其使用方法。Skills 是专用的工具集，能扩展 Trae 的能力，处理特定领域的任务。

## 已安装 Skills 概览

| Skill 名称 | 功能描述 | 适用场景 (何时使用) |
| :--- | :--- | :--- |
| **algorithmic-art** | 使用 p5.js 创建生成艺术 | 需要通过代码生成艺术作品、粒子系统、流场效果时。 |
| **brand-guidelines** | 应用 Anthropic 品牌设计规范 | 需要将文档、UI 或设计调整为 Anthropic 官方品牌风格时。 |
| **canvas-design** | 创建静态视觉设计 (.png/.pdf) | 需要制作海报、艺术图、静态设计稿时。 |
| **doc-coauthoring** | 文档共创工作流 | 需要撰写技术文档、提案、决策文档，并希望通过结构化流程（收集背景、大纲、草稿、评审）完成时。 |
| **docx** | Word 文档处理 | 需要创建、读取、编辑 .docx 文件，或进行格式化排版时。 |
| **frontend-design** | 高质量前端 UI 设计 | 需要构建网页、组件、Dashboard，且要求高审美、非通用的设计风格时。 |
| **internal-comms** | 内部沟通文案写作 | 需要撰写周报、项目更新、FAQ、内部通知等公司内部文档时。 |
| **mcp-builder** | MCP 服务器构建指南 | 需要开发 Model Context Protocol (MCP) 服务器以连接外部数据或工具时。 |
| **pdf** | PDF 文件处理 | 需要读取、合并、拆分、旋转 PDF，或进行 OCR、表单填写时。 |
| **performance-analyzer** | 代码性能与复杂度分析 | 需要分析代码的时间/空间复杂度，查找性能瓶颈或寻求优化建议时。 |
| **pptx** | PPT 演示文稿处理 | 需要创建、修改、读取 PowerPoint 幻灯片 (.pptx) 时。 |
| **skill-creator** | Skill 创建工具 | 需要创建新的 Skill 或更新现有 Skill 时。 |
| **slack-gif-creator** | Slack GIF 制作 | 需要制作适合 Slack 使用的动图（表情包或演示）时。 |
| **theme-factory** | 主题配色工厂 | 需要为文档、幻灯片、网页生成或应用专业的配色方案和字体主题时。 |
| **web-artifacts-builder** | 复杂 Web 制品构建 | 需要构建包含状态管理、路由或复杂组件（React + Tailwind + shadcn/ui）的 Web 应用时。 |
| **webapp-testing** | Web 应用测试 | 需要使用 Playwright 对本地 Web 应用进行功能测试、UI 调试或截图时。 |
| **xlsx** | Excel 表格处理 | 需要创建、读取、编辑 .xlsx/.csv 文件，进行数据清洗或公式计算时。 |

## 如何使用

通常情况下，你不需要手动“调用”这些 Skill。只需在对话中**用自然语言描述你的需求**，Trae 会根据场景自动识别并使用合适的 Skill。

**示例指令：**

*   **处理 Excel**: "帮我把 `data.csv` 里的数据清洗一下，生成一个带图表的 Excel 报表。" (自动触发 `xlsx`)
*   **分析代码**: "分析一下 `main.cpp` 的时间复杂度。" (自动触发 `performance-analyzer`)
*   **生成 PPT**: "根据这份 markdown 文档生成一个 10 页的 PPT。" (自动触发 `pptx`)
*   **前端开发**: "帮我写一个现代风格的登录页面，要用 React 和 Tailwind。" (自动触发 `frontend-design` 或 `web-artifacts-builder`)
*   **PDF 操作**: "把这三个 PDF 合并成一个。" (自动触发 `pdf`)

## Skill 详细说明

### 1. 文件处理类 (xlsx, docx, pptx, pdf)
这些 Skill 提供了对常见办公文档的深度支持。不仅仅是简单的读写，还支持：
*   **xlsx**: 公式计算、格式设置、图表生成。
*   **docx**: 样式应用、目录生成、修订模式。
*   **pptx**: 幻灯片布局、母版编辑。
*   **pdf**: OCR 文字识别、表单填写、页面操作。

### 2. 创作与设计类 (frontend-design, canvas-design, algorithmic-art)
当你需要高质量的视觉输出时使用。
*   **frontend-design**: 专注于避免“AI味”的通用设计，产出具有独特审美的前端代码。
*   **canvas-design**: 产出静态的设计图。
*   **algorithmic-art**: 产出基于代码的动态/生成式艺术。

### 3. 开发辅助类 (performance-analyzer, webapp-testing, mcp-builder)
辅助软件开发过程。
*   **performance-analyzer**: 专业的复杂度分析报告。
*   **webapp-testing**: 自动化测试脚本生成与执行。
*   **mcp-builder**: 扩展 AI 能力的协议开发。

### 4. 写作辅助类 (doc-coauthoring, internal-comms)
提供结构化的写作指导，而不仅仅是生成文本。
*   **doc-coauthoring**: 引导你一步步完成复杂文档，确保内容逻辑严密。
*   **internal-comms**: 遵循企业沟通的最佳实践。

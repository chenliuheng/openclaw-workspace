---
name: guizang-ppt
description: "使用归藏老师的 guizang-ppt-skill 生成瑞士国际主义风格的PPT。触发词：'瑞士风PPT'、'瑞士风'、'guizang PPT'、'帮我做一份瑞士风PPT'、'克莱因蓝'、'柠檬黄'、'柠檬绿'、'安全橙'。包含22个内置版式、GPT-Image配图生成、多平台封面（公众号/小红书/视频号）。"
---

# 归藏PPT Skills

基于 guizang-ppt-skill (github.com/op7418/guizang-ppt-skill)，瑞士国际主义风格。

## 核心风格

**瑞士国际主义 (Swiss Style)**：
- 无衬线字体 (Helvetica/Inter)
- 单一高饱和锚点色
- 网格至上 (16列grid + 16px gap)
- 直角纯色 (无border-radius/box-shadow/渐变)

## 四套主题色

| 主题色 | 适用场景 |
|--------|----------|
| **克莱因蓝 IKB** (默认) | 通用、商业发布、AI产品 |
| **柠檬黄** | 年轻、运动、零售、Y2K复古 |
| **柠檬绿** | 生态、可持续、Z世代品牌 |
| **安全橙** | 警示、新闻、活力主题 |

**重要**：不接受自定义hex色值。

## 22个内置版式

- Cover封面、Statement巨字宣言、KPI Tower柱阵
- Loop Diagram闭环图、Duo Compare对照
- Closing Manifesto收尾
- 横向时间线、Three Forces三力对峙
- System Diagram系统层级、Why Now三论点
- Tech Spec产品规格、Image Hero案例图等

## 7条设计纪律

1. **单一锚点色**：一份deck只允许一个高亮色
2. **极致字号对比**：主标题与正文比例至少8:1
3. **大字越细**：主标题字重200 (ExtraLight)，不能用700+
4. **直角纯色**：无border-radius、无box-shadow、无渐变
5. **网格至上**：16列grid+16px gap，左对齐+大幅留白
6. **无WebGL背景**：纯白底为底色
7. **封面/封底色彩闭环**：首尾用同一色彩主旋律

## 配图能力

如果用户需要配图，使用 **GPT-Image 2.0**：

- 人文纪实照片（胶片质感、Fujifilm质感）
- 信息图（流程、对比、系统关系）
- 截图再设计（按PPT比例重做）
- 数据大字报、流程图、系统关系图

**自动适配**：生成图自动适配当前deck的风格和主题色。

## 多平台封面

| 平台 | 规格 |
|------|------|
| 公众号 | 21:9头图 + 1:1分享卡 |
| 小红书 | 3:4竖图 |
| 视频号 | 横版封面 |

**触发方式**：让AI "基于这份PPT的核心观点，给我一张3:4的小红书封面"

## 使用流程

1. 用户说"帮我做一份瑞士风PPT"
2. 询问选择哪种主题色（克莱因蓝/柠檬黄/柠檬绿/安全橙）
3. 6个澄清问题确认内容
4. 确认后生成PPT
5. 可选：生成配图或多平台封面

## GitHub

- 仓库：github.com/op7418/guizang-ppt-skill
- 触发新风格：说"帮我做一份瑞士风PPT"
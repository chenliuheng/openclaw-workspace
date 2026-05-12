# PPT Skills (归藏老师 guizang-ppt-skill)

## 核心风格
- **瑞士国际主义 (Swiss Style)**：无衬线字体、单一高饱和锚点色、网格至上、直角纯色
- **四套主题色**：
  - 克莱因蓝 IKB (默认)：通用、商业发布、AI产品
  - 柠檬黄：年轻、运动、零售、Y2K复古
  - 柠檬绿：生态、可持续、Z世代品牌
  - 安全橙：警示、新闻、活力主题

## 22个内置版式
- Cover封面、Statement巨字宣言、KPI Tower柱阵、Loop Diagram闭环图
- Duo Compare对照、Closing Manifesto收尾、横向时间线、三力对峙、系统层级
- Why Now三论点、Tech Spec产品规格、Image Hero案例图等

## 7条设计纪律
1. **单一锚点色**：一份deck只允许一个高亮色
2. **极致字号对比**：主标题与正文比例至少8:1
3. **大字越细**：主标题字重200 (ExtraLight)，不能用700+
4. **直角纯色**：无border-radius、无box-shadow、无渐变
5. **网格至上**：16列grid+16px gap，左对齐+大幅留白
6. **无WebGL背景**：纯白底为底色
7. **封面/封底色彩闭环**：首尾用同一色彩主旋律

## 配图能力 (GPT-Image 2.0)
- 人文纪实照片（胶片质感、Fujifilm质感）
- 信息图（流程、对比、系统关系）
- 截图再设计（按PPT比例重做）
- 数据大字报、流程图、系统关系图
- 自动适配当前deck风格和主题色

## 多平台封面
- 公众号：21:9头图 + 1:1分享卡
- 小红书：3:4竖图
- 视频号：横版封面
- 批量生成时风格统一、字号一致、版式各异

## GitHub
- 仓库：github.com/op7418/guizang-ppt-skill
- 安装方式：复制README中的"给AI的安装prompt"给AI Agent
- 触发新风格："帮我做一份瑞士风PPT"

---

# Grsai API 配置

## API 配置
- 地址：https://grsai.dakka.com.cn
- Key：sk-bd5389b636e74686a2a16f875ae3de15

## 生图接口
- Endpoint: POST /v1/draw/completions
- 模型：gpt-image-1.5, sora-image

## 使用示例
```python
import requests

url = 'https://grsai.dakka.com.cn/v1/draw/completions'
headers = {
    'Authorization': 'Bearer sk-bd5389b636e74686a2a16f875ae3de15',
    'Content-Type': 'application/json'
}
data = {
    'model': 'gpt-image-1.5',
    'prompt': '你的提示词',
    'size': '1:1'
}

resp = requests.post(url, headers=headers, json=data, stream=True)
# 处理流式响应...
```

## 查询结果
- Endpoint: POST /v1/draw/result
- 需要任务ID

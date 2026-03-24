# 微信公众号文章模板标准

## 标题格式
```html
<h2 style="font-size: 24px; color: #1a1a1a; margin: 20px 0 15px 0;">{标题}</h2>
```

## 开场白
```html
<p style="font-size: 15px; color: #666666; margin: 10px 0;">小伙伴们好呀～👋</p>
<p style="font-size: 15px; color: #333333; margin: 10px 0;">{开场内容}</p>
```

## Part标题（分章节）
```html
<h3 style="font-size: 20px; color: #e74c3c; margin: 25px 0 15px 0;">Part 1：{章节标题}</h3>
```
颜色轮换：#e74c3c（红）→ #27ae60（绿）→ #9b59b6（紫）→ #3498db（蓝）

## 步骤流程
```html
<p style="font-size: 15px; color: #3498db; margin: 15px 0 5px 0;">📱 <strong>第一步：{步骤名}</strong></p>
<p style="font-size: 14px; color: #666666; margin: 5px 0 15px 25px;">{步骤说明}</p>
```

## 重点内容
```html
<p style="font-size: 15px; color: #333333; margin: 10px 0; padding-left: 15px;">✅ {重点1}<br>
✅ {重点2}</p>
```

## 场景描述
```html
<p style="font-size: 15px; color: #333333; margin: 12px 0;"><strong>🌸 {场景名}</strong>：{场景说明}</p>
```

## 结尾引导
```html
<p style="font-size: 16px; color: #e74c3c; margin: 20px 0; text-align: center;">{互动引导}</p>
<p style="font-size: 18px; color: #27ae60; margin: 20px 0; text-align: center;">{总结语}</p>
```

## 标签
```html
<p style="font-size: 13px; color: #999999; margin: 25px 0 10px 0;">#标签1 #标签2 #标签3</p>
```

---

## 快速生成脚本

```python
def generate_wechat_article(title, parts, scenes, ending, tags):
    html = f'''
<h2 style="font-size: 24px; color: #1a1a1a; margin: 20px 0 15px 0;">{title}</h2>

<p style="font-size: 15px; color: #666666; margin: 10px 0;">小伙伴们好呀～👋</p>
'''
    colors = ['#e74c3c', '#27ae60', '#9b59b6', '#3498db']
    for i, (part_title, part_content) in enumerate(parts):
        html += f'''
<h3 style="font-size: 20px; color: {colors[i%4]}; margin: 25px 0 15px 0;">Part {i+1}：{part_title}</h3>
<p style="font-size: 15px; color: #333333; margin: 10px 0;">{part_content}</p>
'''
    html += f'''
<h3 style="font-size: 20px; color: #9b59b6; margin: 25px 0 15px 0;">应用场景</h3>
'''
    for scene in scenes:
        html += f'<p style="font-size: 15px; color: #333333; margin: 12px 0;"><strong>{scene}</strong></p>'
    
    html += f'''
<h3 style="font-size: 20px; color: #1a1a1a; margin: 25px 0 15px 0;">最后说两句</h3>
<p style="font-size: 15px; color: #333333; margin: 10px 0;">{ending}</p>
<p style="font-size: 13px; color: #999999; margin: 25px 0 10px 0;">{" ".join(["#"+t for t in tags])}</p>
'''
    return html
```

---

## 注意事项
- 内容长度：800-1500字
- 标题长度：不超过20字
- 称呼：统一用"小伙伴们"或"打工人"
- 风格：轻松诙谐，带emoji
- 互动：结尾引导评论

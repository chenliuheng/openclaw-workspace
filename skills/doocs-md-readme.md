# doocs/md 微信公众号排版工具

## 是什么
微信 Markdown 编辑器 - 把 Markdown 渲染成微信公众号可用的样式

## 在线使用
- 地址：https://md.doocs.org
- 12.1k stars, 2.1k forks

## 核心功能
- ✅ 完整 Markdown 支持
- ✅ 数学公式 LaTeX
- ✅ Mermaid/PlantUML 图表
- ✅ 代码高亮
- ✅ 多图床支持（公众号自带/阿里云/GitHub等）
- ✅ AI 辅助创作

## 使用流程

### 方法1：在线编辑器
1. 打开 https://md.doocs.org
2. 左边写 Markdown
3. 右边预览效果
4. 点击"复制"按钮复制渲染后的内容
5. 直接粘贴到公众号后台

### 方法2：CLI 工具（推荐自动化）
```bash
# 安装
npm i -g @doocs/md-cli

# 启动
md-cli

# 指定端口
md-cli port=8899
```

### 方法3：Docker 部署私有
```bash
docker run -d -p 8080:80 doocs/md:latest
```

## 自动化集成方案

由于是网页应用，我可以：
1. 用浏览器打开 md.doocs.org
2. 自动输入 Markdown 内容
3. 自动点击复制按钮
4. 然后粘贴到公众号

或者使用 CLI 版本本地运行，这样更适合自动化。

需要我先写一个自动化脚本来调用这个编辑器吗？

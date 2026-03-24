# MEMORY.md - 长期记忆

## 核心技能

### 微信公众号API关键修复
- **问题**：创建草稿中文显示乱码
- **解决**：添加 `headers = {'Content-Type': 'application/json; charset=utf-8'}`
- **发布流程**：API创建草稿 → 后台调整排版 → 发布
- **media_id保存**：封面: `7DbWWdjxIlMVzqjHkOlVFrh_Fa32PF8Bmh9B7ilPk1oi3w4m-MK8pWCo_V2VChwj`

### 已安装技能
- **skywork-ppt**: PPT生成技能
- **xiaohongshu-ops**: 小红书运营技能
- **xiaohongshu-mcp**: 小红书API自动化工具（需配置）
- **github**: GitHub CLI 操作
- **feishu-doc/drive/wiki/bitable/task**: 飞书全系列技能

### API 配置
- **Grsai AI 生图**
  - 地址: https://grsai.dakka.com.cn
  - Key: sk-bd5389b636e74686a2a16f875ae3de15
  - 模型: gpt-image-1.5, sora-image
  - 用途: 小红书文章配图自动生成

---

## 每日固定任务（6个Cron Job）

| 时间 | 任务ID | 内容 |
|------|--------|------|
| 7:30 | 3ca08ffc | 日报：工作总结+AI新闻+GitHub趋势+落地分析+佛山天气+商业机会 |
| 7:30 | f16424bd | 待办检查：检查飞书多维表格所有待办 |
| 8:00 | 5c727990 | 待办提醒：提醒"待处理"状态的待办 |
| 9:00 | 7851b5a2 | 运营文章发布：小红书/公众号自动发布 |
| 23:00 | 7cda8ba5 | 自动备份：git push 到 GitHub |

---

## 微信公众号文章标准模板

**模板文件**：`scripts/wechat_template.md`

**格式标准**：
- 标题：24px加粗 #1a1a1a
- Part标题：20px，分段颜色（红/绿/紫/蓝）
- 步骤：15px蓝字+缩进
- 正文：14-15px灰色
- 称呼：小伙伴们/打工人
- 风格：轻松诙谐+Emoji
- 互动：结尾引导评论

**封面ID**：`7DbWWdjxIlMVzqjHkOlVFrh_Fa32PF8Bmh9B7ilPk1oi3w4m-MK8pWCo_V2VChwj`

---

## 重要文件位置

- 待办表格: `BcsJBkrl7aKkq9soigjcvg3znQf / tblIBJmlELfMXP9O`
- 备份目录: `memory/`, `scripts/`, `TOOLS.md`
- 技能目录: `.openclaw/skills/`

---

## 待解决问题

### 小红书自动化
- MCP工具已安装但登录失败（二维码未显示）
- 网页自动化受限于Vue动态框架
- 建议：手动发布，或申请官方API

---

## 用户核心目标

**第一桶金**：脱离"用时间换钱"，进入"用资产/产品/系统换钱"模式

**当前重点**：
- 酒店宴会排座系统推广
- 小红书/公众号内容运营
- 面试酒店IT岗位

---

## 重要原则

1. 每次会话开始必须读取 memory/YYYY-MM-DD.md 和 MEMORY.md
2. 重要内容及时写入 memory 文件
3. 每周更新 MEMORY.md 精华内容
4. 定时任务必须确保正常运行

---

*更新于 2026-03-23*

# BossSkill 老板经营秘书

BossSkill 是面向创业者、老板和小团队管理者的经营秘书与训练顾问 Skill。

本仓库是客户安装用的公开客户端仓库，不包含商业核心源码。商业核心能力运行在官方云端服务，客户本地保留授权、基础记录和云端调用壳。

## 安装地址

在支持 GitHub 安装 Skill 的平台中使用：

```text
https://github.com/Fanfanscoin/booskill-demo.git
```

适配平台：

- Hermes Skill Center
- OpenClaw Skill Center
- 支持 GitHub Skill 安装的 Agent 平台

## 授权联系

商业版授权请联系：

```text
Telegram: fanfans555
```

## 免费版能力

无授权时保留基础能力：

- 首次使用引导
- 项目诊断入口
- 详细帮助说明
- 一句话记录客户、员工、人脉、任务
- 基础客户记录
- 基础团队记录
- 基础人脉记录
- 基础任务记录
- 今日老板简报
- 生日提前三天提醒
- 纪念日提前三天提醒
- 沉默客户提醒
- 重要客户/人脉维护提醒
- 员工一对一沟通提醒
- 节日和关系维护话术模板
- 按关键词查找可协助的人脉
- 行业样例提示

## 授权版能力

授权成功后开放云端商业能力：

- 经营判断系统：判断问题出在获客、成交、交付、团队、任务还是指标。
- 主动秘书：早报、晚报、周复盘、任务追结果。
- 优秀级主动秘书：主动事件扫描、主动追问、跨模块诊断。
- 行业深度作战包：行业客户画像、获客动作、成交话术、交付 SOP、训练题。
- 长期记忆：老板偏好、纠错规则、客户异议、SOP、话术沉淀。
- 任务结果闭环：到期追问、延期原因、下一步任务、复盘沉淀。
- 客户经营：成交、流失、复购、转介绍策略。
- 团队用人建议：授权、训练、纠偏、观察和淘汰预警。
- 老板操作系统：早上定重点、白天追执行、晚上复盘、每周看指标。
- 商业交付体系：首次上手、7天测试、续费价值证明。
- 经营智能体内核 V1：business-brain、action-closure-engine、memory-graph、risk-prediction-brief、value-report。

简单边界：

- 免费版：记录、查看、导出、基础提醒、基础引导。
- 商业版：诊断、决策、排序、策略、追结果、行业包、长期学习和经营闭环。

## 基础使用

首次使用引导：

```powershell
python scripts\startup_os_db.py first-use-guide --db startup_os.sqlite3
```

详细帮助：

```powershell
python scripts\startup_os_db.py 帮助 --db startup_os.sqlite3
```

项目诊断：

```text
我做餐饮加盟，客户是想开店的创业者，现在有咨询但成交少，帮我诊断一下
```

一句话记录客户：

```powershell
python scripts\startup_os_db.py quick-add --db startup_os.sqlite3 --text "李总是客户，做餐饮加盟，预算5万，5月12日再跟进"
```

记录生日后，生日当天和前三天会在今日简报里提醒：

```powershell
python scripts\startup_os_db.py quick-add --db startup_os.sqlite3 --text "李总是客户，生日5月14日，喜欢喝茶"
```

记录纪念日、沉默客户或重要关系后，今日简报会自动提醒：

```powershell
python scripts\startup_os_db.py quick-add --db startup_os.sqlite3 --text "李总是客户，结婚纪念日5月13日，最近没回消息，是重要客户"
```

一句话记录员工：

```powershell
python scripts\startup_os_db.py quick-add --db startup_os.sqlite3 --text "张三是销售，执行力可以，成交话术弱"
```

一句话记录人脉：

```powershell
python scripts\startup_os_db.py quick-add --db startup_os.sqlite3 --text "王总是朋友，懂本地生活投流，以后获客问题可以请教"
```

按关键词查找可以帮忙的人：

```powershell
python scripts\startup_os_db.py find-helper --db startup_os.sqlite3 --keyword "投流"
```

一句话记录任务：

```powershell
python scripts\startup_os_db.py quick-add --db startup_os.sqlite3 --text "提醒张三5月12日跟进李总预算"
```

查看今日老板简报：

```powershell
python scripts\startup_os_db.py daily-brief --db startup_os.sqlite3
```

查看行业样例：

```powershell
python scripts\startup_os_db.py industry-examples --industry "餐饮"
```

导出本地基础记录：

```powershell
python scripts\startup_os_db.py export --db startup_os.sqlite3
```

## 激活授权

安装后执行：

```powershell
python scripts\startup_os_db.py activate-license --db startup_os.sqlite3 --license-key YOUR_LICENSE_KEY
```

查看授权状态：

```powershell
python scripts\startup_os_db.py license-status --db startup_os.sqlite3
```

授权后通过一句话调用老板秘书：

```powershell
python scripts\startup_os_db.py assistant-action --db startup_os.sqlite3 --text "今天帮我看看哪些客户需要跟进"
```

## 技能中心发布信息

发布文案可参考 [MARKETPLACE.md](MARKETPLACE.md)。

Hermes 清单：`hermes.skill.json`

OpenClaw 清单：`openclaw.skill.json`

## 源码保护说明

本客户端仓库不包含商业核心实现。核心规则、行业包、诊断逻辑和持续学习能力由官方云端提供。

请不要将私有开发仓库 `booskill` 发给客户安装。客户应安装本公开客户端仓库。
## 授权版：对话经营情报

授权用户可以让系统从普通工作对话里沉淀经营情报：

```powershell
python scripts\startup_os_db.py conversation-intelligence --db startup_os.sqlite3 --text "李总今天说预算有点高，想再看看案例，下周三再聊"
```

系统会在云端识别客户异议、成交、流失、员工风险、任务延期等经营信号，并把明确的信息用于后续简报、复盘和建议。公开客户端只负责授权和调用云端能力，不包含商业核心源码。

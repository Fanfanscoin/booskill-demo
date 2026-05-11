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
- 行业样例提示

## 授权版能力

授权成功后开放云端商业能力：

- 老板秘书智能判断
- 行业深度包
- 持续学习知识库
- 高级经营诊断
- 客户跟进策略和话术
- 团队诊断和动作建议
- SOP 和话术沉淀

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

一句话记录员工：

```powershell
python scripts\startup_os_db.py quick-add --db startup_os.sqlite3 --text "张三是销售，执行力可以，成交话术弱"
```

一句话记录人脉：

```powershell
python scripts\startup_os_db.py quick-add --db startup_os.sqlite3 --text "王总是朋友，懂本地生活投流，以后获客问题可以请教"
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

# BossSkill 老板经营秘书

BossSkill 是面向创业者、老板和小团队管理者的经营秘书与训练顾问 Skill。

本仓库是客户安装用的公开客户端仓库，不包含商业核心源码。商业核心能力运行在官方云端服务，客户本地只保留授权、基础记录和云端调用壳。

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

- 基础客户记录
- 基础团队记录
- 基础任务记录
- 基础训练手册
- 少量本地规则

## 授权版能力

授权成功后开放云端商业能力：

- 老板秘书智能判断
- 行业深度包
- 持续学习知识库
- 高级经营诊断
- 老板偏好学习
- 误判纠错记忆
- SOP 和话术沉淀

## 激活授权

安装后执行：

```powershell
python scripts\startup_os_db.py activate-license --db startup_os.sqlite3 --license-key YOUR_LICENSE_KEY
```

查看授权状态：

```powershell
python scripts\startup_os_db.py license-status --db startup_os.sqlite3
```

## 基础使用

初始化本地数据库：

```powershell
python scripts\startup_os_db.py init --db startup_os.sqlite3
```

通过一句话调用老板秘书：

```powershell
python scripts\startup_os_db.py assistant-action --db startup_os.sqlite3 --text "今天帮我看看哪些客户需要跟进"
```

导出本地基础记录：

```powershell
python scripts\startup_os_db.py export --db startup_os.sqlite3
```

## 技能中心发布信息

发布文案可参考 [MARKETPLACE.md](MARKETPLACE.md)。

Hermes 清单：`hermes.skill.json`

OpenClaw 清单：`openclaw.skill.json`

## 源码保护说明

本客户端仓库不包含商业核心实现。核心规则、行业包、诊断逻辑和持续学习能力由官方云端提供。

请不要将私有开发仓库 `booskill` 发给客户安装。客户应安装本公开客户端仓库。

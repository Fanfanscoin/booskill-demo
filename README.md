# BossSkill Client

BossSkill 客户端安装仓库。

本仓库用于客户安装授权商业版客户端，不包含商业核心源码。商业核心能力运行在官方云端服务：

```text
https://bt.fanfan.la/api/core/run
```

## 客户安装地址

在支持 GitHub 安装 Skill 的平台中使用：

```text
https://github.com/Fanfanscoin/booskill-client.git
```

## 授权激活

安装后执行：

```powershell
python scripts\startup_os_db.py activate-license --db startup_os.sqlite3 --license-key YOUR_LICENSE_KEY
```

查看授权状态：

```powershell
python scripts\startup_os_db.py license-status --db startup_os.sqlite3
```

## 免费版能力

无授权时，只开放基础能力：

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

## 源码保护说明

本客户端仓库不包含商业核心实现。客户本地只保留授权和云端调用壳，核心规则、行业包、诊断逻辑和持续学习能力由官方云端提供。

请勿将私有开发仓库 `booskill` 发给客户安装。

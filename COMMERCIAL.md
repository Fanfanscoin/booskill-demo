# BossSkill 商业版授权说明

当前商业版只区分两种状态：

- 免费版：没有授权码或授权无效。
- 授权版：授权码有效，开放商业能力。

授权时长由授权中心创建：

- `1_month`：1个月
- `1_quarter`：1季度
- `1_year`：1年

## 免费版保留

- 基础客户记录
- 基础团队记录
- 基础任务记录
- 简单 Web 控制台
- 基础训练手册
- 少量本地规则

## 授权版开放

- 老板秘书智能判断
- 行业深度包
- 持续学习知识库
- 自动测试样例库
- 高级经营诊断
- 老板偏好学习
- 误判纠错记忆
- SOP 和话术沉淀
- 后续私有模型/agent 接入

## 激活授权

```powershell
python scripts\startup_os_db.py activate-license --db startup_os.sqlite3 --license-key YOUR_LICENSE_KEY
```

查看授权状态：

```powershell
python scripts\startup_os_db.py license-status --db startup_os.sqlite3
```

也可以使用环境变量：

```powershell
$env:BOOSKILL_LICENSE_KEY="YOUR_LICENSE_KEY"
```

## 授权中心

默认授权中心：

```text
https://bt.fanfan.la
```

授权缓存默认保留 72 小时。短时间断网时，授权版能力可以继续使用；超过缓存时间后需要重新联网校验。

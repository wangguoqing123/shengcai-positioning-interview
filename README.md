# 航海定位官

AI 自媒体轻量版，帮助船员选内容偏向、确定视频形式，完成小红书账号包装。

## 安装

仓库：[wangguoqing123/shengcai-positioning-interview](https://github.com/wangguoqing123/shengcai-positioning-interview)

### Codex

把下面整段复制到 Codex 对话框：

```text
请使用 skill-installer 安装「航海定位官」：
https://github.com/wangguoqing123/shengcai-positioning-interview

Skill 位于仓库根目录，安装名称为 shengcai-positioning-interview。
请保留 SKILL.md 和全部 references 文件，安装后检查文件是否齐全。
```

安装完成后，在下一轮对话调用。如果没有识别到，重启 Codex 再试。依据：[OpenAI 官方安装说明](https://learn.chatgpt.com/docs/build-skills#install-curated-skills-for-local-use)。

已经装过旧版时，让助手从此仓库更新这个 Skill，并保留原有账号资料。

### WorkBuddy

1. [下载 WorkBuddy 安装包](https://github.com/wangguoqing123/shengcai-positioning-interview/raw/refs/heads/main/dist/shengcai-positioning-interview-workbuddy.zip)。
2. 在 WorkBuddy 左侧进入「专家·技能·连接器」→「技能」。
3. 点击「添加技能」→「上传技能」，选择刚下载的 ZIP。
4. 在「已安装」中确认技能已启用，再在对话中调用。

依据：[WorkBuddy 官方技能安装说明](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)。本仓库提供的自定义技能使用上传方式安装。

## 使用方式

已安装本地 Skill 后，在 AI 助手中发送：

```text
使用航海定位官，帮我选择本期 AI 自媒体的内容偏向和视频形式，再给我一套昵称、头像方向和简介。
```

如果已有方向，直接说明，例如：

```text
使用航海定位官。我想分享 AI 视频玩法，不出镜，用录屏配讲解。昵称沿用“小林”，帮我完成账号包装。
```

## 会得到什么

- 一句话内容方向和视频形式。
- 一套推荐昵称、头像方向、2—3 行简介。
- 按需提供背景图文案。

本期作业：一句话内容方向＋设置后的账号主页截图和链接。

默认在对话里给结果，明确要求保存时再写文件。无需建立 Obsidian 目录。

## 文件说明

- `SKILL.md`：轻量流程与范围。
- `references/interview-guide.md`：用户不知道选什么方向时使用。
- `references/profile-bio-guide.md`：昵称、头像和简介的生成原则。
- `references/output-templates.md`：简短结果格式与按需保存规则。
- `agents/openai.yaml`：名称、说明和调用提示。

WorkBuddy 安装包由 `tools/build_workbuddy_package.py` 从主 Skill 和三个参考文件生成；仅补充 WorkBuddy 的展示与版本字段。修改源文件后，运行 `python3 tools/build_workbuddy_package.py` 重新打包。

当前版本：v0.2，AI 自媒体轻量版。调用名保留 `shengcai-positioning-interview`。

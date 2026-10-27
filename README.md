# 航海定位官

面向本期小红书 AI 自媒体航海。内置16个已核对对标及简介参考、7类21条视频和7条互动贴，通过逐步问答帮助船员选择内容方向、制作形式并完成账号包装。

当前版本：v0.3.1。案例为注明日期的课程资料快照；昵称、简介建议同时结合本人事实和真实对标结构，不编造履历或作品。

零基础只影响怎么教、先做什么。昵称与简介突出内容价值、应用场景与作品方向，不默认包装为“从0学AI”或学习打卡号。品牌合作方向通过内容与作品体现；简介不写商务合作入口或联系方式，不编经历和成绩。

## 安装

仓库：[wangguoqing123/shengcai-positioning-interview](https://github.com/wangguoqing123/shengcai-positioning-interview)

### Codex

把下面整段复制到 Codex 对话框：

```text
请使用 skill-installer 安装「航海定位官」：
https://github.com/wangguoqing123/shengcai-positioning-interview

Skill 位于仓库根目录，安装名称为 shengcai-positioning-interview。
请保留 SKILL.md 和全部 references 文件。安装后检查包含 course-context.md、benchmark-accounts.md、template-cases.md 三份课程资料，以及问答、包装和输出说明，共6份参考文件。
```

安装完成后，在下一轮对话调用。如果没有识别到，重启 Codex 再试。依据：[OpenAI 官方安装说明](https://learn.chatgpt.com/docs/build-skills#install-curated-skills-for-local-use)。

已经装过旧版时，复制下面这段：

```text
请把已安装的 shengcai-positioning-interview 更新到此仓库最新版：
https://github.com/wangguoqing123/shengcai-positioning-interview
先检查并备份此 Skill 的现有文件，再只更新该 Skill。保留我的账号资料和作业，不改其他 Skill。
检查6份 references 文件齐全，并确认当前是v0.3.1。
```

### WorkBuddy

1. [下载 WorkBuddy 安装包](https://github.com/wangguoqing123/shengcai-positioning-interview/raw/refs/heads/main/dist/shengcai-positioning-interview-workbuddy.zip)。
2. 在 WorkBuddy 左侧进入「专家·技能·连接器」→「技能」。
3. 点击「添加技能」→「上传技能」，选择刚下载的 ZIP。
4. 在「已安装」中确认技能已启用，再在对话中调用。

依据：[WorkBuddy 官方技能安装说明](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)。本仓库提供的自定义技能使用上传方式安装。

## 使用方式

先在课程1.1选3个对标，记录主页链接、简介摘录、主要内容、2条代表作、视频形式、想借鉴什么、目前能否跟做。看不清的写“待核实”，不猜。

安装完成后，在下一轮对话发送：

```text
使用航海定位官。

这是我的3个对标账号记录：
[粘贴对标记录表，或上传表格截图，并说明看不清的部分]

请先读取内置对标简介和相关样片，再结合我的回答帮我确定内容方向和视频形式。
一次只问一个问题，已回答的不重复问；我不懂的地方请用具体案例解释。
昵称和简介请参考真实对标的写法，说明借鉴点，只使用我的真实信息，不编经历、成绩或博主简介。
零基础只用于安排教学和起步任务。包装突出内容价值与作品方向，不写学习打卡标签，简介不放商务合作入口或联系方式。
最后给出账号方向与包装方案，注明参考来源和下一步，用于本关统一的「账号开工卡」。
```

不用先想好完整定位。不懂方向区别可以随时追问；已有方向、出镜方式或昵称就直接说明，AI只补关键缺口。只想修改某一项也可以直接提出。

## 会得到什么

- 准备帮助谁、主要分享什么、先试的2—3类内容及案例依据。
- 建议的视频形式与要准备的素材，说明为什么适合本人。
- 昵称、头像方向和2—3行简介，说明参考了哪些博主的表达。
- 接下来的操作顺序与待完成项。

默认在对话给结果，要求保存时才写指定位置。无需Obsidian或固定目录。Skill不会自动登录、改主页、发帖或生成视频。

## 作业与后续

关卡1统一交一份「账号开工卡」，小节不单独交作业：对标记录、账号方向、设置后的主页截图和链接、至少3条真实互动贴及观察、首条视频模板和3个扩展题目并选1个。

Skill先帮你完成方向与包装方案。设置主页后，继续1.3发布互动贴、1.4选模板，再在1.5统一交卡。关卡2创作第一条视频。互动贴不抵扣本期至少10条起号视频；另需1条软件测评／商单样片，21天争取1000赞藏。

## 内置资料与维护

- `SKILL.md`：工作流程、资料入口、逐步问答和事实边界。
- `references/course-context.md`：本期路线、内容方向与制作形式建议。
- `references/benchmark-accounts.md`：16个对标的昵称、简介节选、内容与原链接。
- `references/template-cases.md`：21条视频、7条互动贴、结构归纳、扩展题目与资料边界。
- `references/interview-guide.md`：如何结合学员回答逐步追问。
- `references/profile-bio-guide.md`：基于真实对标与本人事实做包装。
- `references/output-templates.md`：对标表、结果格式、统一作业与保存规则。
- `agents/openai.yaml`：名称、说明和调用提示。

简介与作品主要来源于课程2026-10-19已保存的公开主页资料，卡尔简介补核于2026-10-27；视频核对日期2026-10-17至20日，互动贴2026-10-26。每条附原帖或主页链接。简介为原文短节选，结构与方向为编辑归纳，联系方式省略；不包含商业报价、收入或个人凭据。未取得完整视频／提示词的地方保留未核实状态。

WorkBuddy安装包由`tools/build_workbuddy_package.py`从SKILL.md及全部6份参考文件生成，仅补充展示和版本字段。修改资料后运行`python3 tools/build_workbuddy_package.py`，再同步源文件与ZIP。

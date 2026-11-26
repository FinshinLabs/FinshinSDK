# Changelog

本项目的所有重要更改都将记录在此文件中。
格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并且本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### ⚠️ Breaking Changes

- **配置段表与代理档位撤出接口包**：`SECTIONS_BY_PLATFORM`、`ProxyMode`、`FieldKey.PROXY` 与配置里的代理段、代理模式键一并删除，平台自己的配置段改由适配器入口件交出。`ConfigPath` 的段名与键名收原串，`ConfigSection` 只剩本体自带的段。
- **适配器入口件改交段表与检查计划**：`AdapterParts` 五件，新增 `sections` 与 `plan_for`，旧的单通道探测交口撤销。
- **适配器入口件多交凭证声明**：`AdapterParts` 六件，新增的 `credential` 交凭证的名字、提示、非法提示与身份推导，仍按五件构造的旧形状在装载当场报错。
- **会话快照撤掉摘要字段**：`SessionDTO` 与 `SessionPatchDTO` 不再带 `summary`，读写会话的件按新形状构造。
- **AI 配置词表撤出接口包**：`ConfigKey` 只留 `OWNER`、`RECORD_KEEP`、`WAITING`，`ConfigSection` 只留 `DATA`。AI 插件自建段名与键名，盘上段名不变。

### ✨ Added

- **配置来源可交保存轮检查计划**：`SourceDeclaration` 新增可选 `probe`，交一份 `ConnectionPlan`，保存配置时随平台那轮并进进度表。
- **连通检查计划**：`ConnectionPlan`、`ProbeChannel`、`ProbeRow`、`ProbeResult`、`ProbeOutcome`、`PlanVerdict`、`ConfigSnapshot` 与 `PlanFactory` 一起交出，进度行、每路预算、收尾裁决与提示话术都由适配器决定。
- **字段显隐声明**：`FieldCondition` 与 `FieldSpec.visible_when`，按同段另一个字段的取值决定一行显不显示。

## [0.2.0] - 2026-11-19

### ⚠️ Breaking Changes

- **适配器入口件多交平台显示名**：`AdapterParts` 四件一起交，新增的 `title` 是本平台的显示名，配置窗左列那一行用它，仍只交三件的旧形状在装载当场报错。
- **配置段与字段声明自带文案**：`SectionSpec` 必带 `title`，`FieldSpec` 必带 `label` 与 `desc`，按旧形状构造会因缺必填参数报错。
- **配置大类归属撤出声明**：`ConfigGroup` 从公开名里撤掉，`SectionSpec.group` 同时撤销，大类改由配置来源身份定，仍交 `group=` 的旧写法构造即报错。
- **模型段的成员名跟着段名串改**：`ConfigSection.AI = "ai"` 换成 `ConfigSection.MODEL = "model"`，配置文件里该段的表名跟着从 `ai` 变成 `model`。
- **配置项身份换成带来源的对象**：`ConfigPath` 由点分字符串改为装来源、段、键三段的冻结对象，`ConfigKey.path` 多收一个来源参数，`FieldSpec.path` 撤销，拿点分原串当身份的代码要改成取对象。

### ✨ Added

- **插件入口可交配置来源声明**：`BasePlugin.source_declaration` 交出带标题与段组的 `SourceDeclaration`，段组为空即本插件不带配置，配置窗左列那一行用它的标题。

## [0.1.0] - 2026-11-15

### ✨ Added

- **接口包 `finshin-sdk`**：交出插件与适配器共用的契约基类、领域词表、数据形状、异常族与命令绑定。
- **插件声明字段分两处**：清单文件里是名字、显示名、说明、资源与命令段，本插件独有的库取同目录 `pyproject.toml` 的 `[project].dependencies`。
- **版本号单源**：版本号写在 `pyproject.toml`，门面从包元数据取它。

# Changelog

本项目的所有重要更改都将记录在此文件中。
格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并且本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### ⚠️ Breaking Changes

- **平台枚举撤出接口包**：`Platform` 删除，适配器与插件改自交 `PlatformCode` 与 `SourceCode`，实例身份码改用 `ProfileKey`，`make_profile_code` / `platform_of_profile` 换成 `make_profile_key` / `platform_of_key`。
- **配置身份统一点分串**：`ConfigPath` 的串出口只留 `dotted`（来源、段、键三段，返回 `ConfigPathKey`），删 `__str__`、`KEY_SEP` 与 `FieldKey`，`PrincipalDTO`、`MessageRefDTO`、`SessionDTO`、`TaskDTO` 的联合键属性统一叫 `dotted`，`TaskRequestDTO` 补同名出口，`TaskId`、`ContainerKey` 改名 `TaskKey`、`ContainerCode`，`MsgReferenceDTO` 改名 `MessageRefDTO`。
- **配置键与段词表整族撤出接口包**：`ConfigKey`、`ConfigSection`、`SECTIONS_BY_PLATFORM` 与 `ProxyMode` 删除，段名与键名改由本体与插件自持，`ConfigSnapshot` 改名 `ConfigValues`。
- **随包名单、档位表与状态键撤出接口包**：`BUNDLED_PLUGIN_PRIORITY`、`is_enabled`、`resolve_claims`、`StateKey` 删除，随包名单、加载档位、在场判定、命令名抢占与实例状态键归本体，`CommandPriority` 改名 `PluginPriority`，`ManifestKey`、`HelpKey`、`AdapterManifestKey` 改名 `PluginManifestKeys`、`HelpKeys`、`AdapterManifestKeys`，`MANIFEST_FIELDS`、`ADAPTER_MANIFEST_FIELDS` 改名 `PLUGIN_MANIFEST_TABLE`、`ADAPTER_MANIFEST_TABLE`，`ArgsValue` 改名 `FlagValue`，`AdapterFieldSpec` 与 `ManifestFieldSpec` 撤出公开名。
- **装载与插件目录常量撤出**：`ADAPTERS_PKG`、`PLUGINS_PKG`、`INSTALLED_PLUGINS_NAME`、`INSTALLED_PLUGINS_PKG`、`PluginFileName.STATE` 删除，随包插件树名、外部插件挂载点与适配器装载根归本体，`ADAPTER_DECLARATION_FILE` 改名 `ADAPTER_MANIFEST_FILE`。
- **适配器入口件六件**：新增 `sections`、`plan_for` 与 `credential`，`plan_for` 改关键字可调用的私有形状，`credential` 新增 `item`，旧的单通道探测交口撤销，进度行状态收成 `RowStatus`。
- **会话快照撤掉摘要字段**：`SessionDTO` 与 `SessionPatchDTO` 不再带 `summary`，读写会话的件按新形状构造。
- **异常族收窄**：`TelegramServerError` 改名 `ServerUnreachableError`，`DirectTimeoutError`、`TokenError`、`TokenFormatError` 与代理异常族搬回平台适配器。
- **平台专属名回适配器**：`MediaGroupId` 从接口包移到 Telegram 适配器，`MessageKey` 暂不对外。

### ✨ Added

- **插件运行期异常基类**：新增 `PluginError`，外部插件的运行期错误统一挂它下面。
- **配置来源可交保存轮检查计划**：`SourceDeclaration` 新增可选 `probe` 与 `probe_label`，`probe` 吃 `ConfigValues` 回一份 `ConnectionPlan`，保存配置时随平台那轮并进进度表。
- **连通检查计划**：`ConnectionPlan`、`ProbeChannel`、`ProbeRow`、`ProbeResult`、`ProbeOutcome` 与 `PlanVerdict` 一起交出，进度行、每路预算、收尾裁决与提示话术都由适配器决定，`PlanVerdict` 新增 `fatal` 旗。
- **字段显隐与归属标记**：`FieldCondition`、`FieldSpec.visible_when` 与 `FieldSpec.tags`，按同段另一个字段的取值决定一行显不显示，并给字段挂归属标记。

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

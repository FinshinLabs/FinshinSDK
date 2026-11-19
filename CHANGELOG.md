# Changelog

本项目的所有重要更改都将记录在此文件中。
格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并且本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### ⚠️ Breaking Changes

- **适配器入口件多交平台显示名**：`AdapterParts` 四件一起交，新增的 `title` 是本平台的显示名，配置窗左列那一行用它，仍只交三件的旧形状在装载当场报错。
- **配置段与字段声明自带文案**：`SectionSpec` 必带 `title`，`FieldSpec` 必带 `label` 与 `desc`，按旧形状构造会因缺必填参数报错。
- **配置大类归属撤出声明**：`ConfigGroup` 从公开名里撤掉，`SectionSpec.group` 同时撤销，大类改由配置来源身份定，仍交 `group=` 的旧写法构造即报错。
- **模型段的成员名跟着段名串改**：`ConfigSection.AI = "ai"` 换成 `ConfigSection.MODEL = "model"`，配置文件里该段的表名跟着从 `ai` 变成 `model`。

### ✨ Added

- **插件入口可交配置来源声明**：`BasePlugin.source_declaration` 交出带标题与段组的 `SourceDeclaration`，段组为空即本插件不带配置，配置窗左列那一行用它的标题。

## [0.1.0] - 2026-11-15

### ✨ Added

- **接口包 `finshin-sdk`**：交出插件与适配器共用的契约基类、领域词表、数据形状、异常族与命令绑定。
- **插件声明字段分两处**：清单文件里是名字、显示名、说明、资源与命令段，本插件独有的库取同目录 `pyproject.toml` 的 `[project].dependencies`。
- **版本号单源**：版本号写在 `pyproject.toml`，门面从包元数据取它。

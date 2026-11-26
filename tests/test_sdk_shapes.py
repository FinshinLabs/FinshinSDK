"""接口包纯函数用例

- 覆盖配置项身份、实例身份码与各 DTO 的身份串
- 覆盖进度行状态
- 覆盖插件运行期异常基类
- 覆盖插件声明与帮助形状
"""

from finshin_sdk.domain import (
    CommandHelp,
    FlagHelp,
    PluginDeclaration,
    PluginFileName,
    ProbeRow,
    RowStatus,
    SectionHelp,
    TaskStatus,
    make_profile_key,
    platform_of_key,
)
from finshin_sdk.domain.config import ConfigPath
from finshin_sdk.domain.ids import (
    ContainerCode,
    MessageId,
    PlatformCode,
    ProfileKey,
    SourceCode,
    UserId,
)
from finshin_sdk.dto import (
    MessageRefDTO,
    PluginManifestDTO,
    PrincipalDTO,
    SessionDTO,
    TaskDTO,
    TaskRequestDTO,
)
from finshin_sdk.exceptions import BotError, PluginError


def _principal() -> PrincipalDTO:
    """一只固定主体"""
    return PrincipalDTO(
        platform=PlatformCode("demo"),
        container=ContainerCode("g100"),
        user=UserId("456"),
    )


def test_config_path_dotted_keeps_three_segments() -> None:
    """配置项身份串带来源码、段名与键名"""
    path = ConfigPath(source=SourceCode("plugin.AI"), section="ai", key="model")
    assert path.dotted == "plugin.AI.ai.model"


def test_make_profile_key_joins_platform_and_account() -> None:
    """身份码由平台码与账号 id 拼成"""
    assert make_profile_key(PlatformCode("demo"), "12345") == "demo.12345"


def test_platform_of_key_splits_first_dot_only() -> None:
    """身份码只按第一个点号取平台码"""
    assert platform_of_key(ProfileKey("demo.12345")) == "demo"
    assert platform_of_key(ProfileKey("custom.a.b")) == "custom"


def test_platform_of_key_rejects_missing_prefix() -> None:
    """无点号或前缀为空时回 None"""
    assert platform_of_key(ProfileKey("demo12345")) is None
    assert platform_of_key(ProfileKey(".12345")) is None


def test_principal_and_message_ref_dotted() -> None:
    """主体与消息定位各交身份串"""
    principal = _principal()
    ref = MessageRefDTO(
        platform=PlatformCode("demo"),
        container=ContainerCode("g100"),
        message_id=MessageId("9"),
    )
    assert principal.dotted == "demo.g100.456"
    assert ref.dotted == "demo.g100.9"


def test_session_dotted_has_two_segments() -> None:
    """会话快照交会话身份串"""
    session = SessionDTO(
        platform=PlatformCode("demo"),
        container=ContainerCode("g100"),
    )
    assert session.dotted == "demo.g100"


def test_task_dotted_matches_request() -> None:
    """任务视图与创建请求交同一串"""
    principal = _principal()
    ref = MessageRefDTO(
        platform=PlatformCode("demo"),
        container=ContainerCode("g100"),
        message_id=MessageId("9"),
    )
    task = TaskDTO(
        principal=principal,
        kind="say",
        status=TaskStatus.PENDING,
        source_ref=ref,
    )
    request = TaskRequestDTO(principal=principal, kind="say", source_ref=ref)
    assert task.dotted == "demo.g100.456.say"
    assert request.dotted == task.dotted


def test_row_status_has_four_values() -> None:
    """进度行状态四值齐备，新行默认待跑"""
    assert {item.value for item in RowStatus} == {"pending", "ok", "fail", "skip"}
    assert ProbeRow(row_id="r1", title="直连").status is RowStatus.PENDING


def test_plugin_error_subclasses_bot_error() -> None:
    """插件运行期异常挂在自定义异常基类下面"""
    assert issubclass(PluginError, BotError)


def test_plugin_declaration_defaults_to_empty_tuples() -> None:
    """插件声明默认不带资源与帮助段"""
    declaration = PluginDeclaration(title="示例", summary="说明")
    assert declaration.assets == ()
    assert declaration.help == ()


def test_plugin_declaration_composes_assets_and_help() -> None:
    """插件声明可交资源、帮助开关、命令与分段"""
    command = CommandHelp(
        cmd="/demo",
        desc="示例命令",
        flags=(FlagHelp(name="-n", desc="次数"),),
    )
    section = SectionHelp(section="示例", commands=(command,))
    declaration = PluginDeclaration(
        title="示例",
        summary="说明",
        assets=("样例资源",),
        help=(section,),
    )
    assert declaration.assets == ("样例资源",)
    assert declaration.help == (section,)


def test_plugin_file_name_points_to_declaration_module() -> None:
    """插件声明文件名指向代码文件"""
    assert PluginFileName.DECLARATION.value == "_declaration.py"


def test_plugin_manifest_holds_declaration() -> None:
    """插件加载记录收代码声明"""
    declaration = PluginDeclaration(title="示例", summary="说明")
    manifest = PluginManifestDTO(
        name="demo", module="demo", deps=(), declaration=declaration
    )
    assert manifest.declaration is declaration
    assert manifest.deps == ()

"""领域类型门面

- 业务类型与跨平台归一的原始类型
"""

from ._adapter import (
    ADAPTER_ENTRY_ATTR,
    ADAPTER_ENTRY_GROUP,
    ADAPTER_MANIFEST_FILE,
    ADAPTER_MANIFEST_TABLE,
    AdapterManifestKeys,
)
from ._command import (
    BindFailure,
    BoundCommand,
    CommandFlag,
    FlagValue,
    StepInput,
    bind_command,
    is_flag_name,
)
from ._container import make_container
from ._content import ContentKind
from ._plan import (
    ConfigValues,
    ConnectionPlan,
    PlanVerdict,
    ProbeChannel,
    ProbeOutcome,
    ProbeResult,
    ProbeRow,
    RowStatus,
)
from ._platform import ChatScope, make_profile_key, platform_of_key
from ._plugin import (
    PLUGIN_MANIFEST_TABLE,
    ActionRun,
    BackgroundLoop,
    BasePlugin,
    CommandTaken,
    HelpKeys,
    MessageRoute,
    MomentRun,
    MomentSubscription,
    PlatformMoment,
    PluginClaim,
    PluginFileName,
    PluginManifestKeys,
    PluginMark,
    PluginPriority,
    QueuedAction,
    RouteMatcher,
    RouteSink,
)
from ._role import ChatRole, CommandRole
from ._task import TaskPayload, TaskStatus, is_own_action
from .config import (
    ConfigPath,
    ConfigPathKey,
    ConfigValue,
    FieldCondition,
    FieldSpec,
    SectionSpec,
    SourceDeclaration,
)
from .ids import (
    ChatId,
    ContainerCode,
    MessageId,
    PlatformCode,
    PrincipalKey,
    ProfileKey,
    SessionKey,
    SourceCode,
    TaskKey,
    UserId,
)

__all__ = [
    # 字段创建
    "make_container",
    # 实例身份码
    "make_profile_key",
    "platform_of_key",
    # 会话
    "ChatScope",
    # 标识
    "ChatId",
    "UserId",
    "MessageId",
    "ContainerCode",
    "SessionKey",
    "PrincipalKey",
    "TaskKey",
    "ProfileKey",
    "PlatformCode",
    "SourceCode",
    # 适配器
    "ADAPTER_ENTRY_ATTR",
    "ADAPTER_ENTRY_GROUP",
    "ADAPTER_MANIFEST_FILE",
    "AdapterManifestKeys",
    "ADAPTER_MANIFEST_TABLE",
    # 插件
    "PlatformMoment",
    "BackgroundLoop",
    "RouteMatcher",
    "MessageRoute",
    "BasePlugin",
    "MomentSubscription",
    "MomentRun",
    "PluginPriority",
    "CommandTaken",
    "PluginClaim",
    "PluginFileName",
    "PluginMark",
    "PluginManifestKeys",
    "PLUGIN_MANIFEST_TABLE",
    "HelpKeys",
    "RouteSink",
    "QueuedAction",
    "ActionRun",
    # 内容与角色
    "ContentKind",
    "ChatRole",
    "CommandRole",
    # 命令
    "FlagValue",
    "CommandFlag",
    "StepInput",
    "BoundCommand",
    "BindFailure",
    "bind_command",
    "is_flag_name",
    # 任务
    "TaskPayload",
    "is_own_action",
    "TaskStatus",
    # 配置结构
    "ConfigValue",
    "ConfigPath",
    "ConfigPathKey",
    "FieldCondition",
    "FieldSpec",
    "SectionSpec",
    "SourceDeclaration",
    # 连通检查计划
    "ConfigValues",
    "ConnectionPlan",
    "PlanVerdict",
    "ProbeChannel",
    "ProbeOutcome",
    "ProbeResult",
    "ProbeRow",
    "RowStatus",
]

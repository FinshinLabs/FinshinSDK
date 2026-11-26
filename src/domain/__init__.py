"""领域类型门面

- 业务类型与跨平台归一的原始类型
"""

from ._adapter import (
    ADAPTER_ENTRY_ATTR as ADAPTER_ENTRY_ATTR,
    ADAPTER_ENTRY_GROUP as ADAPTER_ENTRY_GROUP,
    ADAPTER_MANIFEST_TABLE as ADAPTER_MANIFEST_TABLE,
    AdapterManifestKeys as AdapterManifestKeys,
)
from ._command import (
    BindFailure as BindFailure,
    BoundCommand as BoundCommand,
    CommandFlag as CommandFlag,
    FlagValue as FlagValue,
    StepInput as StepInput,
    bind_command as bind_command,
    is_flag_name as is_flag_name,
)
from ._container import make_container as make_container
from ._content import ContentKind as ContentKind
from ._plan import (
    ConfigValues as ConfigValues,
    ConnectionPlan as ConnectionPlan,
    PlanVerdict as PlanVerdict,
    ProbeChannel as ProbeChannel,
    ProbeOutcome as ProbeOutcome,
    ProbeResult as ProbeResult,
    ProbeRow as ProbeRow,
    RowStatus as RowStatus,
)
from ._platform import (
    ChatScope as ChatScope,
    make_profile_key as make_profile_key,
    platform_of_key as platform_of_key,
)
from ._plugin import (
    PLUGIN_NAME_PREFIX as PLUGIN_NAME_PREFIX,
    ActionRun as ActionRun,
    BackgroundLoop as BackgroundLoop,
    BasePlugin as BasePlugin,
    CommandHelp as CommandHelp,
    CommandTaken as CommandTaken,
    FlagHelp as FlagHelp,
    MessageRoute as MessageRoute,
    MomentRun as MomentRun,
    MomentSubscription as MomentSubscription,
    PlatformMoment as PlatformMoment,
    PluginClaim as PluginClaim,
    PluginDeclaration as PluginDeclaration,
    PluginFileName as PluginFileName,
    PluginMark as PluginMark,
    PluginPriority as PluginPriority,
    QueuedAction as QueuedAction,
    RouteMatcher as RouteMatcher,
    RouteSink as RouteSink,
    SectionHelp as SectionHelp,
)
from ._role import (
    ChatRole as ChatRole,
    CommandRole as CommandRole,
)
from ._task import (
    TaskPayload as TaskPayload,
    TaskStatus as TaskStatus,
    is_own_action as is_own_action,
)

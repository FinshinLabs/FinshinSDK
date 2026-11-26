"""领域类型门面

- 业务类型与跨平台归一的原始类型
"""

from ._adapter import (
    ADAPTER_ENTRY_ATTR,
    ADAPTER_ENTRY_GROUP,
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
    PLUGIN_NAME_PREFIX,
    ActionRun,
    BackgroundLoop,
    BasePlugin,
    CommandHelp,
    CommandTaken,
    FlagHelp,
    MessageRoute,
    MomentRun,
    MomentSubscription,
    PlatformMoment,
    PluginClaim,
    PluginDeclaration,
    PluginFileName,
    PluginMark,
    PluginPriority,
    QueuedAction,
    RouteMatcher,
    RouteSink,
    SectionHelp,
)
from ._role import ChatRole, CommandRole
from ._task import TaskPayload, TaskStatus, is_own_action

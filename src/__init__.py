"""接口包门面

- 代发插件侧的入口基类与声明结构
- 代发处理上下文与平台交代的那一份能力
- 代发适配器要实现的基类与交互端口
- 代发日志与断链上报两只公开件，实现由本体绑定
- 平台装配与连通检查计划的数据形状
"""

from importlib.metadata import version

from ._adapter import BaseAdapter, InteractionPort, RouterBuilder
from ._assembly import AdapterParts, CredentialSpec, PlatformAssembly
from ._capability import CapabilityCall
from ._context import HandlerContext
from ._link import bind_link_report, link_down, link_up
from ._log import LogLevel, bind_logger, log
from .domain import (
    BackgroundLoop,
    BasePlugin,
    ConfigValues,
    ConnectionPlan,
    HelpCommand,
    HelpFlag,
    HelpSection,
    MessageRoute,
    MomentSubscription,
    PlanVerdict,
    PlatformMoment,
    PluginDeclaration,
    ProbeChannel,
    ProbeOutcome,
    ProbeResult,
    ProbeRow,
    QueuedAction,
    RowStatus,
    SourceDeclaration,
)

# 项目声明文件名，本体、适配器与插件各带一份同格式的它
PROJECT_MANIFEST_FILE = "pyproject.toml"

# 接口包自己的发行件名，插件与适配器在依赖里写它
SDK_DISTRIBUTION = "finshin-sdk"

# 接口包自身的版本号，装载前比对适配器清单的接口要求时取它
SDK_VERSION = version(SDK_DISTRIBUTION)

__all__ = [
    # 接口版本
    "PROJECT_MANIFEST_FILE",
    "SDK_DISTRIBUTION",
    "SDK_VERSION",
    # 插件契约
    "BasePlugin",
    "MessageRoute",
    "BackgroundLoop",
    "QueuedAction",
    "PlatformMoment",
    "MomentSubscription",
    "HelpFlag",
    "HelpCommand",
    "HelpSection",
    "PluginDeclaration",
    "SourceDeclaration",
    "HandlerContext",
    "CapabilityCall",
    # 适配器
    "InteractionPort",
    "BaseAdapter",
    "RouterBuilder",
    # 平台装配与检查计划
    "PlatformAssembly",
    "AdapterParts",
    "CredentialSpec",
    "ConfigValues",
    "ConnectionPlan",
    "PlanVerdict",
    "ProbeChannel",
    "ProbeOutcome",
    "ProbeResult",
    "ProbeRow",
    "RowStatus",
    # 日志与断链上报
    "log",
    "LogLevel",
    "bind_logger",
    "link_down",
    "link_up",
    "bind_link_report",
]

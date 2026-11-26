"""插件对象

- 插件加载优先级、相关文件、清单键名与对象记号的词表
- 插件清单标量字段的类型、必填与默认
- 路由清单、常驻协程、任务处理、时机订阅与来源声明的签名
- 平台侧的路由挂载口
- 命令名抢占判定的记录与结果形状
"""

from collections.abc import Awaitable, Callable, Coroutine
from dataclasses import dataclass
from enum import IntEnum, StrEnum, auto
from typing import Any, Protocol

from .config import SourceDeclaration

# 插件声明的无参常驻协程，随 Bot 服务起停
BackgroundLoop = Callable[[], Coroutine[Any, Any, None]]

# 路由谓词，只吃归一后的处理上下文，返回是否接管这条事件
RouteMatcher = Callable[..., Awaitable[bool]]

# 路由处理函数，首位按位置收本平台原始件且不许读它，归一事件与上下文都从 ctx 取
_PluginHandler = Callable[..., Awaitable[None]]

# 任务处理函数，只吃归一后的处理上下文，报错自行收干净再交回调度
ActionRun = Callable[..., Awaitable[None]]

# 时机订阅的处理函数，收平台召唤时交代的那一份能力
MomentRun = Callable[..., Awaitable[None]]


class PlatformMoment(StrEnum):
    """平台会说出口的机会

    - 加新机会在这里加一名，不在插件入口基类上加方法
    - 名字只说平台发生了什么，不说插件该干什么
    - 插件在入口类上订阅，订了就轮到
    """

    # 轮询开跑前在服务线程的事件循环上轮到，件报错记一笔后接着跑下一个
    BEFORE_ENGINE_RUN = auto()

    # 主人或生效正文变了即轮到，排在清历史那一步
    IDENTITY_CHANGED = auto()

    # 校验通过即说出口，此刻内存里已是刚验过的值
    # 落盘排在随后由界面动手，盘上可能还是旧值
    CONFIG_VERIFIED = auto()


@dataclass(frozen=True, slots=True)
class QueuedAction:
    """一条动作声明

    - 同一动作名只认最先交出来的那个
    """

    kind: str
    run: ActionRun


@dataclass(frozen=True, slots=True)
class MessageRoute:
    """一条路由声明

    - 谓词判真才进处理函数
    """

    predicate: RouteMatcher
    handler: _PluginHandler


@dataclass(frozen=True, slots=True)
class MomentSubscription:
    """一条时机订阅

    - 时机决定什么时候轮到，处理函数收平台交代的那一份能力
    - 同一时机交多条即按交出的顺序跑
    """

    moment: PlatformMoment
    run: MomentRun


class BasePlugin:
    """插件入口基类

    - 五只方法都可以不写，不写即没有那一类能力
    - 交出的清单按交出的顺序生效，本体不认识具体能力
    """

    def message_routes(self) -> tuple[MessageRoute, ...]:
        """来向消息的路由清单"""
        return ()

    def background_loops(self) -> tuple[BackgroundLoop, ...]:
        """随机器人起停的常驻循环"""
        return ()

    def queued_actions(self) -> tuple[QueuedAction, ...]:
        """可排队的动作清单"""
        return ()

    def platform_moments(self) -> tuple[MomentSubscription, ...]:
        """订阅的平台机会清单"""
        return ()

    def source_declaration(self) -> SourceDeclaration:
        """本插件交出的配置来源，段组空即本插件不带配置"""
        return SourceDeclaration(title="", sections=())


class RouteSink(Protocol):
    """平台引擎的路由挂载口"""

    def include_router(self, router: Any) -> Any:
        """挂上一份路由"""


class PluginPriority(IntEnum):
    """插件加载优先级

    - 数值越小越优先，同值按名字典序
    """

    FIRST = 0  # 最先档
    NORMAL = 10  # 常规档，表外插件一律这档
    LAST = 50  # 最后档


@dataclass(frozen=True, slots=True)
class PluginClaim:
    """命令名抢占判定的一条插件记录

    - 命令名项是本插件清单声明的，没声明即空
    """

    name: str
    commands: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class CommandTaken:
    """一条被抢走的命令名与抢走它的插件"""

    cmd: str
    owner: str


class PluginFileName(StrEnum):
    """插件相关文件名"""

    MANIFEST = "plugin.toml"  # 位于各插件目录，存插件自描述清单


class PluginManifestKeys(StrEnum):
    """插件记录的字段名

    - name、title、summary、assets、help 写在插件目录的清单文件里
    - deps 取插件自家声明的依赖表，清单里不再写这一项
    """

    NAME = "name"
    TITLE = "title"
    SUMMARY = "summary"
    DEPS = "deps"
    ASSETS = "assets"
    HELP = "help"


class HelpKeys(StrEnum):
    """帮助贡献键名

    - 段级与命令级共用
    - 顶层那张表的键名也在这只表里，插件读自家清单时用同一份
    """

    HELP = "help"
    SECTION = "section"
    NOTE = "note"
    COMMANDS = "commands"
    CMD = "cmd"
    DESC = "desc"
    FLAGS = "flags"
    ARGS = "args"
    ROLE = "role"


class PluginMark(StrEnum):
    """插件交来的对象上挂的记号

    - 命令名挂在路由谓词上，权限档挂在处理函数上
    """

    COMMAND_NAME = "command_name"
    COMMAND_ROLE = "command_role"


@dataclass(frozen=True, slots=True)
class _ManifestFieldSpec:
    """插件清单标量字段规格"""

    key: PluginManifestKeys
    value_type: type
    default: Any
    required: bool = False


PLUGIN_MANIFEST_TABLE: tuple[_ManifestFieldSpec, ...] = (
    _ManifestFieldSpec(PluginManifestKeys.NAME, str, "", required=True),
    _ManifestFieldSpec(PluginManifestKeys.TITLE, str, "", required=True),
    _ManifestFieldSpec(PluginManifestKeys.SUMMARY, str, "", required=True),
    _ManifestFieldSpec(PluginManifestKeys.ASSETS, list, ()),
)

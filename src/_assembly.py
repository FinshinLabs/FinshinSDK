"""平台装配契约

- 定义适配器入口模块交出的几件与装配结果的数据形状
"""

from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import Protocol

from ._adapter import BaseAdapter
from .domain import (
    BackgroundLoop,
    ConfigValues,
    ConnectionPlan,
    MomentRun,
    PlatformMoment,
    QueuedAction,
)
from .domain.config import ConfigPath, SectionSpec
from .dto import PluginManifestDTO


@dataclass(frozen=True, slots=True)
class PlatformAssembly:
    """一个平台装配出来的件

    - 适配器交运行时托管，其余四件交装配层登记
    - 报告行每项是 (插件清单, 失败异常)，成功那项异常记 None
    """

    adapter: BaseAdapter
    report: Sequence[tuple[PluginManifestDTO, Exception | None]]
    background_loops: tuple[BackgroundLoop, ...]
    queued_actions: tuple[QueuedAction, ...]
    platform_moments: dict[PlatformMoment, tuple[MomentRun, ...]]


class _PlanFactory(Protocol):
    """适配器计划工厂

    - 收各段配置值、凭证与系统代理，回一份检查计划
    """

    def __call__(
        self,
        values: ConfigValues,
        token: str,
        *,
        system_proxy: str | None = None,
    ) -> ConnectionPlan: ...


@dataclass(frozen=True, slots=True)
class CredentialSpec:
    """本平台凭证的声明

    - label 是凭证输入框的名字
    - desc 是输入框下那行提示
    - invalid 是认不出凭证时给人看的一句
    - item 是凭证那一项在配置里的身份
    - identity 收凭证串回身份码，认不出返回空串
    """

    label: str
    desc: str
    invalid: str
    item: ConfigPath
    identity: Callable[[str], str]


@dataclass(frozen=True, slots=True)
class AdapterParts:
    """适配器入口模块交出的件

    - sections 为本平台的配置段，顺序即面板页签顺序
    - assemble 收 token 与代理，回这个平台的运行时
    - plan_for 按当前配置与系统代理造出一份连通检查计划
    - 引擎预热只付导入费
    - 标题是本平台的显示名，配置窗左列那一行用它
    - credential 交代本平台凭证的名字与身份推导
    """

    title: str
    sections: tuple[SectionSpec, ...]
    assemble: Callable[[str, str | None], BaseAdapter]
    plan_for: _PlanFactory
    engine_preload: Callable[[], None]
    credential: CredentialSpec

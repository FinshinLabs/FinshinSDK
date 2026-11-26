"""连通检查计划

- 定义候选通道、进度行与收尾裁决的数据形状
- 插件交出的探测计划也用它
"""

from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass, field
from enum import StrEnum

from .config import ConfigPath, ConfigValue

ConfigValues = Mapping[str, Mapping[str, ConfigValue]]


class RowStatus(StrEnum):
    """进度表行状态"""

    PENDING = "pending"
    OK = "ok"
    FAIL = "fail"
    SKIP = "skip"


@dataclass(frozen=True, slots=True)
class ProbeResult:
    """单通道探测结果

    - accepted 为该通道是否走得通，token 错但通道通也算走得通
    - effective 为可交给运行时的代理地址，直连是空串，未通过为 None
    - field_errors 键为配置项身份，值为给人看的那一句话
    """

    accepted: bool
    detail: str = ""
    field_errors: dict[ConfigPath, str] = field(default_factory=dict)
    effective: str | None = None


@dataclass(frozen=True, slots=True)
class ProbeChannel:
    """一个候选通道

    - row_id 对应进度表那一行
    - label 是日志与表格里的称谓
    - budget 为本路预留的探测秒数
    - run 为这一路的探测协程
    """

    row_id: str
    label: str
    budget: float
    run: Callable[[], Awaitable[ProbeResult]]


@dataclass(frozen=True, slots=True)
class ProbeRow:
    """进度表的一行"""

    row_id: str
    title: str
    status: RowStatus = RowStatus.PENDING
    detail: str = ""


@dataclass(frozen=True, slots=True)
class ProbeOutcome:
    """一轮探测的汇总

    - accepted 为定案通道的结果
    - results 按计划顺序记已完成通道的结果
    """

    accepted: ProbeResult | None = None
    accepted_row: str = ""
    results: tuple[tuple[str, ProbeResult], ...] = ()


@dataclass(frozen=True, slots=True)
class PlanVerdict:
    """一轮检查的收尾裁决

    - field_errors 供面板标红
    - fatal 为致命失败旗
    - failure_detail 为结论行失败句，空串由本体按计数兜底
    - notice 为通过时写 info 日志的那一句
    - warning 为降级使用时写 error 日志的那一句
    """

    field_errors: dict[ConfigPath, str] = field(default_factory=dict)
    fatal: bool = False
    failure_detail: str = ""
    notice: str = ""
    warning: str = ""


@dataclass(frozen=True, slots=True)
class ConnectionPlan:
    """一次连通检查的计划

    - rows 为进度表初态
    - channels 按优先级排列，本体照序取首个通过者
    - reuse_key 反映影响检查结论的输入，相同即可免测
    - finish 收一轮结果，交回字段错误与结论句
    """

    rows: tuple[ProbeRow, ...]
    channels: tuple[ProbeChannel, ...]
    reuse_key: object
    finish: Callable[[ProbeOutcome], PlanVerdict]

"""接口包异常出口

- 代发本体会认的异常类，文案表留本体侧
"""

from ._contracts import (
    BotError as BotError,
    ConnectivityError as ConnectivityError,
    DomainError as DomainError,
    MessageVanishedError as MessageVanishedError,
    PluginError as PluginError,
    ProbeCrashedError as ProbeCrashedError,
    ProbeTimeoutError as ProbeTimeoutError,
    ServerUnreachableError as ServerUnreachableError,
)

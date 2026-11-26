"""异常契约

- 定义所有自定义异常的基类与致命等级
- 定义连接性异常与探测超时
- 定义领域异常基类与消息消失错
"""

from typing import Any, ClassVar

from ..dto import MessageRefDTO


class BotError(Exception):
    """自定义异常基类

    - 关键字参数存为属性供文案模板渲染
    - fatal 定致命等级，兜底那侧按它决定弹窗还是回落向导
    """

    fatal: ClassVar[bool] = False

    def __init__(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)
        super().__init__()


class ConnectivityError(BotError):
    """连接性异常基类"""


class ServerUnreachableError(ConnectivityError):
    """走通代理仍连不上平台服务器"""


class ProbeTimeoutError(ConnectivityError):
    """这一轮探测没在预算内回来"""


class ProbeCrashedError(ConnectivityError):
    """探测自己抛了表外的错"""


class DomainError(BotError):
    """领域异常基类"""


class MessageVanishedError(DomainError):
    """消息不存在

    - 被撤回或删除
    """

    def __init__(self, ref: MessageRefDTO) -> None:
        self.platform = ref.platform
        self.message_id = ref.message_id
        super().__init__()

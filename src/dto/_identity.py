"""身份数据传输对象

- 定义会话主体与消息定位
"""

from dataclasses import dataclass

from ..domain.ids import (
    ContainerCode,
    MessageId,
    MessageKey,
    PlatformCode,
    PrincipalKey,
    UserId,
)


@dataclass(frozen=True, slots=True)
class PrincipalDTO:
    """会话主体标识"""

    platform: PlatformCode
    container: ContainerCode
    user: UserId

    @property
    def dotted(self) -> PrincipalKey:
        """交主体身份串"""
        return PrincipalKey(f"{self.platform}.{self.container}.{self.user}")


@dataclass(frozen=True, slots=True)
class MessageRefDTO:
    """消息定位三元组

    - 图片定位接口的寻址依据
    """

    platform: PlatformCode
    container: ContainerCode
    message_id: MessageId

    @property
    def dotted(self) -> MessageKey:
        """交消息定位串"""
        return MessageKey(f"{self.platform}.{self.container}.{self.message_id}")

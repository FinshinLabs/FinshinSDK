"""会话值对象

- 定义跨平台归一的会话作用域词表
- 定义实例身份码与平台码的双向转换
"""

from enum import StrEnum

from .ids import PlatformCode, ProfileKey


class ChatScope(StrEnum):
    """会话作用域

    - 平台语义在此归一
    """

    PRIVATE = "private"
    GROUP = "group"
    UNKNOWN = "unknown"


def make_profile_key(platform: PlatformCode, account_id: str) -> ProfileKey:
    """拼装实例身份码

    - 平台码即前缀，账号 id 为机器人在该平台的数字 ID
    """
    return ProfileKey(f"{platform}.{account_id}")


def platform_of_key(key: ProfileKey) -> PlatformCode | None:
    """从身份码解析平台码

    - 只按第一个点号切，无点号或前缀为空返回 None
    - 不校验平台码是否已知，由调用方判
    """
    prefix, sep, _ = key.partition(".")
    if not sep or not prefix:
        return None
    return PlatformCode(prefix)

"""容器段归一

- 定义平台 id 到容器码的转换规则
"""

from ._platform import ChatScope
from .ids import ChatId, ContainerCode, UserId


def make_container(scope: ChatScope, chat_id: ChatId, user_id: UserId) -> ContainerCode:
    """归一容器段

    - 群聊 g 前缀加聊天号绝对值
    - 私聊 u 前缀加用户号
    """
    match scope:
        case ChatScope.GROUP:
            return ContainerCode(f"g{abs(int(chat_id))}")  # 非法格式不能静默通过
        case ChatScope.PRIVATE:
            return ContainerCode(f"u{user_id}")
        case _:
            return ContainerCode("")

"""任务数据传输对象

- 定义任务队列的只读视图、创建请求与状态增量
"""

from dataclasses import dataclass

from ..domain import TaskPayload, TaskStatus
from ..domain.ids import TaskKey
from ._identity import MessageRefDTO, PrincipalDTO


@dataclass(frozen=True, slots=True)
class TaskDTO:
    """任务只读视图"""

    principal: PrincipalDTO
    kind: str
    status: TaskStatus
    source_ref: MessageRefDTO  # 任务创建源消息

    payload: TaskPayload = ()

    @property
    def dotted(self) -> TaskKey:
        """交任务身份串"""
        return TaskKey(f"{self.principal.dotted}.{self.kind}")


@dataclass(frozen=True, slots=True)
class TaskRequestDTO:
    """任务创建请求"""

    principal: PrincipalDTO
    kind: str
    source_ref: MessageRefDTO

    payload: TaskPayload = ()

    @property
    def dotted(self) -> TaskKey:
        """交任务身份串"""
        return TaskKey(f"{self.principal.dotted}.{self.kind}")


@dataclass(frozen=True, slots=True)
class TaskPatchDTO:
    """任务增量

    - 状态推进统一走此
    - None 表示不修改
    """

    status: TaskStatus | None = None

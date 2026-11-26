"""数据传输对象门面

- 跨层传递的不可变数据快照
"""

from ._adapter import AdapterManifestDTO
from ._content import ContentDTO, MediaEntryDTO
from ._identity import MessageRefDTO, PrincipalDTO
from ._interaction import CommandDTO, InboundEventDTO, OutboundPayloadDTO
from ._plugin import PluginManifestDTO
from ._session import MessageDTO, SessionDTO, SessionPatchDTO
from ._task import TaskDTO, TaskPatchDTO, TaskRequestDTO

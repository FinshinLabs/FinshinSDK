"""数据传输对象门面

- 跨层传递的不可变数据快照
"""

from ._adapter import AdapterManifestDTO as AdapterManifestDTO
from ._content import (
    ContentDTO as ContentDTO,
    MediaEntryDTO as MediaEntryDTO,
)
from ._identity import (
    MessageRefDTO as MessageRefDTO,
    PrincipalDTO as PrincipalDTO,
)
from ._interaction import (
    CommandDTO as CommandDTO,
    InboundEventDTO as InboundEventDTO,
    OutboundPayloadDTO as OutboundPayloadDTO,
)
from ._plugin import PluginManifestDTO as PluginManifestDTO
from ._session import (
    MessageDTO as MessageDTO,
    SessionDTO as SessionDTO,
    SessionPatchDTO as SessionPatchDTO,
)
from ._task import (
    TaskDTO as TaskDTO,
    TaskPatchDTO as TaskPatchDTO,
    TaskRequestDTO as TaskRequestDTO,
)

"""外部适配器词表

- 定义适配器清单文件名、入口点组名与清单键位
"""

from dataclasses import dataclass
from enum import StrEnum

ADAPTER_MANIFEST_FILE = "pyproject.toml"

# 入口点组名，已装包靠它自报平台，键即平台码
ADAPTER_ENTRY_GROUP = "finshin.adapters"

# 入口点值里冒号后必须指的属性名，由本体规定
ADAPTER_ENTRY_ATTR = "parts"


class AdapterManifestKeys(StrEnum):
    """适配器清单键位，值即清单文件里的段名与键名"""

    PLATFORM = "tool.finshin-adapter.platform"
    DEPS = "project.dependencies"


@dataclass(frozen=True, slots=True)
class _AdapterFieldSpec:
    """适配器清单字段规格"""

    key: AdapterManifestKeys
    value_type: type
    required: bool = False


ADAPTER_MANIFEST_TABLE: tuple[_AdapterFieldSpec, ...] = (
    _AdapterFieldSpec(AdapterManifestKeys.PLATFORM, str, required=True),
    _AdapterFieldSpec(AdapterManifestKeys.DEPS, list),
)

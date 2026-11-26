"""配置结构门面

- 代发配置值类型、配置项身份、字段与段结构体
"""

from ._models import (
    ConfigPath,
    ConfigPathKey,
    ConfigValue,
    FieldCondition,
    FieldSpec,
    SectionSpec,
    SourceDeclaration,
)

__all__ = [
    # 值类型
    "ConfigValue",
    # 配置项身份
    "ConfigPath",
    "ConfigPathKey",
    # 结构体
    "FieldCondition",
    "FieldSpec",
    "SectionSpec",
    "SourceDeclaration",
]

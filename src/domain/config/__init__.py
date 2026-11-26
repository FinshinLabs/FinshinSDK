"""配置结构门面

- 代发配置值类型、配置项身份、段与键、字段与段结构体
"""

from ._models import (
    ConfigKey,
    ConfigPath,
    ConfigSection,
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
    # 段与键
    "ConfigSection",
    "ConfigKey",
    # 结构体
    "FieldCondition",
    "FieldSpec",
    "SectionSpec",
    "SourceDeclaration",
]

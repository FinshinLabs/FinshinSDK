"""配置结构值对象

- 定义配置值类型别名
- 定义配置项身份、段名与键名
- 定义字段、段与来源声明的结构体
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from enum import StrEnum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .._plan import ConnectionPlan

# 单个 TOML 配置值
ConfigValue = str | float | list[str] | None


class ConfigSection(StrEnum):
    """本体自带的配置段名

    - 装配时拼上来源前缀写成点分段名
    """

    DATA = "data"


class ConfigKey(StrEnum):
    """本体自带的配置键名

    - 与段内 TOML 键一一对应
    """

    OWNER = "owner"
    RECORD_KEEP = "record_keep"
    WAITING = "waiting"

    def path(self, source: str, section: str) -> ConfigPath:
        """拼出配置项的完整身份"""
        return ConfigPath(source=source, section=section, key=self)


@dataclass(frozen=True, slots=True)
class ConfigPath:
    """一个配置项的完整身份

    - 来源串为装配时拼出的身份码，本体侧只有来源类型一段
    - 段名与键名是交出者写的原串
    - 屏上文案沿用段与键的点分写法
    """

    source: str
    section: str
    key: str

    def __str__(self) -> str:
        return f"{self.section}.{self.key}"


@dataclass(frozen=True, slots=True)
class FieldCondition:
    """一个字段的显隐条件

    - key 是同段内另一个字段的键名
    - values 命中其中任一值即可见
    """

    key: str
    values: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class FieldSpec:
    """单个配置项的结构定义

    - 选项元组非空即枚举字段，取值为合法值元组
    - 上下界为闭区间，仅 float 字段生效
    - 显隐条件全部命中才显示，空元组即恒显
    """

    section: str
    key: str
    value_type: type
    default: ConfigValue
    label: str
    desc: str
    required: bool = False
    options: tuple[str, ...] = ()
    option_labels: tuple[str, ...] = ()
    bounds: tuple[float, float] | None = None
    visible_when: tuple[FieldCondition, ...] = ()


@dataclass(frozen=True, slots=True)
class SectionSpec:
    """一个配置段的结构定义

    - 字段元组顺序即面板该页字段顺序
    """

    section: str
    title: str
    fields: tuple[FieldSpec, ...]


@dataclass(frozen=True, slots=True)
class SourceDeclaration:
    """一份配置来源声明

    - 标题定面板左列那一行，段组顺序即该来源的页签顺序
    - 来源归属哪一类、身份码是什么由本体定，交出者不写
    - probe 交出保存轮的一次检查计划，不交即本来源不探测
    """

    title: str
    sections: tuple[SectionSpec, ...]
    probe: Callable[[], ConnectionPlan | None] | None = None

"""配置结构值对象

- 定义配置值类型别名
- 定义配置项身份、字段、段与来源声明的结构体
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import TYPE_CHECKING, NewType

if TYPE_CHECKING:
    from .._plan import ConfigValues, ConnectionPlan
    from ..ids import SourceCode

# 单个 TOML 配置值
ConfigValue = str | float | list[str] | None

ConfigPathKey = NewType("ConfigPathKey", str)


@dataclass(frozen=True, slots=True)
class ConfigPath:
    """一个配置项的完整身份

    - 来源码、段名与键名都是交出者写的原串
    """

    source: SourceCode
    section: str
    key: str

    @property
    def dotted(self) -> ConfigPathKey:
        """交配置项身份串"""
        return ConfigPathKey(f"{self.source}.{self.section}.{self.key}")


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
    - tags 由交出者填，本体按标内容解释
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
    tags: tuple[str, ...] = ()


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
    - probe 交出按当前表单值跑的一轮检查计划，不交即本来源不探测
    - probe_label 是检测按钮的文字，留空由本体给默认文案
    """

    title: str
    sections: tuple[SectionSpec, ...]
    probe: Callable[[ConfigValues], ConnectionPlan] | None = None
    probe_label: str = ""

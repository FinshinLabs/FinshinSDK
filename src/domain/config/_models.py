"""配置结构值对象

- 定义配置值类型别名
- 定义配置项身份、段名与键名枚举
- 定义代理模式取值域
- 定义字段、段与来源声明的结构体
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

# 单个 TOML 配置值
ConfigValue = str | float | list[str] | None


class ConfigSection(StrEnum):
    """配置段名

    - 装配时拼上来源前缀写成点分段名
    """

    # Telegram 专属段
    PROXY = "proxy"

    MODEL = "model"
    CHORE = "chore"
    DATA = "data"


class ConfigKey(StrEnum):
    """配置键名

    - 与段内 TOML 键一一对应
    """

    # Telegram 专属键
    PROXY_MODE = "proxy_mode"
    PROXY = "proxy"

    API_KEY = "api_key"
    TEMPERATURE = "temperature"
    OWNER = "owner"
    TRIGGERS = "triggers"
    LOST_LINES = "lost_lines"
    RECORD_KEEP = "record_keep"
    WAITING = "waiting"

    def path(self, source: str, section: ConfigSection) -> ConfigPath:
        """拼出配置项的完整身份"""
        return ConfigPath(source=source, section=section, key=self)


@dataclass(frozen=True, slots=True)
class ConfigPath:
    """一个配置项的完整身份

    - 来源串为装配时拼出的身份码，本体侧只有来源类型一段
    - 屏上文案沿用段与键的点分写法
    """

    source: str
    section: ConfigSection
    key: ConfigKey

    def __str__(self) -> str:
        return f"{self.section}.{self.key}"


class ProxyMode(StrEnum):
    """代理模式协议串

    - 配置字段 proxy_mode 与校验编排共用
    - Telegram 专属取值域
    """

    AUTO = "auto"
    CFG = "cfg"
    SYS = "sys"
    DIRECT = "direct"


@dataclass(frozen=True, slots=True)
class FieldSpec:
    """单个配置项的结构定义

    - 选项元组非空即枚举字段，取值为合法值元组
    - 上下界为闭区间，仅 float 字段生效
    """

    section: ConfigSection
    key: ConfigKey
    value_type: type
    default: ConfigValue
    label: str
    desc: str
    required: bool = False
    options: tuple[str, ...] = ()
    option_labels: tuple[str, ...] = ()
    bounds: tuple[float, float] | None = None


@dataclass(frozen=True, slots=True)
class SectionSpec:
    """一个配置段的结构定义

    - 字段元组顺序即面板该页字段顺序
    """

    section: ConfigSection
    title: str
    fields: tuple[FieldSpec, ...]


@dataclass(frozen=True, slots=True)
class SourceDeclaration:
    """一份配置来源声明

    - 标题定面板左列那一行，段组顺序即该来源的页签顺序
    - 来源归属哪一类、身份码是什么由本体定，交出者不写
    """

    title: str
    sections: tuple[SectionSpec, ...]

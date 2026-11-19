"""Telegram 专属配置段

- 定义 proxy 段字段表
"""

from ._models import (
    ConfigGroup,
    ConfigKey,
    ConfigSection,
    FieldSpec,
    ProxyMode,
    SectionSpec,
)

PROXY_SECTION = SectionSpec(
    section=ConfigSection.PROXY,
    title="连接与代理",
    group=ConfigGroup.BOT,
    fields=(
        FieldSpec(
            section=ConfigSection.PROXY,
            key=ConfigKey.PROXY_MODE,
            value_type=str,
            default=ProxyMode.AUTO,
            label="代理模式",
            desc="自动逐项尝试配置→系统→直连。单路档只校验选定一路，代理软件开 TUN 时选仅直连",
            options=(
                ProxyMode.AUTO,
                ProxyMode.CFG,
                ProxyMode.SYS,
                ProxyMode.DIRECT,
            ),
            option_labels=(
                "自动（配置→系统→直连）",
                "仅配置代理",
                "仅系统代理",
                "仅直连（代理软件开 TUN 时选这个）",
            ),
        ),
        FieldSpec(
            section=ConfigSection.PROXY,
            key=ConfigKey.PROXY,
            value_type=str,
            default="",
            label="代理",
            desc="自动与仅配置代理两档使用该项，其余模式锁定本项",
        ),
    ),
)

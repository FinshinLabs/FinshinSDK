"""全平台一致的配置段

- 定义 ai、chore、data 三个共享段字段表
- 三段同属 AI 大类
"""

from ._models import ConfigGroup, ConfigKey, ConfigSection, FieldSpec, SectionSpec

# AI 配置
_AI_SECTION = SectionSpec(
    section=ConfigSection.AI,
    title="模型",
    group=ConfigGroup.AI,
    fields=(
        FieldSpec(
            section=ConfigSection.AI,
            key=ConfigKey.API_KEY,
            value_type=str,
            default="",
            label="API Key",
            desc="在千问 AI 平台自行创建并填入",
            required=True,
        ),
        FieldSpec(
            section=ConfigSection.AI,
            key=ConfigKey.TEMPERATURE,
            value_type=float,
            default=0.7,
            label="温度",
            desc="取值范围 0~2，越高越有创造性，越低越稳定",
            bounds=(0.0, 2.0),  # OpenAI 兼容规范
        ),
    ),
)

# 杂项
_CHORE_SECTION = SectionSpec(
    section=ConfigSection.CHORE,
    title="主人与触发",
    group=ConfigGroup.AI,
    fields=(
        FieldSpec(
            section=ConfigSection.CHORE,
            key=ConfigKey.OWNER,
            value_type=str,
            default="",
            label="主人",
            desc="具有最高权限的用户 ID（注意实例对应的平台）",
            required=True,
        ),
        FieldSpec(
            section=ConfigSection.CHORE,
            key=ConfigKey.TRIGGERS,
            value_type=list,
            default=[],
            label="触发词",
            desc="用户消息包含关键词触发 AI 回复，不区分大小写",
            required=True,
        ),
        FieldSpec(
            section=ConfigSection.CHORE,
            key=ConfigKey.LOST_LINES,
            value_type=list,
            default=[],
            label="停机交代话术",
            desc="重启时对遗失对话补一句说明，随机取一条，留空交给 AI 现写",
        ),
    ),
)

# 数据维护
_DATA_SECTION = SectionSpec(
    section=ConfigSection.DATA,
    title="记录与运维",
    group=ConfigGroup.AI,
    fields=(
        FieldSpec(
            section=ConfigSection.DATA,
            key=ConfigKey.RECORD_KEEP,
            value_type=float,
            default=30.0,
            label="记录保留（天）",
            desc="取值范围 1~3650，闲置超过这个天数的对话记录与群上下文一并删除",
            bounds=(1.0, 3650.0),
        ),
        FieldSpec(
            section=ConfigSection.DATA,
            key=ConfigKey.WAITING,
            value_type=float,
            default=0.5,
            label="检测间隔（小时）",
            desc="取值范围 0.1~720，间隔多久检测一次后台任务",
            bounds=(0.1, 720.0),
        ),
    ),
)

# 共享配置段
SHARED_SECTIONS = (_AI_SECTION, _CHORE_SECTION, _DATA_SECTION)

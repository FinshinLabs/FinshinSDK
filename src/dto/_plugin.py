"""插件数据传输对象

- 定义插件名称、导入路径、依赖与代码声明
"""

from dataclasses import dataclass

from ..domain import PluginDeclaration


@dataclass(frozen=True, slots=True)
class PluginManifestDTO:
    """插件加载记录"""

    name: str
    module: str
    deps: tuple[str, ...]
    declaration: PluginDeclaration

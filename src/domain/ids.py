"""标识值类型

- 定义跨 DTO 共用的字符串段语义类型
- NewType 运行时即原 str，仅静态检查区分段义
"""

from typing import NewType

# 联合键
SessionKey = NewType("SessionKey", str)  # SessionDTO.dotted
MessageKey = NewType("MessageKey", str)  # MessageRefDTO.dotted
PrincipalKey = NewType("PrincipalKey", str)  # PrincipalDTO.dotted
TaskKey = NewType("TaskKey", str)  # f"{PrincipalDTO.dotted}.{动作名}"

# 平台原始标识
ChatId = NewType("ChatId", str)
UserId = NewType("UserId", str)
MessageId = NewType("MessageId", str)

# 派生单段码
ContainerCode = NewType("ContainerCode", str)  # g/u 前缀
PlatformCode = NewType("PlatformCode", str)
SourceCode = NewType("SourceCode", str)
ProfileKey = NewType("ProfileKey", str)  # 平台码.账号 id

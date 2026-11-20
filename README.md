# 接口包

[![主仓 FinshinImpact](https://img.shields.io/badge/主仓-FinshinImpact-blue.svg)](https://github.com/FinshinLabs/FinshinImpact)

插件与适配器共用的那一包：契约基类、领域词表、数据形状、异常族与命令绑定，本体与外部件同时读这一份。运行时只依赖标准库，Python 3.11 及以上。

## 放在哪儿

本仓不单独开发：clone 进主仓的 `finshin/sdk`，改动在那棵目录里做，代码在 `src` 那一层。挂载与更新的步骤见 [挂载子仓](https://github.com/FinshinLabs/FinshinImpact/blob/main/docs/development.md#挂载子仓)。

## 跑法

```powershell
# 在主仓根执行
python -m pytest devtools/tests/test_public_pieces.py devtools/tests/test_command_bind.py
```

本仓不带用例，门面代发与命令绑定由主仓那棵树里的用例覆盖，全量口径见 [测试](https://github.com/FinshinLabs/FinshinImpact/blob/main/docs/testing.md)。改过 `src/` 先重装再跑：`.venv\Scripts\uv.exe sync --all-packages --reinstall-package finshin-sdk`，测试读的是装进环境的那一份。

## 对外边界与规范

- 对外放什么、不放什么见 [分层职责](https://github.com/FinshinLabs/FinshinImpact/blob/main/docs/coding-style.md#分层职责)。
- 构建、tag 与 release 附件见 [子仓供件](https://github.com/FinshinLabs/FinshinImpact/blob/main/docs/release-workflow.md#子仓供件)。
- 写法与检查见 [代码规范](https://github.com/FinshinLabs/FinshinImpact/blob/main/docs/coding-style.md) 与 [规范扫描器](https://github.com/FinshinLabs/FinshinImpact/blob/main/docs/style-checker.md)，本仓不另立一套规范。

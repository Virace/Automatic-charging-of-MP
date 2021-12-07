# Automatic-charging-of-MP
对于长期连接充电器的手机，配合智能插座(Gosund CP1)按需充电


- [介绍](#介绍)
- [安装](#安装)
- [维护者](#维护者)
- [感谢](#感谢)
- [许可证](#许可证)

### 介绍

前段时间手机电池鼓包了，为了防止家人吃席，购入了这个智能插座，termux配合adb获取电量，根据配置决定是否充电。

### 安装

**要求:**

- termux
- python 环境
- adb环境

### 维护者

**Virace**

- blog: [孤独的未知数](https://x-item.com)

### 感谢

- [@balistof/miio-dreame-vacuum-mqtt](https://github.com/balistof/miio-dreame-vacuum-mqtt/blob/56c75d4f9926b087f96fae74d7dcae4babab9fda/miio/gosund_plug.py), **Gosund CP1**插座控制代码来源
- [@rytilahti/python-miio](https://github.com/rytilahti/python-miio), **MIoT**控制

- 以及**JetBrains**提供开发环境支持

  <a href="https://www.jetbrains.com/?from=kratos-pe" target="_blank"><img src="https://resources.jetbrains.com/storage/products/company/brand/logos/PyCharm.svg"></a>

### 许可证

[GPL-3.0](LICENSE)
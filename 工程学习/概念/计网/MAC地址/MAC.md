MAC地址（Media Access Control Address）是用于唯一标识网络设备的硬件地址，通常由网络适配器制造商在出厂时烧录到设备中。每个网络接口（如网卡）都有一个独特的MAC地址，这使得设备在局域网内能够被识别和定位。

## MAC地址的基本特征

- **长度**：MAC地址为48位，通常以6个字节表示，格式为16进制，例如 `00:11:22:33:44:55`。
- **组成**：
  - **前3字节**（24位）：称为组织唯一标识符（OUI），由IEEE分配给制造商，用于标识设备的生产厂家。
  - **后3字节**（24位）：由制造商自行分配，用于区分同一厂家生产的不同设备。

## MAC地址的类型

1. **单播MAC地址**：
   - 这是最常见的类型，指向单一设备。每个网络设备都有一个唯一的单播MAC地址。

2. **组播MAC地址**：
   - 用于一组设备共享的地址，只有特定设备会接收到发送到该组播地址的数据包。组播地址的第一个字节以 `01` 开头。

3. **广播MAC地址**：
   - 特殊的MAC地址，所有连接到网络的设备都会接收到发送至该地址的数据包。广播地址通常表示为 `ff:ff:ff:ff:ff:ff`。

## MAC地址与IP地址的关系

- **层次结构**：在OSI模型中，MAC地址工作于数据链路层（第二层），而IP地址则位于网络层（第三层）。这意味着MAC地址用于局域网内直接通信，而IP地址用于在更广泛的网络中寻址和路由。
- **功能差异**：MAC地址是硬件相关的，通常是固定不变的，而IP地址可以根据网络环境变化而变化。例如，同一台设备在不同网络中可能会有不同的IP地址。

## 修改MAC地址

尽管MAC地址是硬件烧录的，但在某些情况下可以通过软件手段进行修改。这种操作通常用于测试或隐私保护，但需谨慎使用，因为重复的MAC地址可能导致网络冲突，影响通信。

总之，MAC地址是网络通信中的重要组成部分，通过唯一标识每个设备，在局域网内实现有效的数据传输和管理。

Citations:
[1] https://zh.wikipedia.org/zh-hans/MAC%E5%9C%B0%E5%9D%80
[2] https://blog.csdn.net/qq_35778554/article/details/130772976
[3] https://blog.csdn.net/qq_38048756/article/details/118254985
[4] http://www.mgrzm.com/2021/07/03/mac%E5%9C%B0%E5%9D%80%E8%AF%A6%E8%A7%A3/
# 系统监控模块

## 功能概述
这是一个基于Flask的系统监控模块，用于实时监控和展示系统的各项性能指标，包括CPU使用率、内存使用情况、磁盘使用情况、网络流量以及进程信息。该模块还包含告警功能，当系统指标超过预设阈值时会触发告警。

## 主要功能
1. 实时系统指标监控
2. 性能数据可视化
3. 可配置的告警阈值
4. Top 10 进程监控
5. RESTful API接口

## 技术架构
- **后端框架**: Flask
- **系统监控**: psutil
- **数据存储**: 内存队列（Queue）
- **并发处理**: Python threading

![image-20241206174545306](https://gitee.com/bx33661/image/raw/master/path/image-20241206174545306.png)

## 监控指标详情

### CPU监控
- CPU使用率百分比
- CPU频率

### 内存监控
- 总内存
- 可用内存
- 内存使用率

### 磁盘监控
- 总空间
- 已用空间
- 可用空间
- 使用率

### 网络监控
- 发送字节数
- 接收字节数

### 进程监控
- 进程ID
- 进程名称
- 进程CPU使用率
- 进程内存使用率

## 告警机制
系统内置三种告警阈值：
- CPU使用率 > 80%
- 内存使用率 > 80%
- 磁盘使用率 > 90%

## API接口说明

### 1. 监控页面
- **路径**: `/sysmon/`
- **方法**: GET
- **描述**: 返回系统监控的Web界面

### 2. 获取监控指标
- **路径**: `/sysmon/metrics`
- **方法**: GET
- **返回**: JSON格式的系统监控数据

### 3. 告警阈值管理
- **路径**: `/sysmon/thresholds`
- **方法**: GET/POST
- **功能**: 
  - GET: 获取当前告警阈值
  - POST: 更新告警阈值

## 数据采集
- 数据采集间隔：2秒
- 数据存储容量：最多保存100条历史记录
- 采用队列先进先出机制，超出容量时自动丢弃最早的数据

## 使用示例

### 获取当前告警阈值
```python
import requests

response = requests.get('http://your-server/sysmon/thresholds')
print(response.json())
```

### 更新告警阈值
```python
import requests

new_thresholds = {
    'cpu': 85,
    'memory': 75,
    'disk': 95
}
response = requests.post('http://your-server/sysmon/thresholds', json=new_thresholds)
print(response.json())
```

## 注意事项
1. 监控线程以守护线程方式运行，主程序退出时会自动结束
2. 确保运行程序的用户有足够的系统权限获取这些监控指标
3. 在生产环境中建议调整数据采集间隔和存储容量以适应实际需求
4. 网络指标是累计值，需要自行计算速率
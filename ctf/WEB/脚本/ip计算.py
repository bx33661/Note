def ip_calculator():
    ip_address = input("请输入 IP 地址（格式：xxx.xxx.xxx.xxx）：")
    subnet_mask = input("请输入子网掩码（格式：xxx.xxx.xxx.xxx 或 /xx）：")

    # 处理子网掩码输入
    if '/' in subnet_mask:
        cidr = int(subnet_mask.split('/')[1])
        subnet_mask = ''
        for i in range(4):
            if i < cidr // 8:
                subnet_mask += '255.'
            elif i == cidr // 8 and cidr % 8 != 0:
                subnet_mask += str(256 - (2 ** (8 - (cidr % 8)))).rjust(3, '0') + '.'
            else:
                subnet_mask += '0.'
        subnet_mask = subnet_mask.rstrip('.')

    # 分割 IP 地址和子网掩码
    ip_parts = list(map(int, ip_address.split('.')))
    subnet_parts = list(map(int, subnet_mask.split('.')))

    # 计算网络地址
    network_address = []
    for i in range(4):
        network_address.append(str(ip_parts[i] & subnet_parts[i]))
    network_address = '.'.join(network_address)

    # 计算广播地址
    broadcast_address = []
    for i in range(4):
        broadcast_address.append(str(ip_parts[i] | (255 - subnet_parts[i])))
    broadcast_address = '.'.join(broadcast_address)

    # 计算主机地址范围
    host_range = []
    if subnet_mask == '255.255.255.255':
        host_range.append(ip_address)
        host_range.append(ip_address)
    else:
        first_host = list(ip_parts)
        last_host = list(ip_parts)
        for i in range(4):
            if subnet_parts[i] != 255:
                first_host[i] += 1
                last_host[i] = last_host[i] | (255 - subnet_parts[i])
        host_range.append('.'.join(map(str, first_host)))
        host_range.append('.'.join(map(str, last_host)))

    # 输出结果
    print("IP 地址：", ip_address)
    print("子网掩码：", subnet_mask)
    print("网络地址：", network_address)
    print("广播地址：", broadcast_address)
    print("主机地址范围：", ' ~ '.join(host_range))

if __name__ == "__main__":
    ip_calculator()
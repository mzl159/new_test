import requests

# url = 'http://192.168.1.232:10000/mb?opr=read_do&regstart=0&regnum=4&addr=254'
# a = requests.get(url)
# print(a)
import os

lis_empty = []
def ping_ip(ip):

    # 对于 Unix 系统
    # response = os.system("ping -c 1 " + ip)

    # 对于 Windows 系统, 将上一行替换为:
    response = os.system("ping " + ip)
    print(response)

    if response == 0:
        print(f'{ip} is up')
    else:
        print(f'{ip} is down')
        lis_empty.append(ip)


# ping_ip("10.8.96.147")
#
for i in range(36,250):
    str_ip = f"10.8.96.{str(i)}"
    # print(str_ip,type(str_ip))
    ping_ip(str_ip)
print(lis_empty)

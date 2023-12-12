import paramiko


def ip_connect(ip, user, pwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=user, password=pwd)
    # 万兆网卡品牌查看
    stdin, stdout, stderr = ssh.exec_command('lspci -vv | grep -A2 Eth')
    print(stdout)
    for line in stdout:
        print(line.strip('\n'))
    ssh.close()


def ip_connect_wzwk(ip):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    describe = []
    try:
        ssh.connect(ip, username='mm', password='mm')
        # GPU品牌查看
        stdin, stdout, stderr = ssh.exec_command('lspci -knn | grep VGA -A1')
        for line in stdout:
            # print(line)
            if 'Subsystem:' in line:
                # num = line.split(':')[0]
                GPU_NAME = line.split('Subsystem:')
                GPU_NAME = GPU_NAME[1].strip()
                # print(GPU_NAME)
                describe.append(GPU_NAME)
            if 'DeviceName:' in line:
                GPU_NAME = line.split('DeviceName:')
                GPU_NAME = GPU_NAME[1].strip()
                # print(GPU_NAME)
                describe.append(GPU_NAME)

        ssh.close()
    except Exception as e:
        list_err.append(ip)
        print(ip, "账号或密码不对")
    return describe


list_err = []
list_ip_fwq = ['10.8.96.18', '10.8.96.17', '10.8.96.16', '10.8.96.15', '10.8.96.14',
               '10.8.96.13', '10.8.96.12', '10.8.96.93', '10.8.96.23', '10.8.96.22',
               '10.8.96.21', '10.8.96.20', '10.8.96.19', '10.8.96.11', '10.8.96.10', '10.8.96.09', '10.8.96.08',
               '10.8.96.29', '10.8.96.06', '10.8.96.28', '10.8.96.04', '10.8.96.26',
               '10.8.96.27', '10.8.96.01', '10.8.96.97', '10.8.96.25', '10.8.96.24', '10.8.96.30',
               '10.8.96.31', '10.8.96.32', '10.8.96.33', '10.8.96.34', '10.8.96.35', '10.8.96.36',
               '10.8.96.37', '10.8.96.38', '10.8.96.39', '10.8.96.47', '10.8.96.48']

dic_GPU_name = {}
for i in list_ip_fwq:
    des_GPU_name = ip_connect_wzwk(i)

    if des_GPU_name != []:
        des_GPU_name.insert(0, i)
        dic_GPU_name[i] = des_GPU_name
# print(list_err)
# print(dic_GPU_name)
# for k,v in dic_GPU_name.items():
#     print(len(v))
# ip_connect_wzwk('10.8.96.18')
import pandas as pd

# 将字典转换为DataFrame
df = pd.DataFrame(dic_GPU_name)

# 将DataFrame写入Excel文件
df.to_excel('output.xlsx', header=False)

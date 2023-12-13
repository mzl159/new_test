import serial
import time
import serial.tools.list_ports

# 配置串口参数
# serial_port = '/dev/ttyUSB0'  # Linux 或 macOS 的串口路径
#自动识别串口设备
def refresh_com():
    serial_port = ''
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        serial_port = f'{port}'
    return serial_port


baud_rate = 115200  # 串口波特率
timeout = 1  # 读取超时设置（秒）
# 发送命令函数
def send_command(command):
    # 清空接收缓冲区
    ser.reset_input_buffer()
    # 发送命令
    ser.write(command.encode())
    # 等待数据返回
    time.sleep(0.1)
    while True:
        if ser.in_waiting > 0:
            response = ser.read(ser.in_waiting)
            return response


# 打开串口
if __name__ == '__main__':
    #拿到电脑的串口信息
    serial_port = refresh_com()
    ser = serial.Serial(serial_port, baudrate=baud_rate, timeout=timeout)

    # 检查串口是否打开
    if ser.is_open:
        print(f"串口 {serial_port} 已打开")

        try:
            # 发送命令（确保以正确的格式发送）
            command_to_send = "mount -rw -o remount /"
            send_command(command_to_send)
            time.sleep(5)
            command_to_send = "mount -uw /usr/adaptive"
            send_command(command_to_send)
            time.sleep(5)
            command_to_send = "mount -uw /usr/local"
            send_command(command_to_send)
            time.sleep(2)
            command_to_send = "mv /usr/adaptive/All_build_info.txt /usr/local"
            # send_command(command_to_send)
            # command_to_send = "SOCK=/sock11 ifconfig mc0 192.168.10.50"
            response = send_command(command_to_send)

            # 等待一定时间，让设备有时间响应
            time.sleep(1)
            # 打印响应信息
            if response:
                print("从设备收到的响应: ", response.decode('utf-8-sig'))
            else:
                print("没有收到设备的响应")
        except serial.SerialException as e:
            print(f"发生错误：{e}")
        finally:
            # 关闭串口
            ser.close()
            print(f"串口 {serial_port} 已关闭")
    else:
        print(f"串口 {serial_port} 打开失败")

# -*- coding: utf-8 -*-
# @Author  : Virace
# @Email   : Virace@aliyun.com
# @Site    : x-item.com
# @Software: PyCharm
# @Create  : 2021/11/25 15:42
# @Update  : 2021/12/9 14:59
# @Detail  : 自动充电

import logging
import os
import subprocess
import sys

from Plug.gosund import GosundPlug
from config import LOCAL_IP, MAX_POWER, MAX_TT, MIN_POWER, MIN_TT, PLUG_IP, PLUG_TOKEN, REMOTE_IP, TTC, WX_TOKEN
from push import wxpusher_push

logging.basicConfig(
    level=logging.DEBUG,
    filename=os.path.join(os.path.dirname(__file__), 'main.log'),
    filemode='a',
    encoding='utf-8',
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
log = logging.getLogger()


def run_shell(command, cwd=os.getcwd()):
    cmd = subprocess.Popen(command, cwd=cwd, shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, close_fds=True)
    return cmd.stdout.readlines()


def get_battery_info(ip):
    run_shell(f'adb connect {ip}:5555')
    raw = run_shell(f'adb -s {ip}:5555 shell dumpsys battery')
    res = dict()
    for line in raw:
        d_line = line.decode('utf-8').replace('\r\n', '').strip()
        if ': ' not in d_line:
            continue

        key, value = d_line.split(': ')
        res[key] = value
    return res


class Power:
    def __init__(self, ip, token):
        self.plug = GosundPlug(ip, token)

    def on(self):
        self.plug.on()
        return self.plug.status() is True

    def off(self):
        self.plug.off()
        return self.plug.status() is False


def msg_push(msg):
    wxpusher_push(WX_TOKEN, msg, topic_ids=[3781])


def main():
    power = Power(PLUG_IP, PLUG_TOKEN)
    if 'win' in sys.platform:
        ip = REMOTE_IP
    else:
        ip = LOCAL_IP
    data = get_battery_info(ip)
    ac = True if data['AC powered'].lower() == 'true' else False
    # 剩余电量
    charge = int(data['level'])
    # 电池温度
    temperature = int(data['temperature'])
    status = True if int(data['status']) == 2 else False
    log.debug(f'AC: {ac}, CHARGE: {charge}, STATE: {status}, TP: {temperature / 10}')

    # 温度文件
    target = os.path.join(os.path.dirname(__file__), 'py.ht')

    if charge <= MIN_POWER and ac is False:
        result = power.on()
        msg_push(f'开始充电, 开关状态变更: {result}')

    elif charge >= MAX_POWER and ac is True:
        result = power.off()
        msg_push(f'充电完成, 开关状态变更: {result}')

    elif temperature >= MAX_TT * 10:
        # 温度过高通知
        if not os.path.exists(target):
            os.system(f'echo 1 > {target}')
        else:
            with open(target, 'r+') as f:
                count = int(f.read())
                log.warning(f'temperature anomaly, count: {count + 1}')
                if count >= TTC:
                    if ac is True:
                        result = power.off()
                    msg_push(f'目前温度异常，请及时检查。温度: {temperature / 10}°, 已关闭开关: {result}, 当前电量: {charge}')
                else:
                    f.seek(0)
                    f.write(str(count + 1))
    elif temperature <= MIN_TT * 10 and os.path.exists(target):
        with open(target) as f:
            count = int(f.read())
            if count >= TTC:
                if ac is False:
                    result = power.on()
                    msg_push(f'温度已恢复正常值{temperature / 10}°, 继续充电，开关: {result}, 当前电量: {charge}')
        os.remove(target)


if __name__ == '__main__':
    main()

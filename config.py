# -*- coding: utf-8 -*-
# @Author  : Virace
# @Email   : Virace@aliyun.com
# @Site    : x-item.com
# @Software: Pycharm
# @Create  : 2021/12/7 16:42
# @Update  : 2021/12/7 22:29
# @Detail  : 配置项

# 手机局域网IP
REMOTE_IP = '192.168.31.43'

# 手机内网本机IP
LOCAL_IP = '127.0.0.1'

# 插座IP
PLUG_IP = '192.168.31.42'
# 插座token, 需要使用 https://github.com/Maxmudjon/Get_MiHome_devices_token 获取
PLUG_TOKEN = '2c8481925eddef1a46f24613da644408'

# 微信推送token, https://wxpusher.zjiecode.com/
WX_TOKEN = '*****'


# 最低电量，开始充电
MIN_POWER = 30
# 最高电量，充电结束
MAX_POWER = 90

# 温度阈值
MAX_TT = 44
MIN_TT = 40
# 超过温度阈值几次触发提醒
TTC = 5

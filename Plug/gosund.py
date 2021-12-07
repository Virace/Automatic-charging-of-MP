# -*- coding: utf-8 -*-
# @Author  : Virace
# @Email   : Virace@aliyun.com
# @Site    : x-item.com
# @Software: PyCharm
# @Create  : 2021/11/25 14:54
# @Update  : 2021/11/25 14:54
# @Detail  :

from miio import Device


class GosundPlug(Device):
    def on(self):
        return self.send("set_properties", [{'siid': 2, 'piid': 1, 'did': 'state', 'value': True}])

    def off(self):
        return self.send("set_properties", [{'siid': 2, 'piid': 1, 'did': 'state', 'value': False}])

    def status(self):
        data = self.send("get_properties", [{'siid': 2, 'piid': 1, 'did': 'state'}])
        if data:
            return data[0]['value']




# -*- coding:utf-8 -*-
# @Time:2020/7/30 16:23
# @Author:Lzf
# @File:test_phone_login.py
from test_ddt.test_phone import Phone
import unittest
import ddt
#登录案例
data = [
    {"phone":"15779287194","key":"c889ca7e365e662c70e77a82d86fd8af","expect":"200"},
    {"phone":"","key":"c889ca7e365e662c70e77a82d86fd8af","expect":"201"},
]
d = [
    {"phone":"15779287194","key":"c889ca7e365e662c70e77a82d86fd8af","expect":"200"},
    {"phone":"","key":"c889ca7e365e662c70e77a82d86fd8af","expect":"201"},
]
@ddt.ddt
class TestPhone(unittest.TestCase):
    def setUp(self):
        self.p = Phone()

    @ddt.data(*data)
    # def test_phone(self,t):
    #     print("本次测试数据：%s" % t)
    #     phone = t["phone"]
    #     key = t["key"]
    #     expect = t["expect"]
    #     result = self.p.phone1(phone,key).json()["resultcode"]
    #     self.assertEqual(result,expect)


    def test_phone(self, testdata):
        print(testdata)
        phone = testdata["phone"]
        key = testdata["key"]
        expect = testdata["expect"]
        result = self.p.phone1(phone,key).json()["resultcode"]
        self.assertEqual(result,expect)

if __name__ == '__main__':
    unittest.main()
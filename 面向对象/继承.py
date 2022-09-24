"""
演示面向对象：继承的基础语法
"""


# 演示单继承
class Phone:
    IMEI = None  # 序列号
    producer = "ZH"  # 厂商

    def call_by_4g(self):
        print("4g通话")

    def call_by_5g(self):
        print("使用5g网络进行通话")


class Phone2022(Phone):
    face_id = "10001"  # 面部识别id

    def call_by_5g(self):
        print("2022年新功能：5g通话")


phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()


# 演示多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "ZH"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")


class MyPhone(Phone, NFCReader, RemoteControl):
    pass


phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

print(phone.producer)


# 演示多继承下，父类成员名一致的场景
class MyPhone(Phone):
    producer = "XWF"  # 复写父类的成员属性

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        # 方式1
        # print(f"父类的厂商是：{Phone.producer}")
        # Phone.call_by_5g(self)
        # 方式2
        print(f"父类的厂商是：{super().producer}")
        super().call_by_5g()
        print("关闭CPU单核模式，确保性能")


phone = MyPhone()
phone.call_by_5g()
print(phone.producer)




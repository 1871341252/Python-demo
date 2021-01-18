import time

class Outtime:
        def get_current_time(self):
                current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                #格式化当前时间戳
                # print(current_time)
                return current_time
                #返回时间戳
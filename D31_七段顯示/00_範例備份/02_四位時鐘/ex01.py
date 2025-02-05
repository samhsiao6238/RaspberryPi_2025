
# 時鐘

from time import sleep, localtime, time
from tm1637 import TM1637

# 定義 GPIO 腳位
DIO = 17
CLK = 18

class Clock:
    def __init__(self, tm_instance):
        self.tm = tm_instance
        self.show_colon = False  # 控制冒號顯示狀態
        self.last_toggle_time = time()  # 記錄上次切換冒號的時間

    def run(self):
        while True:
            t = localtime()

            # 每秒切換一次冒號
            if time() - self.last_toggle_time >= 1:
                self.show_colon = not self.show_colon
                self.last_toggle_time = time()

            # 先清除顯示，避免疊影
            self.tm.write([0, 0, 0, 0])
            sleep(0.01)  # 稍微延遲確保清除完成

            # 使用 `numbers()` 正確顯示時間
            self.tm.numbers(t.tm_hour, t.tm_min, self.show_colon)

            sleep(0.0001)  # 保持更新頻率

if __name__ == '__main__':
    tm = TM1637(CLK, DIO)
    tm.brightness(6)  # 設定亮度

    clock = Clock(tm)
    clock.run()

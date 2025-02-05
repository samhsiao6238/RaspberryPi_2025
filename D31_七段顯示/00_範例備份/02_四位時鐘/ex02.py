
# 連續遞增顯示數字，從 0000 到 9999，然後循環

from time import sleep, time
from tm1637 import TM1637

# 定義 GPIO 腳位
DIO = 17
CLK = 18

class CounterDisplay:
    def __init__(self, tm_instance):
        self.tm = tm_instance
        self.counter = 0  # 計數變數
        self.last_update_time = time()  # 記錄上次更新數字的時間

    def run(self):
        while True:
            # 取得當前時間
            current_time = time()

            # **維持數字穩定顯示**
            self.tm.show(f"{self.counter:04d}")  

            # **每秒鐘更新數字**
            if current_time - self.last_update_time >= 1:
                self.counter = (self.counter + 1) % 10000  # 遞增數字，超過 9999 則歸零
                self.last_update_time = current_time  # 更新上次變更時間

            sleep(0.0013)  # **保持顯示刷新頻率，確保畫面穩定**

if __name__ == '__main__':
    tm = TM1637(CLK, DIO)
    tm.brightness(6)  # 設定亮度

    counter_display = CounterDisplay(tm)
    counter_display.run()

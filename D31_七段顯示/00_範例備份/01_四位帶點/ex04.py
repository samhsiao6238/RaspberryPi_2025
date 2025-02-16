import time
from gpiozero import OutputDevice

# 常數
# 每次數字維持時間
INTERVAL = 0.01
# 單個數碼管切換間隔
INTERVAL_FLASH = 1.2
# 0000 顯示時間 (秒)
PAUSE_DURATION = 1
# 最終顯示號碼
FINAL_NUMBER = "1234"


# GPIO 腳位
# DS (Serial Data)
DATA_PIN = OutputDevice(17)
# ST_CP (Storage Register Clock)
LATCH_PIN = OutputDevice(27)
# SH_CP (Shift Register Clock)
CLOCK_PIN = OutputDevice(22)

# 共陰極 7 段顯示器數欄位碼
SEG_MAP = {
    '0': 0b11000000, '1': 0b11111001, '2': 0b10100100, '3': 0b10110000,
    '4': 0b10011001, '5': 0b10010010, '6': 0b10000010, '7': 0b11111000,
    '8': 0b10000000, '9': 0b10010000, '-': 0b10111111, ' ': 0b11111111
}

# 數碼管選擇信號 (低電位啟動)
# 從左到右：數碼管1、2、3、4
DIGIT_MAP = [0b1110, 0b1101, 0b1011, 0b0111]


# 傳送 16-bit (8-bit 段碼 + 8-bit 數碼管選擇)
def shift_out(data1, data2):
    # 關閉鎖存，準備傳輸
    LATCH_PIN.off()

    # 傳送 8-bit 段碼
    for i in range(8):
        bit = (data1 >> (7 - i)) & 1
        DATA_PIN.value = bit
        CLOCK_PIN.on()
        time.sleep(0.001)
        CLOCK_PIN.off()

    # 傳送 8-bit 數碼管選擇
    for i in range(8):
        bit = (data2 >> (7 - i)) & 1
        DATA_PIN.value = bit
        CLOCK_PIN.on()
        time.sleep(0.001)
        CLOCK_PIN.off()

    # 鎖存數據
    LATCH_PIN.on()
    # 確保穩定
    time.sleep(0.001)


# 顯示固定數字 `number` 持續 `duration` 秒
def display_fixed_number(number, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(4):
            shift_out(SEG_MAP[number[i]], DIGIT_MAP[i])
            # 保持穩定顯示，避免閃爍
            time.sleep(INTERVAL_FLASH)


# 輪播顯示 0-9，在所有數碼管
def test_digit_scroll():
    # 程式啟動時先顯示 0000，持續 3 秒
    display_fixed_number(FINAL_NUMBER, PAUSE_DURATION)

    while True:
        # 數字 0-9
        for num in range(10):
            start_time = time.time()
            # 維持 INTERVAL 時間
            while time.time() - start_time < INTERVAL:
                # 四個數碼管同步更新
                for i in range(4):
                    shift_out(SEG_MAP[str(num)], DIGIT_MAP[i])
                    time.sleep(INTERVAL_FLASH)

        # 每輪結束後，顯示 0000，持續 3 秒
        display_fixed_number(FINAL_NUMBER, PAUSE_DURATION)


# 主程式
if __name__ == '__main__':
    try:
        test_digit_scroll()
    except KeyboardInterrupt:
        # 停止時確保顯示 0000
        display_fixed_number(FINAL_NUMBER, 1)
        DATA_PIN.off()
        LATCH_PIN.off()
        CLOCK_PIN.off()

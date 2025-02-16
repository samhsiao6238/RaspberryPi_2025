import time
from gpiozero import OutputDevice

# 常數
INTERVAL = 0.01
INTERVAL_FALSH = 0.0001
# GPIO 腳位
# DS (Serial Data)
DATA_PIN = OutputDevice(17)
# ST_CP (Storage Register Clock)
LATCH_PIN = OutputDevice(27)
# SH_CP (Shift Register Clock)
CLOCK_PIN = OutputDevice(22)

# 共陰極 7 段顯示器數欄位碼
SEG_MAP = {
    '0': 0b11000000,
    '1': 0b11111001,
    '2': 0b10100100,
    '3': 0b10110000,
    '4': 0b10011001,
    '5': 0b10010010,
    '6': 0b10000010,
    '7': 0b11111000,
    '8': 0b10000000,
    '9': 0b10010000,
    '-': 0b10111111,
    ' ': 0b11111111  # 空白
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
    # 確保鎖存穩定
    time.sleep(0.001)

# 清除所有數碼管
def clear_display():
    # 依序清除四個數碼管
    for i in range(4):
        # 顯示空白
        shift_out(SEG_MAP[' '], DIGIT_MAP[i])
    time.sleep(0.5)

# 輪播顯示 0-9，在所有數碼管
def test_digit_scroll():
    # 先清除數碼管，避免殘留數據
    clear_display()
    while True:
        # 數字 0-9
        for num in range(10):
            start_time = time.time()
            # 維持 1 秒的穩定顯示
            while time.time() - start_time < INTERVAL:
                # 快速輪詢 4 個數碼管
                for i in range(4):
                    # 顯示相同數字在所有數碼管
                    shift_out(SEG_MAP[str(num)], DIGIT_MAP[i])
                    # 短暫間隔 (降低閃爍)
                    time.sleep(INTERVAL_FALSH)


if __name__ == '__main__':

    try:
        test_digit_scroll()
    except KeyboardInterrupt:
        clear_display()
        DATA_PIN.off()
        LATCH_PIN.off()
        CLOCK_PIN.off()
import urequests
import time
from boot import connect_wifi

# WiFi 設定
SSID = "SamHome2.4g"
PASSWORD = "sam112233"

# LINE Notify 權杖
LINE_TOKEN = "WemrA5mtsqcBcvTEG59tXmVGVTDj8wifXH51GzjWXx8"

def send_line_notify(message):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": f"Bearer {LINE_TOKEN}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = f"message={message}"
    response = urequests.post(url, headers=headers, data=data)
    print("回應碼：", response.status_code)
    response.close()

# 主流程
if connect_wifi(SSID, PASSWORD):
    print("✅ WiFi 已連線")
    send_line_notify("🎉 Pico W 成功上線並發送通知！")
else:
    print("❌ WiFi 連線失敗")
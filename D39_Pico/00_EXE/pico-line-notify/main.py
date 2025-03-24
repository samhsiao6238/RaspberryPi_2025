import urequests
from boot import connect_wifi
# 存放敏感資料的模組
import mysecrets

# WiFi 設定
SSID = mysecrets.SSID
PASSWORD = mysecrets.PASSWORD

# LINE Notify 權杖
LINE_TOKEN = mysecrets.LINE_TOKEN

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
    send_line_notify("🎉🎉 Pico W 成功上線")
else:
    print("❌ WiFi 連線失敗")
# 發送 Line 通知

_連線 Wi-Fi 並發送 LINE 通知_

<br>

## 敏感資訊

_針對權杖等敏感資訊皆需做保護處理_

<br>

1. 添加腳本處理敏感資訊。

    ```bash
    touch mysecrets.py .gitignore
    ```

<br>

2. 編輯 `.gitignore`，將敏感資訊加入。

    ```bash
    mysecrets.py
    ```

<br>

3. 編輯 `mysecrets.py` 內容。

    ```bash
    # mysecrets.py
    SSID = "<SSID-名稱>"
    PASSWORD = "<SSID-密碼>"
    LINE_TOKEN = "<Line-權杖>"
    ```

<br>

3. 修改 `upload.sh`，將新增的腳本加入上傳。

    ```bash
    #!/bin/bash

    # 上傳 boot.py 與 main.py 到 Pico W
    mpremote connect auto fs cp boot.py :boot.py
    mpremote connect auto fs cp main.py :main.py
    # 添加 `mysecrets.py`
    mpremote connect auto fs cp mysecrets.py :mysecrets.py
    echo "✅ 上傳完成！"
    ```

<br>

4. 修改主腳本 `main.py`；導入存放敏感資訊的腳本，然後透過模組名稱直接調用。

    ```python
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
    ```

<br>

## 編輯腳本

1. 編輯啟動腳本 `boot.py` 處理 Wi-Fi 初始化工作。

    ```python
    import network
    import time

    def connect_wifi(ssid, password):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            print('正在連線到 WiFi...')
            wlan.connect(ssid, password)
            timeout = 10
            while not wlan.isconnected() and timeout > 0:
                time.sleep(1)
                timeout -= 1
        return wlan.isconnected()
    ```

<br>

2. 編輯主腳本 `main.py`，用來連網後發送 LINE 通知

    ```python
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
    ```

<br>

3. 使用組合鍵上傳程式到 Pico W。

<br>

___

_END_
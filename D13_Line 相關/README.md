# 開機通知

_將 LINE Notify 遷移至 Messaging API，並以樹莓派開機通知為例_

## 建立 LINE 官方帳號

1. 前往 [LINE Developers Console](https://developers.line.biz/zh-hant/) 註冊或登入；使用 Line 帳號即可登入。

2. 建立 新的 LINE 官方帳號，該帳號將用於發送開機通知訊息。

## 取得 Channel Access Token

_相關細節先省略_

1. 在 `Messaging API` 中取得 `Channel Secret` 和 `Access Token`。

## 在樹莓派設定 Python 腳本

_以下 Python 腳本會在樹莓派開機時，自動發送通知給 LINE 官方帳號的好友。_

1. 建立虛擬環境。

```bash
mkdir -p ~/Desktop/PythonVenv && cd ~/Desktop/PythonVenv
python -m venv envBot
```

2. 編輯。

```bash
sudo nano ~/.bashrc
```

3. 加入。

```bash
source /home/sam6238/Documents/PythonVenv/envBot/bin/activate
```

4. 安裝必要的 Python 套件

```bash
pip install flask requests
```

## 建立腳本

1. 取得 User ID。

```bash


2. 在文件中建立腳本。

```bash
cd ~/Documents && touch line_notify.py
```

2. 建立 `line_notify.py` 腳本

```python
import requests

# 設定 LINE Messaging API Channel Access Token
LINE_ACCESS_TOKEN = "<輸入-Channel-Access-Token>"
# 可在 LINE Bot加為好友後取得
USER_ID = "<輸入-User-ID>"

def send_line_message(message):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}"
    }
    payload = {
        # 可改為群組 ID 或個人 ID
        "to": USER_ID,
        "messages": [
            {"type": "text", "text": message}
        ]
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code, response.text

if __name__ == "__main__":
    status, response_text = send_line_message("樹莓派已開機！🚀")
    print(f"狀態碼: {status}, 回應: {response_text}")
```

## 取得 User ID

1. 使用 `get_profile` API 取得的 `userId`

    ```bash
    curl -X GET "https://api.line.me/v2/bot/profile/{user_id}" \
            -H "Authorization: Bearer 你的 Channel Access Token"
    ```

2. 也可以讓 BOT 發送 `replyToken` 訊息，並查看 webhook 收到的 userId。

## 開機自動執行

1. 編輯 `rc.local`，適用於樹莓派系統。

    ```bash
    sudo nano /etc/rc.local
    ```

2. 在 `exit 0` 之前加上

    ```bash
    python /home/<使用者帳號>/line_notify.py &
    ```

3. 儲存並退出 `Ctrl+X` → `Y` → `Enter`。

4. 重新啟動樹莓派測試。

    ```bash
    sudo reboot
    ```


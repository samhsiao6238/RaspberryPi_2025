# 開機通知

_將 LINE Notify 遷移至 Messaging API，並以樹莓派開機通知為例_

<br>

## 建立 LINE 官方帳號

1. 前往 [LINE Developers Console](https://developers.line.biz/zh-hant/) 註冊或登入；使用 Line 帳號即可登入。

<br>

2. 建立 新的 LINE 官方帳號，該帳號將用於發送開機通知訊息。

<br>

## 取得 Channel Access Token

_相關細節先省略_

<br>

1. 在 `Messaging API` 中取得 `Channel Secret` 和 `Access Token`。

<br>

## 準備工作

_以下 Python 腳本會在樹莓派開機時，自動發送通知給 LINE 官方帳號的好友。_

<br>

1. 一鍵建立虛擬環境；命名為 `envLineBot`。

    ```bash
    mkdir -p ~/Documents/PythonVenvs
    cd ~/Documents/PythonVenvs
    python -m venv envLineBot
    echo 'source ~/Documents/PythonVenvs/envLineBot/bin/activate' >> ~/.bashrc
    source ~/.bashrc
    ```

<br>

2. 安裝必要的 Python 套件。

    ```bash
    pip install line-bot-sdk flask requests python-dotenv
    ```

<br>

## 建立專案

1. 在 `~/Document` 中建立腳本。

    ```bash
    mkdir -p ~/Documents/exLineMessage
    cd ~/Documents/exLineMessage
    touch line_message.py .env .gitignore
    ```

<br>

2. 使用 VSCode 連線。

3. 編輯 .gitignore。

```bash
.env
```

4. 編輯 `.env`。

```bash
_CHANNEL_ACCESS_TOKEN_=<貼上-TKOKEN>
_CHANNEL_SECRET_=<貼上-SECRET>
_USER_ID=<貼上-Your-user-ID>
```

5. 編輯 `line_message.py`。

    ```python
    import requests
    import os
    from dotenv import load_dotenv
    load_dotenv()

    # 讀取
    _CHANNEL_ACCESS_TOKEN = os.getenv("_CHANNEL_ACCESS_TOKEN_")
    _CHANNEL_SECRET = os.getenv("_CHANNEL_SECRET_")
    _USER_ID = os.getenv("_USER_ID")

    # 設定 LINE Messaging API Channel Access Token
    LINE_ACCESS_TOKEN = _CHANNEL_ACCESS_TOKEN
    # 可在 LINE Bot加為好友後取得
    USER_ID = _USER_ID

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

<br>

## 取得 User ID

1. 使用 `get_profile` API 取得的 `userId`

    ```bash
    curl -X GET "https://api.line.me/v2/bot/profile/{user_id}" \
            -H "Authorization: Bearer 你的 Channel Access Token"
    ```

<br>

2. 也可以讓 BOT 發送 `replyToken` 訊息，並查看 webhook 收到的 userId。

<br>

## 開機自動執行

1. 編輯 `rc.local`，適用於樹莓派系統。

    ```bash
    sudo nano /etc/rc.local
    ```

<br>

2. 在 `exit 0` 之前加上

    ```bash
    python /home/<使用者帳號>/line_message.py &
    ```

<br>

3. 儲存並退出 `Ctrl+X` → `Y` → `Enter`。

<br>

4. 重新啟動樹莓派測試。

    ```bash
    sudo reboot
    ```

<br>

___

_待補全_

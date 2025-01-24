# 部署伺服器 

_使用 Ngrok 將 VPN 伺服器公開到互聯網_

<br>

## 目標

1. 啟動 Ngrok，將樹莓派上的 OpenVPN 伺服器通過公開域名提供給客戶端訪問。

<br>

2. 確保客戶端可以正常通過 Ngrok 訪問 VPN。

<br>

## 設置 Ngrok

1. 安裝 Ngrok

    ```bash
    wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz
    tar -xvzf ngrok-v3-stable-linux-arm64.tgz
    sudo mv ngrok /usr/local/bin
    ```

<br>

2. 註冊一個 [Ngrok 帳戶](https://ngrok.com/)，登錄後取得身份驗證令牌。

<br>

3. 在樹莓派添加令牌。

    ```bash
    ngrok config add-authtoken <自己的-ngrok-令牌>
    ```

<br>

___

_END_
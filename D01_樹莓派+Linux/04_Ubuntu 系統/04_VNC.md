# VNC

_啟用 VNC 伺服器_

## 說明

1. 安裝 VNC Server

```bash
sudo apt update
sudo apt install x11vnc -y
```



### ✅ 設定 VNC 密碼（第一次設定）

```bash
x11vnc -storepasswd
```



### ✅ 建立 systemd 服務（開機自動啟動 VNC）

```bash
sudo nano /etc/systemd/system/x11vnc.service
```

貼上以下內容：

```ini
[Unit]
Description=Start x11vnc at startup.
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/x11vnc -auth guess -forever -loop -noxdamage -repeat -rfbauth /home/sam6238/.vnc/passwd -rfbport 5900 -shared -display :0
User=sam6238
Group=sam6238

[Install]
WantedBy=multi-user.target
```

儲存後執行：

```bash
sudo systemctl daemon-reexec
sudo systemctl enable x11vnc.service
sudo systemctl start x11vnc.service
```



### ✅ 開放防火牆埠（若有）

```bash
sudo ufw allow 5900/tcp
```



### ✅ 在 Mac 上連線

1. 打開 Finder → 前往 → 連接伺服器
2. 輸入：`vnc://<RaspberryPi_IP>`
3. 輸入你剛剛設定的 VNC 密碼



執行後即可成功從 Mac 連線到 Raspberry Pi 的 Ubuntu Desktop 介面。是否需要我幫你建立 systemd 腳本內容為 `.sh` 自動化執行？

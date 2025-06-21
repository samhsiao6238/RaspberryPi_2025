# 安裝桌面版

_Ubuntu 面版燒錄時，並未提示輸入 WiFi、使用者帳密、是否開啟 SSH 等設定；總之，完成燒錄就是一個預設環境的 Ubuntu 系統碟_

<br>

## 開始工作

_將 SD 卡插入樹莓派啟動，會進入歡迎畫面_

<br>

1. 鍵盤、輸入法使用預設，點擊 `Next`

<br>

2. 在 WiFi 設定部分選取並輸入密碼

<br>

3. 時區選擇台灣

<br>

4. 名稱部分主要是 `Username`、`Password`，其餘任意定義。

<br>

5. 進入畫面後，先查詢 IP。

    ```bash
    ip a
    ```

<br>

## SSH

_桌面版與 Server 相同_

<br>

1. 手動安裝 `openssh-server`。

    ```bash
    sudo apt install openssh-server -y
    ```

<br>

2. 啟動開機

    ```bash
    sudo reboot now
    ```

<br>

3. 查詢狀態

    ```bash
    sudo systemctl status ssh
    ```

<br>

_以下尚未編排_

## 設定文件

_在 SD 卡的 `system-boot` 分割區手動編輯設定檔_

## WiFi

1. Raspberry Pi 的 Ubuntu 系統使用 ext4 檔案系統儲存 Wi-Fi 設定，macOS 無法掛載 ext4 分區

## 使用者帳密

2. user-data、cloud-init，設定使用者帳號與密碼


## 查看各項設定

_將卡片插入電腦中查看_

1. 查看

```bash
ls /Volumes/system-boot
```
## VNC

_在樹莓派的 Ubuntu 桌面版中設定 VNC 遠端桌面_

1. 安裝 VNC Server；Ubuntu 沒有內建 VNC Server，建議使用 `x11vnc` 或 `tigervnc`，此處以 `x11vnc` 為例。

```bash
sudo apt update
sudo apt install -y x11vnc
```

2. 設定 VNC 密碼

```bash
x11vnc -storepasswd
```

3. 查看會是亂碼，若需重設可再次執行上一個步驟。

```bash
cat ~/.vnc/passwd
```

4. 建立自動啟動服務，讓 VNC 開機後自動執行

```bash
sudo nano /etc/systemd/system/x11vnc.service
```

5. 貼上以下內容，確認 `--auth` 路徑與 `--display :0` 正確

```ini
[Unit]
Description=Start x11vnc at startup.
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/x11vnc -auth /run/user/1000/gdm/Xauthority -forever -loop -noxdamage -repeat -rfbauth /home/sam6238/.vnc/passwd -rfbport 5900 -shared -display :0
User=sam6238
Group=sam6238

[Install]
WantedBy=multi-user.target
```

6. 啟用與啟動服務

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable x11vnc.service
sudo systemctl start x11vnc.service
```

7. 確認狀態

```bash
sudo systemctl status x11vnc.service
```

8. 編輯登入設定

```bash
sudo nano /etc/gdm3/custom.conf
```

9. 找到這行取消預設的註解

```bash
#WaylandEnable=false
```

10. 重啟系統

```bash
sudo reboot now
```

11. 手動啟動 x11vnc

```bash
sudo x11vnc -display :0 -auth guess -forever -usepw -shared
```

## ✅ 5. 連線方式

* 使用 RealVNC Viewer 或 TigerVNC Viewer
* 輸入 Raspberry Pi 的 IP（如 `192.168.1.157:5900` 或 `raspi.local:5900`）



## 📌 備註

* 如果你無法找到 `Xauthority` 檔案，可使用指令確認：

  ```bash
  sudo find /run/user -name Xauthority
  ```

* 若桌面未啟動或無顯示管理器（如 `gdm3`），也可安裝：

  ```bash
  sudo apt install ubuntu-desktop gdm3
  ```



需要我幫你轉成 cloud-init 設定讓開機自動完成這一切嗎？



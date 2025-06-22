_尚未完成_

<br>

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

4. 這時便可從本機進行連線。

    ```bash
    ssh <使用者帳號>@<樹莓派-IP>
    ```

<br>

_以下尚未編排_

## 設定文件

_在 SD 卡的 `system-boot` 分割區手動編輯設定檔_

<br>

## WiFi

1. Raspberry Pi 的 Ubuntu 系統使用 ext4 檔案系統儲存 Wi-Fi 設定，macOS 無法掛載 ext4 分區

<br>

## 使用者帳密

2. user-data、cloud-init，設定使用者帳號與密碼

<br>

## 查看各項設定

_將卡片插入電腦中查看_

<br>

1. 查看

    ```bash
    ls /Volumes/system-boot
    ```

<br>

___

_END_
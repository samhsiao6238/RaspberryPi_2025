# VPN

_在安卓電視系統上無法直接執行 `.ovpn` 文件，但可透過其他方式實現 VPN 連線_

<br>

## 使用 OpenVPN for Android

1. 下載 `OpenVPN for Android`

<br>

2. 將 `.ovpn` 文件傳輸到電視

    ```bash
    adb push yourfile.ovpn /sdcard/Download/
    ```

<br>

3. 導入 `.ovpn` 配置，從 `/sdcard/Download/` 路徑導入 `.ovpn` 文件。

<br>

4. 建立 VPN 連線

<br>

## 使用 adb 指令啟動自動化腳本

1. 如果想自動化運行 VPN 連線，可將 OpenVPN 配置指令寫入腳本並自動執行

    ```bash
    adb shell am start -n de.blinkt.openvpn/.LaunchVPN -e de.blinkt.openvpn.ARG_PROFILE "profile_name"
    ```

<br>

___

_END_
_無法翻牆，繼續努力_

# OpenVPN

<br>

## 下載

1. [下載](https://apk.ldplayer.tw/apps/net-openvpn-openvpn-apk.html)。

<br>

## 步驟 

1. 將 `china.ovpn` 檔案從 Mac 傳送至小米電視。

    ```bash
    adb push ~/Downloads/china.ovpn /sdcard/Download/
    ```

<br>

2. 檢查檔案是否成功傳送。

    ```bash
    adb shell ls /sdcard/Download/
    ```

<br>

3. 將檔案從本機傳輸到電視並自動安裝安裝；adb install 無法直接讀取 遠端設備上的檔案，僅適用於本地檔案系統；注意，此時電視會出現彈窗，需要確認。

    ```bash
    adb install ~/Downloads/net.openvpn.openvpn-3.0.5.apk
    ```

<br>

4. 檢查安裝狀態。

    ```bash
    adb shell pm list packages | grep openvpn
    ```

<br>

## 遠端檔案

1. 傳送。

    ```bash
    adb push ~/Downloads/uptodown-net.openvpn.openvpn.apk /sdcard/Download/
    ```

<br>

2. 使用 pm 指令安裝。

    ```bash
    adb shell pm install /sdcard/Download/uptodown-net.openvpn.openvpn.apk
    ```

<br>

___

_END_

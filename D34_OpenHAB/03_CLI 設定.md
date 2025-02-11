_尚未成功_

<br>

# 透過終端機指令設定

<br>

## 流程

1. 編輯規則檔案（Rules DSL）並將腳本寫入檔案。  

<br>

2. 將規則放置於 OpenHAB 的 `rules` 目錄中，OpenHAB 會自動加載並執行。  

<br>

## 建立 HTTP Thing

1. 編輯或建立新的 Things 檔案

    ```bash
    sudo nano /etc/openhab/things/linenotify.things
    ```

<br>

2. 貼上

    ```bash
    Thing http:url:linenotify "Line Notify Thing" [
        baseURL="https://notify-api.line.me/api/notify",
        timeout=3000,
        refresh=0
    ]
    ```

<br>

## 建立規則檔案

1. 建立一個新的規則檔，讓 OpenHAB 在啟動時執行 curl 發送 LINE Notify。

    ```bash
    sudo nano /etc/openhab/rules/startup_notify.rules
    ```

<br>

2. 在檔案中貼上以下規則代碼，特別注意，其中包含 Token，儲存並退出。

    ```java
    rule "Test Rule"
    when
        System started
    then
        logInfo("TestRule", "Test Rule has been executed successfully.")
    end
    ```

<br>

3. 檢查檔案權限是否為 openhab 用戶可讀寫

    ```bash
    sudo chown openhab:openhab /etc/openhab/rules/startup_notify.rules
    sudo chmod 644 /etc/openhab/rules/startup_notify.rules
    ```

<br>

4. 重啟 OpenHAB 服務，讓 OpenHAB 加載新規則

    ```bash
    sudo systemctl restart openhab.service
    ```

<br>

## 檢查執行狀況

1. 查看 OpenHAB 日誌，確認規則是否執行成功

    ```bash
    sudo journalctl -u openhab.service -f -n 30
    ```

<br>

2. 檢查語法。

    ```bash
    sudo cat /var/log/openhab/openhab.log | grep -i error
    ```

<br>

3. 檢查 OpenHAB 日誌，確認規則是否已加載

    ```bash
    sudo cat /var/log/openhab/openhab.log | grep "Loaded"
    ```

<br>

___

_END_

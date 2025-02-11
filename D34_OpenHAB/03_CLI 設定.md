_測試中_

<br>

# 建立 openHAB 規則

_啟動時發送 Line Notify_

1. 進入主控台。

```bash
sudo openhab-cli console
```

## 編輯規則檔案

1. 在 `/etc/openhab/rules/` 目錄下建立規則檔案。

```bash
sudo nano /etc/openhab/rules/startup_notify.rules
```

2. 寫入以下內容。

```java
rule "Startup Line Notify"
when
    System started
then
    val token = "Bearer WemrA5mtsqcBcvTEG59tXmVGVTDj8wifXH51GzjWXx8"
    val message = "OpenHAB 啟動成功！"
    val headers = newHashMap(
        "Authorization" -> token,
        "Content-Type" -> "application/x-www-form-urlencoded"
    )
    
    try {
        val response = sendHttpPostRequest("https://notify-api.line.me/api/notify", "application/x-www-form-urlencoded", "message=" + message, headers)
        logInfo("LineNotify", "已發送 Line Notify 訊息: " + response)
    } catch (Exception e) {
        logError("LineNotify", "發送 Line Notify 時發生錯誤: " + e.getMessage)
    }
end
```

3. 重啟 openHAB

```bash
sudo systemctl restart openhab.service
```

4. 檢查日誌。

```bash
sudo journalctl -u openhab.service -f -n 30
```

5. 登入伺服器。

```bash
sudo openhab-cli console
```

6. 檢查伺服器內日誌。

```bash
log:tail;
```

## 測試

1. 手動測試

```bash
openhab:automation trigger startup_notify-1;
```












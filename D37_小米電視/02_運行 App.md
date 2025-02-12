# 啟動應用

## 啟動已安裝的應用

1. 在終端中執行以下命令，列出所有已安裝的應用

```bash
adb shell pm list packages
```

2. 使用以下命令啟動應用

```bash
adb shell monkey -p com.package.name 1
```

3. 啟動 YouTube

```bash
adb shell monkey -p com.google.android.youtube.tv 1
```



## 透過 `am start` 指令精確啟動 Activity

1. 如果知道應用的主 Activity，可以使用 `am start`

```bash
adb shell am start -n com.package.name/.MainActivity
```

2. 啟動 Netflix 應用的主頁

```bash
adb shell am start -n com.netflix.ninja/.MainActivity
```

## 模擬按鍵操作

1. 模擬遙控器按鍵操作，控制電視導航到某個應用並啟動它

```bash
adb shell input keyevent KEYCODE_DPAD_UP       # 上
adb shell input keyevent KEYCODE_DPAD_DOWN     # 下
adb shell input keyevent KEYCODE_DPAD_LEFT     # 左
adb shell input keyevent KEYCODE_DPAD_RIGHT    # 右
adb shell input keyevent KEYCODE_DPAD_CENTER   # 確認
adb shell input keyevent KEYCODE_BACK          # 返回
adb shell input keyevent KEYCODE_HOME          # 返回主畫面
```

2. 遠端執行自訂腳本多步驟操作，並透過 ADB 執行

```bash
adb shell sh /sdcard/myscript.sh
```

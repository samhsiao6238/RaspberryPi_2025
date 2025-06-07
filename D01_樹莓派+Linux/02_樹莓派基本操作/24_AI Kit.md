_整理中_

# Raspberry Pi AI Kit

_搭配 USB 相機與麥克風_

## 安裝必要軟硬體

1. 更新系統。

```bash
sudo apt update && sudo apt full-upgrade -y 
```

2. 更新韌體。

```bash
sudo rpi-eeprom-update
```

3. 安裝 AI Kit 所需套件。

```bash
sudo apt install hailo-all -y
```

4. 列出目前已偵測到的 AI 模組。

```bash
hailortcli scan
```

## 檢查是否成功

1. 重新開機後輸入，如果有看到版本資訊，代表模組成功啟用。

```bash
hailortcli --version
```


---

## 🎥 第二階段：確認 USB 相機與麥克風可用性

### 1. 確認 USB 相機
```bash
ls /dev/video*
```
應該會出現 `/dev/video0`

使用 `ffmpeg` 或 `v4l2-ctl` 測試：
```bash
sudo apt install v4l-utils
v4l2-ctl --list-devices
```

### 2. 確認 USB 麥克風
```bash
arecord -l
```
應該可見 USB 音訊裝置，如：
```
card 1: USB Audio, device 0: ...
```

---

## 🤖 第三階段：實作 AI 專案（以 YOLO 物件偵測為例）

官方提供了一個 [Hailo + YOLOv5](https://github.com/hailo-ai/yolov5) 的套件，以下為精簡步驟：

### 1. 安裝 Git、Python 套件
```bash
sudo apt install git python3-pip
pip3 install opencv-python
```

### 2. 下載範例程式
```bash
git clone https://github.com/hailo-ai/yolov5.git
cd yolov5
```

### 3. 執行範例（使用 USB 相機）
```bash
python3 detect.py --source 0 --device hailo
```
參數說明：
- `--source 0`：使用 `/dev/video0`
- `--device hailo`：使用 Hailo NPU 加速

---

## 🧪 額外驗證與除錯

### 若出現無法開啟攝影機
確認權限與驅動：
```bash
groups $USER
```
確保你屬於 `video` 群組，否則加入：
```bash
sudo usermod -aG video $USER
```
然後重新登入。

---

## 🔊 麥克風語音辨識延伸應用（可選）
你可以使用 `speech_recognition` 搭配 `arecord` 收音並調用 Whisper / Google API：

```bash
pip3 install SpeechRecognition
```

---

是否需要我幫你製作「以語音指令控制物件辨識開關」的專案範例呢？
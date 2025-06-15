# AI Kit

_非使用樹莓派 Camera，搭配 USB 相機與麥克風_

<br>

## 硬體需求

1.  Raspberry Pi 4 或 5，並建議搭配主動散熱。

2. Hailo AI Kit 模組（M.2 或 HAT）。

3. USB 攝影機（UVC 相容）。

4. USB 麥克風。

<br>

## 系統與驅動安裝

1. 系統更新與韌體升級。

    ```bash
    sudo apt update && sudo apt full-upgrade -y
    sudo rpi-eeprom-update
    ```

<br>

2. 安裝 Hailo SDK 全套件；需重新開機。

    ```bash
    sudo apt install hailo-all -y
    sudo reboot now
    ```

<br>

3. 驗證 AI 模組是否正確載入，若成功會看到 `Hailo-8` 類型裝置與版本資訊。

    ```bash
    hailortcli scan
    ```

<br>

4. 查看版本。

```bash
hailortcli --version
```

5. 檢查韌體版本。

```bash
hailortcli fw-control identify
```

## USB 裝置確認

_攝影機與麥克風_

1. 安裝工具。

```bash
sudo apt install v4l-utils -y
sudo apt install rpicam-apps -y
```

2. 列出所有已註冊的攝影機設備節點。

```bash
ls /dev/video*
```

3. 查詢 Video4Linux2 系統中偵測到的攝影機設備。

```bash
v4l2-ctl --list-devices
```

4. 檢查音訊裝置

```bash
arecord -l
```

## AI 物件偵測專案

_YOLOv5 + Hailo_

1. 建立虛擬環境 `envAIKit`

```bash
cd ~/Documents
mkdir PythonVenvs && cd PythonVenvs
python -m venv envAIKit --system-site-packages
cd envAIKit/bin
VENV_PATH=$(pwd)
echo "source $VENV_PATH/activate" >> ~/.bashrc
source ~/.bashrc
```

2. 下載 YOLOv5 + Hailo 專案範例

```bash
cd ~/Documents
git clone https://github.com/hailo-ai/Hailo-Application-Code-Examples.git
cd Hailo-Application-Code-Examples/runtime/hailo-8/python/object_detection
```

3. 安裝依賴套件

```bash
python -m pip install -r requirements.txt
```

4. 下載 YOLOv5 模型等資源

```bash
bash download_resources.sh
```

5. 執行基本物件偵測；預設會讀取 yolov5s.hef 並從 /dev/video0 讀入影像來源，就是連接的 USB 攝像頭。

```bash
python object_detection.py
python object_detection.py --net yolov8n.hef
python object_detection.py --net yolov8n.hef --input /dev/video0

```

## 🪳 延伸應用：蟑螂偵測專案建議

你可以透過以下方式進一步客製化：

### ✅ 若你要訓練只辨識蟑螂：

1. 自行準備蟑螂圖片（收集 + 標註）
2. 使用 [Roboflow](https://roboflow.com/) 製作 YOLOv5 格式資料集
3. 在 PC 上用 GPU 訓練 YOLOv5 輕量模型（如 YOLOv5n、YOLOv5s）
4. 將模型轉為 `.onnx → .tflite → .hailomodel`
5. 使用 `hailomgr` 將模型燒錄至 AI Kit

若有需要，我可以幫你設計這整套流程與訓練腳本。



## 🗣️ 延伸應用：語音辨識入門

### 安裝語音辨識工具：

```bash
pip3 install SpeechRecognition
```

### 透過 `arecord` 收音 + Whisper API 辨識（示意）：

```python
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    print("請說話...")
    audio = r.listen(source)

text = r.recognize_google(audio, language="zh-TW")
print("你說的是：", text)
```

> 若 USB 麥克風不是預設裝置，需設定 `device_index`。



## ✅ 小結

| 模組           | 狀態                  |
|  | - |
| Hailo AI Kit | ✅ 已安裝並啟用            |
| USB 攝影機      | ✅ `/dev/video0` 可讀取 |
| USB 麥克風      | ✅ `arecord -l` 可列出  |
| YOLOv5 偵測    | ✅ 可即時辨識鏡頭畫面         |
| 語音辨識         | ✅ 初步實作語音輸入          |



需要我接下來幫你撰寫「蟑螂專屬訓練模型」的詳細步驟嗎？還是先幫你測試 USB 攝影機能否順利擷取影像？你想從哪一步開始？

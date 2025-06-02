# application.py 解析

_這是整個語音助理系統的主控核心，包含 `音訊處理`、語音識別與語音輸出、協議通訊、IoT 控制、喚醒詞偵測、模式切換（自動 / 手動）。_

## 系統初始化

_採用 Singleton 設計模式，確保整個應用程式只會建立一個 `Application` 實例。_

1. 配置管理器（`ConfigManager`）

2. 音訊編解碼器（`AudioCodec`）

3. 喚醒詞偵測器（`WakeWordDetector`）

4. 顯示介面（GUI 或 CLI）

5. 協議選擇（MQTT 或 WebSocket）

## 喚醒詞功能支援

1. 在 `config.json` 進行設定。

```json
"USE_WAKE_WORD": true,
"WAKE_WORDS": ["小智", "你好小明"]
```

1. 會依據以上設置進行初始化 `WakeWordDetector`，當喚醒詞被偵測到時，自動切換到 `連接 → 聆聽` 狀態並發送 `wake_word_detected` 事件。

## 狀態管理

_管理 4 種設備狀態_

1. `IDLE`（待命）

2. `CONNECTING`（連接中）

3. `LISTENING`（聆聽中）

4. `SPEAKING`（說話中）

## 事件循環

_提供事件循環 `_main_loop()` 處理_

1. 音訊輸入事件（錄音）

2. 音訊輸出事件（播放語音）

3. 任務排程事件（schedule）

## 協議處理

1. 支援 `WebSocketProtocol` 和 `MqttProtocol` 兩種通訊方式。

2. 對伺服器的訊息進行處理，包含 `tts` 語音回應、`stt` 使用者語音轉文字、`llm` LLM 模型的情緒反饋、`iot` 物聯網控制命令。

## 音訊流控制

1. 初始化 `AudioCodec`，管理 `輸入流（錄音）`、輸出流（語音播放）、音訊資料的讀取、編碼與解碼、支援模擬音量控制，若系統不支援實際調整。

## IoT 裝置整合

1. 在 `_initialize_iot_devices()` 中註冊裝置（如燈、喇叭、播放器、攝像頭、RAG模組等）。

2. 處理 IoT 控制命令，並透過 MQTT/WebSocket 傳送執行結果或狀態更新。

## 多執行緒與非同步設計

1. 採用 `asyncio` 搭配 `threading.Thread` 分離主循環與協議連接。

2. 音訊流、喚醒詞檢測等都透過獨立執行緒處理，保持即時性。

## 使用者介面支援

1. CLI 與 GUI 雙模支援，分別由 `cli_display.py` 與 `gui_display.py` 控制。

2. 回饋目前狀態、表情、音量等資訊。

## 錯誤處理與重連

1. 若遇到網路錯誤、自動中斷連接、重試最多 3 次。

4. 若連接失敗則提示用戶並恢復至 `IDLE` 狀態。



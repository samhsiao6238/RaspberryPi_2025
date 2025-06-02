# 腳本解析

_`main.py` 是 `Py-Xiaozhi` 的主啟動腳本，支持 `CLI` 與 `GUI` 模式切換，通訊協議可選擇 `mqtt` 或 `websocket`。_

<br>

## `argparse`

1. 參數解析

    ```python
    --mode        # 指定運行模式：cli 或 gui，預設為 gui
    --protocol    # 指定通訊協議：mqtt 或 websocket，預設為 websocket
    ```

<br>

2. 執行如下

    ```bash
    python main.py --mode cli --protocol websocket
    ```

<br>

## `signal_handler(sig, frame)`

1. 這是用來攔截 Ctrl+C（SIGINT），安全關閉應用

    ```python
    Application.get_instance().shutdown()
    ```

<br>

## `main()`

1. 設定日誌，從 `from src.utils.logging_config import setup_logging` 導入。

    ```bash
    setup_logging()
    ```

<br>

2. 建立應用，從 `from src.application import Application` 導入。

    ```bash
    # 導入
    from src.application import Application

    # 調用並建立
    app = Application.get_instance()
    ```

<br>

3. 啟動應用並傳入參數。

    ```bash
    app.run(
        mode=args.mode,
        protocol=args.protocol
    )
    ```

<br>

## `main.py` 其他依賴腳本

1. `src/application.py`，這是核心應用邏輯，包含 `Application.get_instance()`、`run()`、`shutdown()` 等方法。

<br>

2. `src/utils/logging_config.py`，自定義日誌初始化器 `setup_logging()`，控制 `logs/app.log` 輸出等。

<br>

3. `src/display/gui_display.py`、`cli_display.py` 是視覺化界面處理，根據 `--mode` 決定導入 GUI 或 CLI。

<br>

4. `src/network/mqtt_client.py`、`websocket_client.py` 是通訊協議相關模組，根據 `--protocol` 選擇。

<br>

5. `config/config.json` 是系統設定，例如 MQTT、喚醒詞、設備資訊等。

<br>

6. `models/` 是 VOSK 語音辨識模型、喚醒詞模型資料夾。

<br>

7. `src/audio/` 是音訊處理模組，如音訊輸入、播放等。

<br>

## 客製執行行為

1. 修改 `main.py` 的 `argparse` 設定

    ```python
    parser.add_argument('--config', help='自訂設定檔路徑')
    ```

<br>

2. 可加入新的通訊協議，在 `src/network/` 下新增模組，如 `grpc_client.py`，並在 `Application.run()` 中動態選擇初始化。

<br>

3. 可客製 CLI 行為，修改 `src/display/cli_display.py` 自訂輸入指令、顯示更多系統狀態、實作互動式命令列。

<br>

___

_END_
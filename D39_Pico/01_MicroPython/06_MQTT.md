接下來，我將引導你如何讓 Pico W 作為 MQTT 發佈端（Publisher），並透過 MicroPython 定時傳送內建溫度資料到 MQTT broker，供你在樹莓派 5 上作為訂閱端接收。



## ✅ 架構總覽

```
📟 Pico W（MicroPython） ──MQTT──▶ 🥧 Raspberry Pi 5（Subscriber）
```

- 發佈主題：`pico/temperature`
- 發佈內容：晶片溫度（格式為 `27.65` 文字）



## 🧰 第一步：準備 MQTT Broker

你可使用其中一種：

### ✅ 選項 1：使用 Raspberry Pi 5 架設 Mosquitto（建議）
```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
sudo systemctl enable mosquitto
```

Broker 就會在 `localhost` 上啟動，IP 請以實際樹莓派 IP 為準（例如 `192.168.1.50`）

### ✅ 選項 2：使用公開 MQTT Broker（測試用）
```text
broker.hivemq.com
```



## 🧾 第二步：編寫 MicroPython 發佈腳本（`main.py`）

### ✅ 請確認你已有上傳 `umqtt.simple` 套件（或使用 Pico W 含網路功能韌體）

```python
import network
import time
import machine
from umqtt.simple import MQTTClient

# 設定 Wi-Fi
ssid = '你的WiFi名稱'
password = '你的WiFi密碼'

# 設定 MQTT 參數
mqtt_server = '192.168.1.50'  # 或 broker.hivemq.com
client_id = 'pico-w-temp'
topic_pub = b'pico/temperature'

# 建立 Wi-Fi 連線
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("🔌 連接 Wi-Fi...")
while not wlan.isconnected():
    time.sleep(0.5)
print("✅ Wi-Fi 已連接，IP：", wlan.ifconfig()[0])

# 設定感測器
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / 65535

def read_temp():
    reading = sensor_temp.read_u16() * conversion_factor
    temperature_c = 27 - (reading - 0.706) / 0.001721
    return temperature_c

# 連接 MQTT
client = MQTTClient(client_id, mqtt_server)
client.connect()
print("📡 已連接 MQTT broker")

while True:
    temp = read_temp()
    msg = b"{:.2f}".format(temp)
    client.publish(topic_pub, msg)
    print("📤 發佈溫度：", msg)
    time.sleep(5)
```



## 📤 第三步：上傳並執行

```bash
mpremote connect auto fs cp main.py :main.py
```

> 可搭配 `boot.py` 自動連接 Wi-Fi，如有需求可再提供範例。



## 🧪 第四步：在 Raspberry Pi 5 訂閱接收溫度資料

```bash
mosquitto_sub -h localhost -t pico/temperature
```

若你是在別台樹莓派接收，請改成：

```bash
mosquitto_sub -h 192.168.1.50 -t pico/temperature
```



## 🧩 附加建議

- 若出現 `ImportError: no module named 'umqtt.simple'`，你需要使用支援 MQTT 的 MicroPython 韌體，或手動將 `umqtt` 上傳至 Pico。
- 可搭配 `boot.py` 自動啟動 Wi-Fi 與主程式。



是否需要我也提供一份自動佈署 `boot.py`、`main.py`、以及 `umqtt.simple.py` 的完整腳本？讓你一次上傳到 Pico？
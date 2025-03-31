# MQTT

_使用 Pico W 作為 MQTT `發佈端（Publisher）`，並定時傳送內建溫度資料到 MQTT broker，然後在另一台樹莓派上作為訂閱端接收。_

## 説明

1. 發佈主題是 `pico/temperature`，發佈內容是晶片溫度，格式為 `27.65` 文字。

2. 準備 MQTT Broker，可使用後續三中方式之一。

## 方式一

1. 可使用樹莓派 5 架設 Mosquitto。

```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
sudo systemctl enable mosquitto
```

2. Broker 就會在 `localhost` 上啟動，IP 請以實際樹莓派 IP 為準（例如 `192.168.1.50`）

## 方式二

1. 使用公開 MQTT Broker

```text
broker.hivemq.com
```

## 方式三

1. 上傳 `umqtt.simple` 套件，編寫發佈腳本（`main.py`）

```python
import network
import time
import machine
from umqtt.simple import MQTTClient

# 設定 Wi-Fi
ssid = '<WiFi-名稱>'
password = '<WiFi-密碼>'

# 設定 MQTT 參數，或 broker.hivemq.com
mqtt_server = '192.168.1.50'
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



## 上傳並執行

1. 透過 `mpremote` 進行連線，可搭配 `boot.py` 自動連接 Wi-Fi，如有需求可再提供範例。

```bash
mpremote connect auto fs cp main.py :main.py
```





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
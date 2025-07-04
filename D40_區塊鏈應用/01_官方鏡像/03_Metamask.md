這是根據你目前的進度，**整理後的 Metamask 與 Grafana 連接教學筆記**，已符合你樹莓派區網內的節點環境，保留 Markdown 格式供複製記錄使用：

---

# 🦊 Metamask 自訂 RPC 設定

*供本機開發或區網內其他裝置連接 Geth*

---

## 1. 查詢樹莓派 IP

```bash
hostname -I
```

> 📌 結果類似：`192.168.1.133`（以你的顯示為例）

---

## 2. 確認 Geth RPC 已啟用

Geth 節點需以以下方式啟動：

```bash
sudo geth \
  --datadir /mnt/ssd/geth \
  --http \
  --http.addr 0.0.0.0 \
  --http.api eth,net,web3 \
  --authrpc.addr 127.0.0.1 \
  --authrpc.port 8551 \
  --authrpc.vhosts=* \
  --authrpc.jwtsecret /mnt/ssd/geth/jwt.hex
```

確認 HTTP API 埠號 `8545` 正在 Listen：

```bash
sudo lsof -i :8545
```

---

## 3. 設定 Metamask 自訂 RPC

在 Metamask 中：

1. 點選「設定」→「網路」→「新增網路」
2. 填入以下資訊：

| 項目               | 內容                                |
| ------------------ | ----------------------------------- |
| 網路名稱           | RaspberryPi Ethereum Node           |
| 新的 RPC URL       | `http://192.168.1.133:8545`       |
| Chain ID           | `1`（主網）或 1337（開發鏈）      |
| Currency Symbol    | `ETH`                             |
| Block Explorer URL | 留空或填入 `https://etherscan.io` |

> ⚠️ 若 Geth 尚未同步完成，Metamask 可能無法顯示帳戶餘額或交易資訊

---

# 📊 加入 Grafana + Prometheus 監控 Lighthouse

---

## 1. 安裝 Prometheus

```bash
sudo apt install -y prometheus
```

---

## 2. 設定 Prometheus 抓取 Lighthouse 資料

修改 Prometheus 設定檔：

```bash
sudo nano /etc/prometheus/prometheus.yml
```

新增：

```yaml
scrape_configs:
  - job_name: 'lighthouse'
    static_configs:
      - targets: ['localhost:5054']
```

> 🔍 預設 Lighthouse metrics 開在 `localhost:5054`，若你有自訂 `--metrics-port`，請調整成對應數字。

儲存後重新啟動 Prometheus：

```bash
sudo systemctl restart prometheus
```

---

## 3. 安裝並啟動 Grafana

```bash
sudo apt install -y grafana
sudo systemctl enable grafana-server
sudo systemctl start grafana-server
```

瀏覽器開啟 Grafana：

```bash
http://<你的樹莓派 IP>:3000
```

登入預設帳密：

```bash
使用者名稱：admin
密碼：admin
```

---

## 4. 在 Grafana 中連接 Prometheus 並匯入 Dashboard

1. 點左側「⚙️ 設定」→「Data Sources」
2. 選擇 Prometheus，輸入 URL：

```
http://localhost:9090
```

3. 儲存並測試連線
4. 匯入社群儀表板（Dashboard）：

→ 點選左側「+」→「Import」

→ 輸入 ID：`13157`（或其他 Lighthouse 社群 Dashboard）

---

# ✅ 小結

你目前已完成：

* 🧱 成功啟動 Geth（執行層）與 Lighthouse（共識層）
* 🌐 可從區網裝置或瀏覽器連上 `8545` 做 JSON-RPC 查詢
* 🦊 可於 Metamask 加入自訂 RPC，進行本地測試或 DApp 開發
* 📊 可用 Grafana 監控區塊同步、狀態與 Peer 資訊

---

若你未來要開始 Validator 節點（進行 staking），再提醒我，我可提供：

* `lighthouse vc` 驗證者模組啟動方式
* 匯入 Keystore.json、驗證助記詞教學
* Rocket Pool / DappNode 架設方式（選配）

需要我補充 `curl` 測試範例與 Metamask debug 技巧嗎？

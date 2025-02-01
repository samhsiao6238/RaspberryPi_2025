# 無法轉發

_假如 Docker 的 `docker0` 網橋沒有取得 IPv4 地址，會導致容器內部的網路轉發無法正常進行；因為 OpenVPN 需要透過 `docker0` 進行 NAT 轉發，而 `docker0` 沒有 IP 的話，封包就無法通過。_

## 測試

1. 執行以下指令確認 `docker0` 是否正確取得到 IP

```bash
ip addr show docker0
```

2. 或者使用以下指令，如果輸出結果沒有類似 `inet 172.17.0.1` 這樣的 IPv4 地址，那可能是 `docker0` 沒有取得 IP，導致轉發失敗。

```bash
ifconfig docker0
```

## 解決方法

1. 最簡單的做法就是重啟 Docker

```bash
sudo systemctl restart docker
```

2. 如果是用 Snap 安裝的 Docker，則使用

```bash
sudo snap restart docker
```

3. 重啟後，再次檢查 `docker0` 是否取得到 IP。

4. 如果重啟無效，可以手動為 `docker0` 設定 IP

```bash
sudo ip link set docker0 down
sudo ip addr add 172.17.0.1/16 dev docker0
sudo ip link set docker0 up
```

5. 然後再檢查

```bash
ip addr show docker0
```

6. 如果 `docker0` 沒有正確啟動，可能是 Docker 網路的問題，可以嘗試重建，然後再次檢查 `docker0` 是否取得 IP。

```bash
sudo systemctl stop docker
sudo ip link delete docker0
sudo systemctl start docker
```

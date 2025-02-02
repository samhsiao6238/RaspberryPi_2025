# 

##

1. 編輯

```bash
code ~/.ssh
```

2. 寫入

```bash
Host buff
    HostName 192.168.11.1
    User root
```

3. 連線

```bash
ssh buff
```

## 檢查

1. DD-WRT 路由器內建 `OpenVPN`，可運行以下指令確認 `/usr/sbin/openvpn` 存在。

```bash
ls /usr/sbin/openvpn
```

2. 插入 USB 之後。

## 嘗試手動啟動 OpenVPN

1. 執行以下指令來手動測試 OpenVPN 是否能夠正常啟動

```bash
/usr/sbin/openvpn --config /tmp/mnt/sda1/chine.ovpn --verb 4
```

### 步驟 2：檢查 OpenVPN 是否正在運行
```sh
ps | grep openvpn
```
如果只有 `grep openvpn` 的回應，代表 OpenVPN 並未成功啟動。



### 步驟 3：檢查網路接口
```sh
ifconfig tun0
```
如果回應 `Device not found`，代表 OpenVPN 並未建立 VPN 隧道，可能的問題如下：
1. OpenVPN 配置錯誤
2. DNS 設定問題
3. NAT 設定錯誤



### 步驟 4：確認日誌
執行以下指令檢查 OpenVPN 啟動記錄：
```sh
logread | grep openvpn
dmesg | grep openvpn
```
如果 `logread` 無法使用，請先啟動 `syslogd`：
```sh
syslogd -O /tmp/syslog.log
logread | grep openvpn
```



### 步驟 5：確保 `ip_forward` 已啟用
執行以下指令確保路由器允許 VPN 流量：
```sh
echo 1 > /proc/sys/net/ipv4/ip_forward
```
🔹 這應該已經在你的 Startup Scripts 中啟用，但請再次確認。



### 步驟 6：手動啟用 NAT 規則
```sh
iptables -t nat -A POSTROUTING -o tun0 -j MASQUERADE
iptables -A FORWARD -i br0 -o tun0 -j ACCEPT
iptables -A FORWARD -i tun0 -o br0 -j ACCEPT
```
這將確保 VPN 流量能夠轉發到內部網絡。

⚠️ 重要提醒：這些 NAT 規則不會永久生效，若能解決問題，請到 DD-WRT → Administration → Commands 加入 `Firewall` 規則。



### 步驟 7：確認 OpenVPN 服務是否啟動
如果手動運行 OpenVPN 可以成功連接，但無法在 DD-WRT 內部啟動，請執行：
```sh
nvram show | grep openvpn
```
這將顯示目前 OpenVPN 相關的設定。

若 `nvram` 內沒有 `openvpn_enable=1`，請執行：
```sh
nvram set openvpn_enable=1
nvram commit
reboot
```
這將確保 OpenVPN 服務開機時自動啟動。



### 請執行這些步驟，並回報結果，我可以進一步幫助你排除問題！ 🚀
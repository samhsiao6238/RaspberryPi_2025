完成 PiVPN 的安裝和基本設置後，接下來需要進一步設定 Linksys 路由器，確保 VPN 伺服器可通過互聯網訪問，並將客戶端正確連接到 VPN。以下是詳細步驟：

---

## **1. 設定 Linksys 路由器 - 埠轉發 (Port Forwarding)**
PiVPN 的伺服器需要能從外部網路訪問，需在 Linksys 路由器中設置埠轉發：

### **步驟：**
1. **登入路由器管理頁面：**
   - 在瀏覽器輸入路由器的 IP（例如 `192.168.1.1`）。
   - 使用管理員帳戶登入。

2. **找到埠轉發設置：**
   - 在 Linksys 路由器中進入「**Security > Apps and Gaming > Port Forwarding**」。
   - 如果是 Velop 系列，找到「Port Forwarding」設置。

3. **新增埠轉發規則：**
   - **應用名稱 (Application Name)：** OpenVPN
   - **外部埠 (External Port)：** 1194（預設 OpenVPN 使用的埠號，或你在安裝 PiVPN 時選擇的埠號）
   - **內部埠 (Internal Port)：** 1194
   - **協議 (Protocol)：** UDP
   - **內部 IP 地址 (Device IP Address)：** 樹莓派的內網 IP（例如 `192.168.1.100`，可用 Pi 的 `ifconfig` 指令確認）。

4. **保存設置並應用：**
   - 完成後，保存設置，確保埠轉發生效。

---

## **2. 檢查公有 IP 或動態 DNS**
- 如果你的 Linksys 路由器使用的是靜態公有 IP：
  - 客戶端可以直接使用公有 IP（例如 `150.116.96.45`）連接。
- 如果是動態 IP（可能會改變）：
  - 建議設定 **動態 DNS (Dynamic DNS)**：
    1. 在路由器管理頁面找到 **Dynamic DNS (DDNS)** 功能。
    2. 配置服務（例如 `DuckDNS` 或 `No-IP`），設置域名（例如 `myvpn.duckdns.org`）。
    3. 確保 DDNS 功能正確同步公有 IP。

---

## **3. 測試 VPN 伺服器的連通性**
在 PiVPN 安裝完成後，使用以下指令檢查 VPN 伺服器是否正在運行：
```bash
sudo systemctl status openvpn
```
- 如果服務運行正常，你會看到 `active (running)`。

---

## **4. 配置 VPN 客戶端**
現在需要將生成的 `.ovpn` 文件導入客戶端設備，並進行連接測試：

### **步驟：**
1. **將 `.ovpn` 文件傳輸到客戶端設備：**
   - 使用 `scp` 或 USB 傳輸 `.ovpn` 文件到需要連接 VPN 的設備。

2. **在客戶端設備上安裝 OpenVPN 客戶端：**
   - **Windows**: 安裝 [OpenVPN GUI](https://openvpn.net/community-downloads/)。
   - **MacOS**: 安裝 [Tunnelblick](https://tunnelblick.net/)。
   - **Android/iOS**: 安裝 OpenVPN Connect（可從應用商店下載）。

3. **導入 `.ovpn` 配置文件：**
   - 打開 OpenVPN 客戶端，選擇「導入配置」，並加載 `.ovpn` 文件。

4. **連接 VPN：**
   - 啟動 VPN 客戶端，嘗試連接到 PiVPN 伺服器。
   - 連接成功後，所有網路流量將通過樹莓派上的 VPN 伺服器。

---

## **5. 測試連接效果**
1. **檢查 IP 是否通過 VPN：**
   - 打開瀏覽器訪問 [WhatIsMyIP](https://whatismyipaddress.com/)。
   - 確認顯示的 IP 地址是樹莓派所在網路的公有 IP（例如 `150.116.96.45`），而非客戶端的原始 IP。

2. **測試內部網路訪問：**
   - 如果需要，確認是否可以通過 VPN 訪問 Linksys 路由器或其他內部設備。

---

## **6. 問題排查**
如果連接失敗，檢查以下幾點：
1. **埠轉發配置是否正確：**
   - 確認 Linksys 路由器的埠轉發設置。
2. **防火牆設置：**
   - 確認路由器或樹莓派沒有阻擋 UDP 1194 的流量。
3. **VPN 日誌：**
   - 在樹莓派上查看 OpenVPN 日誌：
     ```bash
     sudo journalctl -u openvpn
     ```

---

如果還有其他需求或遇到問題，隨時告訴我，我可以進一步協助！
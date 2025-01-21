# 關於 Linksys

_Linksys 路由器支持安裝和使用 VPN_

## 支援的 VPN 類型

_Linksys 路由器通常支援以下幾種類型的 VPN_

1. VPN 客戶端模式 (VPN Client)：適合將整個網路流量通過 VPN 伺服器。

2. VPN 伺服器模式 (VPN Server)：適合遠端用戶連接至家用網路。

## 原生支持的 VPN

_某些高端型號（如 Linksys WRT 或 Velop 系列）內建支持以下功能_

1. OpenVPN Server： 允許遠端設備透過 VPN 連接到家用網路。

2. VPN Passthrough： 支援第三方 VPN 用戶端（例如 PPTP、L2TP/IPsec）的流量通過。

## 自訂韌體 (Custom Firmware)

如果路由器不直接支持 VPN，可以透過安裝自訂韌體（例如 DD-WRT 或  OpenWRT ）來實現 VPN 支援。步驟如下：

1. 確認路由器相容性： 到 [DD-WRT](https://dd-wrt.com/) 或 [OpenWRT](https://openwrt.org/) 官方網站，檢查你的 Linksys 型號是否支援這些韌體。
2. 備份現有設定： 確保你的路由器可以回復到原始狀態。
3. 刷入自訂韌體： 下載合適的韌體並按照說明進行安裝。
4. 設定 VPN： 在韌體中啟用 OpenVPN 或其他支持的 VPN 協議。



## 4. 使用 Linksys 應用或網頁管理界面

若路由器內建 VPN 支援，以下是基本設定步驟：

1. 登入管理界面： 使用瀏覽器訪問路由器的 IP 地址（通常是 `192.168.1.1`）。
2. 進入 VPN 設定：
   * 開啟 VPN Server 功能（如 OpenVPN）。
   * 輸入 VPN 伺服器詳細資訊（伺服器地址、憑證等）。
3. 保存並啟用： 確保設定正確並啟用功能。



## 5. 注意事項

型號限制： 部分入門級路由器可能不支持 VPN 功能。
效能影響： VPN 會增加路由器的處理負擔，建議使用硬體規格較高的型號。
安全性： 使用強加密的協議（如 OpenVPN 或 WireGuard），避免使用過時的 PPTP 協議。

如果需要更詳細的安裝或設定指引，請提供你的 Linksys 路由器具體型號，我可以為你準備相關步驟！

根據你的配置，兩台 Linksys MX4200 和三台 WHW03 (Velop) 屬於 Linksys 的 Velop 系列網狀路由器，這些路由器主要提供簡單易用的家庭網路解決方案，但其 VPN 支援相對有限。以下是針對你網路環境的 VPN 設置方法與選項：



### 1. 確認內建 VPN 支援
- MX4200 和 WHW03 並不內建 OpenVPN 伺服器或 VPN 客戶端功能。
- 它們支援 VPN Passthrough，允許通過外部裝置（例如電腦或路由背後的 VPN 伺服器）進行 VPN 連線。

如果你需要 VPN 客戶端或伺服器功能，你可能需要其他解決方案。



### 2. 透過 VPN Passthrough 使用第三方裝置
你可以利用 VPN Passthrough 功能，通過網路中的其他裝置來運行 VPN。方法如下：

#### A. 使用電腦作為 VPN 客戶端
1. 在你的電腦（Windows/Mac）上安裝 VPN 軟體，例如 NordVPN、ExpressVPN 或 OpenVPN。
2. 確保電腦連接到 Velop 網路。
3. 使用 VPN 軟體連線到 VPN 伺服器。
   - Velop 路由器將允許這些加密的 VPN 流量通過。

#### B. 添加獨立的 VPN 路由器
1. 購買支持 VPN 功能的路由器（如 Linksys WRT3200ACM 或其他支持 OpenVPN 的路由器）。
2. 設置該路由器為 Velop 網狀網路的從屬路由器（Bridge 模式）。
3. 在該路由器上配置 VPN 客戶端或伺服器。
4. 將需要 VPN 的裝置連接到此路由器。



### 3. 使用第三方韌體（需進階操作）
Linksys Velop 系列並不直接支援自訂韌體（如 DD-WRT 或 OpenWRT），因此你可能無法通過刷韌體來啟用 VPN 功能。



### 4. 遠端連接家庭網路（非商用 VPN 解決方案）
如果你的需求是遠端連接家用網路，以下是一些替代選項：

#### A. 使用 Linksys Velop 的外部訪問功能
1. 透過 Linksys App 開啟遠端管理功能：
   - 在 App 中進入「路由器設置」，啟用「遠端訪問」。
   - 使用 Linksys 帳號登入，即可從遠端管理路由器。
2. 此功能僅限管理用途，不適用於加密流量的 VPN。

#### B. 使用 NAS 或樹莓派搭建 VPN 伺服器
如果你有 NAS 或 Raspberry Pi，可以將其配置為 VPN 伺服器：
1. 配置 NAS（例如 Synology 或 QNAP）的 OpenVPN Server。
2. 或在樹莓派上安裝 OpenVPN 或 WireGuard。
3. 將 MX4200 設置為允許外部連接到內部伺服器的流量：
   - 開啟 埠轉發 (Port Forwarding)，將 VPN 流量（例如 TCP 1194 或 UDP 51820）轉發到伺服器的內部 IP。



### 5. 具體步驟：開啟埠轉發
若需搭建 VPN 伺服器，你需要在 MX4200 中設定埠轉發：
1. 登入管理介面：
   - 開啟瀏覽器並輸入 `192.168.1.1`，或使用 Linksys App 登入。
2. 進入埠轉發設置：
   - 在設定介面中找到「Security > Port Forwarding」。
3. 添加埠轉發條目：
   - 協議：TCP 或 UDP（取決於你的 VPN 協議）
   - 外部埠與內部埠：1194（OpenVPN 預設埠）或 51820（WireGuard 預設埠）
   - 內部 IP：指定伺服器（例如 NAS 或樹莓派）的內部 IP。
4. 保存設置並測試連線。



### 6. 更佳選項：購買支持 VPN 的路由器
如果上述方法太複雜，你可以考慮升級到支持 VPN 伺服器功能的路由器，例如：
- Linksys WRT3200ACM
- Asus RT-AX88U
- Netgear Nighthawk R7000

將這些路由器與 Velop 系統結合使用（作為 VPN 路由器），即可輕鬆實現 VPN 功能。

如果需要進一步的設定指引或有其他疑問，請隨時告訴我！
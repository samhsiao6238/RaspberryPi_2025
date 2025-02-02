# 使用 OpenVPN Access Server

_這是 OpenVPN 官方提供的 Web 管理介面版本_

<br>

## 準備工作

_在本機中進行_

<br>

1. 檢查 Docker 是否安裝。

   ```bash
   docker --version
   ```

<br>

2. 檢查 Docker 服務是否運行。

   ```bash
   docker info
   ```

<br>

3. 啟動 Docker Desktop 即可啟動服務。

<br>

## 上傳鏡像

_因爲在雲端似乎難以拉取，所以從本地上傳_

<br>

1. 先確認能遠程連線，因為後續要使用 `scp` 指令。

   ```bash
   ssh ali
   ```

<br>

2. 本機下載 `linux/amd64` 架構的 `OpenVPN` 鏡像；若建立 `linux/arm64` 實例，則無需加入參數。

   ```bash
   cd ~/Downloads && docker pull --platform linux/amd64 openvpn/openvpn-as
   ```

<br>

3. 檢查是否有重複；從這個案例來看確實出現重複。

   ```bash
   docker images | grep openvpn
   ```

   ![](images/img_56.png)

<br>

4. 依據指定標籤刪除鏡像。

   ```bash
   docker rmi 066e8adf3a47
   ```

<br>

5. 壓縮；務必確認當前工作路徑。

   ```bash
   docker save -o openvpn-as.tar openvpn/openvpn-as
   ```

<br>

6. 傳送到雲端；需要一段時間。

   ```bash
   scp ~/Downloads/openvpn-as.tar ali:~/
   ```

   ![](images/img_33.png)

<br>

7. 確認鏡像的作業系統。

   ```bash
   docker inspect --format='{{.Os}} {{.Architecture}}' <鏡像-ID>
   ```

   ![](images/img_76.png)

<br>

## 設置雲端環境

_使用 SSH 連線 ECS 實例_

<br>

1. 安裝 Docker；假如是有預裝的實例，可跳過這第一步。

   ```bash
   apt update && apt install -y docker.io
   ```

<br>

2. 安裝後會自動啟動服務，可透過指令查看運行狀態。

   ```bash
   systemctl status docker
   ```

   ![](images/img_19.png)

<br>

3. 若未啟動，可手動啟動服務。

   ```bash
   systemctl enable --now docker
   ```

<br>

4. 載入上傳的鏡像壓縮文件。

   ```bash
   docker load -i /root/openvpn-as.tar
   ```

   ![](images/img_20.png)

<br>

5. 確認鏡像是否成功載入。

   ```bash
   docker images
   ```

   ![](images/img_34.png)

<br>

6. 使用本地鏡像啟動 `OpenVPN Access Server`。

   ```bash
   docker run -d \
      --name openvpn-as \
      --restart always \
      --cap-add=NET_ADMIN \
      --cap-add=NET_RAW \
      --privileged \
      -v /run:/run \
      -p 943:943 \
      -p 9443:9443 \
      -p 1194:1194/udp \
      openvpn/openvpn-as
   ```

   ![](images/img_21.png)

<br>

7. 檢查容器狀態。

   ```bash
   docker ps
   ```

   ![](images/img_22.png)

<br>

8. 可確認端口是否都正確設置。

   ![](images/img_57.png)

<br>

## 監聽測試

_進行後續步驟之前，先進行端口轉發測試，特別注意，是否正確轉發流量皆以這個步驟為準_

<br>

1. 開啟三個終端視窗，分別進入容器、進入宿主機以及本地電腦，進入容器的指令如下。

   ```bash
   docker exec -it openvpn-as bash
   ```

<br>

2. 先檢查兩者的端口監聽；一般來說，宿主機應可看到監聽 `1194`，但容器沒有。

   ```bash
   netstat -tulnp
   ```

<br>

3. 在容器內安裝 `tcpdump`。

   ```bash
   apt update && apt install -y tcpdump
   ```

<br>

4. 在容器內監控 `UDP 1194`，這會顯示所有發 `容器 1194 端口` 的流量。

   ```bash
   tcpdump -i any udp port 1194
   ```

   ![](images/img_77.png)

<br>

5. 在宿主機監控 `UDP 1194`，與前一步驟相同，顯示的訊息也會相同。

   ```bash
   sudo tcpdump -i any udp port 1194
   ```

<br>

5. 複製 ECS 公網 IP 如 `121.41.38.218`，在本地電腦使用 `netcat (nc)` 發送 `UDP` 封包到宿主機 `1194` 端口。

   ```bash
   nc -u -v 121.41.38.218 1194
   ```

   ![](images/img_78.png)

<br>

6. 在本地終端中繼續輸入任意文字後按下 `ENTER`；對於一個封包來說，宿主機公網介面 eth0 收到來自 45.96.116.150 的 UDP 封包並轉發宿主機、宿主機內部的 Docker 橋接網路 (docker0) 會將這個封包 NAT 轉發給內部的 Docker 容器（IP 172.17.0.2），最後是容器的虛擬網卡 (vethXXXXXX) 扮演宿主機內的 `橋接通道`，將封包轉發到容器內的 eth0 介面；而容器內只會透過自己的 eth0 接收封包，所以只看到一條流量。

   ![](images/img_79.png)

<br>

7. 由測試結果可知，容器內 `1194` 的監聽是 OpenVPN 自動管理的，不需過度關注 netstat 的輸出結果，只要 `tcpdump` 顯示有流量，並且 OpenVPN 能正常運行，則代表一切都運行正常

<br>

## 檢查端口監聽

_補充相關指令_

<br>

1. 檢查端口監聽。

   ```bash
   netstat -tulnp
   ```

<br>

2. 進入容器。

   ```bash
   docker exec -it openvpn-as bash
   ```

<br>

3. 在宿主機建立 `iptables` 規則，將宿主機 `1194` 流量轉發到容器的 `918`。

   ```bash
   iptables -t nat -A PREROUTING -p udp --dport 1194 -j DNAT --to-destination 172.17.0.2:918
   iptables -t nat -A POSTROUTING -p udp --dport 918 -j MASQUERADE
   ```

<br>

4. 檢查宿主機是否有將外部的 `1194 UDP` 端口轉發到容器的內部端口。

   ```bash
   iptables -t nat -L -n -v | grep 1194
   ```

<br>

5. 在容器內部確認是否在監聽 `918 UDP` 端口。

   ```bash
   netstat -tulnp | grep 918
   ```

<br>

## 設定配置

1. 進入容器。

   ```bash
   docker exec -it openvpn-as bash
   ```

<br>

2. 更新套件列表並安裝 `nano`；通常系統只預設安裝 `vim`。

   ```bash
   apt update && apt install -y nano
   ```

<br>

3. 確認 `nano` 已安裝成功。

   ```bash
   nano --version
   ```

<br>

4. 修改 `as.conf` 配置；這是 `OpenVPN Access Server` 的主要配置文件。

   ```bash
   nano /usr/local/openvpn_as/etc/as.conf
   ```

<br>

5. 在文件底部添加以下設定。

   ```bash
   vpn.server.port=1194
   vpn.server.daemon.udp=openvpn
   vpn.server.daemon.udp.n_daemons=2
   vpn.server.daemon.tcp.port=443
   vpn.server.daemon.tcp.n_daemons=2
   ```

<br>

## 設定檔說明

_`as.conf` 設定內容介紹，無需實作_

<br>

1. 預設內容說明。

   ```bash
   # 指定私鑰位置
   cs.ca_key=~/web-ssl/ca.key

   # Web 伺服器的動態端口範圍
   cs.dynamic_port_base=870

   # 啟動的服務群組
   # Web 管理介面
   sa.initial_run_groups.0=web_group
   # VPN 伺服器
   sa.initial_run_groups.1=openvpn_group

   # 伺服器的單位編號
   sa.unit=0

   # 是否自動開放 Web 端口，包含 943、9443、443 等端口
   iptables.web=true

   # 伺服器運行的用戶與群組
   # 確保 OpenVPN 服務不以 root 權限運行，以增強安全性
   vpn.server.user=openvpn_as
   vpn.server.group=openvpn_as
   ```

<br>

2. 添加內容說明。

   ```bash
   # 設定伺服器監聽的 UDP 端口
   vpn.server.port=916
   # 使用 UDP 模式運行
   vpn.server.daemon.udp=openvpn
   # 產生 2 個 UDP 處理進程，提高性能
   vpn.server.daemon.udp.n_daemons=2
   # 同時監聽 TCP 443 端口
   vpn.server.daemon.tcp.port=443
   # 產生 2 個 TCP 處理進程
   vpn.server.daemon.tcp.n_daemons=2
   ```

<br>

## 重啟服務

1. 設定文件變動時需重啟；透過輸出可確認服務的重啟狀態。

   ```bash
   /usr/local/openvpn_as/scripts/sacli stop
   /usr/local/openvpn_as/scripts/sacli start
   ```

   ![](images/img_58.png)

<br>

2. 檢查容器內的指定端口 `1194` 是否被監聽。

   ```bash
   netstat -tulnp | grep 1194
   ```

<br>

## 嘗試排除無法監聽 `1194` 的問題

_以下紀錄原本使用預設端口 `1194` 時，嘗試的各種可能的方式排查容器無法監聽 `1194` 的問題，最終未能排除，僅做紀錄參考_

<br>

1. 查詢 OpenVPN 是否嘗試監聽 1194；正確。

   ```bash
   /usr/local/openvpn_as/scripts/sacli ConfigQuery | grep "vpn.server.port"
   ```

   ![](images/img_59.png)

<br>

2. 確認 OpenVPN 是否正常運行；正確。

   ```bash
   /usr/local/openvpn_as/scripts/sacli Status
   ```

   ![](images/img_60.png)

<br>

3. 檢查 OpenVPN Access Server 日誌；無錯誤。

   ```bash
   cat /var/log/openvpnas.log | tail -20
   ```

<br>

4. 確認容器是否正確開放 1194 端口；正確。

   ```bash
   cat /usr/local/openvpn_as/etc/as.conf | grep vpn.server
   ```

   ![](images/img_61.png)

<br>

5. 在實例終端機運行指令，檢查 Docker 端口映射；正確。

   ```bash
   docker ps | grep openvpn-as
   ```

   ![](images/img_62.png)

<br>

## 其他指令

_補充說明，無需實作_

<br>

1. 停止容器。

   ```bash
   docker stop openvpn-as
   ```

<br>

2. 使用參數 `rm` 移除容器。

   ```bash
   docker rm openvpn-as
   ```

<br>

3. 使用參數 `rmi` 移除包含鏡像在內的全部容器文件。

   ```bash
   docker rmi openvpn/openvpn-as
   ```

<br>

4. 重啟容器。

   ```bash
   docker restart openvpn-as
   ```

<br>

## 檢查端口監聽

_以下使用端口 `916`_

<br>

1. 查詢容器的端口監聽。

   ```bash
   netstat -tulnp
   ```

<br>

2. 在宿主機檢查是否有監聽 1194。

   ```bash
   netstat -tulnp | grep 1194
   ```

   ![](images/img_23.png)

<br>

3. 進入容器內部。

   ```bash
   docker exec -it openvpn-as bash
   ```

<br>

4. 檢查 OpenVPN 是否有監聽 1194。

   ```bash
   netstat -tulnp | grep 1194
   ```

   ![](images/img_35.png)

<br>

## 手動設定 916

_即使在 Docker 啟動時設置 `-p 1194:1194/udp`，仍需手動設置 `sacli` 來確保 OpenVPN 伺服器使用 `UDP`。_

<br>

1. 在容器內運行指令改用端口 `916`；特別注意，這個變更的設定會被寫入 `OpenVPN Access Server` 的內部設定資料庫，而不會直接修改 `as.conf`；另外，不建議直接修改 `as.conf`，因為 `OpenVPN Access Server` 主要使用內部設定資料庫來管理配置，直接修改 `as.conf` 可能不會生效，且容易在更新或重啟時被覆蓋。

   ```bash
   /usr/local/openvpn_as/scripts/sacli --key "vpn.server.port" --value "1194" ConfigPut
   /usr/local/openvpn_as/scripts/sacli --key "vpn.server.daemon.udp" --value "openvpn" ConfigPut
   ```

<br>

2. 檢查當前設定值。

   ```bash
   /usr/local/openvpn_as/scripts/sacli ConfigQuery | grep "vpn.server"
   ```

   ![](images/img_63.png)

<br>

3. 同時也修改 `as.conf`。

   ```bash
   nano /usr/local/openvpn_as/etc/as.conf
   ```

<br>

4. 將端口修正為原本的 `1194`。

   ![](images/img_65.png)

<br>

5. 再次重啟 OpenVPN。

   ```bash
   /usr/local/openvpn_as/scripts/sacli stop
   /usr/local/openvpn_as/scripts/sacli start
   ```

<br>

6. 宿主機添加對應規則，先安裝套件。

   ```bash
   apt install netfilter-persistent -y
   ```

<br>

7. 宿主機添加規則。

   ```bash
   iptables -A INPUT -p udp --dport 1194 -j ACCEPT
   netfilter-persistent save
   netfilter-persistent reload
   ```

<br>

8. 確認宿主機允許 UDP 1194。

   ```bash
   iptables -L -n -v | grep 1194
   ```

<br>

9. 若有重複規則，可進行刪除；一次會刪除一個。

   ```bash
   iptables -D INPUT -p udp --dport 1194 -j ACCEPT
   ```

<br>

___

_END_

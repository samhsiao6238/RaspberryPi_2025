# 使用 OpenVPN Access Server

_這是 OpenVPN 官方提供的 Web 管理介面版本_

<br>

## 本地

1. 先確認能遠程連線，因為後續要使用 `scp` 指令。

   ```bash
   ssh ali
   ```

<br>

2. 本機下載 `linux/amd64` 架構的 `OpenVPN` 鏡像。

   ```bash
   cd ~/Downloads && docker pull --platform linux/amd64 openvpn/openvpn-as
   ```

<br>

3. 壓縮；務必確認當前工作路徑。

   ```bash
   docker save -o openvpn-as.tar openvpn/openvpn-as
   ```

<br>

4. 傳送到雲端；需要一段時間。

   ```bash
   scp ~/Downloads/openvpn-as.tar ali:~/
   ```

   ![](images/img_33.png)

<br>

## 設置雲端環境

_使用 SSH 連線 ECS 實例_

<br>

1. 安裝 Docker；假如有勾選預裝，可跳過這第一步。

   ```bash
   sudo apt update && sudo apt install -y docker.io
   sudo systemctl enable --now docker
   ```

<br>

2. 查看 Docker 運行狀態。

   ```bash
   sudo systemctl status docker
   ```

   ![](images/img_19.png)

<br>

3. 載入上傳的 Docker 鏡像壓縮文件；運行指令後要稍等一下，不會立即開始。

   ```bash
   docker load -i /root/openvpn-as.tar
   ```

   ![](images/img_20.png)

<br>

4. 確認鏡像是否成功載入；輸出中預設還有另一個鏡像。

   ```bash
   docker images
   ```

   ![](images/img_34.png)

<br>

5. 啟動 OpenVPN Access Server；特別注意，這裡嘗試 改用 `914` 而不是預設的 `1194` 來監聽 OpenVPN，倘若失敗再改回來。

   ```bash
   sudo docker run -d \
      --name openvpn-as \
      --restart always \
      --cap-add=NET_ADMIN \
      --cap-add=NET_RAW \
      --privileged \
      -v /run:/run \
      -p 943:943 \
      -p 9443:9443 \
      -p 914:914/udp \
      openvpn/openvpn-as
   ```

   ![](images/img_21.png)

<br>

6. 檢查容器狀態。

   ```bash
   sudo docker ps
   ```

   ![](images/img_22.png)

<br>

## 設定配置

1. 進入容器。

   ```bash
   sudo docker exec -it openvpn-as bash
   ```

<br>

2. 更新套件列表並安裝 nano。

   ```bash
   apt update && apt install -y nano
   ```

<br>

3. 確認安裝成功。

   ```bash
   nano --version
   ```

<br>

4. 修改 as.conf 配置。

   ```bash
   nano /usr/local/openvpn_as/etc/as.conf
   ```

<br>

5. 在文件底部添加。

   ```bash
   vpn.server.port=914
   vpn.server.daemon.udp=openvpn
   vpn.server.daemon.udp.n_daemons=2
   vpn.server.daemon.tcp.port=443
   vpn.server.daemon.tcp.n_daemons=2
   ```

<br>

6. 應用新的設定。

   ```bash
   /usr/local/openvpn_as/scripts/sacli stop
   /usr/local/openvpn_as/scripts/sacli start
   ```

<br>

7. 確認是否成功監聽。

   ```bash
   netstat -tulnp | grep 914
   ```

<br>

## 其他指令

_補充說明，無需實作_

<br>

1. 停止容器。

   ```bash
   sudo docker stop openvpn-as
   ```

<br>

2. 移除容器。

   ```bash
   sudo docker rm openvpn-as
   ```

<br>

3. 完全移除，包含鏡像。

   ```bash
   sudo docker rmi openvpn/openvpn-as
   ```

<br>

## 檢查

_以下使用端口 `914`_

<br>

1. 在宿主機檢查是否有監聽 914。

   ```bash
   netstat -tulnp | grep 1194
   ```

   ![](images/img_23.png)

<br>

2. 進入容器內部。

   ```bash
   sudo docker exec -it openvpn-as bash
   ```

<br>

3. 檢查 OpenVPN 是否有監聽 914；會顯示並無監聽。

   ```bash
   netstat -tulnp | grep 914
   ```

   ![](images/img_35.png)

<br>

## VSCode 連線容器

_這裡補充說明如何透過 `Dev Containers` 插件連線進入容器內_

<br>

1. 開啟 VSCode，先使用 `遠端管理` 透過 SSH 連線宿主機；確認左下方已顯示。

   ![](images/img_36.png)

<br>

2. 連線後，開啟 `命令選擇區` 面板，並輸入 `Remote-Containers: Attach to Running Container`。

   ![](images/img_37.png)

<br>

3. 會出現容器，點擊選取。

   ![](images/img_38.png)

<br>

4. 會彈出新的 VSCode 工作視窗，右下角顯示 `連線到開發人員容器`；等候進度條完成。

   ![](images/img_24.png)

<br>

5. 開啟以下路徑，並找到設定文件 `etc/as.conf`。

   ```bash
   /usr/local/openvpn_as/
   ```

<br>

4. 在 `as.conf` 文件的 底部 添加或修改以下設定。

   ```bash
   # 設置 OpenVPN 服務監聽的端口
   vpn.server.port=914
   vpn.server.daemon.udp=openvpn
   vpn.server.daemon.udp.n_daemons=2
   vpn.server.daemon.tcp.port=443
   vpn.server.daemon.tcp.n_daemons=2
   ```

<br>

5. 應用設定並重啟 OpenVPN Access Server 在容器內執行；啟動後可略作觀察，確認 OpenVPN 服務正常啟動。

   ```bash
   /usr/local/openvpn_as/scripts/sacli stop
   /usr/local/openvpn_as/scripts/sacli start
   ```

   ![](images/img_39.png)

<br>

6. 查看容器對 `914` 的監聽；這裡沒有任何輸出，代表並未正常啟動監聽。

   ```bash
   netstat -tulnp | grep 914
   ```

<br>

7. 透過指令觀察監聽中的端口。

   ```bash
   netstat -tulnp
   ```

   ![](images/img_40.png)

<br>

8. 若要查看設定文件內容。

   ```bash
   cat /usr/local/openvpn_as/etc/as.conf
   ```

<br>

## 手動改用 914

_若已經設定了 `1194`，可透過以下步驟改用 `914`；若已設置為 `914` 可忽略以下步驟_

<br>

1. 在容器內運行指令改用端口 `914`。

   ```bash
   /usr/local/openvpn_as/scripts/sacli --key "vpn.server.port" --value "914" ConfigPut
   /usr/local/openvpn_as/scripts/sacli --key "vpn.server.daemon.udp" --value "openvpn" ConfigPut
   ```

<br>

2. 再次重啟 OpenVPN。

   ```bash
   /usr/local/openvpn_as/scripts/sacli stop
   /usr/local/openvpn_as/scripts/sacli start
   ```

<br>

3. 確認新端口是否監聽。

   ```bash
   netstat -tulnp | grep 914
   ```

<br>

## 設置使用者

_在容器內運行_

<br>

1. 進入 `openvpn-as` 容器。

   ```bash
   sudo docker exec -it openvpn-as bash
   ```

<br>

2. 建立使用者 `openvpn` 及密碼 `Sam-112233`。

   ```bash
   cd /usr/local/openvpn_as/scripts && ./sacli --user openvpn --new_pass "Sam-112233" SetLocalPassword
   ```

   ![](images/img_53.png)

<br>

3. 將使用者 `openvpn` 設置為 `管理員 superuser`。

   ```bash
   cd /usr/local/openvpn_as/scripts
   ./sacli --user openvpn --key type --value admin UserPropPut
   ./sacli --user openvpn --key prop_superuser --value true UserPropPut
   ./sacli start
   ```

<br>

4. 退出容器。

   ```bash
   exit
   ```

<br>

## 容器外運行內部指令

_以下示範在容器外運行容器內指令_

<br>

1. 若要在容器外對容器內運行指令。

   ```bash
   sudo docker exec -it openvpn-as bash -c "<將指令寫在這>"
   ```

<br>

2. 檢查用戶 `openvpn` 的屬性是否正確設置。

   ```bash
   sudo docker exec -it openvpn-as bash -c "/usr/local/openvpn_as/scripts/sacli --user openvpn UserPropGet"
   ```

<br>

3. 重新啟動 OpenVPN Access Server；`sacli start` 是容器內部針對 OpenVPN 的服務啟動指令。

   ```bash
   sudo docker exec -it openvpn-as bash -c "/usr/local/openvpn_as/scripts/sacli start"
   ```

<br>

## 取得網頁管理網址

1. 在實例中運行，可取得 OpenVPN 管理介面網址。

   ```bash
   SERVER_IP=$(curl -s ifconfig.me)
   echo "管理介面: https://$SERVER_IP:943/admin"
   echo "客戶端介面: https://$SERVER_IP:943/"
   ```

<br>

2. 先登入管理頁面，帳號密碼在前面步驟所自定。

   ![](images/img_54.png)

<br>

## 設定 IP

1. 登入管理頁面後，切換到 `Network Settings` 設置 `Hostname or IP Address` 為 `實例 IP`。

   ![](images/img_10.png)

<br>

2. 點擊下方的儲存。

   ![](images/img_41.png)

<br>

3. 點擊上方的更新。

   ![](images/img_42.png)

<br>

4. 點擊後會顯示 `無法連上 ...`，這是正常的，無需理會。

   ![](images/img_43.png)

<br>

5. 進入客戶端，輸入相同帳號密碼。

   ![](images/img_44.png)

<br>

6. 下載設定文件。

   ![](images/img_45.png)

<br>

7. 使用客戶端連線。

<br>

## 關於安全群組

_這裡記錄安全群組內容_

<br>

1. 當前的安全組。

   ![](images/img_09.png)

<br>

2. UDP 1194/1194，OpenVPN UDP。

<br>

3. TCP 9443/9443 是 OpenVPN Web UI 的管理頁面。

<br>

4. TCP 943/943 是OpenVPN Web UI 客戶端登入。

<br>

5. RDP TCP 3389 是遠端桌面 Windows。

<br>

6. ICMP 允許 ICMP Ping，可透過遠端透過 `ping` 指令進行連線測試。

<br>

7. TCP 22/22 是 SSH 連線。

<br>

## .ovpn 文件

1. 當前設定。

   ```bash
   # 加密演算法使用 AES-256-CBC 加密 VPN 流量
   cipher AES-256-CBC
   # 指定此配置用於客戶端模式
   client
   # 當客戶端嘗試連接伺服器時，最多等候 4 秒鐘
   server-poll-timeout 4
   # 不綁定本地端口
   # 允許客戶端使用動態端口，而不是固定的本地端口，適用於 NAT 環境
   nobind
   # 透過 TCP 連線到指定 IP 的 443 HTTPS 端口
   remote 8.136.110.37 443 tcp
   # 透過 UDP 連線到指定 IP 的 1194 OpenVPN 預設端口
   remote 8.136.110.37 1194 udp
   # 使用 TUN（Tunnel）介面，適用於 L3 隧道，路由模式
   dev tun
   # 明確指定設備類型為 TUN
   dev-type tun
   # 確保連接的伺服器提供有效的 TLS 憑證
   remote-cert-tls server
   # 只允許 TLS 1.2 以上的加密通訊，提升安全性
   tls-version-min 1.2
   # 設定 **604800 秒（7 天）**後，重新執行金鑰協商
   reneg-sec 604800
   # 設定最大傳輸單元，適合大部分網路環境的值，有助於減少封包分段
   tun-mtu 1420
   # 客戶端連接時，需要用戶名和密碼來進行身份驗證
   auth-user-pass
   # 日誌模式設定 `3`，顯示錯誤、警告與連線過程訊息
   verb 3
   # 讓伺服器接收客戶端的資訊
   # 客戶端會將一些系統資訊發送給伺服器
   push-peer-info

   <ca>
   -----BEGIN CERTIFICATE-----
   <略>
   -----END CERTIFICATE-----
   </ca>
   <cert>
   -----BEGIN CERTIFICATE-----
   <略>
   -----END CERTIFICATE-----
   </cert>
   <key>
   -----BEGIN PRIVATE KEY-----
   <略>
   -----END PRIVATE KEY-----
   </key>
   <tls-crypt-v2>
   -----BEGIN OpenVPN tls-crypt-v2 client key-----
   <略>
   -----END OpenVPN tls-crypt-v2 client key-----
   </tls-crypt-v2>
   ```

<br>

___

_END_

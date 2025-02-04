# VSCode 連線容器

_這裡補充說明如何透過 `Dev Containers` 插件連線進入容器內_

<br>

1. 開啟 VSCode，先使用 `遠端管理` 透過 SSH 連線宿主機；確認左下方已顯示。

   ![](images/img_36.png)

<br>

2. 連線後，開啟 `命令選擇區` 面板，並輸入 `Remote-Containers: Attach to Running Container`。

   ![](images/img_37.png)

<br>

3. 會出現容器，點擊選取；依照這個實作來說，只會有一個 `OpenVPN-as` 容器可選。

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

6. 在 `as.conf` 文件的 底部 添加或修改以下設定。

   ```bash
   # 設置 OpenVPN 服務監聽的端口
   vpn.server.port=1194
   vpn.server.daemon.udp=openvpn
   vpn.server.daemon.udp.n_daemons=2
   vpn.server.daemon.tcp.port=443
   vpn.server.daemon.tcp.n_daemons=2
   ```

<br>

7. 應用設定並重啟 OpenVPN Access Server 在容器內執行；啟動後可略作觀察，確認 OpenVPN 服務正常啟動。

   ```bash
   /usr/local/openvpn_as/scripts/sacli stop
   /usr/local/openvpn_as/scripts/sacli start
   ```

   ![](images/img_39.png)

<br>

8. 查看容器對 `1194` 的監聽；這裡沒有任何輸出，代表並未正常啟動監聽。

   ```bash
   netstat -tulnp | grep 1194
   ```

<br>

9. 透過指令觀察監聽中的端口。

   ```bash
   netstat -tulnp
   ```

   ![](images/img_40.png)

<br>

10. 若要查看設定文件內容。

   ```bash
   cat /usr/local/openvpn_as/etc/as.conf
   ```

<br>

___

_END_

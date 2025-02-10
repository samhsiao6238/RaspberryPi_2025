# 安裝 OpenVPN Access Server

_在樹莓派透過 Docker 安裝，參考 [官方說明](https://as-portal.openvpn.com/instructions/docker/installation)_

<br>

## 使用 Docker 安裝

_因為官方不支援樹莓派系統安裝，所以使用容器_

<br>

1. 安裝 Docker；特別注意，在樹莓派運行需要使用 `sudo`。

    ```bash
    sudo apt update && sudo apt install -y docker.io && sudo systemctl enable --now docker
    ```

<br>

2. 運行 `OpenVPN Access Server Docker` 鏡像，為該容器指定名稱為 `openvpn-as`，並加入參數 `-d` 以分離模式在後台運行容器。

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
        -p 1194:1194/udp \
        openvpn/openvpn-as
    ```

    ![](images/img_01.png)

<br>

3. 確認安裝完成。

    ```bash
    sudo docker ps
    ```

<br>

## 操作容器

_如要刪除容器，或是要重建容器，都可依據以下相同步驟進行_

<br>

1. 列出所有容器，添加參數 `-a` 會包括已停止的容器。

    ```bash
    sudo docker ps -a
    ```

<br>

2. 若要刪除已經存在的容器時，需先將容器停止 `stop`；這裡要刪除的容器是 `openvpn-as`。

    ```bash
    sudo docker stop openvpn-as
    ```

<br>

3. 然後刪除容器。

    ```bash
    sudo docker rm openvpn-as
    ```

<br>

4. 建立或重建容器；這裡指令與前面 _完全一致_。

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
        -p 1194:1194/udp \
        openvpn/openvpn-as
    ```

<br>

5. 再次確認容器狀態。

    ```bash
    sudo docker ps
    ```

    ![](images/img_03.png)

<br>

## 操作容器

_建立使用者_

<br>

1. 使用以下指令可進入容器中進行操作；進入後會顯示容器的 ID，可從前一個步驟的查詢結果驗證。

    ```bash
    sudo docker exec -it openvpn-as bash
    ```

    ![](images/img_04.png)

<br>

2. 建立使用者 `openvpn` 及密碼 `Sam-112233`。

    ```bash
    cd /usr/local/openvpn_as/scripts && ./sacli --user openvpn --new_pass "Sam-112233" SetLocalPassword
    ```

    ![](images/img_05.png)

<br>

3. 將該使用者 `openvpn` 設置為 `管理員 superuser`。

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

5. 檢查用戶 `openvpn` 的屬性是否正確設置。

    ```bash
    sudo docker exec -it openvpn-as bash -c "/usr/local/openvpn_as/scripts/sacli --user openvpn UserPropGet"
    ```

    ![](images/img_06.png)

<br>

6. 重新啟動 OpenVPN 伺服器；`sacli start` 是針對 OpenVPN 容器內部的 _服務啟動指令_。

    ```bash
    sudo docker exec -it openvpn-as bash -c "/usr/local/openvpn_as/scripts/sacli start"
    ```

<br>

7. 若需要可在宿主機上重新啟動容器；`docker restart` 是針對名為 `openvpn-as` 的 Docker 容器進行完整的重啟操作。

    ```bash
    sudo docker restart openvpn-as
    ```

<br>

8. 使用指令驗證用戶屬性。

    ```bash
    sudo docker exec -it openvpn-as bash -c "/usr/local/openvpn_as/scripts/sacli --user sam6238 UserPropGet"
    ```

<br>

9. 查看日誌。

    ```bash
    sudo docker logs openvpn-as
    ```

<br>

## 訪問伺服器

1. 確認樹莓派 IP。

    ```bash
    PI_IP=$(hostname -I | awk '{print $1}') && echo "https://$PI_IP:943/admin"
    ```

<br>

2. 訪問輸出的網址。

    ![](images/img_02.png)

<br>

3. 輸入自訂的帳號密碼。

    ![](images/img_08.png)

<br>

4. 同意之後登入。

    ![](images/img_07.png)

<br>

5. 展開左側 `Configuration`，進入 `Network Settings` 頁籤後，將 IP Address 改為樹莓派的 IP。

    ![](images/img_09.png)

<br>

6. 先按底部儲存。

    ![](images/img_10.png)

<br>

7. 再點擊頂部的 `Update Running Server`。

    ![](images/img_11.png)

<br>

8. 會先出現 `無法連上這個網站` 的提示，可不予理會。

    ![](images/img_18.png)

<br>

## 訪問客戶端網址

1. 訪問客戶端。

    ```bash
    PI_IP=$(hostname -I | awk '{print $1}') && echo "https://$PI_IP:943/"
    ```

<br>

2. 同樣輸入帳號密碼後登入，點擊下載 `.ovpn` 文件。

    ![](images/img_12.png)

<br>

4. 使用桌面應用登入。

    ![](images/img_13.png)

<br>

___

_END_



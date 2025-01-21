# 安裝 OpenVPN Access Server

_在樹莓派安裝_

## 使用 Docker 安裝

_因為官方不支援樹莓派系統安裝，所以使用容器_

1. 安裝 Docker。

    ```bash
    sudo apt update
    sudo apt install -y docker.io
    sudo systemctl enable --now docker
    ```

2. 運行 OpenVPN Access Server Docker 鏡像。

    ```bash
    sudo docker run --name openvpn-as -v /etc/openvpn:/etc/openvpn -d -p 943:943 -p 9443:9443 -p 1194:1194/udp openvpn/openvpn-as
    ```

## 建立容器

_如有必要刪除重建也是相同步驟_

1. 列出所有容器，包括已停止的容器。

    ```bash
    sudo docker ps -a
    ```

2. 如果已經存在或是重複，可先刪除容器。

    ```bash
    sudo docker rm openvpn-as
    ```

3. 建立或重建容器。

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

4. 再次確認容器狀態。

```bash
sudo docker ps
```

## 操作容器

1. 進入 openvpn-as 容器。

```bash
sudo docker exec -it openvpn-as bash
```

2. 建立使用者及密碼。

```bash
cd /usr/local/openvpn_as/scripts
./sacli --user sam6238 --new_pass sam112233 SetLocalPassword
```

3. 將該使用者 `sam6238` 設置為 `管理員 superuser`。

```bash
cd /usr/local/openvpn_as/scripts
./sacli --user sam6238 --key type --value admin UserPropPut
./sacli --user sam6238 --key prop_superuser --value true UserPropPut
./sacli start
```

4. 退出容器。

```bash
exit
```

5. 檢查用戶的屬性是否正確設置。

```bash
sudo docker exec -it openvpn-as bash -c "/usr/local/openvpn_as/scripts/sacli --user sam6238 UserPropGet"
```

6. 重新啟動 OpenVPN Access Server。

```bash
sudo docker exec -it openvpn-as bash -c "/usr/local/openvpn_as/scripts/sacli start"
```

7. 若需要可在宿主機上重新啟動容器。

```bash
sudo docker restart openvpn-as
```

8. 使用指令驗證用戶屬性。

```bash
sudo docker exec -it openvpn-as bash -c "/usr/local/openvpn_as/scripts/sacli --user sam6238 UserPropGet"
```

9. 查看日誌。

```bash
sudo docker logs openvpn-as
```

## 訪問伺服器

1. 訪問樹莓派 eth0 網址上指定端口所運作的容器。

```bash
https://192.168.1.154:943/admin/
```

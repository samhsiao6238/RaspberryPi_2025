# 安裝 MiniKube

_`MiniKube` 是一個用於本地 `Kubernetes` 集群的工具，它適合在開發環境中使用，以下在 `樹莓派 A` 進行安裝_

<br>

## 更新並安裝 Docker

_因為 `MiniKube` 依賴於 `Docker` 作為容器運行，所以先安裝 Docker。_

<br>

1. 更新樹莓派系統。

    ```bash
    sudo apt update
    sudo apt upgrade -y
    sudo apt autoremove -y
    ```

<br>

2. 透過查詢版本確認 `Docker` 是否已經安裝。

    ```bash
    docker -v
    ```

<br>

3. 若無版本號表示尚未安裝 `Docker`，運行以下安裝指令；以下指令搭配管道 `|` 直接執行，不留下腳本檔。

    ```bash
    curl -fsSL https://get.docker.com | sudo sh
    ```

<br>

4. 補充說明，若要先下載、再執行並保留安裝腳本，則運行以下指令；參數 `-o` 會把下載內容寫到檔案，不會輸出到標準輸出。

```bash
curl -fsSL https://get.docker.com -o get-docker.sh \
    && sudo sh get-docker.sh
```

## 設定權限

1. 檢查當前用戶群組；使用 `"$USER"` 或 `"$(whoami)"` 可指定當前用戶。

    ```bash
    groups "$USER"
    ```

<br>

2. 若不帶任何參數，`groups` 查詢結果也是當前使用者所屬群組。

    ```bash
    groups
    ```

<br>

3. 假如 `當前用戶` 不在群組 `docker` 內，則將其加入。

    ```bash
    sudo usermod -aG docker $USER
    ```

<br>

4. 特別注意，完成安裝 `Docker` 後，必須重啟系統或重啟終端套用變更，否則會出現錯誤。

    ```bash
    sudo reboot
    ```

    ![](images/img_45.png)

<br>

## 安裝 MiniKube

1. 安裝 MiniKube：下載並安裝 MiniKube 的二進制文件。

    ```bash
    curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-arm64
    ```

<br>

2. 添加執行權限。

    ```bash
    chmod +x minikube
    ```

<br>

3. 將執行文件搬移到系統路徑 `/usr/local/bin/` 中。

    ```bash
    sudo mv minikube /usr/local/bin/
    ```

<br>

4. 使用 Docker 作為驅動器啟動 MiniKube；無參數時效果與參數 `--driver=docker` 相同，都會在容器中啟動。

    ```bash
    minikube start
    ```

    ![](images/img_21.png)

<br>

5. 檢查 MiniKube 狀態，確認 MiniKube 已經成功啟動並運行。

    ```bash
    minikube status
    ```

    ![](images/img_01.png)

<br>

6. 檢查容器 IP；這是固定的。

    ```bash
    minikube ip
    ```

    _輸出_

    ```bash
    192.168.49.2
    ```

<br>

## 新增橋接 IP

1. 安裝了 Minikube 之後會添加一個橋接 IP `192.168.49.1/24`，這是 Minikube 建立的虛擬網路，用於管理 Kubernetes 集群內的 Pod 和服務之間的通信；Minikube 使用這個網路來分配 Kubernetes 集群內部的 IP 地址，確保 Pod 和服務之間的通信不受外部網路影響；使用 `kubectl` 指令時，Kubeconfig 文件中的 server 會指向這個網路的 IP 地址，通常是 Minikube 容器的 IP，例如 `192.168.49.2`。

<br>

2. 安裝了 Docker 之後會添加一個橋接 IP `172.17.0.1/16`，這是 Docker 預設建立的橋接網路，用於管理 Docker 容器之間的通信。

<br>

___

_END_
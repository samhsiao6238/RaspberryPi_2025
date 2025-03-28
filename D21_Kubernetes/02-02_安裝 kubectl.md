#  安裝 kubectl

_必須在要部署的設備上安裝 [kubctl on MacOS](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/)，而樹莓派也可以安裝指定版本 [kubctl on Linux](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)_

<br>

## 說明

1. K3s 自帶 kubectl，更適合在 Raspberry Pi 這類資源有限的設備上使用，無需手動安裝，獨立安裝 kubectl，適合用在開發環境或遠程管理其他叢集。

<br>

2. 不同場景選擇不同安裝方式，在樹莓派上安裝 K3s 這種場景，手動安裝 kubectl 並無必要；而本地開發環境如 Mac 需要連接遠程 Kubernetes 叢集時，只需要一個 kubectl 客戶端來管理外部 Kubernetes 叢集，這種手動安裝是必要的。

<br>

## MacOS 安裝 kubectl

_兩種安裝方式，這是第一種，簡單一點可以使用 Homebrew_

<br>

1. 先切換到下載路徑中。

    ```bash
    cd ~/Downloads
    ```

<br>

2. 下載最新版本。

    ```bash
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl"
    ```

<br>

3. 下載的是 kubectl 的 SHA-256 校驗和文件，用於驗證 kubectl 二進制文件的完整性。

    ```bash
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl.sha256"
    ```

<br>

4. 根據校驗和檔案驗證 kubectl 二進位檔案。

    ```bash
    echo "$(cat kubectl.sha256)  kubectl" | shasum -a 256 --check
    ```

    _輸出 OK 代表正確_

    ```bash
    kubectl: OK
    ```

<br>

5. 使 kubectl 二進位檔案可執行。

    ```bash
    chmod +x ./kubectl
    ```

<br>

6. 將 kubectl 二進位檔案移到系統上的檔案位置 `/usr/local/bin/kubectl`。

    ```bash
    sudo mv ./kubectl /usr/local/bin/kubectl && sudo chown root: /usr/local/bin/kubectl
    ```

<br>

7. 測試以確保安裝的版本是最新的。

    ```bash
    kubectl version --client
    ```

    _輸出顯示當前版本_

    ![](images/img_23.png)

<br>

8. 安裝並驗證 kubectl 後，刪除校驗和檔案。

    ```bash
    rm kubectl.sha256
    ```

<br>

## 樹莓派安裝 kubectl

_若樹莓派僅作客戶端來管理外部 Kubernetes 叢集，可在樹莓派也安裝 kubectl_

<br>

1. 先切換到下載路徑中。

    ```bash
    cd ~/Downloads
    ```

<br>

2. 下載最新版本；與 MacOS 下載的不同，這裡下載的是 Linux 系統使用的版本。

    ```bash
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl"
    ```

<br>

3. 下載驗證文件。

    ```bash
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl.sha256"
    ```

<br>

4. 根據校驗和檔案驗證 kubectl 二進位檔案。

    ```bash
    echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
    ```

    _通過驗證一樣會顯示 OK_

    ![](images/img_24.png)

<br>

5. 安裝 kubectl。

    ```bash
    sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
    ```

<br>

6. 刪除臨時文件。

    ```bash
    rm kubectl.sha256 kubectl
    ```

<br>

7. 測試安裝是否成功。

    ```bash
    kubectl version --client
    ```

    _輸出_

    ```bash
    Client Version: v1.30.3
    Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
    ```

<br>

___

_END_
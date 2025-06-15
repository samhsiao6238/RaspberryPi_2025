# 使用 SSD

_若要提升效能，可使用 SSD；這裡示範使用 SSD，並把 npm 的全域資料夾指到 SSD；若無該硬體設備則略過_

<br>

## 步驟說明

1. 建立。

    ```bash
    sudo mkdir -p /mnt/ssd/npm-global
    npm config set prefix /mnt/ssd/npm-global
    export PATH=/mnt/ssd/npm-global/bin:$PATH
    ```

<br>

2. 確認 `/mnt/ssd/npm-global` 目錄擁有你的帳號寫入權限。

    ```bash
    sudo chown -R $USER:$USER /mnt/ssd/npm-global
    ```

<br>

3. 設定 `npm` 全域安裝路徑。

    ```bash
    npm config set prefix /mnt/ssd/npm-global
    ```

<br>

4. 將 `npm-global/bin` 加入 `PATH`。

    ```bash
    export PATH=/mnt/ssd/npm-global/bin:$PATH
    ```

<br>

5. 每次登入自動生效。

    ```bash
    echo 'export PATH=/mnt/ssd/npm-global/bin:$PATH' >> ~/.bashrc
    source ~/.bashrc
    ```

<br>

___

_END_

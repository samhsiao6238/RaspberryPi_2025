# Pagekite

_在樹莓派上使用 Pagekite 建立安全反向隧道，將本機服務公開至網路_

<br>

## 建立帳號與 Kite 名稱

1. 訪問 [Pagekite.net](https://pagekite.net/)；點擊右上角的 `Sign Up` 註冊帳號。

<br>

2. 輸入 `Email`，並為第一個 Kite 設定子域名稱，如 `sam6238.pagekite.me`，完成註冊後前往信箱點擊驗證連結。

    ![](images/img_246.png)

<br>

## 在樹莓派上安裝 Pagekite

1. 使用官方安裝腳本，取得最新版 `pagekite.py`；這會把最新版的 pagekite.py 安裝到了 `/usr/local/bin`。

    ```bash
    cd ~/Downloads
    curl -s https://pagekite.net/pk/ | sudo bash
    ```

<br>

2. 第一次執行 QuickStart，註冊服務。

    ```bash
    sudo pagekite.py --signup sam6238.pagekite.me
    ```

<br>

3. 按提示輸入 Email 及 Secret，並選擇儲存配置至 `/root/.pagekite.rc`；完成後可進行查看。

    ```bash
    sudo cat /root/.pagekite.rc
    ```

<br>

4. 若斷線，可運行以下指令重新啟動臨時隧道，並映射至本機 80 埠。

    ```bash
    sudo pagekite.py 80 sam6238.pagekite.me
    ```

<br>

5. 在背景啟動服務。

    ```bash
    sudo python -m http.server 80 &
    ```

<br>

6. 在外部網路打開網址，即可看到本機服務。

    ```bash
    http://sam6238.pagekite.me
    ```

<br>

## 以套件方式安装

_特別注意，透過官方的安裝腳本只把 `pagekite.py` 拷貝到 `/usr/local/bin`，並沒有安裝 Debian 套件版，所以不會在 `/etc/pagekite.d/` 底下放任何範本或設定檔案_

<br>

1. 按 Debian 包方式安装。

    ```bash
    sudo apt update
    sudo apt install pagekite -y
    sudo systemctl enable pagekite
    sudo systemctl start pagekite
    ```

<br>

2. 若兩者同時存在，要繼續使用腳本啟動，必須指定在哪裡讀取設定。

    ```bash
    sudo pagekite.py --clean --optdir=/etc/pagekite.d
    ```

<br>

3. 複製設定文件到預設路徑；`10_account.rc` 用以儲存 Pagekite 帳號憑證。

    ```bash
    sudo mkdir -p /etc/pagekite.d
    sudo cp /root/.pagekite.rc /etc/pagekite.d/10_account.rc
    sudo chown root:root /etc/pagekite.d/10_account.rc
    ```

<br>

4. 編輯 `20_frontends.rc`，定義要用哪些 front-end relay、要把哪些本地埠映射到哪個 Kite 子域；特別注意，`Pagekite` 會依檔案名稱的字典序 `10_ → 20_ → 90_ ...` 逐一載入，這樣就能把 `帳號` 和 `服務映射` 拆成兩階段、分開維護。

    ```bash
    sudo nano /etc/pagekite.d/20_account.rc
    ```

<br>

5. 填入以下內容。

    ```bash
    # 使用官方預設 relay
    defaults

    # 將本機 HTTP(80) 對外公開
    service_on = 80 sam6238.pagekite.me

    # 同時映射 SSH(22)
    service_on = 22 ssh.sam6238.pagekite.me
    ```

<br>

## 以服務方式啟動

_補_

<br>

___

_END_

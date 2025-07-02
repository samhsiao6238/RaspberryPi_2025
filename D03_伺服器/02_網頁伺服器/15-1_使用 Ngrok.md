# Ngrok 

_[Ngrok 官網](https://ngrok.com/)；Ngrok 本身並不是一種 `伺服器服務`，而是一種 `通道服務`，執行後可取得 Ngrok 公開服務器的通道，讓外部使用者可以透過這個通道訪問本地網站，也就是讓樹莓派上的伺服器可被外網訪問_

<br>

## 安裝 Homebrew

1. 前往 [官網](https://brew.sh/) 複製安裝指令。

    ![](images/img_158.png)

<br>

2. 在樹莓派執行。

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

<br>

3. 依據提示把 Homebrew 加入環境變數

    ```bash
    echo >> /home/sam6238/.bashrc
    echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
    eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
    ```

    ![](images/img_159.png)

<br>

4. 依據建議安裝基本依賴套件

    ```bash
    sudo apt-get install build-essential
    ```

    ![](images/img_160.png)

<br>

## 安裝 Ngrok

1. 前往 [官網](https://dashboard.ngrok.com/get-started/setup/raspberrypi) 下載頁面，切換到樹莓派的 `Homebrew` 選項中。

    ![](images/img_161.png)

<br>

2. 複製指令運行。

    ```bash
    curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
        | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
        && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
        | sudo tee /etc/apt/sources.list.d/ngrok.list \
        && sudo apt update \
        && sudo apt install ngrok
    ```

<br>

3. 接著運行以下指令。

    ```bash
    ngrok config add-authtoken <輸入個人-TOKEN>
    ```

<br>

4. 完成時會提示儲存位置。

    ```bash
    ~/.config/ngrok/ngrok.yml
    ```

    ![](images/img_162.png)

<br>

5. 啟動 Ngrok 並指定端口為 8080。

    ```bash
    ngrok http 8080
    ```

    ![](images/img_163.png)

<br>

6. 複製 `Forwarding` 網址並開啟瀏覽器訪問。

    ![](images/img_164.png)

<br>

7. 點擊 `Visit Site`。

    ![](images/img_165.png)

<br>

8. 就會看到當前在 `8080` 端口運行的伺服器，目前是 `Ngnix` 伺服器。

    ![](images/img_166.png)

<br>

## 錯誤排除

1. 假如啟動時出現以下訊息代表尚未驗證獲授權。 

    ![](images/img_117.png)

<br>

2. 假如是訪問看到如下錯誤，也是因為尚無授權資訊。

    ![](images/img_95.png)

<br>

3. 當系統中已存在設定檔案，在版本更新時可能出現設定檔錯誤警告；可運行以下指令自動轉換設定檔。

    ```bash
    ngrok config upgrade
    ```

<br>

## 註冊

1. 前往 [Ngrok 官網](https://ngrok.com/) 點擊 `Sign up`，已有帳戶可點擊 `Login in`。

    ![](images/img_32.png)

<br>

2. 建議使用 Google 帳號快速註冊。

    ![](images/img_33.png)

<br>

3. 複製 `Authtoken` 或保留瀏覽頁面備用。

    ![](images/img_31.png)

<br>

4. 在終端機執行以下指令進行授權，完成時會輸出儲存路徑。

    ```bash
    ngrok authtoken <複製下來的-Authtoken>
    ```

    ![](images/img_118.png)

<br>

5. 假如是依照官網指示安裝的版本，可以適用以下新版指令，在沒有其他參數時，兩者效果一致，這裡不做贅述。

    ```bash
    ngrok config add-authtoken <複製下來的-Authtoken>
    ```

    ![](images/img_94.png)

<br>

6. 再次啟動服務；以下指令是使用端口 `80`，若使用其他端口則自行修正參數。

    ```bash
    ./ngrok http 80
    ```

<br>

7. 假如版本過低會出現以下警告。

    ![](images/img_34.png)

<br>

8. 可複製公網網址進行訪問。

    ![](images/img_140.png)

<br>

9. 若正常運行會顯示如下，點擊 `Visit Site` 。

    ![](images/img_96.png)

<br>

10. 就會看到目前樹莓派的 Nginx 服務器了；同時終端機會顯示 `200 OK`。

    ![](images/img_97.png)

<br>

## 將 Ngrok 移動到系統 PATH 中

_可先關閉 Ngrok_

<br>

1. 切換到當前所在的路徑中。

    ```bash
    ls ~/Documents/NgrokApp/ngrok
    ```

<br>

2. 確保具有可執行權限。

    ```bash
    sudo chmod +x ~/Documents/NgrokApp/ngrok
    ```

<br>

3. 將 `ngrok` 執行檔移動到 `/usr/local/bin`，使其成為系統全域指令。

    ```bash
    sudo mv ~/Documents/NgrokApp/ngrok /usr/local/bin/ngrok
    ```

<br>

4. 同時也可進一步檢查 `/usr/local/bin` 是否已經在 PATH 環境變數中。

    ```bash
    echo $PATH
    ```

    ![](images/img_141.png)

<br>

5. 如果 `/usr/local/bin` 不在 PATH 中，請添加到配置文件 `.bashrc`。

    ```bash
    echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bashrc
    source ~/.bashrc
    ```

<br>

6. 完成後，切換到任意目錄中並運行以下指令，確認設置是否完成；特別注意，設定完成後執行的就是全域指令，也就是系統路徑中的 `ngrok`，所以不使用 `./`；另外，在尚未建立全域變數時，即便位在腳本所在路徑中也必須加上 `./`，因為 `Linux/macOS` 系統預設不會將 `當前目錄` 加入 `$PATH`。

    ```bash
    cd ~ && ngrok --version
    ```

<br>

7. 嘗試透過以下指令添加憑證。

    ```bash
    ngrok config add-authtoken <輸入自己的憑證>
    ```

<br>

8. 啟動服務。

    ```bash
    ngrok http 80
    ```

<br>

___

_END_
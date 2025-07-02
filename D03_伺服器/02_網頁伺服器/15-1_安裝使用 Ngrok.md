# Ngrok 

_[Ngrok 官網](https://ngrok.com/)；Ngrok 本身並不是一種 `伺服器服務`，而是一種 `通道服務`，執行後可取得 Ngrok 公開服務器的通道，讓外部使用者可以透過這個通道訪問本地網站，也就是讓樹莓派上的伺服器可被外網訪問_

<br>

## 安裝 Homebrew

_將使用 brew 安裝 Ngrok_

<br>

1. 前往 [官網](https://brew.sh/) 複製安裝指令。

    ![](images/img_158.png)

<br>

2. 在樹莓派執行。

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

<br>

3. 依據提示把 Homebrew 加入環境變數。

    ```bash
    echo >> /home/sam6238/.bashrc
    echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
    eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
    ```

    ![](images/img_159.png)

<br>

4. 依據建議安裝基本依賴套件。

    ```bash
    sudo apt-get install build-essential
    ```

    ![](images/img_160.png)

<br>

## 安裝 Ngrok

1. 前往 [官網](https://dashboard.ngrok.com/get-started/setup/raspberrypi) 並切換到下載頁面。

    ![](images/img_168.png)

<br>

2. 選擇樹莓派系統。

    ![](images/img_169.png)

<br>

3. 切換到 `Homebrew` 選項。

    ![](images/img_161.png)

<br>

4. 複製指令運行。

    ```bash
    curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
        | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
        && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
        | sudo tee /etc/apt/sources.list.d/ngrok.list \
        && sudo apt update \
        && sudo apt install ngrok
    ```

<br>

## 設定權杖

1. 運行指令將權杖加到本地。

    ```bash
    ngrok config add-authtoken <輸入個人-TOKEN>
    ```

<br>

2. 完成時會提示儲存位置。

    ```bash
    ~/.config/ngrok/ngrok.yml
    ```

    ![](images/img_162.png)

<br>

## 啟動服務

1. 啟動 Ngrok 並指定端口為 8080。

    ```bash
    ngrok http 8080
    ```

    ![](images/img_163.png)

<br>

2. 複製 `Forwarding` 網址並開啟瀏覽器訪問。

    ![](images/img_164.png)

<br>

3. 點擊 `Visit Site`。

    ![](images/img_165.png)

<br>

4. 就會看到當前在 `8080` 端口運行的伺服器，目前是 `Ngnix` 伺服器。

    ![](images/img_166.png)

<br>

___

_END_
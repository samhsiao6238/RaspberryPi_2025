# 阿里雲

_建立 OpenVPN 伺服器連回中國內地_

<br>

## 申請阿里雲帳號

1. 前往 [阿里雲官網](https://www.aliyun.com) 註冊帳號並完成實名認證，使用 `gsam6238@gmail.com`。

<br>

## 建立 ECS 實例

_Elastic Compute Service_

<br>

1. 打開阿里雲 [ECS 控制台](https://ecs.console.aliyun.com)

<br>

2. 點擊 `建立更多試用 ECS`。

    ![](images/img_01.png)

<br>

3. 地區選擇 `華東 1（杭州）`。

    ![](images/img_25.png)

<br>

4. 規格選擇 `2 核心、2 GiB 經濟型 e`。

    ![](images/img_02.png)

<br>

3. `操作系統` 選擇 `Ubuntu 20.04 64 位`。

    ![](images/img_03.png)

<br>

4. 預裝應用可選 Docker。

    ![](images/img_11.png)

<br>

5. 點擊 `我同意` 及右下角 `立即試用`。

    ![](images/img_04.png)

<br>

6. 建立成功，點擊 `管理試用`。

    ![](images/img_26.png)

<br>

7. 點擊 `實例`，就可看到新建立的 ECS，點擊實例鏈接可進入。

    ![](images/img_27.png)

<br>

## 使用主控台登入

1. 點擊 `綁定密鑰對`。

    ![](images/img_12.png)

<br>

2. 若無密鑰，選擇 `建立密鑰對`；輸入名稱後會自動下載。

    ![](images/img_13.png)

<br>

3. 回到主控台，再次點擊 `綁定密鑰` 進行綁定。

    ![](images/img_06.png)

<br>

4. 綁定後要 `重啟實例`。

    ![](images/img_14.png)

<br>

## 遠程連線

_先回到本地處理密鑰文件_

1. 將下載的密鑰文件修改權限為 `400`。

    ```bash
    chmod 400 <拖曳文件至此即可>
    ```

<br>

2. 點擊 `遠程連線`。

    ![](images/img_15.png)

<br>

3. 點擊 `立即登入`。

    ![](images/img_16.png)

<br>

4. 點擊 `SSH 密鑰認證`，然後上傳密鑰對後點擊 `確認`。

    ![](images/img_17.png)

<br>

5. 完成後會進入終端機畫面。

    ![](images/img_28.png)

<br>

## 免密碼 SSH 登入

_複製本地公鑰到實例_

<br>

1. 進入實例密鑰文件路徑，可看到 `authorized_keys` 文件已經存在。

    ```bash
    cd ~/.ssh && ls
    ```

    ![](images/img_29.png)

<br>

2. 編輯文件貼上本地公鑰；關於本地公鑰取得部分暫時略過。

    ```bash
    nano authorized_keys
    ```

    ![](images/img_18.png)

<br>

## 快速連線

1. 複製 ECS 公網 IP `118.31.77.245`。

    ![](images/img_05.png)

<br>

2. 開啟本地設定文件 `config`。

    ```bash
    code ~/.ssh
    ```

<br>

3. 添加以下別名，使用者預設為 `root`，IP 需依據實際填入。

    ```bash
    Host ali
        HostName 118.31.77.245
        User root
    ```

<br>

4. 快速連線。

    ```bash
    ssh ali
    ```

<br>

## 彈性 IP

1. 點擊。

    ![](images/img_30.png)

<br>

2. 彈窗顯示。

    ![](images/img_31.png)

<br>

3. 會直接綁定原本配發的 IP。

    ![](images/img_32.png)

<br>

## 安全組配置

_在安全組中添加規則，設置 `0.0.0.0/0` 允許所有 IP 連線；特別注意，安全群組與實例是獨立但可綁定的對象。_

<br>

1. 1194 UDP，OpenVPN 預設端口。

<br>

2. 9443/943 TCP。

<br>

3. 22 TCP（SSH 遠程管理）

<br>

4. 3389 TCP（如需遠程桌面）

<br>

___

_END_
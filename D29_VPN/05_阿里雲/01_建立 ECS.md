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

2. 點擊 `建立我的 ECS`。

    ![](images/img_01.png)

<br>

3. 地區選擇 `華東 1（杭州）`。

<br>

4. 規格選擇 2 核心、2 GiB 經濟型 e。

    ![](images/img_02.png)

<br>

3. `操作系統` 選擇 `Ubuntu 20.04 64 位`。

    ![](images/img_03.png)

<br>

4. 不需要預裝應用。

<br>

5. 立即試用。

    ![](images/img_04.png)

<br>

## 使用主控台登入

1. 建立密鑰對

<br>

2. 在主控台先綁定密鑰對。

    ![](images/img_06.png)

<br>

3. 重啟實例。

<br>

4. 下載後，修改權限為 400。

<br>

5. 遠程連線，上傳密鑰對

<br>

## SSH 登入

1. ECS 公網 IP：`118.31.77.245`  

    ![](images/img_05.png)

<br>

2. 終端機指令

    ```bash
    ssh -i <密鑰對路徑>  root@<實例公網 IP>
    ```

<br>

## 免密碼

1. 上傳本機公鑰

    ```bash
    sudo nano ~/.ssh/authorized_keys
    ```

<br>

2. 本機建立 SSH 設置

    ```bash
    Host ali
        HostName 118.31.77.245
        User root
    ```

<br>

3. 快速連線

    ```bash
    ssh ali
    ```

<br>

## 安全組配置

_在安全組中添加規則，設置 `0.0.0.0/0` 允許所有 IP 連線_

<br>

1. 1194 UDP（OpenVPN 預設端口）

<br>

2. 443 TCP（如果要偽裝成 HTTPS）

<br>

3. 22 TCP（SSH 遠程管理）

<br>

4. 3389 TCP（如需遠程桌面）

<br>

___

_END_
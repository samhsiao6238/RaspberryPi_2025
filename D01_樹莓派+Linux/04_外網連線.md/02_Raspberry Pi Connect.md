# Raspberry Pi Connect 

_官方連線工具_

<br>

## 介紹

1. 這是官方在 2024/05/07 發佈的功能，使用 `WebRTC` 技術來建立安全的點對點連接；特別注意，官方服務不支援以標準 SSH 協定連線，因此無法直接用 `VSCode Remote - SSH` 連線。

    ![](images/img_147.png)

<br>

2. 硬體需求樹莓派 4、5 或 400；其他版本硬體進行安裝不會報錯，只是重啟後並不會看到服務啟動。

<br>

3. 系統至少需安裝 `Bookworm 64 位元` 以上版本。

<br>

4. 使用 Wayland 窗口服務器，在 Linux 中用以替代傳統的 X Window System（X11），負責管理應用程式視窗的顯示和輸入事件，設計更簡潔且效能更佳，提供更流暢的圖形輸出和更安全的顯示環境。

<br>

## 安裝步驟

_新版系統已預設安裝好，可直接跳過 `安裝步驟`_

<br>

1. 更新系統。

    ```bash
    sudo apt update && sudo apt upgrade -y
    ```

<br>

2. 安裝 `Raspberry Pi Connect`；新版系統已預裝，可直接在桌面 `Turn On` 應用。

    ```bash
    sudo apt install rpi-connect
    ```

<br>

3. 若是手動安裝，須重啟樹莓派讓服務啟動。

    ```bash
    sudo reboot
    ```

<br>

## 初次連線

1. 透過 VNC 連線桌面，會在右上角看到功能的圖標，預設是反白的。

    ![](images/img_01.png)

<br>

2. 點擊此圖標開啟功能。

    ![](images/img_02.png)

<br>

3. 會自動開啟瀏覽器進入 [Sign in](https://connect.raspberrypi.com/sign-in) 頁面。

    ![](images/img_141.png)

<br>

4. 有帳號的話可點擊登入。

    ![](images/img_03.png)

<br>

## 註冊帳號

_初次使用先 `建立帳號`_

<br>

1. 點擊 [create one for free](https://id.raspberrypi.com/sign-up) 註冊新帳號。

    ![](images/img_142.png)

<br>

2. 填入相關資訊，需要驗證郵件。

    ![](images/img_04.png)

<br>

## 登入

1. 輸入帳號密碼。

    ![](images/img_143.png)

<br>

2. 可設置雙重驗證。

    ![](images/img_05.png)

<br>

3. 對設備任意命名，然後點擊 `Create device and sign in`。

    ![](images/img_144.png)

<br>

4. 登入完成會亮起顏色；特別注意，必須先在樹莓派完成登入，才能到其他設備上進行遠端連線。

    ![](images/img_150.png)

<br>

## 設置完成後的操作

_可在任意設備中的瀏覽器進行兩種連線方式訪問樹莓派_

<br>

1. 使用其他設備訪問 [Raspberry Pi Connect](https://connect.raspberrypi.com/)，登入後系統會看到可連線設備及連線方式。

    ![](images/img_145.png)

<br>

2. 點擊右側 `Connect via` 展開選單；依據官網說明，這個網路連線在一般情況下會是 `點對點` 的連接，建立連接後，無需通過伺服器進行流量傳輸；如果無法建立直接連接，流量會通過位於英國的 TURN 伺服器進行中繼。

    ![](images/img_146.png)

<br>

## 使用 Screen sharing

1. 展開後點擊 `Screen sharing`。

    ![](images/img_151.png)

<br>

2. 會開啟樹莓派專用的遠端桌面。

    ![](images/img_152.png)

<br>

## 使用 `Remote shell`

1. 展開後點擊 `Remote shell`。

    ![](images/img_153.png)

<br>

2. 會開啟樹莓派專用的桌面終端機。

    ![](images/img_154.png)

<br>

3. 查詢只會看到內網 IP，因為這個服務並不會直接分配外網 IP 給設備，而是透過雲端代理服務，建立一條中繼通道，讓使用者可從外網透過中繼代理服務連接到樹莓派。

    ![](images/img_06.png)

<br>

## 刪除設備

1. 點擊設備進入。

    ![](images/img_38.png)

<br>

2. 展開右上方選單，點擊 `Delete` 可刪除設備；`Rename`也在選單內，另外 `Transfer` 功能僅有 `Organisation` 帳號的管理員具有權限，這裡不作說明。

    ![](images/img_39.png)

<br>

3. 點擊刪除。

    ![](images/img_40.png)

<br>

## 透過終端機建立設備

_不進入樹莓派桌面，若已經建立設備，可先進行刪除_

<br>

1. 使用 SSH 連線樹莓派後，在終端機中輸入以下指令，畫面會輸出附帶授權碼的登入網址。

    ```bash
    rpi-connect signin
    ```

    ![](images/img_184.png)

<br>

2. 複製該網址後，在本機中開啟瀏覽器進行訪問，便會看到設備的設定畫面。

    ![](images/img_185.png)

<br>

3. 輸入任意名稱後點擊登入。

    ![](images/img_186.png)

<br>

4. 畫面會顯示成功。

    ![](images/img_187.png)

<br>

5. 終端機也會同步顯示登入成功訊息。

    ![](images/img_188.png)

<br>

6. 點擊瀏覽器中的 `view all devices` 連結

    ![](images/img_41.png)

<br>

7. 便可看到該設備。

    ![](images/img_189.png)

<br>

## 補充

_不能直接將 Raspberry Pi Connect 的 SSH 連線整合到 VSCode Remote-SSH 擴充中使用_

<br>

1. Raspberry Pi Connect 的 Remote Shell 是瀏覽器內嵌的 `WebShell`，是基於 WebRTC / Relay 的抽象連線，它並不開放真正的 SSH port（22），也不提供 SSH Host/IP 給 VSCode 使用。

<br>

2. 服務預設開機啟動，所以重啟之後依舊可以連線。

<br>

___

_END_
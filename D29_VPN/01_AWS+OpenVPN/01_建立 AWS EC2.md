# 建立 AWS EC2

_透過 AWS 的 AMI 訂閱快速安裝 OpenVPN Access Server_

<br>

## 建立 `Key Pairs`

_這裡僅是將建立步驟獨立出來，因為這個 Key 是可以沿用的，無需每次都重建，若是初次建立則在建立 EC2 步驟中進行即可_

<br>

1. 登入控制台。

<br>

2. 建立一個 `Key Pairs` 備用。

   ![](images/img_01.png)

<br>

3. 任意命名如 `MyKey0122`，然後點擊 `Create key pair`；完成後會自動下載到本地。

   ![](images/img_02.png)

<br>

## 進入 EC2

1. 建立 EC2 實例。

   ![](images/img_03.png)

<br>

2. 點擊 `Browse more AMIs`。

   ![](images/img_04.png)

<br>

3. 切換到 `AWS Marketplace AMIs` 頁籤，在上方搜尋欄中輸入 `openvpn`，點擊 `ENTER` 之後，選取第一個搜尋結果。

   ![](images/img_05.png)

<br>

4. 點擊右下角 `Subscribe now`。

   ![](images/img_06.png)

<br>

5. 切換 `Instance type` 為免費的 `t2.micro`。

   ![](images/img_07.png)

<br>

6. `Key pair` 選取前面建立好的 `MyKey0122`。

   ![](images/img_08.png)

<br>

7. 其他使用預設，點擊右下角 `Launch instance`。

   ![](images/img_09.png)

<br>

8. 回到列表，若有多個實例，選取正確的實例之後，點擊上方 `connect`。

   ![](images/img_10.png)

<br>

9. 先停留在這一頁，後續將使用 SSH 連線。

   ![](images/img_11.png)

<br>

## 修改憑證權限

1. 使用終端機進入本機下載路徑中。

   ```bash
   cd ~/Downloads
   ```

<br>

2. 依規定，修改 .pem 文件的權限為 400。

   ```bash
   chmod 400 MyKey0122.pem
   ``` 

<br>

3. 複製前面步驟提供的連線指令。

   ```bash
   ssh -i "MyKey0122.pem" root@ec2-3-1-205-62.ap-southeast-1.compute.amazonaws.com
   ```

<br>

4. 連線後會看到提示先輸入 `yes`，接著繼續提示要更改使用者名稱為 `openvpnas`。

   ![](images/img_12.png)

<br>

5. 重新連線。

   ```bash
   ssh -i "MyKey0122.pem" openvpnas@ec2-3-1-205-62.ap-southeast-1.compute.amazonaws.com
   ```

<br>

## 開始設定

1. 第一個先輸入 `yes`。

   ![](images/img_13.png)

<br>

2. 接下來全部選項都按下 `ENTER` 使用預設值，直到看到設定密碼的提示。

   ![](images/img_14.png)

<br>

3. 依規定需輸入一個大小字母及一個符號，例如 `Xxx-0000`；需要輸入兩次，過程中看不到自己的輸入。

   ![](images/img_15.png)

<br>

4. 下一個提示依舊按下 `ENTER` 使用預設；至此完成初步設定。

   ![](images/img_16.png)

<br>

## 登入管理介面

1. 複製網址進行訪問。

   ![](images/img_17.png)

<br>

2. 展開 `進階`。

   ![](images/img_42.png)

<br>

3. 接著點擊繼續前往指定的網址。

   ![](images/img_18.png)

<br>

4. 帳號為 `openvpn`，密碼就是前面步驟自訂的密碼，然後點擊 `Sign in`。

   ![](images/img_19.png)

<br>

5. 接著點擊 `Agree`。

   ![](images/img_20.png)

<br>

6. 左側切換到 `VPN Settings`。

   ![](images/img_21.png)

<br>

7. 在 `Routing` 區塊將第一個按鈕切換到 `Yes`。

   ![](images/img_22.png)

<br>

8. 滑動到最下方點擊 `Save Settings`。

   ![](images/img_23.png)

<br>

9. 接著點擊最上方的 `Update Running Server`。

   ![](images/img_24.png)

<br>

## 訪問客戶端

1. 複製並訪問客戶端網址。

   ![](images/img_25.png)

<br>

2. 輸入相同的帳號密碼之後 `Sign in`。

   ![](images/img_26.png)

<br>

3. 使用蘋果電腦系統，所以點擊 `Apple` 圖標，點擊後會自動下載桌面應用。

   ![](images/img_27.png)

<br>

4. 下載完成點擊開啟，並點擊對應的系統。

   ![](images/img_28.png)

<br>

## 回到客戶端網頁

1. 點擊下方 `Profiles Management`。

   ![](images/img_31.png)

<br>

2. 點擊 `Create` 就會下載 `.ovpn` 文件。

   ![](images/img_32.png)

<br>

3. 點擊 `Browse` 選取下載的 `.ovpn` 文件。

   ![](images/img_29.png)

<br>

4. 輸入密碼後點擊 `Connect`。

   ![](images/img_30.png)

<br>

5. 完成連線伺服器。

   ![](images/img_33.png)

<br>

6. 訪問 [TunnelBear](https://www.tunnelbear.com/whats-my-ip)。

   ![](images/img_34.png)

<br>

___

_接續下一單元_
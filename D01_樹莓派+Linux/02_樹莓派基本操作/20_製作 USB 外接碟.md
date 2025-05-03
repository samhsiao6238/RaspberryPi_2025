# 製作 USB 外接碟

_將燒錄好樹莓派系統的 USB 行動碟插入現有系統中，可藉此建立包含多個分區的樹莓派系統碟_

<br>

## 簡介

_僅說明，無需操作_

<br>

1. 針對等於或高於 `樹莓派四` 規格的硬體，可支援使用 `USB 儲存裝置` 作為系統啟動碟，低於該型號的樹莓派只能從 `microSD 卡` 進行啟動。

<br>

2. 使用外部儲存設備作為主要的儲存和引導裝置可得到更快的讀寫速度和更大的儲存空間，實現這個功能前必須更新樹莓派的 `EEPROM`。

<br>

3. 特別注意，透過官方燒錄軟件製作系統碟時，預設只會使用 `5G` 的儲存裝置空間；如下圖所示，這是將燒錄好的 `64G SD 卡` 插入另一台運作中的樹莓派所查詢的結果。

    ![](images/img_135.png)

<br>

4. 延續上一點，在官方文件有提到，初次啟動樹莓派系統時會自動將根分區擴展到整個 SD 卡或USB 磁碟的可用空間，這是為了確保用戶可以使用整個儲存設備的可用空間，且不需要手動進行設置；經實測，若先進行手動調整分區大小，再將 USB 插入作為系統碟，這個自動擴展機制不會生效，基於這樣的設計，可將燒錄好的記憶卡或 USB 儲存裝置使用分區工具如 `gparted` 進行手動調整分區，再將其作為系統碟使用，這樣後續在進行 A/B 機制設定時將較為方便。

<br>

5. 若只是要使用 USB 儲存設備作為啟動碟，僅需燒錄完成後插入使用即可，無須另做任何設定；以下的操作是在運行中的樹莓派系統中，對另一個儲存裝置進行分區設定的過程，而不是單純使用外部儲存裝置作為開機系統。

<br>

## 操作說明

1. 使用 `官方燒錄軟件`，分別對 SD 卡及 USB 行動碟進行系統燒錄。

<br>

2. 完成後，先插入 SD 卡進行啟動。

<br>

3. 將 USB 裝置插入樹莓派 USB 接口，透過以下指令查詢當前資訊，其中 `mmcblk0` 就是新插入的 USB 碟。


    ```bash
    lsblk
    ```

    ![](images/img_53.png)  

<br>

## 分配分區

_安裝分配分區圖形化界面工具 GParted_

<br>

1. 按標準程序，在安裝工具之前先更新運作中的樹莓派系統。

    ```bash
    sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
    ```

<br>

2. 在樹莓派中安裝工具 `GParted` 來管理分區。

    ```bash
    sudo apt install gparted -y
    ```

<br>

3. 同時安裝分處理區格式等附屬工具。

    ```bash
    sudo apt install dosfstools mtools -y
    ```

<br>

## 啟動工具

_以下截圖中的分區名稱若有不一致，請予以忽略_

<br>

1. 這是一個圖形化界面工具，所以要進入樹莓派並從終端啟動 `GParted`。

    ```bash
    sudo gparted
    ```

<br>

2. 啟動後會顯示當前開機的 SD 卡或儲存裝置的分區資訊。

    ![](images/img_54.png)

<br>

3. 在右上角選單中切換為 SSD 的 `/dev/sdb`，可看到在新的外部裝置上有兩個分區，及一個 `未配置` 空間；這兩個分區是燒錄完成時生成的， `bootfs` 是引導分區、`rootfs` 是系統文件分區。

    ![](images/img_48.png)

<br>

4. 先對系統文件分區進行容量修改，在該分區上點右鍵，然後點擊 `調整大小/移動`。

    ![](images/img_50.png)

<br>

5. 接著在 `新的大小` 欄位中手動輸入分區大小，輸入完成按下 `ENTER` 使其生效，然後點擊右下角的 `調整大小`，若未生效時，`調整大小` 按鍵會反白無法點擊。

    ![](images/img_49.png)

<br>

6. 點擊工具欄上的綠色 `打勾` 按鈕來套用並執行變更。

    ![](images/img_51.png)

<br>

7. 在彈出視窗中再次點擊 `套用` 完成設定。

    ![](images/img_52.png)

<br>

8. 完成時可展開 `詳細資訊` 查看所進行的變更。

    ![](images/img_55.png)

<br>

## 新增分區

1. 拓展現有系統資料分區大小之後，接著在 `未配置` 點擊右鍵後選取 `新增`。

    ![](images/img_136.png)

<br>

2. 再建立一個 30G 的分區然後打勾，特別注意，這個分區的大小並不重要，因為在之後的步驟中，樹莓派預設會將剩餘空間全部指派給這個最後建立的分區，因為要觀察這個流程，建議不要把剩餘空間一次分配。

    ![](images/img_138.png)

<br>

3. 完成後進行格式化為 `ext4`，同樣再打勾；特別注意。

    ![](images/img_139.png)

<br>

## 查看 

1. 查看磁碟資訊，可觀察到新添加的分區並未掛載。

    ```bash
    lsblk
    ```

    ![](images/img_117.png)

<br>

2. 查詢已掛載分區，其中確實沒有新添加的分區。

    ```bash
    df -h
    ```

    ![](images/img_118.png)

<br>

3. 接著運行以下指令進行關機，然後拔出 SD 卡，僅保留外接儲存裝置並重新開機；或是斷電後拔出記憶卡，然後插入電源重啟。

    ```bash
    sudo shutdown now
    ```

<br>

## 再次查看

_使用外接儲存裝置進行啟動_

<br>

1. 查詢，發現第三個分區已經自動掛載；其中 `/media/sam6238/` 之後所接續的是 Linux 系統用來唯一標識分割區的識別碼。

    ```bahs
    lsblk
    ```

    ![](images/img_119.png)

<br>

2. 修改掛載點名稱，首先，卸載該分區。

    ```bash
    sudo umount /media/sam6238/<複製完整的唯一識別碼>
    ```

    ![](images/img_120.png)

<br>

3. 先確認 `PARTUUID`。

    ```bash
    sudo blkid
    ```

    ![](images/img_170.png)

<br>

4. 使用 `e2label` 命令來更改分區的標籤，例如要 `sda4` 將標籤更改為 `data`。

    ```bash
    sudo e2label /dev/sda4 data
    ```

<br>

5. 編輯 `/etc/fstab` 文件，將原有的長標籤名稱更改為新的標籤名稱。

    ```bash
    sudo nano /etc/fstab
    ```

<br>

6. 編輯如下，其中掛載點尚未建立。

    ```bash
    proc            /proc           proc    defaults          0       0
    PARTUUID=343dcec1-01  /boot/firmware    vfat    defaults          0       2
    PARTUUID=343dcec1-02  /                 ext4    defaults,noatime  0       1
    PARTUUID=343dcec1-03  /media/sam6238/data   ext4   defaults,noatime  0       1
    ```

<br>

7. 建立新的掛載目錄。

    ```bash
    sudo mkdir -p /media/sam6238/data
    ```

<br>

8. 重新掛載所有文件系統；若順利完成會顯示如下訊息。

    ```bash
    sudo mount -a
    ```

    ![](images/img_171.png)

<br>

9. 複製提示的指令並執行，並輸入密碼。

    ```bash
    systemctl daemon-reload
    ```

    ![](images/img_172.png)

<br>

## 完成

1. 查詢。

    ```bash
    lsblk
    ```

    _輸出_

    ```bash
    NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
    sda      8:0    0 476.9G  0 disk 
    ├─sda1   8:1    0   512M  0 part /boot/firmware
    ├─sda2   8:2    0  97.7G  0 part /
    └─sda3   8:3    0 281.1G  0 part /media/sam6238/data
    ```

<br>

2. 查詢已掛載分區。

    ```bash
    df -h
    ```
    _輸出_
    ```bash
    Filesystem      Size  Used Avail Use% Mounted on
    udev            3.8G     0  3.8G   0% /dev
    tmpfs           805M  5.8M  800M   1% /run
    /dev/sda2        97G  4.3G   88G   5% /
    tmpfs           4.0G  288K  4.0G   1% /dev/shm
    tmpfs           5.0M   48K  5.0M   1% /run/lock
    /dev/sda1       510M   75M  436M  15% /boot/firmware
    tmpfs           805M  160K  805M   1% /run/user/1000
    /dev/sda3       276G   28K  262G   1% /media/sam6238/data
    ```

<br>

## 關於分區目錄

1. 如果在系統中建立了一個目錄，但未在 `/etc/fstab` 中指定掛載點，這個目錄仍然是可用的，但它會作為一個普通的空目錄存在於文件系統中，可以用來存放文件和資料夾，它不會自動掛載任何設備或分區，也就是說這個目錄並不會在開機時自動掛載任何設備或分區，必須手動掛載或者在需要時動態掛載。

<br>

2. 當更新 `/etc/fstab` 並運行 `sudo mount -a` 或者重啟系統後，新分區會才會掛載到這個目錄。

<br>

## 建立別名

_為自動生成的長路徑設置一個快捷命令來快速切換到該路徑_

<br>

1. 編輯 `~/.bashrc` 配置文件，是 `用戶級別` 的配置文件，用於配置 `Bash shell` 環境。

    ```bash
    nano ~/.bashrc
    ```

<br>

2. 在文件中添加以下指令建立一個別名，添加的位置並無規範，能集中便於查看或編輯即可。

    ```bash
    alias cddata='cd /media/sam6238/data'
    ```

3. 也可以建立一個環境變數來指向該路徑。

    ```bash
    export mydata='/media/sam6238/data'
    ```

<br>

4. 完成後要進行設置的刷新讓其生效。

    ```bash
    source ~/.bashrc
    ```

<br>

5. 完成以上步驟，透過以下兩個指令皆可將工作目錄切換到指定路徑中；特別注意，使用 `cd` 命令時，環境變數必須加上 `$` 才能正確引用，若僅執行 `cd mydata` 時， `mydata` 會被視為一個普通目錄名稱，而不是引用環境變數。

    ```bash
    # 透過環境參數切換目錄
    cd $mydata
    # 透過指令別名切換目錄
    cddata
    ```

<br>

## 建立符號鏈接

_不想使用 `$` 引用環境變數，也可透過符號鏈接來實現_

<br>

1. 在 `家目錄 (~)` 中建立一個名為 `mydata` 的 `符號鏈接`。

    ```bash
    ln -s /media/sam6238/data ~/mydata
    ```

    _建立後可進行查看_

    ![](images/img_140.png)

<br>

2. 這樣便可透過任何地方進行切換到家目錄中的鏈接符號中，但實際會指向該分區根目錄。

    ```bash
    cd ~/mydata
    ```

<br>

___

_END_

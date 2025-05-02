# 製作 USB 啟動碟

_使用 USB 外接裝置作為系統碟_

## 說明

_燒錄步驟與 `SD 卡` 相同，插入樹莓派進行啟動，並啟用 `VNC`。_

1. 查詢目前分割區。

```bash
lsblk
```

_結果_

![](images/img_114.png)

2. 依據結果顯示，USB 磁碟（`/dev/sda`）預設被分割為兩個區域，第一個區域 `/dev/sda1` 容量 `512MB`，格式為 `FAT32`，這是用於存放開機韌體和引導檔案；第二個區域是 `/dev/sda2` 使用儲存裝置的剩餘容量 `57.2GB`，格式為 `ext4`，這是作為根檔案系統（root filesystem）。

## 一鍵拓展

_若根分割區（/dev/sda2）在某些狀況下並未自動擴展至整個磁碟的可用空間_

1. 使用 raspi-config 工具。

```bash
sudo raspi-config
```

2. 在選單中選擇，這會將根分割區擴展至磁碟的最大可用空間。

```bash
Advanced Options → Expand Filesystem
```

## 重新分割 `/dev/sda`

_以下使用圖形化的分割工具 `gparted` 將 `/dev/sda` 重新分割為多個區域以便於資料管理或安裝其他作業系統，在進行分割操作前，可備份根分割區 `/dev/sda2` 中的重要資料，以防資料遺失；另外，由於根分割區正在使用所以無法調整其大小；[參考資料](https://learn.adafruit.com/resizing-raspberry-pi-boot-partition?view=all&utm_source=chatgpt.com)。_

1. 安裝 `gparted`。

```bash
sudo apt update && sudo apt install gparted -y
```

2. 使用 VNC 進行連線，在 VNC 中開啟終端機並啟動 `gparted`。

```bash
sudo gparted
```

![](images/img_115.png)

3. 關於 `新增、刪除或格式化分割區` 的說明將在下個章節説明，或參考 [Boot the Raspberry Pi From USB - Instructables](https://www.instructables.com/Boot-the-Raspberry-Pi-from-USB/?utm_source=chatgpt.com)。


## 更新開機設定

1. 如果更改了 `/boot` 分割區的位置或大小，可能需要更新 `/boot/cmdline.txt` 中的 `root=` 參數，以指向新的根檔案系統位置。

```bash
root=/dev/sda2
```

2. 完成分割和設定後，重新啟動樹莓派，確保系統能正常啟動。

## 使用命令列工具

_parted_

1. 啟動 parted 工具

```bash
sudo parted /dev/sda
```

2. 查看當前分割區資訊

```bash
print
```

3. 刪除現有的第二個分割區，這將刪除該分割區上的所有資料。

```bash
rm 2
```

4. 建立新的分割區，將剩餘的空間分為兩個新的分割，這個命令將從 541MB 開始，分別建立兩個大小為約 31.5GB 的分割區。

```bash
mkpart primary ext4 541MB 32GB
mkpart primary ext4 32GB 62.0GB
```

5. 退出 parted

```bash
quit
```

6. 格式化新的分割區，使用 mkfs 命令將新的分割區格式化為 ext4 檔案系統。

```bash
sudo mkfs.ext4 /dev/sda2
sudo mkfs.ext4 /dev/sda3
```

7. 卸載分割區

```bash
sudo umount /dev/sda2
```

8. 使用 partprobe 通知內核重新讀取分割區表

```bash
sudo partprobe /dev/sda
```

9. 或 kpartx

```bash
sudo kpartx -u /dev/sda
```
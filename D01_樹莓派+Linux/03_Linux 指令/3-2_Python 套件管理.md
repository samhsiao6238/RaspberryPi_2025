#  Python 開發環境套件工具

<br>

## 說明

1. `conda`：Python / 資料科學界常用，管理虛擬環境與套件。

<br>

2. `pip`：Python 的套件管理工具。

<br>

3. `brew`：macOS 常用，但也支援 Linux，稱為 Homebrew on Linux。

<br>

## 套件來源

_`sources.list`_

<br>

1. 可開啟來源清單觀察。

    ```bash
    sudo nano /etc/apt/sources.list
    ```

<br>

2. 其中第一行 `bookworm` 提供 Bookworm 發行版的核心套件；第三行 `bookworm-updates` 則是提供 Bookworm 發行後的小幅修正與重要 bug 修補。

    ```bash
    deb http://deb.debian.org/debian bookworm main contrib non-free non-free-firmware
    deb http://deb.debian.org/debian-security/ bookworm-security main contrib non-free non-free-firmware
    deb http://deb.debian.org/debian bookworm-updates main contrib non-free non-free-firmware
    ```

<br>

3. 可修改或新增套件來源，以下舉例更換為台灣 Debian 鏡像站。

    ```bash
    deb http://ftp.tw.debian.org/debian bookworm main contrib non-free
    deb http://security.debian.org/debian-security bookworm-security main
    ```

<br>

4. 更新套件索引。

    ```bash
    sudo apt update
    ```

<br>

___

_END_
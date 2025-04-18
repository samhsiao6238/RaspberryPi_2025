# 多版本 Python

_這裡示範的是使用 pyenv 進行多版本安裝全記錄_

<br>

##  前置作業

1. 進行更新。

    ```bash
    sudo apt-get update && sudo apt-get upgrade -y
    ```

<br>

2. 運氣不錯，一開始就遇到問題。

    ![](images/img_01.png)

<br>

3. 處理到麻木了，不管啥原因，直接註解更新列表，先切換到管理資料夾。

    ```bash
    cd /etc/apt/sources.list.d/ 
    ```

<br>

4. 透過指令 `ls -al` 查詢，只有一個 `.list` 檔案，這好辦。

    ![](images/img_02.png)

<br>

5. 進行編輯。

    ```bash
    sudo nano raspi.list
    ```

<br>

6. 註解起來就對了。

    ![](images/img_03.png)

<br>

7. 在更新一次，順利完成。

    ![](images/img_04.png)

<br>

## 安裝 pyenv

1. 後續會以編譯的方式安裝 Python，而 Python 的某些標準函式庫需要這些庫的支援才能正常運作，所以先安裝以下套件，以下有些已經內建在新版作業系統中，重複執行並不衝突。

    ```bash
    sudo apt install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev
    ```

<br>

2. 下載與執行 `pyenv` 安裝腳本。

    ```bash
    curl https://pyenv.run | bash
    ```

<br>

3. 編輯環境參數。

    ```bash
    sudo nano ~/.bashrc
    ```

<br>

4. 添加以下內容。

    ```ini
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    ```

    ![](images/img_05.png)

<br>

4. 重新載入設定。

    ```bash
    source ~/.bashrc
    ```

<br>

5. 查詢 pyenv 版本。

    ```bash
    pyenv --version
    ```

    ![](images/img_06.png)

<br>

## 安裝指定版本的 Python

1. 進入 [Python 官網](https://www.python.org/) 。


<br>


1. 點擊 `Downloads` 進入下一個畫面。

    ![](images/img_07.png)


<br>

3. 點擊 `All releases` 查看有哪些版本。

    ![](images/img_08.png)

<br>

4. 這裡示範安裝 `3.10.13`，這需要相當時間。

    ```bash
    pyenv install 3.10.13
    ```

    ![](images/img_09.png)

<br>

## 驗證安裝

1. 查詢當前 Python 版本。

    ```bash
    python --version
    ```

    ![](images/img_10.png)

<br>

2. 查詢當前運行的 Python 路徑，可發現 Python 現在已經由 `.pyenv` 進行管理了。

    ```bash
    which python
    ```

    ![](images/img_11.png)

<br>

3. 查詢 Python 存放在系統中的哪些目錄中。

    ```bash
    whereis python
    ```

<br>

4. 結果
    
    ```bash
    python: 
    /usr/bin/python 
    /usr/bin/python3.9-config 
    /usr/bin/python3.9 
    /usr/lib/python2.7 
    /usr/lib/python3.9 
    /etc/python3.9 
    /usr/local/lib/python3.9 
    /usr/include/python3.9m 
    /usr/include/python3.9 
    /home/sam6238/.pyenv/shims/python3.10-config 
    /home/sam6238/.pyenv/shims/python 
    /home/sam6238/.pyenv/shims/python3.10 
    /usr/share/man/man1/python.1.gz
    ```

<br>

5. 接下來就特別留意了，pyenv 看似將 Python 安裝在了 `/home/sam6238/.pyenv/shims` 資料夾內，實際進入查看可以發現，pyenv 是通過 shims 機制來管理不同版本的 Python，而非將 Python 安裝於此。

    ![](images/img_12.png)

<br>

6. 分別透過以下指令查詢版本並觀察結果。
    
    ```bash
    /home/sam6238/.pyenv/shims/python --version
    ```
    結果
    ```bash
    Python 3.9.2
    ```
    
    <br>

    ```bash
    /home/sam6238/.pyenv/shims/python3 --version
    ```
    結果
    ```bash
    Python 3.9.2
    ```

    <br>

    或是
    ```bash
    /home/sam6238/.pyenv/shims/python3.10 --version
    ```
    結果
    ```bash
    pyenv: python3.10: command not found

    The `python3.10' command exists in these Python versions:
    3.10.13

    Note: See 'pyenv help global' for tips on allowing both
        python2 and python3 to be found.
    ```

<br>

7. 可以查看 pyenv 當前管理的 Python 版本。

    ```python
    pyenv versions
    ```

<br>

## _究竟在哪裡？_

1. 實際路徑在 `/home/sam6238/.pyenv/versions/3.10.13/bin` 。

    ![](images/img_13.png)

<br>

2. 再次查詢。

    ```bash
    /home/sam6238/.pyenv/versions/3.10.13/bin/python --version
    ```

<br>

3. 確定路徑後，回到 `~/Documents` 或其他指定資料夾建立虛擬環境。

    ```bash
    /home/sam6238/.pyenv/versions/3.10.13/bin/python -m venv env3.10.13
    ```

<br>

4. 編輯環境參數文件 `~/.bashrc` ，添加以下內容。

    ```txt
    source /home/sam6238/Documents/env3.10.13/bin/activate
    ```

<br>

5. 載入更新後的環境設置。

    ```bash
    source ~/.bashrc
    ```

<br>

6. 查詢虛擬環境的 Python 版本。

    ![](images/img_14.png)

<br>

## 再裝一版

1. 安裝指定版本的 Python。

    ```bash
    pyenv install 3.12.0
    ```

<br>

2. 其餘步驟省略，查看最後結果。

    ![](images/img_15.png)

<br>

3. 目前安裝了哪些版本。

    ```bash
    pyenv versions
    ```

    ![](images/img_16.png)

<br>

## pyenv 的官方用法

_刻意寫在了最後面_

<br>

1. 建立一個目錄。

    ```bash
    mkdir envTest
    ```

<br>

2. 透過 `pyenv` 的 `local` 參數設定當前目錄要使用的版本。

    ```bash
    pyenv local 3.12.0
    ```

<br>

3. 使用 `ls -al` 觀察一下，會看到目錄內添加了一個檔案 `.python-version`。

    ![](images/img_17.png)

<br>

4. 這時候無需進入任何虛擬環境透過 `python --version` 查詢當前版本。

    ![](images/img_18.png)

<br>

5. 可手動編輯內容 `sudo nano .python-version` ，達成暴力更改當前版本的目的。

    ![](images/img_19.png)

<br>

6. 在查詢一次 `python --version` ，版本確實就更改了。

    ![](images/img_20.png)

<br>

7. 這時，只要在這個資料夾內建立虛擬環境，就會是指定的 Python 版本，只是這個虛擬環境會在這個路徑之下，雖然版本設定的部分變得很直觀，但虛擬環境的管理卻顯得混亂，我個人是比較建議將版本安裝與虛擬環境管理分開，僅透過 `pyenv` 進行多版本的安裝，虛擬環境管理還是比照原有模式。當然，這僅是個人建議，如何最順手都依主觀執行即可。

<br>

## 其他指令

_除了 `pyenv local` 外，還有其他指令進行設定和切換_

<br>

1. `pyenv global`：
   - 用於設置系統全域的 Python 版本。
   - 這個設置決定執行 Python 時的預設版本。

2. `pyenv shell`：
   - 在當前終端機視窗中設置臨時的 Python 版本。
   - 這個設置不會影響其他終端機或目錄的設置，關閉後即失效。

3. `pyenv versions`：
   - 顯示所有已安裝的 Python 版本，並標示當前選擇的版本。

4. `pyenv install`：
   - 用於安裝新的 Python 版本。

5. `pyenv uninstall`：
   - 用於卸載已安裝的 Python 版本。

<br>

---

_END：多玩幾次就熟悉了_
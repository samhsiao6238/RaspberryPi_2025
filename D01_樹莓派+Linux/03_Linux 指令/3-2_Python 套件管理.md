# Python 開發環境套件工具

_涵蓋虛擬環境、套件安裝、Python 版本管理等工具_

<br>

## 套件與環境管理工具

1. `venv`：Python 自 `3.3` 起內建的虛擬環境管理工具，啟動虛擬環境後安裝的套件僅影響該目錄，不會影響全系統。

```bash
# 建立並啟用虛擬環境
python -m venv venv
source venv/bin/activate
```

<br>

2. `pip`：Python 官方的套件管理工具，預設會從 [PyPI](https://pypi.org) 安裝套件，以下指令用於安裝指定套件。

    ```bash
    pip install requests
    ```

<br>

3. `conda`：由 `Anaconda` 提供的套件與環境管理器，常用於資料科學與機器學習領域，跨平台支援 Python 與非 Python 套件；同時也提供 `miniconda` 精簡版。

    ```bash
    # 建立並啟用虛擬環境
    conda create -n myenv python=3.11
    conda activate myenv
    ```

<br>

4. `pyenv`：適用於多個 Python 版本的情境，常與 `venv` 搭配使用；建議透過 `brew` 安裝，安裝後需將設定加入環境變數，在此不做贅述。

    ```bash
    # 使用 Homebrew 安裝 pyenv
    brew install pyenv

    # 安裝與切換版本
    pyenv install 3.11.7
    pyenv global 3.11.7
    ```

<br>

5. `brew（Homebrew）`：這是 `macOS/Linux` 上的套件管理器，可用來安裝開發工具。

    ```bash
    # 安裝 Python
    brew install python

    # 安裝 pyenv
    brew install pyenv
    ```

## 進階管理工具

_進階工具整合了虛擬環境與依賴鎖定等功能，適合用於專案開發與部署_

<br>

1. `pipenv`：結合 `pip` 與 `venv` 的功能，可自動建立虛擬環境並管理依賴，產生 `Pipfile` 與 `Pipfile.lock`；`Pipfile` 記錄目前安裝的套件需求，`Pipfile.lock` 鎖定精確版本以保證可重現環境。

    ```bash
    # 建立新專案環境並安裝套件
    pipenv install requests

    # 啟用虛擬環境
    pipenv shell
    ```

<br>

2. `poetry`：現代化的 Python 套件與專案管理工具，整合建構、發佈、依賴鎖定、虛擬環境於一體；使用 `pyproject.toml` 取代傳統的 `setup.py`、`requirements.txt`，支援打包與發佈到 PyPI，適合製作第三方套件、複雜專案或 CI/CD 流程。

    ```bash
    # 建立新專案
    poetry new myproject

    # 安裝依賴，會自動建立虛擬環境
    poetry add requests

    # 啟動虛擬環境
    poetry shell
    ```

<br>

___

_END_
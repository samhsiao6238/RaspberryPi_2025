# 比較 Python 內建模組與 Conda 的異同


_在樹莓派上使用 Conda 建立虛擬環境和使用 `python -m venv` 建立的虛擬環境主要差異_

<br>

## 比較

1. 工具的來源與目的:
   - `python -m venv`: 是 Python 的內建模組，專為建立輕量級、隔離的 Python 環境而設計。
   - `Conda`: 是一個開源的包管理系統和環境管理系統，不僅可管理 Python，還可管理其他語言的包，常用於數據科學、機器學習等場景，特別適用於 `涉及許多外部依賴項和特定版本的包` 。

2. 跨平台:
   - `python -m venv`: 主要用於Python環境。
   - `Conda`: 可用於多個平台和多種語言。例如，可在 Windows、macOS 和 Linux 上使用 Conda，並可用來管理 Python、R、Ruby 等語言的包。

3. 包的管理:
   - `python -m venv`: 使用`pip`來安裝和管理 Python 包。
   - `Conda`: 使用自己的包管理系統，所以允許安裝非 Python 軟體。

4. 二進制的依賴項:
   - `python -m venv`: 不會自動處理非 Python 的依賴項，這會在某些情況下導致問題，特別是在需要特定版本的系統庫的情況下。
   - `Conda`: 能夠處理 Python 和非 Python 的二進制依賴項，這使得在有許多外部依賴項的情況下建立環境變得更簡單。

5. 在樹莓派上的兼容性:
   - `python -m venv`: 是 Python 的標準模組，所以在樹莓派的標準 Python 安裝中可用。
   - `Conda`: 雖然 Conda 支持樹莓派的 ARM 架構，但對此平台的支援不如對 x86 平台的支援那麼完整，可能會遇到某些包不可用的問題。

6. 性能和大小:
   - `python -m venv`: 相對輕量級，但可能需要手工處理某些依賴項。
   - `Conda`: 擁有全功能性質，但同時也比`venv`更加龐大，也需要更多的磁碟空間。

<br>

## 結論

1. 選擇哪種工具取決於需求。
   
2. 如果只需要一個輕量級的 Python 環境，那 `python -m venv` 會是首選，如果需要一個功能強大且能夠管理多個依賴項的環境，那 Conda 可能是更好的選擇。
   
3. 在樹莓派上，由於硬件和軟體的限制、兼容性問題等，`python -m venv` 可能是一個更加安全的選擇。

<br>

---

_END_
# PageKite + Streamlit

_進階使用_

<br>

## 準備工作

_基於 `PEP 668`，所以要使用虛擬環境_

<br>

1. 一鍵完成虛擬環境建立與啟動，這裡預設的名稱是 `envStreamlit`；確認終端機命令行前綴變更為 `envStreamlit` 即表示成功。

    ```bash
    mkdir -p ~/Documents/PythonVenvs
    cd ~/Documents/PythonVenvs
    python -m venv envStreamlit
    echo 'source ~/Documents/PythonVenvs/envStreamlit/bin/activate' >> ~/.zshrc
    source ~/.zshrc
    ```

    ![](images/img_34.png)

<br>

2. 安裝套件。

    ```bash
    pip install streamlit
    ```

<br>

3. 建立並進入專案資料夾。

    ```bash
    mkdir -p ~/Documents/exStreamlit
    cd ~/Documents/exStreamlit
    touch app.py
    ```

<br>

4. 編輯腳本。

    ```bash
    nano app.py
    ```

<br>

5. 貼上以下代碼。

    ```python
    import streamlit as st
    import random
    import time

    st.set_page_config(
        page_title="📊 Streamlit 儀表板範例",
        layout="wide",
    )

    # 側邊欄設定
    with st.sidebar:
        st.title("🔧 控制面板")
        refresh = st.button("🔄 模擬即時更新")
        stock = st.selectbox(
            "📈 選擇股票",
            ["台積電", "鴻海", "聯發科", "大立光", "中華電信"]
        )
        show_details = st.checkbox("顯示詳細資訊", value=True)

    st.title(f"📋 {stock} 模擬股市儀表板")

    # 隨機模擬資料
    base_price = random.randint(100, 500)
    price_now = base_price + random.uniform(-10, 10)
    price_open = base_price
    price_change = price_now - price_open
    percent_change = (price_change / price_open) * 100

    # 顯示資訊
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("開盤價", f"{price_open:.2f} 元")
    with col2:
        st.metric("即時價", f"{price_now:.2f} 元")
    with col3:
        color = "normal"
        delta_text = f"{price_change:+.2f} 元 ({percent_change:+.2f}%)"
        st.metric("漲跌", f"{price_now:.2f} 元", delta=delta_text)

    # 圖表模擬
    st.markdown("### 📊 模擬股價走勢")
    chart_data = {
        "價格": [round(price_open + random.uniform(-5, 5), 2) for _ in range(20)]
    }
    st.line_chart(chart_data)

    # 詳細資訊
    if show_details:
        st.markdown("---")
        st.subheader("📄 股票說明")
        st.info(
            f"{stock} 是台灣知名企業之一，相關說明僅供展示用途。"
        )

    st.markdown("---")
    st.caption("本頁面使用 Streamlit 建立，模擬展示股價介面。")
    ```

<br>

## 啟動服務

_同樣需要兩個終端機_

<br>

1. 執行 `app.py`，預設會在 `http://localhost:8501` 運行；特別說明，不建議使用 `80`，除了 `非 root` 無法監聽 `1024` 以下的低位元埠口外，還得額外設置路徑。

    ```bash
    streamlit run app.py
    ```

    ![](images/img_42.png)

<br>

2. 啟動反向代理。

    ```bash
    sudo pagekite.py 8501 sam6238.pagekite.me
    ```

<br>

3. 若有變更設定，可加入參數 `--clean` 清除 `--optdir` 指定目錄中的暫存檔，重新註冊並啟用對應的 Kite。

    ```bash
    sudo pagekite.py --clean --optdir=/etc/pagekite.d 8501 sam6238.pagekite.me
    ```

<br>

4. 開啟瀏覽器進行訪問。

    ```bash
    https://sam6238.pagekite.me
    ```

    ![](images/img_35.png)

<br>

## 使用官方範例

_說明如何快速套用官網範例_

<br>

1. 前往 [官網 API Reference](https://docs.streamlit.io/develop/api-reference)。

    ![](images/img_43.png)

<br>

2. 任意選擇一個範例如 [st.map](https://docs.streamlit.io/develop/api-reference/charts/)。

    ![](images/img_44.png)

<br>

3. 複製範例代碼。

    ![](images/img_45.png)

<br>

4. 關閉運行中的腳本，重新編輯。

    ```bash
    nano app.py
    ```

<br>

5. 再次運行。

    ```bash
    streamlit run app.py
    ```

<br>

6. 刷新頁面。

    ```bash
    https://sam6238.pagekite.me
    ```

    ![](images/img_46.png)

<br>

___

_END_
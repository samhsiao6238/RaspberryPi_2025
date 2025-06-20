# RAG

_以下延續前面步驟實作 RAG，給出完整步驟與程式碼，使用本地知識、網頁強化，以及 embedding 建立、查詢與結合 Claude API 回答。_

<br>

## 說明

1. RAG，Retrieval-Augmented Generation，關鍵是把知識切片、建立向量索引、依問題動態檢索，最後只把最相關內容傳給 LLM 進行回答。

<br>

## 準備工作

_安裝向量庫與 embedding 模型_

<br>

1. 選用 `sentence-transformers` 作 embedding，`faiss-cpu` 作本地向量查詢。

    ```bash
    pip install sentence-transformers faiss-cpu
    ```

<br>

## 開始進行

1. 知識片段切割，將解析後的文本做分段，稱為 `chunk`，常見片段大小為 `300～1000` 字，可依資料類型調整。

    ```python
    def split_text(text, chunk_size=500, overlap=50):
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            if chunk.strip():
                chunks.append(chunk)
            start = end - overlap
        return chunks
    ```

<br>

2. 建立 Embedding，使用 `HuggingFace sentence-transformers` 多語模型，如 `paraphrase-multilingual-MiniLM-L12-v2`，支援中、英、日等多語文本。

    ```python
    from sentence_transformers import SentenceTransformer

    # 初始化一次，記憶體不足時建議放在全域
    model = SentenceTransformer(
        'paraphrase-multilingual-MiniLM-L12-v2'
    )

    def embed_chunks(chunks):
        return model.encode(chunks, show_progress_bar=True)
    ```

<br>

3. 向量索引建構，將 embedding 存入本地 FAISS 索引，之後可快速搜尋與問題最相近的片段。

    ```python
    import faiss
    import numpy as np

    def build_faiss_index(embeddings):
        dim = embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(embeddings)
        return index
    ```

<br>

4. 整合知識庫初始化流程，從解析文本到分片、Embedding、索引。

    ```python
    # 1. 整理本地與網頁知識
    docs = load_local_files('~/Documents/knowledge/')
    docs += fetch_webpage(
        'https://zh.wikipedia.org/zh-tw/米家空氣清淨器5Pro'
    )

    # 2. 切割文本
    chunks = split_text(
        docs, 
        chunk_size=500, 
        overlap=50
    )

    # 3. 建立 Embedding
    embeddings = embed_chunks(chunks)
    embeddings = np.array(embeddings).astype('float32')

    # 4. 建立索引
    faiss_index = build_faiss_index(embeddings)
    ```

<br>

5. 動態檢索：根據問題找相關片段，查詢時將問題 `embedding`，找最相近的 `N` 個片段，這裡設定為 `3` 個。

    ```python
    def retrieve_relevant_chunks(
        question, model, index, chunks,
        top_k=3
    ):
        q_vec = model.encode([question])
        D, I = index.search(
            np.array(q_vec).astype('float32'),
            top_k
        )
        return [chunks[i] for i in I[0]]
    ```

<br>

6. 結合 Claude API 回答，只把檢索到的 context 片段合併後傳給 Claude，大幅減少 token 消耗、提升回應品質。

    ```python
    def ask_claude(question, context, api_key):
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        data = {
            "model": "claude-3-sonnet-20240229",
            "max_tokens": 1024,
            "system": "你是一個知識查詢助理，根據 context 回答使用者問題。",
            "messages": [{
                "role": "user",
                "content": f"知識內容：\n{context}\n\n請根據上述內容回答：{question}"
            }]
        }
        r = requests.post(url, headers=headers, json=data)
        if r.ok:
            resp = r.json()
            return resp['content'][0]['text']
        else:
            print("API 錯誤：", r.text)
            return None
    ```

<br>

## 開始問答

1. 示範一個完整查詢。

    ```python
    from dotenv import load_dotenv
    import os

    load_dotenv()
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    # 互動式查詢
    while True:
        q = input("請輸入你的問題：")
        relevant_chunks = retrieve_relevant_chunks(
            q, model, faiss_index, chunks, top_k=3
        )
        rag_context = '\n\n'.join(relevant_chunks)
        ans = ask_claude(q, rag_context, api_key)
        print("Claude 回答：", ans)
    ```

<br>

## 關於模型選擇

1. 目前專案使用的 Claude 模型是 `claude-3-sonnet-20240229`，在以下代碼處可設定。

    ```python
    data = {
        "model": "claude-3-sonnet-20240229",
        # ...
    }
    ```

<br>

2. `Claude 3 Sonnet` 是 `Claude 3` 系列中屬於 `中高階` 的模型，這個系列主要有三個版本 `Haiku`（最輕量、最快）、`Sonnet`（主流/性價比）、`Opus`（旗艦、最強）；其中 `Sonnet` 比 `Haiku` 強不少，同樣，`Opus` 也比 `Sonnet` 強，價格也最高。

<br>

3. 已官方數據來說，費用如下；`Sonnet` 費用是 `Haiku` 的 `10～12` 倍，`Opus` 又比 `Sonnet` 高 `5` 倍。

    ```bash
    * Haiku：\$0.25/百萬輸入 token，\$1.25/百萬輸出 token
    * Sonnet：\$3/百萬輸入 token，\$15/百萬輸出 token
    * Opus：\$15/百萬輸入 token，\$75/百萬輸出 token
    ```

<br>

4. 若專案允許降級，可考慮 `claude-3-haiku-20240307`，效能對知識檢索大部分場景仍足夠，費用會低很多。

    ```python
    "model": "claude-3-haiku-20240307",
    ```

<br>

___

_END_
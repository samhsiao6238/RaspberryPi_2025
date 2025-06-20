# 實作 RAG

_Retrieval-Augmented Generation，以 PostgreSQL 向量資料庫實作 RAG_

<br>

# 說明

1. 可搭配 `pgvector` 擴充模組支援向量儲存與相似度查詢，在 PostgreSQL 上實作 RAG 架構。

<br>

2. 向量查詢是使用 `cosine` 或 `L2` 距離排序。

<br>

3. 可嵌入 OpenAI Embedding API、SentenceTransformers、本地模型等，透過 LLM 如 OpenAI、Ollama、LLaMA.cpp 回答生成。

<br>

## 安裝

_使用 PostgreSQL 官方 PGDG 倉庫，Debian 預設套件源中沒有提供 pgvector 模組，但 PostgreSQL 官方維護的 PGDG apt repository 有支援該套件。_

<br>

1. 安裝 PostgreSQL 官方倉庫。

    ```bash
    sudo apt install -y curl gnupg lsb-release
    curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/pgdg.gpg
    echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list
    ```

<br>

2. 更新 apt 並安裝 pgvector。

    ```bash
    sudo apt update
    sudo apt install postgresql-15-pgvector -y
    ```

<br>

3. 連線資料庫。

    ```bash
    sudo -u postgres psql -d testdb
    ```

<br>

4. 在資料庫中啟用 pgvector 向量擴充模組。

    ```sql
    CREATE EXTENSION IF NOT EXISTS vector;
    ```

<br>

5. 建立表格，OpenAI Embedding 維度。

    ```sql
    CREATE TABLE documents (
        id SERIAL PRIMARY KEY,
        content TEXT,
        embedding VECTOR(1536)
    );
    ```

<br>

## 建立腳本

1. 安裝 OpenAI 套件。

    ```bash
    pip install openai python-dotenv psycopg2-binary numpy
    ```

<br>

2. 建立文件；腳本任意命名如 `ex02.ipynb`，使用筆記本即可。

    ```bash
    touch .env .gitignore ex02.ipynb
    ```

<br>

3. 編輯腳本。

    ```python
    import os
    from openai import OpenAI
    import psycopg2
    from dotenv import load_dotenv

    # 載入 .env 檔案中的敏感資訊
    load_dotenv()

    # 初始化 OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # 取得嵌入向量
    def get_embedding(text):
        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input=[text]
        )
        return response.data[0].embedding

    # 建立資料庫連線
    conn = psycopg2.connect(
        dbname="testdb",
        user="postgres",
        password=os.getenv("POSTGRES_PASSWORD"),
        host="localhost",
        port=5432
    )
    cursor = conn.cursor()

    # 要儲存的文本
    text = "什麼是 RAG？"
    embedding = get_embedding(text)

    # 寫入向量與文本
    cursor.execute("""
        INSERT INTO documents (content, embedding)
        VALUES (%s, %s)
    """, (text, embedding))

    conn.commit()
    # cursor.close()
    # conn.close()
    print("✅ 向量已成功寫入 PostgreSQL")
    ```

<br>

4. 寫入更多文字，只要調用一次 get_embedding() 並將結果寫入即可。

    ```python
    texts = [
        "什麼是 RAG？",
        "PostgreSQL 是一種關聯式資料庫。",
        "pgvector 可以用來儲存與查詢向量。",
    ]

    for text in texts:
        embedding = get_embedding(text)
        cursor.execute(
            "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
            (text, embedding)
        )
        print(f"✅ 已寫入：{text}")

    conn.commit()

    ```

<br>

5. 要關閉連線時運行。

    ```python
    cursor.close()
    conn.close()
    ```

<br>

6. 相似度查詢。

    ```python
    import numpy as np

    # 查詢最相似內容
    question = "請問什麼是向量資料庫？"
    query_embedding = get_embedding(question)

    # 將向量轉為字串格式並轉型為 vector
    embedding_str = "[" + ",".join(map(str, query_embedding)) + "]"

    cursor.execute("""
        SELECT content
        FROM documents
        ORDER BY embedding <#> %s::vector
        LIMIT 3;
    """, (embedding_str,))

    rows = cursor.fetchall()
    print("🔍 與問題最相近的資料：")
    for row in rows:
        print("-", row[0])
    ```

<br>

7. 將查詢結果送入 LLM 完成回答。

    ```python
    context = "\n".join([row[0] for row in rows])
    prompt = f"根據以下內容回答問題：\n{context}\n\nQ: {question}"

    # 使用新版 openai.Chat API 調用
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", 
                "content": "你是資料查詢助理，請根據提供內容回答問題"
            },
            {
                "role": "user", 
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content
    print("🤖 回答：", answer)
    ```

<br>

___

_END_


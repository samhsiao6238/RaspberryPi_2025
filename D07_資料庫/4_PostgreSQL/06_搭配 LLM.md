# 實作 RAG

_Retrieval-Augmented Generation，整合 PostgreSQL 向量資料庫與 LangChain / LlamaIndex 框架_

<br>

# 說明

1. PostgreSQL 搭配 `pgvector` 可作為 LangChain / LlamaIndex 的向量儲存後端。

2. 可支援 Embedding 查詢、Document 存取、查詢後送入 LLM 回答。

3. 使用者可依照不同任務選擇 LangChain 的 `VectorStore` 或 LlamaIndex 的 `VectorStoreIndex` 整合。

<br>

## LangChain 整合 pgvector

1. 安裝必要套件

```bash
pip install langchain pgvector tiktoken
pip install -U langchain-community
```

<br>

2. 修正 .env

```json
OPENAI_API_KEY=<填入-API-Key>
POSTGRES_PASSWORD=<填入密碼>
POSTGRES_USER=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=testdb
```

3. 建立 pgvector 向量儲存物件

```python
from langchain_community.vectorstores.pgvector import PGVector
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
import os

# 載入 .env
load_dotenv()

# 檢查參數是否成功載入
print("[DEBUG] DB 連線資訊：")
print("USER:", os.getenv("POSTGRES_USER"))
print("PORT:", os.getenv("POSTGRES_PORT"))
print("DB:", os.getenv("POSTGRES_DB"))

# 建立連線字串
connection_string = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)

embedding = OpenAIEmbeddings()

# 建立 PGVector 實例
vectorstore = PGVector(
    collection_name="documents",
    connection_string=connection_string,
    embedding_function=embedding
)
```

<br>

4. 向量查詢並生成回答；會得到有限的答案。

```python
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=vectorstore.as_retriever()
)

query = "請問什麼是向量資料庫？"
result = qa_chain.run(query)
print("🤖 回答：", result)
```

<br>

5. 插入新資料到 pgvector 資料表（documents）

```python
from langchain_community.vectorstores.pgvector import PGVector
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
import os

# 載入 .env（內含 OPENAI_API_KEY, POSTGRES_*）
load_dotenv()

# 建立 Embedding 物件
embedding = OpenAIEmbeddings()

# 建立 PGVector 儲存後端
vectorstore = PGVector(
    collection_name="documents",
    connection_string=(
        f"postgresql://{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@"
        f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/"
        f"{os.getenv('POSTGRES_DB')}"
    ),
    embedding_function=embedding
)

# 測試插入資料
texts = [
    "向量資料庫是一種支援語意查詢的資料庫，常用於 AI 與 NLP 領域。",
    "RAG 是一種結合語意檢索與生成的技術，可提升 LLM 回答正確率。",
    "PostgreSQL 搭配 pgvector 可以儲存並查詢 embedding 向量。",
]
vectorstore.add_texts(texts)
print("✅ 已插入測試資料")
```



6. 重新查詢資料並讓 LLM 回答；附加說明，`vectorstore.add_texts([...])` 會自動計算 embedding 並寫入 PostgreSQL，無需手動建表，`PGVector` 會在找不到時自動建立 `documents` 資料表（包含 `id`, `content`, `embedding` 欄位）。

```python
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# 建立 QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=vectorstore.as_retriever()
)

# 提出問題
query = "請問什麼是向量資料庫？"
result = qa_chain.run(query)
print("🤖 回答：", result)
```


## LlamaIndex 整合 PostgreSQL

1. 安裝必要套件

```bash
pip install llama-index-embeddings-openai llama-index-vector-stores-postgres
pip install llama-index-llms-openai
```

<br>

2. 建立索引並寫入文件

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.postgres import PGVectorStore
from dotenv import load_dotenv
import os

# 載入 .env 環境變數
load_dotenv()

# 檢查並建立測試資料夾與檔案
doc_path = "./docs"
os.makedirs(doc_path, exist_ok=True)
test_file_path = os.path.join(doc_path, "sample.txt")
if not os.path.exists(test_file_path):
    with open(test_file_path, "w", encoding="utf-8") as f:
        f.write("向量資料庫是一種支援語意查詢的資料庫系統，可搭配 embedding 與 LLM 回答問題。")

# 載入資料夾中的文件
documents = SimpleDirectoryReader(doc_path).load_data()

# 建立 PostgreSQL 向量儲存後端
vector_store = PGVectorStore.from_params(
    database="testdb",
    host="localhost",
    password=os.getenv("POSTGRES_PASSWORD"),
    user="postgres",
    port=5432,
    table_name="documents"
)

# 建立索引
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=OpenAIEmbedding(),
    vector_store=vector_store
)
```

<br>

3. 啟動查詢引擎並回傳回答

```python
query_engine = index.as_query_engine()
response = query_engine.query("什麼是 RAG？")
print("🤖 回答：", response)
```

<br>

___

_END_

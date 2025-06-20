# 使用 Python 操作

_在樹莓派使用 Python 操作 PostgreSQL_

<br>

## 環境準備

1. 建立並啟動虛擬環境。

    ```bash
    cd ~/Documents
    mkdir exPostgreSQL
    mkdir PythonVenvs && cd PythonVenvs
    python -m venv envPostgreSQL
    echo "source ~/Documents/PythonVenvs/envPostgreSQL/bin/activate" >> ~/.bashrc
    source ~/.bashrc
    ```

<br>

2. 安裝 Python PostgreSQL 套件 `psycopg2`。

    ```bash
    pip install psycopg2-binary
    ```

<br>

## 操作範例

1. 匯入與建立連線。

    ```python
    import psycopg2
    import psycopg2.extensions

    # 建立連線到預設資料庫
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="<更改為自己設定的密碼>",
        host="localhost",
        port=5432
    )
    conn.set_isolation_level(
        psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
    )

    cursor = conn.cursor()
    ```

<br>

2. 建立資料庫。

    ```python
    cursor.execute("CREATE DATABASE testdb;")
    ```

<br>

3. 建立資料表 employees 並插入初始資料。

    ```python
    # 建立資料表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            position TEXT,
            salary NUMERIC
        );
    """)

    # 插入初始資料
    cursor.execute("""
        INSERT INTO employees (name, position, salary)
        VALUES 
            ('Alice', 'Manager', 80000),
            ('Bob', 'Developer', 60000),
            ('Charlie', 'Designer', 55000)
        ON CONFLICT DO NOTHING;
    """)

    conn.commit()
    ```

<br>

4. 查詢所有資料。

    ```python
    cursor.execute("SELECT * FROM employees;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    ```

<br>

5. 插入資料。

    ```python
    cursor.execute("""
        INSERT INTO employees (name, position, salary)
        VALUES (%s, %s, %s);
    """, ("David", "Tester", 40000.0))
    conn.commit()
    ```

<br>

6. 更新資料。

    ```python
    cursor.execute("""
        UPDATE employees
        SET salary = %s
        WHERE name = %s;
    """, (45000.0, "David"))
    conn.commit()
    ```

<br>

7. 刪除資料。

    ```python
    cursor.execute("DELETE FROM employees WHERE name = %s;", ("David",))
    conn.commit()
    ```

<br>

8. 關閉連線。

    ```python
    cursor.close()
    conn.close()
    ```

<br>

___

_END_

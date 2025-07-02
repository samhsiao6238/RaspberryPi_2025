# Docker 常用指令

<br>

## 鏡像操作

_Images_

<br>

1. 下載 Docker 鏡像；從 Docker Hub 或其他 Registry 取得指定鏡像。

    ```bash
    docker pull <image-name>
    ```

<br>

2. 列出本地鏡像。

    ```bash
    docker images
    ```

<br>

3. 刪除本地鏡像。

    ```bash
    docker rmi <image-id 或 image-name>
    ```

<br>

## 運行容器參數

_說明主指令中的 `[options]`_

<br>

1. 建立並啟動一個新的容器實例。

    ```bash
    docker run [options] <image-name>
    ```

<br>

2. 背景執行，detached 模式；容器啟動後在背景執行，不佔用終端機。

    ```bash
    docker run -d <image-name>
    ```

<br>

3. 自訂容器名稱；預設會隨機產生名稱，可透過 --name 指定易記名稱。

    ```bash
    docker run --name <container-name> <image-name>
    ```

<br>

4. 埠口對映 `Port Mapping`；將容器內部服務的埠口映射到主機，讓主機可訪問容器服務。

    ```bash
    docker run -p <外部埠>:<內部埠> <image-name>
    ```

<br>

5. 可掛載資料卷 `Volumn`；將主機目錄掛載到容器內，實現資料持久化或資料共享。

    ```bash
    docker run -v <主機路徑>:<容器路徑> <image-name>
    ```

<br>

6. 使用主機網路模式 `Host Network`；容器與主機共用網路堆疊，適用需要廣播、低延遲的應用。

    ```bash
    docker run --network=host <image-name>
    ```

<br>

## 容器操作

_Containers_

<br>

1. 列出運行中的容器。

    ```bash
    docker ps
    ```

<br>

2. 列出包含停止的所有容器。

    ```bash
    docker ps -a
    ```

<br>

3. 列出所有容器 ID。

    ```bash
    docker ps -aq
    ```

<br>

4. 停止指定容器。

    ```bash
    docker stop <container-id 或 container-name>
    ```

<br>

5. 啟動已停止容器。

    ```bash
    docker start <container-id or container-name>
    ```

<br>

6. 刪除指定容器。

    ```bash
    docker rm <container-id or container-name>
    ```

<br>

7. 強制刪除容器，包含仍在執行中的容器。

    ```bash
    docker rm -f <container-id or container-name>
    ```

<br>

8. 一次刪除所有容器。

    ```bash
    docker rm -f $(docker ps -aq)
    ```

<br>

9. 一次停止所有運行中的容器。

    ```bash
    docker stop $(docker ps -aq)
    ```

<br>

## 系統與服務

1. 啟動 Docker 系統服務。

    ```bash
    sudo service docker start
    ```

<br>

## 查詢與格式化顯示

1. 僅顯示容器 ID 與鏡像名稱。

    ```bash
    docker ps --format "{{.ID}}  {{.Image}}"
    ```

<br>

___

_End_

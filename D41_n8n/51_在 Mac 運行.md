# 快速運行 n8n

_在本機上操作，可使用以下三種方式中的一種_

## 使用 npx

_這個方式會即時從網路抓最新版本執行，不會在全域安裝任何檔案，每次關閉後都只剩下指定的資料目錄；適用於臨時試用、快速驗證_

1. 直接拉最新版本並啟動

```bash
npx n8n
```

2. 啟動後編輯器會跑在 [http://localhost:5678](http://localhost:5678)，資料（設定、工作流等）會儲存在 `~/.n8n`。

3. 這個方式啟動服務後，預設會把 `SQLite` 資料庫、憑證等放在 `~/.n8n` 資料夾。關機或停止服務後，資料會保留在磁碟上，若要徹底清除需手動刪除資料夾 `~/.n8n`。

```bash
rm -rf ~/.n8n
```

4. 若要一次性的實例，可在啟動時指定資料目錄到暫存路徑如下；如此在系統關機後，`/tmp/n8n-data` 的內容會隨系統清理而移除。

```bash
npx n8n start --data-dir /tmp/n8n-data
```

## 全域安裝

_這方式會下載完整套件在全局 `node_modules` 目錄，完成後可直接執行 n8n 指令，離線也能使用；適合長期本機使用_

1. 安裝。

```bash
npm install -g n8n
```

2. 重設檔案權限，需使用 sudo

```bash
sudo chmod 600 ~/.n8n/config
```

3. 修正 ~/.n8n 及 ~/.cache/n8n 的擁有權與權限

```bash
sudo chown -R $(id -u):$(id -g) ~/.n8n
find ~/.n8n -type d -exec chmod 700 {} \;
find ~/.n8n -type f -exec chmod 600 {} \;

sudo chown -R $(id -u):$(id -g) ~/.cache/n8n
find ~/.cache/n8n -type d -exec chmod 700 {} \;
find ~/.cache/n8n -type f -exec chmod 600 {} \;
```

4. 在 ~/.zshrc 中加入以下語句，可消除不影響運作的警告。

```bash
export N8N_RUNNERS_ENABLED=true
```

![](images/img_49.png)

5. 啟動

```bash
n8n
```

6. 依據畫面提示進行訪問。

![](images/img_50.png)


## Docker 部署

_適合伺服器、容器化環境_

1. 確認本機 Docker 狀態

```bash
docker -v
```

2. 透過終端機啟動 Docker Desktop；參數 `--background` 會讓應用在背景運行。

```bash
open --background -a Docker
```

3. 啟動後可查看詳細資訊。

```bash
docker info
```

4. 查看容器運行。

```bash
docker ps -a
```

5. 在 Docker 中建立一個儲存空間並命名 `n8n_data`，可用於永久保存 n8n 的資料。

```bash
docker volume create n8n_data
```

2. 以互動模式啟動容器

```bash
docker run -it --rm \
    --name n8n \
    -p 5678:5678 \
    -v n8n_data:/home/node/.n8n \
    docker.n8n.io/n8nio/n8n
```

3. 編輯器在 `5678` 端口運行，所有資料都存在 `n8n_data` volume 中

## 設定環境變數

_在以上任一方式前，可設定環境變數以控制資料庫、埠號、時區等_

1. 用 SQLite、設定時區

```bash
export DB_TYPE="sqlite"
export GENERIC_TIMEZONE="Asia/Taipei"
export N8N_PORT=5678
export N8N_HOST="0.0.0.0"
```


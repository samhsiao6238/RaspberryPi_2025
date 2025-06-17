# 建立 n8n 開發環境
_在 MacOS 上_


## 🔧 步驟一：安裝 Node.js（透過 nvm 管理）

```bash
brew install nvm
mkdir ~/.nvm
```

將以下內容加入 `~/.zshrc`（或你使用的 shell 設定檔）：

```bash
export NVM_DIR="$HOME/.nvm"
source "$(brew --prefix nvm)/nvm.sh"
```

重新載入設定檔並安裝 Node.js：

```bash
source ~/.zshrc
nvm install 18
nvm use 18
nvm alias default 18
```



## 🔧 步驟二：安裝與初始化 n8n 專案

```bash
git clone https://github.com/n8n-io/n8n.git
cd n8n
npm ci
```

📌 說明：

* `npm ci` 比 `npm install` 更適合用於乾淨環境下的專案安裝，會完全依照 `package-lock.json` 進行安裝。



## 🔧 步驟三：本地開發啟動

```bash
npm run dev
```

成功啟動後會看到：

```text
n8n ready on 0.0.0.0, port 5678
```

可在瀏覽器開啟 [http://localhost:5678](http://localhost:5678) 進入 n8n 編輯介面。



## 📂 專案結構簡介（重要目錄）

| 目錄                    | 說明               |
|  | - |
| `packages/cli`        | 核心 CLI 執行進入點     |
| `packages/editor-ui`  | 前端 Vue 編輯器       |
| `packages/workflow`   | workflow 定義與處理邏輯 |
| `packages/nodes-base` | 範例與內建節點（Node）定義  |



## 📌 補充建議

* 若安裝依賴失敗，建議清除 node\_modules：

  ```bash
  rm -rf node_modules package-lock.json
  npm ci
  ```

* 建議使用 VS Code，並安裝以下 Extension：

  * ESLint
  * Prettier
  * Volar（若你要修改前端）

* 可考慮將本地端執行改為 Docker 模式（第二部會說明）



如您確認此格式可接受，我可以繼續撰寫第二部（例如：整合 Docker、設置 Postgres、或開發自定義節點） ✨是否繼續？

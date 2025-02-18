# 安裝 Docker

## 步驟

1. 下載並執行腳本。

```bash
curl -fsSL https://get.docker.com | sudo sh
```

2. 啟動並設定 Docker

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

3. 確保當前用戶可以使用 Docker

```bash
sudo usermod -aG docker $USER
newgrp docker
```

## 登入 Github

_需取得憑證_

<br>

1. 在終端機建立帳號與憑證的變數。

```bash
ACCOUNT=samhsiao6238
TOKEN=
```

2. 若遇到需登入 GitHub 帳戶才能下載的 GHCR 容器，運行以下指令。

```bash
docker login ghcr.io -u $ACCOUNT --password-stdin
```
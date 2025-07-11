# 安裝 Docker

<br>

## 步驟

1. 下載並執行腳本。

    ```bash
    curl -fsSL https://get.docker.com | sudo sh
    ```

<br>

2. 啟動並設定 Docker。

    ```bash
    sudo systemctl enable docker
    sudo systemctl start docker
    ```

<br>

3. 確保當前用戶可以使用 Docker。

    ```bash
    sudo usermod -aG docker $USER
    newgrp docker
    ```

<br>

## 取得 Github 憑證

1. 登入 GitHub 帳號，點右上角的頭像，選 `Settings`。

<br>

2. 左側選單滑動到最底，點 `Developer settings`。

<br>

3. 展開左側選單 `Personal access tokens`，點及 `Tokens (classic)` 或 `Fine-grained tokens` 皆可。

<br>

4. 按 `Generate new token`；其餘省略。

<br>

## 登入 Github

_需取得憑證_

<br>

1. 在終端機建立帳號與憑證的變數。

    ```bash
    ACCOUNT=samhsiao6238
    TOKEN=
    ```

<br>

2. 若遇到需登入 GitHub 帳戶才能下載的 GHCR 容器，運行以下指令。

    ```bash
    echo "$TOKEN" | docker login ghcr.io -u "$ACCOUNT" --password-stdin
    ```

<br>

___

_END_
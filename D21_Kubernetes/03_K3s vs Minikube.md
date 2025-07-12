# K3s vs Minikube

_同為輕量級 `Kubernetes` 方案，但各自有不同使用場景_

<br>

## 目標用途

1. `Minikube` 是專為本地開發與測試設計，在單一 `VM` 或 `容器` 中模擬 `Kubernetes` 叢集。

<br>

2. `K3s` 是針對 `生產` 及 `邊緣` 環境優化，支援多節點部署，適合 `樹莓派`、`IoT 裝置` 與 `輕量伺服器`。

<br>

## 安裝與運行

1. `Minikube` 透過安裝 `minikube CLI`，執行 `minikube start` 即可啟動單節點叢集，內建多種 `Driver` 如 `Docker`、`VirtualBox`、`Hyperkit`。

<br>

2. `K3s` 透過官方提供指令下載二進位文件進行安裝，`Server` 和 `Agent` 要分別安裝，完成部署可跨機器自動組成多節點叢集。

    ```bash
    curl -sfL https://get.k3s.io | sh -
    ```

<br>

## 資源需求

1. `Minikube` 需為 `VM` 或 `容器` 預留至少 `2 GB RAM`，並佔用 `本機 CPU`。

<br>

2. `K3s` 核心元件精簡至約 `40 MB`，單節點最低 `512 MB RAM` 即可起動；預設內建 `SQLite`，也可切換至 `MySQL/PostgreSQL`。

<br>

## 組件與功能

1. `Minikube` 包含完整 `Kubernetes` 標準元件，並支援常見 `附加套件（Addon）`。

<br>

2. `K3s` 移除或改用輕量替代方案，如 `SQLite` 取代 `etcd`，並自動管理 `TLS` 和 `憑證`。

<br>

## 運行環境

1. `Minikube` 僅限本地 `VM` 或 `容器`，適合開發者 `工作站`，需穩定的 `Hypervisor` 或 `Docker` 環境。

<br>

2. `K3s` 適用於 `邊緣`、`IoT`、`裸機伺服器` 或 `雲端 VM`，對網路和硬體資源要求低，能在不穩定網路環境中持續運行。

<br>

## 社群支持與生態

1. `Minikube` 由 `CNCF` 官方維護，生態系統成熟，有豐富的教學與第三方擴充套件。

<br>

2. `K3s` 由 `Rancher Labs` 主導開發，雖社群規模較小，但對輕量與邊緣應用需求回應迅速，並逐步整合至 `Rancher` 平台。

<br>

___

_END_

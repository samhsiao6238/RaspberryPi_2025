# 快速導覽

_在 `樹莓派 5` 使用 `K3s` 建立 `Kubernetes 叢集`；可參考 [網路文章](https://everythingdevops.dev/step-by-step-guide-creating-a-kubernetes-cluster-on-raspberry-pi-5-with-k3s/)_

<br>

## Kubernetes 簡介

_K8s_

<br>

1. `Kubernetes` 簡稱 `K8s`，是一個容器編排系統，用來自動部署、擴展和管理容器化應用；所謂 `容器化應用` 是指將應用程式及其所有依賴封裝到一個 `容器` 中運行，確保應用能夠在不同環境中保持一致的執行，最常見的 `Docker` 就是一種提供標準化應用打包的方式，而 `K8s` 是負責管理、調度大量容器，並提供高可用性與負載均衡。

<br>

2. `Minikube` 則是模擬 K8s 的本地測試工具，適用於開發與學習而不適合生產環境。

<br>

## 關於 K3s

1. `K3s` 是 `K8s` 的輕量級版本，針對資源受限環境如 _IoT 設備或邊緣運算設備_ 而設計，並已針對 `ARM 架構` 進行優化，故適用於樹莓派。

<br>

2. 輕量化設計佔用資源較少，同時簡化安裝程序，比傳統 Kubernetes 更簡單，另外也內建 `kubectl`，可直接使用 `kubectl` 指令。

<br>

___

_END_
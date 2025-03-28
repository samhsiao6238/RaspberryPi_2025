## 拓展

_連線 WiFi 並傳回 IP_

1. main.cpp（連線 WiFi 並輸出取得的 IP）

```cpp
#include "pico/stdlib.h"
#include "pico/cyw43_arch.h"
// 為 netif_default
#include "lwip/netif.h"
// 為 ip4_addr_t
#include "lwip/ip_addr.h"
#include <cstdio>

int main() {
    // 初始化標準輸出（USB 或 UART）
    stdio_init_all();

    if (cyw43_arch_init()) {
        printf("無法初始化 WiFi 模組\n");
        return -1;
    }

    // 啟用 Station 模式
    cyw43_arch_enable_sta_mode();

    // WiFi 網路名稱與密碼
    const char* ssid = "SamHome2.4g";
    const char* password = "sam112233";

    printf("嘗試連線至 WiFi：%s...\n", ssid);

    int err = cyw43_arch_wifi_connect_timeout_ms(
        ssid, 
        password, 
        CYW43_AUTH_WPA2_AES_PSK, 
        10000
    );
    if (err) {
        printf("WiFi 連線失敗，錯誤碼：%d\n", err);
    } else {
        printf("✅ WiFi 已連線！\n");
    }

    // 持續輸出目前的 IP 位址
    while (true) {
        const ip4_addr_t* ip = netif_ip4_addr(netif_default);
        printf("目前 IP 位址：%s\n", ip4addr_ntoa(ip));
        sleep_ms(1000);
    }

    cyw43_arch_deinit();
    return 0;
}
```

2. CMakeLists.txt（支援 WiFi 連線所需庫）。

```bash
cmake_minimum_required(VERSION 3.13)

# 引入 Pico SDK 初始化腳本（必須在 project 之前）
include($ENV{PICO_SDK_PATH}/pico_sdk_init.cmake)

# 專案名稱
project(_ex0327_)

# 初始化 SDK
pico_sdk_init()

# 建立執行檔，加入主程式碼
add_executable(_ex0327_
    main.cpp
)

# 啟用 USB 輸出，關閉 UART
pico_enable_stdio_usb(_ex0327_ 1)
pico_enable_stdio_uart(_ex0327_ 0)

# 連結 WiFi 所需函式庫
target_link_libraries(_ex0327_
    pico_stdlib
    pico_cyw43_arch_lwip_threadsafe_background
)

# 輸出 uf2/bin/hex/map 檔案
pico_add_extra_outputs(_ex0327_)
```

3. 刪除重建。

```bash
cd ..
rm -rf build
mkdir build && cd build
```

4. 編譯。

```bash
cmake ..
make -j4
```

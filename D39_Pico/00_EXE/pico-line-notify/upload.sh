#!/bin/bash

# 上傳 boot.py 與 main.py 到 Pico W
mpremote connect auto fs cp boot.py :boot.py
mpremote connect auto fs cp main.py :main.py
echo "✅ 上傳完成！"
# Ngrok

_撰寫自動化腳本啟動 Ngrok_

<br>

## 建立自動化腳本

_使用 `zenity` 來搭建_

<br>

1. 安裝套件。

   ```bash
   sudo apt install zenity
   ```

<br>

2. 在 `~/Documents/NgrokApp` 資料夾內建立腳本。

   ```bash
   cd ~/Documents/NgrokApp
   nano start_ngrok.sh
   ```

<br>

3. 編輯內容；完成後使用快速鍵存檔、退出。

   ```bash
   #!/bin/bash
   # 這個腳本會以指定的端口啟動

   # 詢問要用哪個端口
   PORT=$(zenity --entry --title="Enter Port for ngrok" --text="Enter the port you want to use:")

   # 檢查是否取消
   if [ -z "$PORT" ]; then
       exit 1
   fi

   # 啟動
   # ./ngrok http $PORT
   NGROK_PATH=~/Documents/NgrokApp/ngrok
   "$NGROK_PATH" http "$PORT"
   read -p "Ngrok 啟動完成，按 Enter 結束..."
   ```

<br>

4. 賦予腳本執行權限。

   ```bash
   sudo chmod +x start_ngrok.sh
   ```

<br>

5. 進入桌面。

   ```bash
   cd ~/Desktop
   ```

<br>

6. 建立腳本。

   ```bash
   nano start_ngrok.desktop
   ```

<br>

7. 編輯內容。

   ```bash
   [Desktop Entry]
   Type=Application
   Name=Start Ngrok
   Comment=Start ngrok for HTTP 80
   Exec=bash -c 'cd ~/Documents/NgrokApp && ./start_ngrok.sh'
   Icon=terminal
   Terminal=true
   ```

<br>

8. 賦予權限。

   ```bash
   sudo chmod +x start_ngrok.desktop
   ```

<br>

## 進入樹莓派桌面

1. 點擊運行。

   ![](images/img_98.png)

<br>

2. 在彈窗中點擊 `Execute`。

   ![](images/img_99.png)

<br>

3. 輸入指定的端口如 `80` 然後點擊 `OK`，接著去訪問網頁看看。

   ![](images/img_100.png)

<br>

## 優化自動化腳本

_添加輸入 Token 的對話框_

<br>

1. 修改原本的腳本。

   ```bash
   sudo nano ~/Documents/NgrokApp/start_ngrok.sh
   ```
   _技巧提示：在編輯器中以 CTRL+K 可以快速刪除一整行_

<br>

2. 編輯內容。

   ```bash
   #!/bin/bash
   # 這個腳本會提示用戶輸入端口和Ngrok token，然後啟動ngrok

   # 詢問用戶要用哪個端口
   PORT=$(zenity --entry --title="Enter Port for ngrok" --text="Enter the port you want to use (Current Port):")

   # 如果用戶按下取消或不輸入端口，則退出
   if [ -z "$PORT" ]; then
      exit 1
   fi

   # 詢問用戶的Ngrok token
   TOKEN=$(zenity --entry --title="Enter Ngrok Token" --text="Enter your ngrok token (if you want to authenticate):")

   # 如果用戶提供了token，使用它來認證
   if [ ! -z "$TOKEN" ]; then
      ./ngrok authtoken $TOKEN
   fi

   # 使用指定的端口啟動ngrok
   ./ngrok http $PORT
   ```

<br>

3. 雙擊啟動桌面腳本。

   ![img](images/img_35.png)

<br>

4. 點擊 `執行`。

   ![img](images/img_36.png)

<br>

5. 輸入端口。

   ![img](images/img_37.png)

<br>

6. 可輸入 `Authtoken` ，假如已經存過可以按下 `ENTER` 以預設值運行，假如要切換帳號就要輸入該帳號的 `Authtoken` 。

   ![img](images/img_38.png)

<br>

7. 複製這個網址即可。

   ![img](images/img_39.png)

<br>

8. 在任意瀏覽器瀏覽，點擊 `Visit Site`。

   ![img](images/img_40.png)

<br>

9. 就會看到在指定端口的網站，比如說是 `80`，等價於終端機執行以下指令。
   
   ```bash
   ./ngrok http <端口號>
   ```

   ![img](images/img_42.png)

<br>

## 避免終端機自動關閉

1. 在某些終端機的版本中，運行後會自動關閉，可在腳本最後添加 `read` 指令，如此腳本在運行完成後會等待用戶輸入，從而保持終端機開啟。

   ```bash
   #!/bin/bash
   # 這個腳本會提示用戶輸入端口和Ngrok token，然後啟動ngrok

   # 詢問用戶要用哪個端口
   PORT=$(zenity --entry --title="Enter Port for ngrok" --text="Enter the port you want to use (Current Port):")

   # 如果用戶按下取消或不輸入端口，則退出
   if [ -z "$PORT" ]; then
      exit 1
   fi

   # 詢問用戶的Ngrok token
   TOKEN=$(zenity --entry --title="Enter Ngrok Token" --text="Enter your ngrok token (if you want to authenticate):")

   # 如果用戶提供了token，使用它來認證
   if [ ! -z "$TOKEN" ]; then
      ./ngrok authtoken $TOKEN
   fi

   # 使用指定的端口啟動ngrok
   ./ngrok http $PORT

   # 保持開啟直到用戶動作
   read
   ```

___

_END_

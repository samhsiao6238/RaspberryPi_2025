# CLI

<br>

## 步驟 

1. [官方載點](https://www.alibabacloud.com/help/en/cli/install-cli-on-macos?spm=a2c63.p38356.0.i0#32865bfe14am6:~:text=Download%20links%3A-,Official%20website,-%3A%20You%20can%20download)

<br>

2. 解壓縮。

    ```bash
    tar xzvf ~/Downloads/aliyun-cli-macosx-latest-universal.tgz
    ```

<br>

3. 複製到指定路徑。

    ```bash
    sudo cp ~/Downliads/aliyun /usr/local/bin
    ```

<br>

4. 測試。

    ```bash
    aliyun version
    ```

<br>

## 取得 AccessKey

1. 顯示。

    ![](images/img_66.png)

<br>

2. 創建。

    ![](images/img_67.png)

<br>

3. 再次確認，然後要進行驗證。

    ![](images/img_68.png)

<br>

4. 完成後，先下載。

    ![](images/img_69.png)

<br>

5. 點擊 `確定` 關閉視窗。

    ![](images/img_70.png)

<br>

## 設定

1. 設定憑證。

    ```bash
    aliyun configure
    ```

<br>

2. 其中預設區域設定為 `華東1`，ID 為 `cn-hangzhou`。

    ![](images/img_72.png)

<br>

3. 預設語言繁體中文，代碼為 `zh-Hant`。

    ![](images/img_71.png)

<br>

4. 完成。

    ![](images/img_73.png)

<br>

## 查詢

1. 查詢並列出指定欄位。

    ```bash
    aliyun ecs DescribeInstances | jq -r '.Instances.Instance[] | {InstanceId, InstanceName, InstanceType, Status, RegionId, ZoneId, PublicIpAddress, PrivateIpAddress}'
    ```

    ![](images/img_74.png)


<br>

## 清理資源

1. 查詢當前 ECS 實例。

    ```bash
    aliyun ecs DescribeInstances --RegionId "cn-hangzhou"
    ```

<br>

2. 確保 ECS 實例已停止。

    ```bash
    aliyun ecs StopInstance --InstanceId "<實例-Id>"
    ```

<br>

3. 徹底刪除 ECS 實例。

    ```bash
    aliyun ecs DeleteInstance --InstanceId "<實例-Id>" --Force true
    ```

<br>

4. 查詢當前安全群組。

    ```bash
    aliyun ecs DescribeSecurityGroups --RegionId "cn-hangzhou"
    ```

<br>

5. 刪除安全群組。

    ```bash
    aliyun ecs DeleteSecurityGroup --RegionId "cn-hangzhou" --SecurityGroupId "<安全組-Id>"
    ```

<br>

6. 查詢已建立的密鑰對。

    ```bash
    aliyun ecs DescribeKeyPairs --RegionId "cn-hangzhou"
    ```

<br>

7. 刪除密鑰對；特別注意，參數後的中括號 `[]` 必須搭配單引號 `''` 來包覆，這是避免命令行工具誤判這是 `shell` 的語法。

    ```bash
    aliyun ecs DeleteKeyPairs --RegionId "cn-hangzhou" --KeyPairNames '["<密鑰對-名稱>"]'
    ```

    ![](images/img_75.png)

<br>

___

_持續補充_
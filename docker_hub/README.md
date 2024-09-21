# Docker Hub
在前面的章節，我們在執行container時，本機若不存在image file，docker會去registry(登錄伺服器)去尋找對應的image file  

目前最被廣泛使用的registry就是docker hub (也是docker官方預設去尋找docker image file的registry) 即使我們沒有註冊登入docker hub，docker還是會去docker hub尋找對應的image file  

在quick start章節，我們登入了docker hub，是因為後續還可以使用一些docker hub的功能  

由於在quick start章節已經有示範過如何登入docker hub，這邊就不介紹  
但為了後續方便可以先把docker hub的帳號名稱設定成一個變數，後續若需要用到這個帳戶名稱則可以直接使用此變數  

以linux為例，在".bashrc"或".zshrc"內加入這行，然後重新執行此檔案，即可得到帳戶名的變數
```
export dockerId="帳戶名稱"
```

## Image reference
Docker在尋找image file時是利用image file name來去docker hub尋找對應的image file  
但會遇到一個情況，有可能會出現相同image file name的image file，這是就需要用image reference(完整的image file name)來去尋找

Image reference包含了四個部份:  
1. registry網址 (docker hub的話是 docker.io)  
2. image file的擁有者帳戶 (可以是個人或團隊帳戶)  
3. repository(儲存庫)名稱 (用於標示應用程式名稱，一個repository可以儲存多個版本(tag)的image file)  
4. image tag (用於標示應用程式的版本，預設是latest)

範例如下:  
```
docker.io/library/python:3.9.20-slim
```

## Push image file
要將docker image推到docker hub上基本上和github大同小異，一樣是用"push"這個指令  

步驟如下:  
1. 建置完image file後，此時的image reference是沒有標註帳戶名稱的  
   因此我們要用tag指令來為騎上帳戶名稱，同時為此image file上一個版本的tag  
   ```
   docker image tag 映像檔名 $dockerId/映像檔名:版本號
   ```

2. 用push指令將其push到docker hub上  
   ```
   docker image push $dockerId/映像檔名:版本號
   ```

若該映像檔名是第一次上傳，則docker hub會自動創建一個repository(預設為public)  

## tag
在應用程式開發過程，通常會衍生出好幾個版本，docker中的image tag就是一個很好區分不同版本的方法(和git的tag類似)  

Docker的image tag可以是任何的字串，並且一個image file可以對應到多個image tag  

Docker image tag版本號大多的命名方針如下:  
```
[主要版本].[次要版本].[修補版本]
```
主要版本: 不同的主要版本可能會具有完全不同的功能  
次要版本: 不同的次要版本可能會添加部份小功能但不會影響主要版本的主功能  
修補版本: 基本不會有不同功能，但會修復bug或是進行優化  

但其實沒有硬性規定要怎麼訂定版本，基本上還是看個人習慣  

## Golden image
Docker hub是一個完全open source的社群，這時不免會有有心人將病毒放入image file中，等待大家去pull  
為了解決此問題，docker hub透過驗證發佈者和官放映像檔來解決該問題  

經過驗證的發佈者像是Microsoft, Oracle等等這些大公司製作出穩定且安全的基礎image file，然後以此基礎image file製作出穩定且安全的image file通常被稱為golden image  

因為golden image其實本質上也image file的一種，所以用法和一般的image file一樣，如下
```
FROM golden/dotnetcore-sdk:3.0 AS builder
```

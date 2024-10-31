# Docker 數據保存
Docker container有一個特性就是無狀態(stateless)，及docker container不會永久的保存data，在docker container關閉時data也會跟著消失  

但很常有應用程式是有狀態的(stateful)，意思是說今天我們關閉應用程式下次再次開啟時原先的data也應保存下來  

讓docker從stateless變成stateful大致上可以分為兩種方式:
1. Docker volume  
2. Docker 掛載(mount) 資料夾  

## Docker volume
Docker volume可以視為docker的隨身碟，volume和docker本身是獨立的

Docker volume在docker內部會以資料夾的形式呈現

使用docker volume有兩種方式:
1. 在dockerfile建立一個新的docker volume  
   如下dockerfile
   ```
   FROM diamol/dotnet-aspnet
   WORKDIR /app
   ENTRYPOINT ["dotnet", "ToDoList.dll"]

   # 創建一個volume並掛載到container的 /data
   VOLUME /data
   COPY --from=builder /out/ .
   ```
2. 在外面創建docker volume並掛載(attach)到container上  
   如下
   ```
   創建一個volume todo-list
   docker volume create todo-list
   使用-v參數來掛載volume到container的/data上
   docker container run -d -p 8011:80 -v todo-list:data --name todo-v1 diamol/ch06-todo-list
   ```

上面兩種方法都可以使用到docker volume但若兩者同時使用呢? (dockerfile有定義volume，在執行命令時有用-v參數)  
如果兩者同時使用的話-v會蓋掉dockfile內的volume而不會在創一個docker volume

\* 這裡所說的掛載(attach)和之後講的掛載(mount)本地資料夾在英文上不一樣，不過其實只是因為主詞不同動作視差不多的，所以之後都會寫掛載不區分兩者

也可以兩個不同的container掛載到相同的docker volume上，例如
```
假設todo1在dockerfile建立了自己的docker volume
docekr container run --name todo1 -d diamol/ch06-todo-list
t3使用了todo1的volume，兩者共用
docker container run -d --name t3 --volume-from todo1 diamol/ch06-todo-list
```

\* 但要注意若A和B共用了同一個docker volume，表示A和B都可以對volume修改，有可能會導致conflict

## Bind mount (掛載本地資料夾)
Bind mount是可以讓docker container和本機直接共享儲存的方式，如下
```
先寫好變數以縮短後面的指令
source="$(pwd)/databases" && target='/data'
創建一個資料夾
mkdir ./databases
執行docker container並掛載databases資料夾
docker container run --mount type=bind,source=$source,target=$target -d -p 8012:80 diamol/ch06-todo-list
```

Bind mount是雙向的，你可以在container中使用，也可以在本機上使用  

不過因為安全性的問題，因此docker會以最低權限的帳戶來執行，所以若有需要一些高權限的操作，就需要在dockerfile中使用USER指令來提高權限

### Bind mount的限制
1. 若container的資料夾中本來就存在檔案，此時我們將本地資料夾掛載到container的資料夾上，則原本container的資料會被覆蓋消失  
   ```
   設定變數
   source="$(pwd)/data" && target="/data"
   執行container，假設此container會列出/data下的所有檔案
   docker container run diamol/ch06-bind-mount
   ==============
   abc.txt
   def.txt
   ==============
   執行docker container並掛載
   docker container run --mount type=bind,source=$source,target=$target diamol/ch06-bind-mount
   ==============
   123.txt
   456.txt
   ==============
   ```
2. 若只掛載單一檔案的話則會合併在一起(Windows不支援單一檔案掛載)

3. 若將分散式系統(例如: nas)掛載到docker container上則有可能需要用對應的指令來操作，若對其進行不支援的指令的話會產生error

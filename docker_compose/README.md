# Docker compose
Docker compose是一個工具用來定義並運行多個docker container  

若沒有使用docker compose，要運行多個container，就是用docker CLI(command line interface)一個一個執行建立起來，但這樣很沒效率又不好管理，因此有docker compose來解決單純用docker CLI的問題

Docker compose使用YAML(.yml檔)作為標準格式，docker compose的核心也是唯一一個問件就叫做docker-compose.yml  

docker-compose.yml大致上包含了以下部份:  
1. version: 必須要有，用來指名所用的docker compose所用的版本  
2. services: 至少要有一個，基本上就是用來定義container的，要跑幾個container就會有幾個子項  
3. 其他: 可選，包含volumns, networks等等，若有需要可配置

docker-compose.yml示意如下:  
ref: [科技毒蟲](https://yhtechnote.com/what-is-docker-compose/)
```
# 通常建議用最新版本
viersion: '3.9'

service:
	frontend:
		# build表示透過buildc後面所寫的路徑下的dockerfile去創建此container
		build .
		# 設定container的port和主機的port的端口轉發(理解成主機和container連接即可)
		post:
			- "8020:80"
		# 此container所使用的volumes (volumes也可設成跟service同階，則為全部共用)
		volumes:
			- "/usr/:/user"

	db:
		# 透過image創建
		image: mysql/mysql-server:5.7
		# 設定環境變數
		environment:
			MY_USER: user
			MY_PASSWORD: 123
			MY_DATABASE: database
```

Docker compose的指令和docker的指令是獨立開的，可以查看[官方網站](https://docs.docker.com/reference/cli/docker/compose/)

## 補充
docker compose雖然解決了單純用docker CLI的問題，但跟一些容器平台(ex: K8s, Docker Swarm ...)有一些差異  

這邊舉兩個例子容器平台能作到但單純用docker compose做不到的:
1. 若要在多個節點或是VM上去運行相同的application，單純docker compose是無法作到的(多節點部署)  
2. 若在建置container時失敗，docker compose不會自動重啟，而是必須要手動啟動

還有其他docker compose做不到的事這邊就不贅述，這也是為什麼企業幾乎都會使用容器平台，而不是只使用docker compose  

不過若是個人學習練習或是小型專案，其實docker compose也夠用了

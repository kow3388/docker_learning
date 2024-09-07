# 第一階段: 建置階段，使用較大的基底映像來建置應用程式
FROM python:3.10.12-slim AS builder

MAINTAINER wangyuwen <lspss93121@yahoo.com.tw>

# 設定工作目錄
WORKDIR /work_dir

# 將 Python 應用程式檔案複製到映像中
COPY main.py .

# 安裝所需的 Python 套件
RUN pip install numpy

# 測試程式碼（若有）

# 第二階段: 運行階段
FROM python:3.10.12-slim

# 設定工作目錄
WORKDIR /work_dir

# 從建置階段複製已安裝的套件
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# 從建置階段複製所需的程式碼
COPY --from=builder /work_dir/main.py .

# 指定執行的指令
CMD ["python3", "main.py"]

#用官方python作為basic image
FROM python:3.10.12-slim

MAINTAINER wangyuwen <lspss93121@yahoo.com.tw>

#在docker中創建一個work_dir得資料夾
WORKDIR /work_dir

#將我們所需的檔案copy至work_dir中
COPY main.py /work_dir/

#pip install numpy
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir numpy

CMD ["python3", "main.py"]

# Укажите необходимую версию python
FROM python:3.9

# Выберите папку, в которой будут размещаться файлы проекта внутри контейнера
WORKDIR /app

# Скопируйте в контейнер файлы, которые редко меняются
COPY ./requirements.txt /src/requirements.txt

# Установите зависимости
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

# Скопируйте всё оставшееся. Для ускорения сборки образа эту команду стоит разместить ближе к концу файла.
COPY /src ./

# Укажите порт, на котором приложение будет доступно внутри Docker-сети
EXPOSE 8000/tcp

#Этой командой запускать, если в main.py не запускается сервер
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
ENTRYPOINT ["python3", "main.py"]
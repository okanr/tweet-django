FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN ./src/manage.py makemigrations
RUN ./src/manage.py migrate

EXPOSE 8000

CMD [ "python", "./src/manage.py", "runserver", "0.0.0.0:8000"]
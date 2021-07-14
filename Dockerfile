FROM python:3.7.3-stretch

WORKDIR /app

COPY ["app.py", "requirements.txt"] /app/

RUN pip install --upgrade pip

RUN pip install  -r requirements.txt

# --trusted-host pypi.python.org

EXPOSE 8080

CMD ["python", "app.py"]

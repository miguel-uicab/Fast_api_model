FROM python:3.9

# RUN apt-get update
# RUN apt-get install python


WORKDIR /home/project/app

COPY requirements_update.txt /home/project/app
RUN pip install --no-cache-dir -r requirements_update.txt

COPY . /home/project/app


ENTRYPOINT ["uvicorn"]
CMD ["app.main:app", "--host", "0.0.0.0","--port", "5000"]
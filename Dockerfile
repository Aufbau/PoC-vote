FROM python:3.8.7-alpine3.12
WORKDIR /app
COPY ./vote_app/requirements.txt .
RUN pip install -r requirements.txt
COPY ./vote_app/ .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
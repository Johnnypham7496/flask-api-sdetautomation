FROM python:3.10.11

EXPOSE 5000

CMD ["--workers=4", "--bind=0.0.0.0:5000", "app:my_app"]

RUN mkdir /flask_api_sdetautomation && \
    apk upgrade --update && \
    apk add --no-cache postgresql-dev gcc python3-dev musl-dev && \
    python -3 venv venv/

COPY . /flask_api_sdetautomation
WORKDIR /flask_api_sdetautomation

RUN . venv/Scripts/Activate %% pip install -r requirements.txt
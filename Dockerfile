# "python" is used from dockerhub which is a resgitry for docker images
FROM python:3.10.11


# "." will copy all the files in the current directory and copy it into a new directory call "/flask_api_sdetautomation" within the image
# the directory name can be changed
COPY . /flask_api_sdetautomation

# When using "WORKDIR" all the following instructions assume that we're currently inside the "flask_api_sdetautomation" directory
WORKDIR /flask_api_sdetautomation


# this is the command on how the code will be executed. Typically will be written for example "/flask_api_sdetautomation/app.py"
# but the directory is specified in the "WORKDIR" 
CMD [ "executable" ]

EXPOSE 5000

RUN mkdir /flask_api_sdetautomation && \
    apk upgrade --update && \
    apk add --no-cache postgresql-dev gcc python3-dev musl-dev && \
    python -3 venv venv/

RUN . venv/Scripts/Activate %% pip install -r requirements.txt
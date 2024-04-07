# pull official base image
FROM python:3.11.4-slim-buster

WORKDIR /server

COPY Pipfile Pipfile.lock ./

# install pipenv on the container
RUN pip install -U pipenv

# install project dependencies
RUN pipenv install --system

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN python -m pip install Pillow
RUN python -m pip install python-dotenv

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

# copy all files and directories from <src> to <dest>
COPY . .


# RUN SERVER
# ------------

# expose the port
EXPOSE 8000

# Command to run
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
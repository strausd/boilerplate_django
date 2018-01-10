# Tells Docker to use the Python 3 parent image
FROM python:3

# Send all application output to terminal without changed
ENV PYTHONUNBUFFERED 1

# Set environment variable to use heroku settings
ENV RANDOM_TEST='this_is_working'
ENV ANOTHER NOPE

# Make container directory for our code inside of Docker
RUN mkdir /code

# Set the container working directory to the one we just created
WORKDIR /code

# Copy all source files to container working directory
COPY . /code/

# Install dependencies. This will break if no requirements.txt
RUN pip install -r requirements.txt

# Migrate DB
CMD python3 manage.py migrate

# Start django server using port from Heroku
CMD python3 manage.py runserver 0.0.0.0:$PORT
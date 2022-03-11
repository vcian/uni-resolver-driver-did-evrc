# Use python 3.8-alpine light python base image for testing

FROM python:3.8

# Set myproject as working directory and add all files into it
#RUN mkdir /myproject
WORKDIR /evrc_method
ADD . /evrc_method

# Upgrade pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python","wsgi.py"]

# Define production command to be run when launching the container
# port = int(os.environ.get("PORT", 5000))
# CMD gunicorn app:app --bind 0.0.0.0:$PORT --reload
#BASE IMAGE
FROM python:3.14.0b4-slim

#Create a directory inside the container
WORKDIR /flaskapp

#Copy this application file,requirements.txt from my computer to container
COPY . /flaskapp/

#Run requirements.txt
RUN pip install -r requirements.txt

#Run the flask application
CMD ["python", "app.py"]
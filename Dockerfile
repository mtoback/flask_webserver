from python:3.7.7-slim
WORKDIR /home/app
COPY /angular/package.json /home/app/package.json
RUN apt-get update
RUN apt-get -y install curl gnupg libpq-dev python3-dev
RUN curl -sL https://deb.nodesource.com/setup_12.16  | bash -
RUN apt-get -y install nodejs

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH
RUN npm install
RUN npm install -g @angular/cli@9.1.1

# add app
COPY /angular/src/app /app

COPY templates templates
COPY hello.py hello.py
COPY requirements.txt requirements.txt
run pip install -r requirements.txt
ENV FLASK_APP=main.py
# start flask app
CMD ["flask", "run","--host=0.0.0.0"] 
# start angular app
CMD ng serve --host 0.0.0.0

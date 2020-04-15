from python:3.7.7-slim
COPY templates templates
COPY hello.py hello.py
COPY requirements.txt requirements.txt
run pip install -r requirements.txt
ENV FLASK_APP=hello.py
CMD ["flask", "run","--host=0.0.0.0"] 

from python:3.7.7-slim
WORKDIR /home/app

COPY requirements.txt requirements.txt
run pip install -r requirements.txt
COPY main.py main.py
COPY company_data.py company_data.py
COPY db_processing.py db_processing.py
COPY db_tables.py db_tables.py
COPY run_test.py run_test.py
COPY school_data.py school_data.py
COPY sqlalchemy_encoder.py sqlalchemy_encoder.py
COPY test_flask.py test_flask.py
ENV FLASK_APP=main.py
# start flask app
CMD ["flask", "run","--host=0.0.0.0"] 

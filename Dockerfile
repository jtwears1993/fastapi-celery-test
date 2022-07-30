ARG PYTHON_VERSION=3.10

FROM python:${PYTHON_VERSION}

ARG shared_workspace=/opt/workspace

# Set work directory
WORKDIR /


RUN apt-get update && apt-get install build-essential
RUN apt-get update && apt-get install curl

RUN pip install fastapi 
RUN pip install awswrangler
RUN pip install psycopg2-binary 
RUN pip install scikit-learn 
RUN pip install redis 
RUN pip install sqlalchemy
RUN pip install alembic
RUN pip install uvicorn
RUN pip install celery
RUN pip install flower
RUN pip install httpx


COPY . /app/

CMD uvicorn main:app --reload
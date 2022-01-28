FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

CMD python manage.py migrate && gunicorn --bind :8000 welltory_data_analysis.wsgi:application

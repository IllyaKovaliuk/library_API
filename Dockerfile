FROM python:3.9
ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /library

COPY requirements.txt /library/
RUN pip install -r requirements.txt

COPY . /library/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
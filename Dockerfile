FROM python:3.9

WORKDIR /app

RUN pip install flask requests

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
FROM python:3

RUN pip install flask
RUN pip install flask_restful
RUN pip install sympy

WORKDIR /app

COPY . .

EXPOSE 80

CMD ["python", "app/main.py"]

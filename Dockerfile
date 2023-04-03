FROM pypy:latest

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python", "semantic.py"]

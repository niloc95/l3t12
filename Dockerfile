FROM pypy:latest
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "semantic.py"]

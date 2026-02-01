FROM python:3.9
WORKDIR /webapp
COPY ./Docker-Python/req.txt ./
RUN pip install --no-cache-dir -r req.txt
COPY . .
EXPOSE 5000
CMD ["python", "python/main.py"]

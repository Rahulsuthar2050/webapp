FROM python:3.9
WORKDIR /webapp
RUN addgroup --system appgroup && adduser --system --group webapp
RUN apt-get update && apt-get install -y
COPY ./Docker-Python/req.txt ./
RUN pip install --no-cache-dir -r req.txt
COPY . .
RUN chown -R webapp:appgroup /webapp
EXPOSE 5000
CMD ["python", "python/main.py"]

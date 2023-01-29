FROM python:latest
WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY entrypoint.sh .
RUN sed -i 's/\r$//g' ./entrypoint.sh
RUN chmod +x ./entrypoint.sh
COPY . .
EXPOSE 8000
ENTRYPOINT ["/bin/bash","./entrypoint.sh"]

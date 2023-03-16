FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY fountain_to_audio.py .

RUN apt-get update && apt-get install -y ffmpeg

ENTRYPOINT ["python", "fountain_to_audio.py"]

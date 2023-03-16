FROM python:3.10

RUN apt-get update && \
    apt-get install -y \
    espeak-ng \
    libespeak-ng1 \
    libespeak-ng-dev \
    ffmpeg
    
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "fountain_parser.py" ]

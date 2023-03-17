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

RUN sed -i 's/translate.google.\\(.*\\)/translate.google.com/' /usr/local/lib/python3.10/site-packages/gtts/tts.py
RUN sed -i 's/tld = ".*"/tld = "com"/' /usr/local/lib/python3.10/site-packages/gtts/lang.py

COPY . .

CMD [ "python", "fountain_parser.py" ]

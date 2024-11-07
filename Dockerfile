FROM python:3.13.0 as builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/
COPY requirements.txt /app/
RUN python3 -m pip install --no-cache-dir --no-warn-script-location --user -r requirements.txt 

FROM python:3.13.0-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/
COPY --from=builder /root/.local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
RUN useradd summarybot -u 5323 -M --home "/app" -s /bin/false
USER summarybot
COPY --chown=summarybot:summarybot . .
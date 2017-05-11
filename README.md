
version: '2'
services:
  ssl-exporter:
    build: .
    ports:
      - 9188:9188
    environment:
      - BIND_PORT=9188
      - DOMAINS=google.com,microsoft.com

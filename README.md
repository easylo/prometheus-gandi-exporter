
```
version: '2'
services:
  gandi-exporter:
    build: .
    ports:
      - 9189:9189
    environment:
      - BIND_PORT=9189
      - API_KEY=YOUR_API_KEY_HERE
```
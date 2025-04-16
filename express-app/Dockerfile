# ADD CODE HERE
version: '3.8'

services:
  backstage:
    image: backstage/backstage
    container_name: backstage
    ports:
      - "4567:7007"
    volumes:
      - ./app-config.yaml:/app/app-config.yaml
      - ./plugins:/app/plugins
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - NODE_ENV=development
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    working_dir: /app
    command: yarn dev

  # Optional PostgreSQL container (Backstage needs a database for production)
  postgres:
    image: postgres:13
    container_name: backstage-db
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    volumes:
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres-data:

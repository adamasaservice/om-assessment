# ADD CODE HERE
version: '3.8'

services:
  app:
    build: .
    ports:
      - "4567:4567"  # Host:Container port mapping
    environment:
      - NODE_ENV=development
      - PORT=4567    # Ensure your app listens on this port
    volumes:
      - ./:/usr/src/app
      - /usr/src/app/node_modules  # Prevent host/node_modules overwrite
    restart: unless-stopped
    networks:
      - app-network

networks:
  app-network:
    driver: bridge

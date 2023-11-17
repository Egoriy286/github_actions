version: "3.1"

services:
  frontend:
    image: github_actions/frontend
    build:
      context: frontend
      dockerfile: ../frontend.Dockerfile

  backend:
    image: github_actions/backend
    build:
      context: backend
      dockerfile: ../backend.Dockerfile

volumes:
  frontend:
  backend:

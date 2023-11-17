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

  custom:
    build: ~/custom

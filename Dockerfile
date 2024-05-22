# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install Poetry
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root

# Copy the rest of the application code into the container
COPY . .

EXPOSE 4000

# Specify the command to run the application
# CMD ["poetry", "run", "python", "main.py", "--host=0.0.0.0", "--port=4000"]
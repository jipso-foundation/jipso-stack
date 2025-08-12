FROM jipsofoundation/jipso:base

WORKDIR /app

# Copy project files
COPY pyproject.toml poetry.lock ./
COPY jipso ./jipso

# Install project dependencies via poetry
RUN poetry install --no-root --extras "cloud" --only main

# Install CLI entrypoint (project code)
RUN poetry install --only-root

# Default command: jipso CLI
ENTRYPOINT ["poetry", "run", "jipso"]
CMD ["--help"]

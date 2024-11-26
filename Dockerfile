FROM python:3.10-slim

RUN pip3 install poetry

WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root
COPY src /app/src

CMD ["poetry", "run", "python3", "src/provider/app.py"]
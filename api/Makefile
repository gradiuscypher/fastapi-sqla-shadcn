.PHONY: api test lint fmt migrate upgrade downgrade stamp db-init
api:
	uv run uvicorn api:app --host 0.0.0.0 --port 8000 --reload

test:
	uv run pytest tests/ -vv

lint:
	uv run ruff check .

fmt:
	uv run ruff format .

migrate:
	uv run python -m alembic -c alembic.ini revision --autogenerate -m "$(m)"

upgrade:
	uv run python -m alembic -c alembic.ini upgrade head

downgrade:
	uv run python -m alembic -c alembic.ini downgrade -1

stamp:
	uv run python -m alembic -c alembic.ini stamp head

# Initialize Alembic with a temporary empty DB to capture full schema
db-init:
	ALEMBIC_URL=sqlite:///./.alembic_tmp.db uv run python -m alembic -c alembic.ini revision --autogenerate -m "initial schema"
run:
	python main.py
fmt:
	isort . && black .

lint:
	pre-commit run

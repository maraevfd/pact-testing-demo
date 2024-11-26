build:
	docker build -t pact-testing-provider .
run-app:
	docker run -d -p 5000:5000 --name pact-testing-provider pact-testing-provider
run-api-tests:
	poetry run python3 -m pytest -v tests/api_tests.py
run-pact-tests:
	poetry run python3 -m pytest -vv tests/pact_tests.py
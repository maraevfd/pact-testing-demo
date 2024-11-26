build:
	docker build -t pact-testing-provider .
run-app:
	docker run -d -p 5000:5000 --name pact-testing-provider pact-testing-provider
install-requirements:
	pip3 install -r requirements.txt

run-server:
	python3 server.py

lint:
	pep8 ./

test:
	py.test tests/

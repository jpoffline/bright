setup:
	python3 -m venv .venv
	pip install -r requirements.txt

activate:
	souce .venv/bin/activate

test:
	pytest bright/
setup:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

test:
	.venv/bin/python -m pytest bright/

run:
	.venv/bin/python main.py

clean: 
	rm -rf .venv
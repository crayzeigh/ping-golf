URL = "https://get.from.cockroachdb"

run: setup
	export DATABASE_URL="$(URL)"; \
	./venv/bin/python3 web.py

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

setup: venv/bin/activate

clean:
	rm -rf __pycache__
	rm -rf venv
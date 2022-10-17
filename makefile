URL = "https://get.from.cockroachdb"
ANYCAST_IP = "anycast_ip"

run: bird setup
	export DATABASE_URL="$(URL)"; \
	nohup ./venv/bin/python3 web.py &

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

/etc/bird/bird.conf:
	./scripts/create_bird_conf.sh $(ANYCAST_IP)

bird: /etc/bird/bird.conf

setup: venv/bin/activate

clean:
	rm -rf __pycache__
	rm -rf venv
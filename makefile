init:
	conda create -n awx-automation
	source activate awx-automation
	pip3 install --upgrade pip3 setuptools wheel
	pip3 install -r requirements.txt

exec-transferwise:
	source activate awx-automation
	python3 src/scrape_transferwise.py
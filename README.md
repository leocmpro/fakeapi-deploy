# Fake API

Fake API REST for test load-balancing using Nginx

## Setup

```bash
python -m venv pyenv
source pyenv/bin/activate

pip install -r requirements.txt
```

## Run

```bash
# for development
python fakeapi.py

# for production
gunicorn -w 1 -k eventlet -b 0.0.0.0:<port> fakeapi:app
```

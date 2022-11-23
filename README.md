# Week 5 Assignment

This is an assignment for Week 5 of Software Architect and Design (CPSC-61200)

Work by **Satshree Shrestha** *(L30063661)*

# API

Access these APIs from the browser

- Index HTML Template
```
http://<root>/ [GET]
```

- JSON message
```
http://<root>/hello/ [GET]
```

# Instructions

1. Virtual Environment
```bash
python3 -m venv env # this is only for first time
```
```bash
source ./env/bin/activate
```

2. Install dependencies (this step is only for first time)
```bash
pip install --upgrade pip 
```
```bash
pip install -r requirements.txt 
```

3. Start server
```bash
python manage.py runserver
```
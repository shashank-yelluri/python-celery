# python-celery

## Commands
- celery -A tasks worker --loglevel=INFO
- python3 -m uvicorn main:app --reload

## Description
We are defined one task and made use of fastAPI to create two routes, one which works with celery and one without. 

# rsort

rsort is a Python utility to sort requirements alphabetically, considering manual grouping and comments

## Example
```bash
rsort.py ./requirements.txt
```

source
```
pymysql==0.9.3
lxml==4.4.1

# celery
celery-flower==1.0.1
celery==4.3.0

# tests
pytest-mock==1.10.4
black==19.3b0
pytest-cov==2.7.1
pytest==5.0.0
```

result
```
lxml==4.4.1
pymysql==0.9.3

# celery
celery==4.3.0
celery-flower==1.0.1

# tests
black==19.3b0
pytest==5.0.0
pytest-cov==2.7.1
pytest-mock==1.10.4
```

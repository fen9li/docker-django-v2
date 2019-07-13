# changelog001

Change backend database to mariadb

## add 'mysqlclient' as mysql connector to requirements.txt

```
feng@ubuntu:~/docker-django-v2$ cat requirements.txt 
Django>=2.0,<3.0
mysqlclient
feng@ubuntu:~/docker-django-v2$ 
``` 

## update docker-compose.yml

```
feng@ubuntu:~/docker-django-v2$ cat docker-compose.yml 
version: '3'

services:
  db:
    image: mariadb:10.3
    restart: on-failure
    volumes:
      - koala:/var/lib/mysql
    ports:
      - 3306:3306
    expose:
      - 3306
    environment:
      MYSQL_DATABASE: koala
      MYSQL_USER: koalauser
      MYSQL_PASSWORD: password
      MYSQL_ROOT_PASSWORD: password
    networks:
      - backend
  web:
    build: .
    restart: on-failure
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - 8000:8000
    networks:
      - backend
    depends_on:
      - dbmysqlclient
    
volumes:
  koala:
networks:
  backend:
feng@ubuntu:~/docker-django-v2$ 
```

## update 'koala/settings.py'

```
feng@ubuntu:~/docker-django-v2$ sed -n '73,85p' koala/settings.py 
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'koala',
        'USER': 'koalauser',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': 3306,
    }
}
feng@ubuntu:~/docker-django-v2$ 
```

## connect to mariadb in container

After running docker-compose up -d, you should be able to connect to the database, but using 127.0.0.1 as host. 

```
docker-compose down
docker-compose up -d --build

feng@ubuntu:~/docker-django-v2$ mysql -h 127.0.0.1 -P 3306 -u koalauser -p -D koala
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 8
Server version: 10.3.16-MariaDB-1:10.3.16+maria~bionic mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [koala]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| koala              |
+--------------------+
2 rows in set (0.001 sec)

MariaDB [koala]> quit
Bye
feng@ubuntu:~/docker-django-v2$ 

```
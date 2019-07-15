

## run test

* clean up remaining db container after running the test

```
feng@ubuntu:~/docker-django-v2$ sudo docker-compose run web python manage.py test
Creating network "docker-django-v2_backend" with the default driver
Creating docker-django-v2_db_1 ... done
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.097s

OK
Destroying test database for alias 'default'...
feng@ubuntu:~/docker-django-v2$ 

feng@ubuntu:~/docker-django-v2$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
8135656278d6        mariadb:10.3        "docker-entrypoint.s…"   2 minutes ago       Up 2 minutes        0.0.0.0:3306->3306/tcp   docker-django-v2_db_1
feng@ubuntu:~/docker-django-v2$
```
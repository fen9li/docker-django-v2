
## add person, role models 

```
feng@ubuntu:~/docker-django-v2$ sudo docker-compose run web python manage.py makemigrations home
Starting docker-django-v2_db_1 ... done
Migrations for 'home':
  home/migrations/0002_auto_20190715_0033.py
    - Create model Person
    - Change Meta options on movie
    - Create model Role
    - Add field actors to movie
    - Add field director to movie
    - Add field writers to movie
feng@ubuntu:~/docker-django-v2$ 

feng@ubuntu:~/docker-django-v2$ sudo docker-compose run web python manage.py migrate home
Starting docker-django-v2_db_1 ... done
Operations to perform:
  Apply all migrations: home
Running migrations:
  Applying home.0002_auto_20190715_0033... OK
feng@ubuntu:~/docker-django-v2$ 
```

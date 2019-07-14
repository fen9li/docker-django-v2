# make model, migrations and migrate

## the 'home/models.py'

feng@ubuntu:~/docker-django-v2$ cat home/models.py 
from django.db import models

/# Create your models here.
```
class Movie(models.Model):
    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_R = 3
    RATINGS = (
        (NOT_RATED, 'NR - Not Rated'),
        (RATED_G,
        'G - General Audiences'),
        (RATED_PG,
        'PG - Parental Guidance Suggested'),
        (RATED_R,
        'R - Restricted'),
    )

    title = models.CharField(max_length=140)
    plot = models.CharField(max_length=140)
    year = models.PositiveIntegerField()
    rating = models.PositiveIntegerField(
        choices=RATINGS,
        default=NOT_RATED    )
    runtime = models.PositiveIntegerField()
    website = models.URLField(blank=True)

    def __str__(self):
        return '{} ({})'.format(self.title, self.year)
feng@ubuntu:~/docker-django-v2$ 
```

## make migrations and migrate

```
feng@ubuntu:~/docker-django-v2$ sudo docker-compose run web python manage.py makemigrations home
Starting docker-django-v2_db_1 ... done
Migrations for 'home':
  home/migrations/0001_initial.py
    - Create model Movie
feng@ubuntu:~/docker-django-v2$ sudo docker-compose run web python manage.py migrate home
Starting docker-django-v2_db_1 ... done
Operations to perform:
  Apply all migrations: home
Running migrations:
  Applying home.0001_initial... OK
feng@ubuntu:~/docker-django-v2$ 
```

## double check koala database

```
feng@ubuntu:~/docker-django-v2$ mysql -h 127.0.0.1 -P 3306 -u koalauser -p -D koala
Enter password: 
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 20
Server version: 10.3.16-MariaDB-1:10.3.16+maria~bionic mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [koala]> show tables;
+----------------------------+
| Tables_in_koala            |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
| home_movie                 |
+----------------------------+
11 rows in set (0.002 sec)

MariaDB [koala]> describe home_movie;
+---------+------------------+------+-----+---------+----------------+
| Field   | Type             | Null | Key | Default | Extra          |
+---------+------------------+------+-----+---------+----------------+
| id      | int(11)          | NO   | PRI | NULL    | auto_increment |
| title   | varchar(140)     | NO   |     | NULL    |                |
| plot    | varchar(140)     | NO   |     | NULL    |                |
| year    | int(10) unsigned | NO   |     | NULL    |                |
| rating  | int(10) unsigned | NO   |     | NULL    |                |
| runtime | int(10) unsigned | NO   |     | NULL    |                |
| website | varchar(200)     | NO   |     | NULL    |                |
+---------+------------------+------+-----+---------+----------------+
7 rows in set (0.042 sec)

MariaDB [koala]> quit;
Bye
feng@ubuntu:~/docker-django-v2$ 
```
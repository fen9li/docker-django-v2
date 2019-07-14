# start new app home

## how to do it

```
feng@ubuntu:~/docker-django-v2$ pwd
/home/feng/docker-django-v2
feng@ubuntu:~/docker-django-v2$ 

feng@ubuntu:~/docker-django-v2$ git checkout -b develop
Switched to a new branch 'develop'
feng@ubuntu:~/docker-django-v2$ git status
On branch develop
nothing to commit, working tree clean
feng@ubuntu:~/docker-django-v2$

feng@ubuntu:~/docker-django-v2$ docker-compose up -d
Creating network "docker-django-v2_backend" with the default driver
Creating docker-django-v2_db_1 ... done
Creating docker-django-v2_web_1 ... done
feng@ubuntu:~/docker-django-v2$ 

feng@ubuntu:~/docker-django-v2$ docker container ls
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS                    NAMES
5c150ffdb017        docker-django-v2_web   "python manage.py ru…"   13 minutes ago      Up 13 minutes       0.0.0.0:8000->8000/tcp   docker-django-v2_web_1
a5bec241133a        mariadb:10.3           "docker-entrypoint.s…"   13 minutes ago      Up 13 minutes       0.0.0.0:3306->3306/tcp   docker-django-v2_db_1
feng@ubuntu:~/docker-django-v2$ docker container exec -it 5c15 sh
# pwd
/code
# ls
Dockerfile  README.md  changelogs  docker-compose.yml  images  koala  manage.py  requirements.txt
# exit
feng@ubuntu:~/docker-django-v2$ 

feng@ubuntu:~/docker-django-v2$ sudo docker-compose run web python manage.py startapp home
[sudo] password for feng: 
Starting docker-django-v2_db_1 ... done
feng@ubuntu:~/docker-django-v2$ 

feng@ubuntu:~/docker-django-v2$ sudo chown -R $USER:$USER home
feng@ubuntu:~/docker-django-v2$ ls -la | grep home
drwxr-xr-x  3 feng feng 4096 Jul 14 11:24 home
feng@ubuntu:~/docker-django-v2$  
```

## git housekeeping

```
feng@ubuntu:~/docker-django-v2$ git status
On branch develop
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   koala/urls.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        changelogs/changelog002-home.md
        home/

no changes added to commit (use "git add" and/or "git commit -a")
feng@ubuntu:~/docker-django-v2$ 

git add .
git commit -am "Changelog002 add home app"
git push --set-upstream origin develop

feng@ubuntu:~/docker-django-v2$ 
```
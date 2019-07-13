# [Sample Application] (https://docs.docker.com/compose/django/)

WARNING: Image for service web was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.

## git housekeeping

### create new repo in github and extract git_url

```
feng@ubuntu:~/docker-django-v2$ curl -u 'fen9li' https://api.github.com/user/repos -d '{"name":"docker-django-v2"}' | jq '.ssh_url'
Enter host password for user 'fen9li':
"git@github.com:fen9li/docker-django-v2.git"
feng@ubuntu:~/docker-django-v2$ 
```

### git commands 
```
git init
git remote add origin git@github.com:fen9li/docker-django-v2.git

feng@ubuntu:~/docker-django-v2$ git remote -v
origin  git@github.com:fen9li/docker-django-v2.git (fetch)
origin  git@github.com:fen9li/docker-django-v2.git (push)
feng@ubuntu:~/docker-django-v2$ 

git add Dockerfile README.md requirements.txt docker-compose.yml 
git commit -am "Initial commit"

feng@ubuntu:~/docker-django-v2$ git push --set-upstream origin master
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 1.97 KiB | 1007.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To github.com:fen9li/docker-django-v2.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
feng@ubuntu:~/docker-django-v2$
```
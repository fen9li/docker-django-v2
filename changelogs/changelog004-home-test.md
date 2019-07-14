# create 1st test for home app

## test homepage view

```
feng@ubuntu:~/docker-django-v2$ cat home/tests.py 
from django.test import TestCase

# Create your tests here.

class HomepageViewTests(TestCase):
    def test_homepage_view(self):
        """
        homepage view
        Hello, world. You're at home.
        """
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "at home")
feng@ubuntu:~/docker-django-v2$  
```

## run test

```
feng@ubuntu:~/docker-django-v2$ sudo docker-compose run web python manage.py test
Starting docker-django-v2_db_1 ... done
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.010s

OK
Destroying test database for alias 'default'...
feng@ubuntu:~/docker-django-v2$ 
```
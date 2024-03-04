# django-with-docker

RUN AND BUILD

```bash
docker-compose up
docker-compose up -d
docker-compose up --build
docker-compose up --build --force-recreate
```

LIST IMAGES OR REMOVE IMAGE

```bash
docker image ls
dockerr rmi <id>
```

LIST CONTAINERS

```bash
docker container ps
```

CLOSE

```bash
docker-compose down
```

RUN CODE PYTHON

```bash
docker-compose run djangoapp python manage.py startapp blog
```

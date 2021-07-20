### python-webserver

A python webserver in a docker container

#### Building the image

```bash
$ docker build -t python-webserver .
```

#### Running the container

```
$ docker run -dp 4000:4000 python-webserver
```

#### Sample usage

```
> curl -X POST http://localhost:4000/set?a=b
{
  "a": "b"
}

> curl http://localhost:4000/get?key=a
a = b

> curl -X DELETE http://localhost:4000/remove?key=a
{}
```

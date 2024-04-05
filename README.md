## Docker

Build

```shell
docker -H "ssh://rpi@192.168.1.222" build -t vadviktor.xyz/aws-workmail-aliases:1.0.0 -f Dockerfile .
```

Run

```shell
docker \
  -H "ssh://rpi@192.168.1.222" \
  run \
  --detach \
  --name aws-workmail-aliases \
  --restart=always \
  -p 0.0.0.0:3010:8080/tcp \
  vadviktor.xyz/aws-workmail-aliases:1.0.0 \
  waitress-serve --no-ipv6 app:app
```

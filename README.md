## Docker

```shell
docker -H "ssh://rpi@192.168.1.222" build -t vadviktor.xyz/aws-workmail-aliases:1.0.0 -f Dockerfile .
```

```shell
docker \
  -H "ssh://rpi@192.168.1.222" \
  run \
  --detach \
  --name aws-workmail-aliases \
  --network rpi-services \
  --restart=always \
  -p 0.0.0.0:3010:8080/tcp \
  -e FLASK_SECRET_KEY="" \
  -e AWS_ORG_ID="" \
  -e AWS_USER_ID="" \
  -e AWS_REGION_GLOBAL="us-east-1" \
  -e AWS_ACCESS_KEY_ID="" \
  -e AWS_SECRET_ACCESS_KEY="" \
  -e AWS_DEFAULT_REGION="eu-west-1" \
  vadviktor.xyz/aws-workmail-aliases:1.0.0 \
  waitress-serve --no-ipv6 app:app
```
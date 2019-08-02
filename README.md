# docker-etcd

### start a single node etcd

## pre-requirements

- Centos 7
- docker 18.09 with docker swarm

## create etcd-data

```bash
mkdir ./default.etcd
```

## deploy_127.0.0.1.sh

```bash
docker-compose up -d etcd-127_0_0_1
```

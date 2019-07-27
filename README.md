# docker-etcd

## pre-requirements

- Centos 7
- docker 18.09 with docker swarm

## create etcd-data

```bash
mkdir /tmp/etcd-data
```

## create_etcd.sh

```bash
docker service create \
  --publish 2379:2379 \
  --publish 2380:2380 \
  --mount type=bind,source=/tmp/etcd-data.tmp,destination=/etcd-data \
  --name etcdv3 \
  quay.io/coreos/etcd:v3.3.13 \
  /usr/local/bin/etcd \
  --name s1 \
  --data-dir /etcd-data \
  --listen-client-urls http://0.0.0.0:2379 \
  --advertise-client-urls http://0.0.0.0:2379 \
  --listen-peer-urls http://0.0.0.0:2380 \
  --initial-advertise-peer-urls http://0.0.0.0:2380 \
  --initial-cluster s1=http://0.0.0.0:2380 \
  --initial-cluster-token tkn \
  --initial-cluster-state new
```

import etcd3
import json


client = etcd3.client(
    host='127.0.0.1',
    port=2379
)

service_name = 'user.srv'
results = client.get_prefix('/micro-registry/' + service_name)
for result, md in results:
    service_info = json.loads(result.decode('utf-8'))

    # print(service_info['name'])
    # print(service_info['version'])
    # print(services['endpoints'])
    # print(service_info['nodes'])

    nodes_info = service_info['nodes']
    for node_info in nodes_info:
        print(json.dumps(node_info, indent=4))
        break

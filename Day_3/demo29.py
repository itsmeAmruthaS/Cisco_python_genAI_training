
import pprint

network_params = {}

with open('network.cfg','r') as fobj:
    for var in fobj.readlines():
        var = var.strip()
        K,V = var.split('=')
        network_params[K] = V



pprint.pprint(network_params)

network_params['Interface'] = 'eth1'
network_params['bootproto'] = 'static'
network_params['onboot'] = 'yes'
network_params['IPADD'] = '192.168.1.10'
network_params['PREFIX'] = 24
network_params['DNS1'] = '122.33.344.555'

print('\nupd dict details')
pprint.pprint(network_params)

with open('new network.cfg', 'w') as wobj:
    for var in network_params:
        wobj.write(f'{var}={network_params[var]}\n')

import pprint
prod = {}
prod['id'] = [101, 102, 103]
prod['names'] = ['pA', 'pB', 'pC']
prod['cost'] = [1000, 2000, 3000]
prod['qty'] = [10, 20, 30]
pprint.pprint(prod)

print('\n')

prod = []
prod.append({'id': 101, 'names': 'pA', 'cost': 1000, 'qty': 10})
prod.append({'id': 102, 'names': 'pB', 'cost': 2000, 'qty': 20})
prod.append({'id': 103, 'names': 'pC', 'cost': 3000, 'qty': 30})

pprint.pprint(prod)

print('\n')

prod = {}
prod['id'] = {'id1':101, 'id2':102, 'id3':103}
prod['names'] = {'name1':'pA', 'name2':'pB', 'name3':'pC'}
prod['cost'] = {'cost1':1000, 'cost2':2000, 'cost3':3000}
prod['qty'] = {'qty1':10, 'qty2':20, 'qty3':30}
pprint.pprint(prod)

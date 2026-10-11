
hosts = {}
print(f"number of elements in dict: {len(hosts)}")

cnt = 0
while(cnt < 5):
    h = input("Enter host name: ")
    ip = input("Enter IP address: ")
    hosts[h] = ip
    cnt += 1

print(f"number of elements in dict: {len(hosts)}")

for var in hosts:
    print(f"Host name: {var}\t IP address: {hosts[var]}")

h = input("Enter host name: ")
if h in hosts:
    hosts[h] = "127.0.0.1"
   
else:
    print("sorry hostname {h} doesn't exist")
    hosts[h] = "127.0.0.1"
    print("upd dict")

for var in hosts:
    print(f"Host name: {var}\t IP address: {hosts[var]}")
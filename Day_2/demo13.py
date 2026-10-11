
hosts = []
print(f"Number of elements in the list:{len(hosts)}")

c = 0
while c < 5:
    h = input("enter hostname:")
    hosts.append(h)
    c += 1

print(f"\nNumber of elements in the list:{len(hosts)}")

for var in hosts:
    print(var)

host_name = input("enter hostname:")
if host_name in hosts:
    hosts[-1] = host_name
else:
    hosts.append(host_name)

print("\n")
for var in hosts:
    print(var)
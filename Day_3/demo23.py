
import time

devices = ["switches", "routers", "ethernet", "rs232"]
config = {'ID' : 'A-123', 'app': 'demoApp', 'port': 3030, 'fname': '/etc/app.cfg'}

wobj = open("r2.log", "w")
for var in devices:
    wobj.write(f"device name: {var}\n")

wobj.write("----done----\n")


for var in config:
    wobj.write(f"{var} : {config[var]}\n")

wobj.write("----done----\n")
wobj.write(f"created on: {time.ctime()}\n")
wobj.close()

port = input('enter port number:')

if int(port) > 5000 and int(port) < 6000:
    app_name = "flask"
else:
    app_name = "webapp"

print(f"app name is :{app_name} running port number is :{port}")
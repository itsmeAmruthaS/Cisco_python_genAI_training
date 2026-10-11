

app_name = input('enter app name:')

if(app_name == "flask"):
    port = 5000
elif(app_name== "fastapi"):
    port = 8080
elif (app_name == 'promotheus'):
    port = 9090
else:
    app_name = 'web2.0'
    port = 8000

print(f"app name is :{app_name} running port number is :{port}")


pin = 1234
cnt = 0
while(cnt < 3):
    user_pin = int(input("enter your pin:"))
    cnt += 1
    if(user_pin == pin):
        print(f"pin is valid - cnt is : {cnt}")
        break

if pin != user_pin:
    print("pin blocked")

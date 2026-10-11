import time

def pin_test():
    fobj = open('pin_history.log', "a")
    pin = 1234
    cnt = 0

    while(cnt < 3):
        p = input('enter pin num')
        cnt += 1
        if (int(p) == pin):
            print(f'success - {cnt}')
            fobj.write(f'success - {cnt} pin input date/time:{time.ctime()}\n')
            break
        else:
            fobj.write(f"failed - user input:{p} date/time:{time.ctime()}\n")

    if (int(p) != pin):
        print('pin blocked')
        fobj.write(f'pin blocked - {time.ctime()}\n')
    fobj.close()

pin_test()
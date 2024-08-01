import datetime

while True:
    second_before = datetime.datetime.now().second
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    diference = 0
    while diference <= 1:
        second_after = datetime.datetime.now().second + 1
        diference = second_after - second_before
        if diference <= -1:
            diference = 2
    print("\n"*140)
    print(f"{hour}:{minute}:{second_before}")

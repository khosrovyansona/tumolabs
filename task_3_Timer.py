import time 

hour = input('Insert an hour: ')
minute = input('Insert a minute: ')
second = input('Insert a second: ')

while True:
    if not (hour.isdigit() and minute.isdigit() and second.isdigit()):
        print("All inputs must be numbers. Please try again.")
    else:
        hour = int(hour)
        minute = int(minute)
        second = int(second)

        if not (0 <= hour <= 23) or not (0 <= minute <= 59) or not (0 <= second <= 59):
            print("Invalid time! Hour must be 0-23, minute and second 0-59. Please try again.")
        else:
            break  

    hour = input('Insert an hour: ')
    minute = input('Insert a minute: ')
    second = input('Insert a second: ')

while hour >- 1:
    for i in range(minute,-1,-1):
        for j in range(second,-1,-1):
            if hour<10:
                if i<10:
                    if j<10:
                        print(f'0{hour}:0{i}:0{j}')   
                    else:
                        print(f'0{hour}:0{i}:{j}') 
                elif j<10:
                    if i>10:
                        print(f'0{hour}:{i}:0{j}') 
            elif hour>10:
                if i<10:
                    if j<10:
                        print(f'{hour}:0{i}:0{j}')   
                    else:
                        print(f'{hour}:0{i}:{j}') 
                elif j<10:
                    if i>10:
                        print(f'{hour}:{i}:0{j}') 

            time.sleep(1)

        second = 59

    hour-=1
    minute = 59


import time

hour = int(input('Insert an hour: '))
minute = int(input('Insert an minute: '))
second = int(input('Insert an second: '))


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



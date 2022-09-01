# import time
# hour = 0
# while hour < 24:
#     minute = 0
#     while minute < 60:
#         second = 0
#         while second < 60:
#             time.sleep(1)
#             current_time = f'Time Elapsed: {hour:0>2} : {minute:0>2} : {second:0>2}'
#             print(current_time, end='\r')
#             second += 1
#         minute += 1
#     hour += 1
import time
print('Count Down Timer')
minute = int(input('Enter time out (Minutes): '))-1
while minute >= 0:
    second = 59
    while second >= 0:
        ms = 99
        while ms >= 0:
            time.sleep(0.01)
            current_time = f'\rTime Elapsed: {minute:0>2} : {second:0>2} : {ms:0>2}'
            print(current_time, end='')
            ms -= 1
        second -= 1
    minute -= 1
print('\nTime Up !!')

import argparse
from time import sleep, strftime, gmtime
from datetime import timedelta, datetime

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first-name', required=True)
    parser.add_argument('-ln', '--last-name', required=True)
    parser.add_argument('-hr', '--hours', required=True)
    parser.add_argument('-m', '--minutes', required=True)
    parser.add_argument('-s', '--seconds', required=True)
    args = parser.parse_args()

    result_time = timedelta(hours=int(args.hours), minutes=int(args.minutes), seconds=int(args.seconds))
    total_seconds = result_time.total_seconds()
    current_time = datetime.now()

    with open('log.txt', 'a+') as file:
        file.write(f'User - {args.first_name}\t{args.last_name}.\n'
                   f'{current_time.strftime("%x %H:%M:%S")}\n')

    while total_seconds:
        print(strftime('%H:%M:%S', gmtime(total_seconds)))
        total_seconds -= 1
        sleep(1)



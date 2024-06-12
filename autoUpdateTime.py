import os
import requests
import subprocess
from datetime import datetime, timezone
import platform

def get_current_time():
    try:

        response= requests.get('http://worldtime.org/api/ip')
        response.raise_for_status()
        data = response.json()

        utc_datetime= datetime.fromisoformat(data['utc_datetime'].rstrip('z')).replace(tzinfo=timezone.utc)

        local_datetime= utc_datetime.astimezone()
        return local_datetime

    except requests.RequestException as e:

        print(f"Error fetching time: {e}")
        return none

    except KeyError as e:

        print(f"Unexpected API response structure: {e}")
        return none

    except ValueError as e:

        print(f"Error passing datetime: {e}")
        return none

def set_system_time(new_datetime):
    try:

        if platform.system()=='windows':

            time_format= new_datetime.strftime('%H:%M:%S')
            date_format= new_datetime.strftime('%m-%d-%y')

            os.system(f'time{time_format}')
            os.system(f'date{date_format}')

        elif platform.system()=='Linux' or platform.system()=='Darwin':

            time_str= new_datetime.strftime('%m%d%H%M%Y.%S')

            subprocess.call(['sudo','date',time_str])

        else:
            print("Unsupported OS")

    except Exception as e:

        print(f"Error setting system time: {e}")

def main():

    current_time= get_current_time()

    if current_time:
        print(f"Current Internet Time: {current_time} ")
        set_system_time(current_time)
        print("System time Updated successfully.")
    else:
        print("Failed to get current time.")

if __name__=="__main__":
    main()






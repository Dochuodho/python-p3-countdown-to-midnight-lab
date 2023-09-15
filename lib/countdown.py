# your code goes here!
import time
def countdown(count):
    while count > 0:
        print(f"{count} SECONDS(S)!")
        count -=1
    print()
        
countdown(10)

def countdown_with_sleep(count):
    while count > 0:
        print(f"{count} SECONDS(S)!")
        time.sleep(1)
        count -=1
    print("HAPPY NEW YEAR!")
countdown_with_sleep(10)


import time
seconds=int(input("Enter time in number of seconds"))
def count_timer(seconds) :
    while (seconds>0):
        mins=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{mins}:{secs}'
        print(timer,end='\r')
        time.sleep(1)
        seconds -=1
    print("timeup")

    
    

count_timer(seconds)

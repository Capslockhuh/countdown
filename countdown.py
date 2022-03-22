# countdown.py - counts down and plays an audio file

import time, subprocess

print('How long do you want your countdown to be? (seconds)')
countTime = input()

timeLeft = int(countTime)
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1
from pygame import mixer
import time


def sound():
    mixer.init()
    mixer.music.load('C:/Users/LENOVO\PycharmProjects\OTPSystem\carol_of_the_bells-alarm.mp3')


def alarm():
    hour = int(input("Enter the hour-"))
    minutes = int(input("Enter the minutes-"))
    seconds = int(input("Enter the seconds-"))

    n = 4

    print('Alarm set for' + str(hour) + str(minutes) + str(seconds))
    while True:
        if time.localtime().tm_hour == hour and time.localtime().tm_min == minutes and time.localtime().tm_sec == seconds:
            print("Wake Up!")
            break

    sound()
    while n > 0:
        mixer.music.play()
        time.sleep(2)

        sn = str(input('Snooze!'))
        if sn == 's':
            n = 3
            time.sleep(100)
        while n > 0:
            mixer.music.play()
            time.sleep(2)
        else:
            exit()

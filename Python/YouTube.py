import random
import webbrowser
import datetime
import time


def choose_video_link():
    input_file=open("links.txt","r")
    emp=""
    lst_links=[]
    line=input_file.readline()
    while line!=emp:
        lst_links.append(line)
        line=input_file.readline()
    random_video=random.choice(lst_links)
    return random_video       #returns a random youtube video


def play_video(link):
    webbrowser.open(link)   #open the link in a new tab


def check_alarm_time(time):
    if len(time)==1:
        if time[0]>=0 and time[0]<=24:
            return True
    elif len(time)==2:
        if time[0]>=0 and time[0]<=24 and time[1]>=0 and time[1]<=60:
            return True
    elif len(time)==3:
        if time[0]>=0 and time[0]<=24 and time[1]>=0 and time[1]<=60 and time[2]>=0 and time[2]<=60:
            return True
    return False


def enter_time():
    alarm_time=input("Set the time for alaram to go off : ").split(":")
    for i in range(len(alarm_time)):
        while not alarm_time[i].isdigit():
            print("ERROR:Enter only colon separated numerical values .")
            alarm_time=input("Set the time for alaram to go off: ").split(":")
    return alarm_time

alaram_time=enter_time()
for i in range(len(alaram_time)):
    n=int(alaram_time[i])
    alaram_time[i]=n

while not check_alarm_time(alaram_time):
    print("ERROR:Enter in proper format i.e HH:MM or HH:MM:SS. ")
    enter_time()
    break


def in_seconds(time_lst):
    if len(time_lst)==1:
        return time_lst[0]*3600
    elif len(time_lst)==2:
        return (time_lst[0]*3600+time_lst[1]*60)
    elif len(time_lst)==3:
        return (time_lst[0]*3600+time_lst[1]*60+time_lst[2])


second_h_m_s=[3600,60,1]

now=datetime.datetime.now()
total_seconds=in_seconds(alaram_time)   #time in seconds i.e for which alarm is set

current_time_seconds=sum([a*b for a,b in zip(second_h_m_s, [now.hour,now.minute,now.second])])



time_diff=total_seconds-current_time_seconds

if time_diff<0:
    time_diff+=86400
    print("Alaram is set for Tomorrow!!!!")
    print("The alaram will go off in ",time_diff," seconds !!")
    time.sleep(time_diff)
    print("Wake Up...Video launching in 3...2...1..Goooo....")
    time.sleep(4)
    url=choose_video_link()
    play_video(url)





else:
    print("The alaram is SET!!! ")
    print("The alaram will go off in ",time_diff," seconds !!")
    time.sleep(time_diff)
    print("Wake Up...Video launching in 3...2...1..Goooo....")
    time.sleep(4)
    url=choose_video_link()
    play_video(url)

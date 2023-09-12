import re

def time_to_minute(time):
    # re로 해보기
    #p = re.compile("[d]")
    return int(time[:2])* 60 + int(time[3:])




def solution(n, t, m, timetable):
    answer = ''
    time_table_in_minutes = []
    for time in timetable:
        time_table_in_minutes.append(time_to_minute(time))



    return answer
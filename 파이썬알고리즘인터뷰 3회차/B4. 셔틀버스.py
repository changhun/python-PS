import re

def time_to_minute(time):
    # index 와 re 두가지 방법으로 해보기
    #p = re.compile("[d]")
    return int(time[:2])* 60 + int(time[3:])


def minute_to_time(minutes):
    h = minutes // 60
    m = minutes % 60
    hh = str(h).zfill(2)
    mm = str(m).zfill(2)
    return hh + ":" + mm


def solution(n, t, m, timetable):
    time_table_in_minutes = []
    for time in timetable:
        time_table_in_minutes.append(time_to_minute(time))
    # print(time_table_in_minutes)
    # for minutes in time_table_in_minutes:
    #     print(minute_to_time(minutes))

    time_table_in_minutes.sort()
    pi = mi = 0
    bus_time = time_to_minute("09:00")

    for ni in range(n):
        mi = 0
        while pi < len(timetable) and mi < m and time_table_in_minutes[pi] <= bus_time:
            pi += 1
            mi += 1
        if pi == len(timetable):
            break
        bus_time += t

    #if (pi == len(timetable) and ni < n and mi < m) or pi == 0:
    if (ni < n and mi < m) or pi == 0:
        return minute_to_time(time_to_minute("09:00") + (n-1)*t)

    return minute_to_time(time_table_in_minutes[pi-1] - 1)

n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]

n = 3
t = 1
m = 2
timetable = ["06:00", "23:59", "05:48", "00:01", "00:01"]
ret = solution(n, t, m, timetable)
print(ret)

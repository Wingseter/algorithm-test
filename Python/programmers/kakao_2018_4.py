def str_to_minute(time):
    return 60 * int(time[:2]) + int(time[3:])

def minute_to_str(minute):
    return "{0:02d}".format(int(minute / 60)) + ":" + "{0:02d}".format(minute % 60)

def solution(n, t, m, timetable):
    answer = ''
    
    time_default = str_to_minute("09:00")
    converted_time = [str_to_minute(time) for time in timetable]
    converted_time.sort()
    
    buss = [list() for _ in range(n)]
    
    if n == 1:
        answer = "09:00"
    
    time_now = time_default
    target = converted_time.pop(0)
    for bus in buss:
        counter = 0
        
        while target < time_now + t and counter < m:
            bus.append(target)
            counter += 1 
            if counter == m:
                break
            elif len(converted_time) != 0:
                target = converted_time.pop(0)
    print(buss)
    return answer

solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])
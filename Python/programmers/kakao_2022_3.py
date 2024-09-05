import collections, math

def solution(fees, records):
    answer = []
    #[0]: last time [1] last action
    car_check_dict = collections.defaultdict(int)
    inout_check_dict = collections.defaultdict(str)
    time_check_dict = collections.defaultdict(int)

    def str_to_time(time):
        return int(time[:2]) * 60 + int(time[3:])

    # calc total time
    for record in records:
        time, car_num, action = record.split()

        conv_time = str_to_time(time)
        
        if action == "IN":
            car_check_dict[car_num] = conv_time
            inout_check_dict[car_num] = "IN"
        else: # out
            time_check_dict[car_num] += conv_time - car_check_dict[car_num]
            inout_check_dict[car_num] = "OUT"
    
    # calc if car not go out
    for key in car_check_dict.keys():
        max_time = str_to_time("23:59")

        if inout_check_dict[key] == "IN":
            time_check_dict[key] += max_time - car_check_dict[key]
    
    def calc_fees(time):
        fee = 0
        basic_time = fees[0]
        basic_money = fees[1]
        part_time = fees[2]
        part_money = fees[3]
        
        if time < basic_time:
            fee = basic_money
            return fee
        else:
            return basic_money + math.ceil((time - basic_time) / part_time) * part_money
    
    times = []
    # total time list from lower carNum
    for key in sorted(time_check_dict.keys()):
        times.append(time_check_dict[key])

    for time in times:
        answer.append(calc_fees(time))

    return answer

solution([], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
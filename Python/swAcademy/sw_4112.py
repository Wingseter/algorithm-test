import sys
sys.stdin = open('sample_input.txt', "r")

T = int(input())

for test_case in range(1, T + 1):
    start, end = map(int, input().split())

    if start == end:
        answer = 0
    else:
        if start > end:
            end, start = start, end

        start_pos = None
        end_pos = None

        # initialize
        flore = 1
        flore_start_num = 1
        flore_end_num = 1
        # find position
        while start_pos is None or end_pos is None:
            if flore_start_num <= start <= flore_end_num:
                start_pos = (flore, start - flore_start_num + 1)
            if flore_start_num <= end <= flore_end_num:
                end_pos = (flore, end - flore_start_num + 1)
            flore_start_num += flore 
            flore += 1
            flore_end_num = flore_start_num + flore - 1
        
        # find result
        # add height
        answer = end_pos[0] - start_pos[0]

        if end_pos[1] >= start_pos[1]:
            answer += max(0, (end_pos[1] - start_pos[1]) - (end_pos[0] - start_pos[0]))
        else:
            answer += start_pos[1] - end_pos[1]



    print("#{0} {1}".format(test_case, answer))

        
def solution(places):
    answer = []
    
    x_check = [-1, 1, 0, 0]
    y_check = [0, 0, -1, 1]
    
    for place in places:
        exit_flag = False
        # loop all seat
        for y in range(5):
            for x in range(5):
                p_counter = 0
                if place[y][x] == 'P':
                    p_counter += 1

                if place[y][x] == 'O' or place[y][x] == 'P':
                    # loop four direction
                    for i in range(4):
                        ny = y + y_check[i]
                        nx = x + x_check[i]
                        if 0 <= ny and ny < 5 and 0 <= nx and nx < 5 and place[ny][nx] == 'P':
                            p_counter += 1

                # stop when find danger people
                if p_counter > 1:
                    answer.append(0)
                    exit_flag = True
                    break
                    
            if exit_flag == True:
                break
                
        if exit_flag == False:
            answer.append(1)
                
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
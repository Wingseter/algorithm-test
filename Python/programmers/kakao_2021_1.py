import re
# https://programmers.co.kr/learn/courses/30/lessons/72410
def solution(new_id):
    answer = ''
    # stage 1
    new_id = new_id.lower()

    # stage 2
    targets = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    new_id = ''.join(x for x in new_id if x in targets)
    
    # stage 3
    new_id = re.sub('(([.])\\2{1,})', '.', new_id)
    
    # stage 4
    new_id = new_id.strip('.')
    
    # stage 5
    if new_id == "":
        new_id = "a"
    
    # stage 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
        
    # stage 7
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]
    answer = new_id
    return answer
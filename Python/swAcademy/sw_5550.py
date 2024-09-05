import sys
sys.stdin = open('sample_input.txt', "r")

T = int(input())

one_cycle = ['c','r','o','a','k', None]
def get_next_word(letter):
    return one_cycle[one_cycle.index(letter) + 1]
    
for test_case in range(1, T + 1):

    memorize = list()
    answer = -1
    sounds = list(input())

    if len(sounds) % 5 == 0:
        now_singing = 0
        is_available = False 

        for letter in sounds:
            if letter == "c":
                if 'k' in memorize:
                    memorize.pop(memorize.index('k'))
                    memorize.append('c')
                else:
                    now_singing += 1
                    memorize.append('c')
            else:
                for i in range(now_singing - 1, -1, -1):
                    target = get_next_word(memorize[i])
                    if target == letter:
                        memorize[i] = letter
                        is_available = True
                        break
                if is_available == False:
                    break
        
        if is_available == False:
            now_singing = -1
        else:
            for i in range(now_singing):
                if memorize[i] != 'k':
                    now_singing = -1
                    break

        answer = now_singing

    print("#{0} {1}".format(test_case, answer))

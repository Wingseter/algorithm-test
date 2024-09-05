answer = list()
def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        answer.append((source, destination))
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    answer.append((source, destination))
    TowerOfHanoi(n-1, auxiliary, destination, source)
          
N = int(input())
TowerOfHanoi(N,1,3,2) 
print(len(answer))
for ans in answer:
    print(f"{ans[0]} {ans[1]}")
    
    
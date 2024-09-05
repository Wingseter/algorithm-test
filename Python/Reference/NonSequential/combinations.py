import itertools


def combine_with_dfs(self, n:int, k:int) -> List[List[int]]:
    results = []
    def dfs(elements, start: int, k: int):
        if k == 0:
            results.append(elements[:])
            return

        for i in range(start, n + 1):
            elements.append(i)

    dfs([], 1, k)
    return results

def combine(self, n:int, k:int)->List[List[int]]:
    return list(itertools.combinations(range(1, n + 1), k))
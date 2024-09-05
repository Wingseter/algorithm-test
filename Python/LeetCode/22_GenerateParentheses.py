class Solution:
    answer = list()
    def search(self, template, index, n):
        if template.count('(') < template.count(')') \
            or template.count('(') > n:
            return
        elif index == (2 * n):
            if template[-1] == '(':
                return
            Solution.answer.append(''.join(map(str, template)))
        else:
            self.search(template + '(', index + 1, n)
            self.search(template + ')', index + 1, n)
        
            
    def generateParenthesis(self, n: int) -> List[str]:
        self.answer.clear()
        template = '('
        self.search(template, 1, n)
        return self.answer
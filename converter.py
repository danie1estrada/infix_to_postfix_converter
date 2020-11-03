class Converter:
    OPERATORS = ('+', '-', '*', '/', '^')

    def __init__(self):
        self.stack = []

    def to_postfix(self, expression):
        postfix_expr = ''
        
        for element in expression.split(' '):
            if self.is_operand(element): 
                postfix_expr += f'{element} '

            elif element == '(':
                self.stack.append(element)

            elif element == ')':
                while self.stack[-1] != '(':
                    postfix_expr += f'{self.stack.pop()} '
                self.stack.pop()
            
            elif element in self.OPERATORS:
                while len(self.stack) > 0 and self.get_precedence(self.stack[-1]) >= self.get_precedence(element):
                    postfix_expr += f'{self.stack.pop()} '
                self.stack.append(element)            

            else:
                return 'Invalid infix expression'

        while self.stack:
            postfix_expr += f'{self.stack.pop()} '

        return postfix_expr

    def is_operand(self, element):
        return element not in self.OPERATORS and element not in ('(', ')')

    def get_precedence(self, operator):
        return { '^': 3, '*': 2, '/': 2, '+': 1, '-': 1 }.get(operator, 0)

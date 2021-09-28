class Calculator(object):
    def __init__(self):
        self.operator = None
        self.operation = {
            '*' : self.multiply,
            '/' : self.divide,
            '+' : self.add,
            '-' : self.substract
        }

    def evaluate(self, string):
        elements = string.split(' ')
        elements_count = len(elements)
        a = None
        i = 0

        while i < elements_count:
            if len(elements[i]) > 1:
                #split if there is missing space between digit and parenthese for example '2(' in test case
                elements, elements_count = self._split_if_incorrect(elements, elements_count, i)

            if elements[i] in self.operation.keys():
                #set operator for next calculation
                self.operator, i = elements[i], i + 1
                continue

            elif elements[i] == '(':
                #evaluate elements in parentheses by opening another Calculator with inserting string of elements from parentheses
                a, i = self._eval_parentheses(a, elements, i)
                continue

            elif i != len(elements) - 1:
                #evaluating by priority is for example 2 + 3 * 4 , it will calculate 3 * 4 first and then the result will evaluate with + 2
                if elements[i+1] == '*':
                    if a is not None:
                        a, i = self._multiply_by_priority(a, elements, i)
                        continue

            a = self._eval_a(a, elements[i])
            i += 1
        
        return float(a)
    
    def _split_if_incorrect(self, elements, elements_count, i): 
        elements_list = list(elements[i])
        
        for el in elements_list:
            if not el.isdigit() and el != '.':
                del elements[i]
                elements[i:i] = elements_list
                elements_count += len(elements_list) - 1
                break

        return elements, elements_count
        
    def _eval_parentheses(self, a, elements, i):
        closing_parentheses = [x for x in range(len(elements)) if elements[x] == ")"]
        string_in_parentheses = ' '.join(elements[i+1:closing_parentheses[-1]])
        parentheses_result = Calculator().evaluate(string_in_parentheses)

        if a is None:
            a = parentheses_result
        else:
            b = parentheses_result
            a = self.operation[self.operator](a, b)
            
        return a, closing_parentheses[-1] + 1

    
    def _multiply_by_priority(self, a, elements, i):
        for x, z in enumerate(elements[i:]):
            if z in ('*', '/'):
                last_priority_index = i + x + 2
            elif z in('+', '-'):
                break
        
        b = Calculator().evaluate(' '.join(elements[i:last_priority_index]))
        a = self.operation[self.operator](a, b)
        i = last_priority_index       
        
        return a, i
    
    
    def _eval_a(self, a, element):
        return float(element) if a is None else self.operation[self.operator](a, float(element))

    def add(self, a, b):
        return a + b
    
    def substract(self, a, b):
        return a - b
    
    def divide(self, a, b):
        return a / b

    def multiply(self, a, b):
        return a * b
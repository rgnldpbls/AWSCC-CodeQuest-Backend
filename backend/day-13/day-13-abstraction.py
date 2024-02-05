class Calculator:
    def sum(self, numlist: list):
        _sum = 0
        for num in numlist:
            _sum += num

        return _sum

numlist = [10, 20, 30, 40, 50]
new_calculator = Calculator()
sum = new_calculator.sum(numlist)
print(sum)
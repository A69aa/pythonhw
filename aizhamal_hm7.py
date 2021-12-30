class Sort:
    def init(self, numbers: list):
        self.numbers = numbers

    def divide(self, lst):
        if len(lst) <= 1:
            return lst
        element = lst[0]
        left = list(filter(lambda num: num < element, lst))
        center = [num for num in lst if num == element]
        right = list(filter(lambda num: num > element, lst))

        return self.divide(left) + center + self.divide(right)
    def quick_sort(self,numbers):
        if len(self.numbers) <= 1:
            return self.numbers
        element = self.numbers[0]
        left = list(filter(lambda num: num < element, self.numbers))
        center = [num for num in self.numbers if num == element]
        right = list(filter(lambda num: num > element, self.numbers))

        return self.divide(left) + center + self.divide(right)

    def str(self):
        return f"List of numbers: {self.numbers}\n"


num = Sort(numbers =[3, 1, 81, 35, 22] )
print(num)
print(num.quick_sort([3, 1, 81, 35, 22]))



# Второе задание Алгоритм легкий
n = int(input("Введите трехзначные числа: "))
a = n % 10
b = n % 100 // 10
c = n // 100
if a == c:
    print("Да,это число уникальное")
else:
    print("Это число не уникальное")
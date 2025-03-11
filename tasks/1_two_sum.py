# Дан массив целых чисел nums и целое число target, вернуть индексы двух чисел, чтобы их сумма давала target .

# Первый способ, зато понятный
class Solution:  # определили класс Solution
    # метод внутри класса
    # nums: List[int] - nums должен быть списком целых чисел, target - одно число
    # -> List[int] - функция должна возвращать список индексов
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):  # первый индекс
            for j in range(i+1,len(nums)):  # второй индекс
                if nums[i] + nums[j] == target:  # проверяем сумму
                    return [i,j]
                
# Проверка 
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))  # [0,1]
print(solution.twoSum([3,2,4], 6))  # [1,2]



# Второе, наиболее правильное решение
class Solution:  # определили класс Solution
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # второй способ
        num_dict = {}  # создаем словарь
        for i, num in enumerate(nums):  # перебираем массив nums с индексами
            complement = target - num  # второе нужное число
            if complement in num_dict:  # если оно уже есть в словаре
                return [num_dict[complement], i]  # возвращаем индексы
            num_dict[num] = i  # добавляем текущее число в словарь
            
# Проверка
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))  # [0,1]
print(solution.twoSum([3,2,4], 6))  # [1,2]
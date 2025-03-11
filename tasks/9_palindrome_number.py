# Дано целое число x, вернуть, true если x это палиндром, и false в противном случае .


# первый способ
# НЕ работает, так как возвращает строку, а при отрицательных значениях такую строку нельзя преобразовать в число.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == x
    
# Проверка
solution = Solution()
print(solution.isPalindrome(121))  # True
print(solution.isPalindrome(-10))  # False



# способ второй
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # отрицательное не подходит
            return False
        if (x % 10 == 0 and x != 0):  # с нулем в конце тоже, кроме 0
            return False

        reversed_half = 0  # задаем переменную. Это будет "перевёрнутая" половина числа, вначале она пустая, т.е. 0
        while x > reversed_half:  # пока х > второй половины (т.е. кол-во цифр в первой половине больше, чем во второй)
            reversed_half = reversed_half * 10 + x%10  # берем последнюю цифру х 
            # (в начале получается 0 + x%10 - это остаток от деления, т.е. последняя цифра x)
            x //= 10  # убираем последнюю цифру х (то же самое, что и x = x//10 - целочисленное деление)

        return x == reversed_half or x == reversed_half//10  # учитываем четные и нечетные длины чисел (раз цикл остановился, 
        # то вторая половина стала больше, чем первая. Сравниваем первую половину с зеркальной второй ИЛИ 
        # первую половину с зеркальной второй БЕЗ последнего значения - если количество цифр в числе НЕчетное)
        
# Проверка
solution = Solution()
print(solution.isPalindrome(121))  # True
print(solution.isPalindrome(-10))  # False



# третий способ
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False 

        original = x  # запоминаем оригинальное число
        resersed_num = 0  # это будет перевернутое число

        while x > 0:  # начинаем переворачивать число до конца сразу (пока x > 0)
            resersed_num = resersed_num * 10 + x % 10 # перевернутое число равно первые цифры смещаем на 1 влево, 
            # умножая на 10, т.е. добавляем 0 в конце. Далее добавяем остаток от деления (последнюю цифру) от х
            x //= 10  # сам х уменьшаем на последнюю цифру

        return original == resersed_num  # сравниваем
    
# Проверка
solution = Solution()
print(solution.isPalindrome(121))  # True
print(solution.isPalindrome(-10))  # False
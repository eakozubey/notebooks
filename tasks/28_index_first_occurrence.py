# 28. Find the Index of the First Occurrence in a String


# Решение с методом .find()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle) # find() - сам ищет вхождение и возвращает индекс первого значения

# Проверка 
solution = Solution()
print(solution.strStr("hello", "ll"))  # 2
print(solution.strStr("abcdef", "gh"))  # -1


# Ручной способ проверки
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n,m = len(haystack), len(needle)  # фиксируем длину обеих частей

        for i in range(n - m + 1):  # перебираем все возможные стартовые позиции. 
            # Где n-m+1 - ограничивает стартовую позицию, чтобы длина n вместила в себя m полностью, 
            # т.е. начиналась максимально с позиции на 1 больше, чем разность длин. 
            # Значит i будет принимать значения индекса только те, которые смогут вместить в себя m после
            if haystack[i : i+m] == needle:  # проверяем подстроку длины needle. От индекса i до i+m (добавляем длину m).
                # Т.е. haystack[i : i+m] - это вырезанная часть из haystack длины needle. 
                # Если она равна needle - возвращаем индекс, который проверяли
                return i  # если нашли совпадение - возвращаем индекс

        return -1  # если не нашли, - возвращаем -1
    
# Проверка 
solution = Solution()
print(solution.strStr("hello", "ll"))  # 2
print(solution.strStr("abcdef", "gh"))  # -1
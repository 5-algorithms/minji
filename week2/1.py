def solution(n,m):
    answer = 0
    numbers = list(range(n, m+1))

    def is_palindrome(number):
        str_number = str(number)
        if str_number == str_number[::-1]:
            return True
        else:
            return False

    for number in numbers:
        if is_palindrome(number):
            answer += 1

    return answer
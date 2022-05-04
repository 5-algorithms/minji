def solution(s):
    answer = ''
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    def check_numbers(word, answer):
        if word in numbers:
            answer += str(numbers.index(word))
            word = ''
        return word, answer
    
    if s.isdigit():
        answer = s
    else:
        word = ''
        for character in s:
            if character.isdigit():
                answer += character
            else:
                word += character
            word, answer = check_numbers(word, answer)
    return int(answer)
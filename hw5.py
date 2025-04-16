def read_single_digit(digit):
    digit_korean = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    print(digit_korean[int(digit)], end=" ")

def read_number(number):
    for digit in number:
        read_single_digit(digit)

number = input("세 자리 정수 입력: ")
read_number(number)

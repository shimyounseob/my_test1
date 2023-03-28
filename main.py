import random

answer = random.randint(1, 100)
guess = 0
tries = 0

print("1부터 100까지의 숫자를 맞추세요.")

while guess != answer:
    guess = int(input("숫자를 입력하세요: "))
    tries += 1

    if guess < answer:
        print("너무 작아요.")
    elif guess > answer:
        print("너무 커요.")

print(f"축하합니다! {tries}번 만에 맞추셨습니다.")

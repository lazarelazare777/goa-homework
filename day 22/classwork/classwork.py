password = "lazare003"
def check_password():   
    guess=input("შეიყვანეთ პაროლი: ")
    while guess != password:
       guess= input("პაროლი არასწორია ცადეთ კიდევ: ") 
    return "პაროლი საწორია"

def analyze_password(password):
    vowel = "aeiouAEIOU"
    vowel_count = 0
    for char in password:
        if char in vowel:
            vowel_count = vowel_count +1
    consonant="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    consonant_count = 0
    for char in password:
        if char in consonant:
            consonant_count = consonant_count + 1               
    numbers = "0123456789"
    numbers_count = 0
    for num in password:
        if num in numbers:
            numbers_count = numbers_count + 1
    return f"თქვენს პაროლში არის {vowel_count} ხმოვანი, {consonant_count} თანხმოვანი და {numbers_count} რიცხვი"

def ask_for_game():
    response = input("გსურთ თამაში? (კი/არა): ").lower()
    return "კი" if response == "კი" else "არა"

def math_game():
    score = 0
    question = input('7+6: ')
    if question == '13':
        score = score + 1
    question2 = input('76 - 16: ')
    if question2 == '50':
        score = score + 1
    question3 = input('5*5: ')
    if question3 == "15":
        score = score + 1
    question4 = input('30 / 3: ')
    if question4 == '10':
        score = score + 1
    question5 = input('34 + 34: ')
    if question5 == '68':
        score = score + 1
    question6 = input('54 - 13: ')
    if question6 == '41':
        score = score + 1
    question7 = input('6 * 6: ')
    if question7 == '36':
        score = score +1
    question8 = input('129 / 3: ')
    if question8 == '43':
        score = score +1
    question9 = input('234 + 256: ')
    if question9 == "490":
        score = score +1
    question10 = input(345 - 123)
    if question10 == "222":
        score = score + 1
    question11 = input('23 * 3')
    if question11 == '69':
        score = score + 1
    print('შენი შეფასებაა ', score)

def word_game():
    word_score = 0
    word_question = input('dog: ')
    if word_question == 'ძაღლი':
        word_score = word_score + 1
    word_question2 = input('numbers: ')
    if word_question2 == 'ციფრები': 
        word_score = word_score + 1
    word_question3 = input('sum: ')
    if word_question3 == 'ძამი':
        word_score = word_score + 1
    word_question4 = input('cloudy: ')
    if word_question4 == 'მოღრუბლული':
        word_score = word_score + 1
    word_question5 = input('day: ')
    if word_question5 == 'დღე':
        word_score = word_score + 1
    word_question6 = input('search: ')
    if word_question6 == 'მოძებნა':
        word_score = word_score + 1
    word_question7 = input('home: ')
    if word_question7 == 'სახლი':
        word_score = word_score + 1
    print('თქვენი საბოლოო შეფასებაა ' , word_score)
    print('მადლობა მონაწილეობისთვის')


print(check_password())
print(analyze_password(password))
print(ask_for_game())
print(math_game())
print(word_game())
# HOMEWORK
# შექმენი ჯეირანის თამაში if ის გამოყენებით 

while True:
    list = ["1.ჭა", "2.ფურცელი", "3.მაკრატელი"]
    print(list)
    მოთამაშე1 = int(input('გთხოვთ შეიყვანთ თქვენი არჩევანი(1 დან 3 ის ჩათვლით)'))
    მოთამაშე2 = int(input('გთხოვთ შეიყვანთ თქვენი არჩევანი(1 დან 3 ის ჩათვლით)'))
    if მოთამაშე1 == 1 and მოთამაშე2 == 1:
        print("ფრე!")
    elif მოთამაშე1 == 1 and მოთამაშე2 == 2:
        print('მოთამაშე2-მა გაიმარჯვა!')
    elif მოთამაშე1 == 1 and მოთამაშე2 == 3:
        print('მოთამაშე1-მა გაიმარჯვა!')
    elif მოთამაშე1 == 2 and მოთამაშე2 == 1:
        print('მოთამაშე1-მა გაიმარჯვა!')
    elif მოთამაშე1 == 2 and მოთამაშე2 == 2:
        print('ფრე!')
    elif მოთამაშე1 == 2 and მოთამაშე2 == 3:
        print('მოთამაშე2-მა გაიმარჯვა!')
    elif მოთამაშე1 == 3 and მოთამაშე2 == 1:
        print('მოთამაშე2-მა გაიმარჯვა!')
    elif მოთამაშე1 == 3 and მოთამაშე2 == 2:
        print('მოთამაშე1-მა გაიმარჯვა   !')
    elif მოთამაშე1 == 3 and მოთამაშე2 == 3:
        print('ფრე!')
    else:
        print('არასწორი მცდელობა, ცადე თავიდან')
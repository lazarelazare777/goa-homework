# HOMEWORK
# 1 - დავალება: დაწერე ფუნქცია, რომელიც იღებს ერთ რიცხვს და აბრუნებს "დადებითია", "უარყოფითია" ან "ნულია".
def check_number(num):
    if num > 0:
        return "დადებითია"
    elif num < 0:
        return "უარყოფითია"
    else:
        return "ნულია"

print(check_number(10))  
print(check_number(-5))  
print(check_number(0))   

#  2 - დავალება: დაწერე ფუნქცია, რომელიც იღებს სიტყვას და აბრუნებს "გრძელია", თუ სიტყვა 6-ზე მეტი სიმბოლოსგან შედგება, სხვა შემთხვევაში "მოკლეა".
def check_word(word):
    if len(word) > 6:
        return "გრძელია"
    else:
        return "მოკლეა"

print(check_word("საქართველო"))  
print(check_word("მზე"))        

# 3 - დავალება: დაწერე ფუნქცია, რომელიც იღებს რიცხვების სიას და აბრუნებს მათ ჯამს.
def num(numbers):
    return sum (numbers)
print(num(16,23,455,6,65,312,23,7,89,8987))
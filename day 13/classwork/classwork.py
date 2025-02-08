# 1) დავალება: შექმენი ფუნქცია, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ ჯამს.
def num(number1, number2):
    return number1 + number2
print(num(10, 45))

# 2)  შექმენი ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს "ლუწია" ან "კენტია" დამოკიდებულია მის სიდიდეზე.
def even_or_odd(number):
    if number %2 !=0:
        return "odd"
    elif number % 2 ==0:
        return "even"
print(even_or_odd(16))

# 3) დავალება: შექმენი ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს მის სიგრძეს.
def num(name):
    return len(name)
print(num('lazare'))

# 4) შექმენი ფუნქცია, რომელიც იღებს სიას და აბრუნებს მასში ყველაზე პატარა და ყველაზე დიდ რიცხვს.
def num(numbers):
    return min(numbers) , max(numbers)
print(num([11,1,2,54,77,89,8,7,766,6,5,5,444,123]))

# 5)  შექმენი ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს მას შებრუნებულად.
def world(name):
    return name [::-1]
print(world('lazare'))

# 6) შექმენი ფუნქცია, რომელიც იღებს სამ რიცხვს და აბრუნებს მათ ნამრავლს.
def num(a ,b ,c):
    return a*b*c
print(num(2 ,6 ,10))
# 1: დაწერე Python პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს რაიმე მნიშვნელობა (input()-ით) და შემდეგ ამოწმებს, რომელი ტიპის მონაცემია.

# მომხმარებლის შეყვანილი მნიშვნელობა შეამოწმე type()-ის გამოყენებით.

# დაბეჭდე, თუ ეს არის int, float, str ან სხვა ტიპის მონაცემი. 
num = input()
print("შეყვანილი მნიშვნელობა არის: "+ str(type(num)))

# 2: დაწერე პროგრამა, რომელიც:

# ქმნის სამ სხვადასხვა ტიპის ცვლადს (int, float, str).
# თითოეული ცვლადის ტიპს type()-ის გამოყენებით ბეჭდავს.
num1=15
num2=1.67
num3="67"
print("შეყვანილი მნიშვნელობა არის: "+ str(type(num1)))
print("შეყვანილი მნიშვნელობა არის: "+ str(type(num2)))
print("შეყვანილი მნიშვნელობა არის: "+ str(type(num3)))
'''Q1. Basic f-string
You have the following variables:
name = "Ikrama"
age = 22
Print the output:
My name is Ikrama and I am 22 years old.'''

name = "Ikrama"
age = 21
print(f"My name is {name} and I am {age} years old.")

'''Q2. Using .format()
Given:
city = "Ahmedabad"
country = "India"
Print:
I live in Ahmedabad, India.
using the .format() method.'''

city = "Ahmedabad"
country = "India"
print("I live in {}, {}".format(city,country))

'''Q3. Format Multiple Variables
Given:
language = "Python"
version = 3.13
Print:
I am learning Python version 3.13
using an f-string.'''

language = "Python"
version = 3.13
print(f"I am learning {language} version {version}")

'''Q4. Decimal Formatting
Given:
price = 499.9876
Print:
Price: ₹499.99
(Round to 2 decimal places.)'''

price = 499.9876
print(f"Price : {price:.2f}")

'''Q5. Percentage Formatting
Given:
score = 0.875
Print:
Success Rate: 87.50%
Without multiplying the number manually.'''

score = 0.875
print(f"Success Rate: {score:.2%}")

'''Q6. Padding Numbers
Given:
order_id = 57
Print:
Order ID: 00057
using string formatting.'''

order_id = 57
print(f"Order ID: {order_id:07d}")

'''Q7. Align Text
Given:
name = "Python"
Print it in a field of 15 characters, left-aligned.
Example:
Python
(total width should be 15 characters)'''

name1 = "Python"
print(f"{name1:<15}")

'''Q8. Table Formatting

Given:
product = "Laptop"
price = 55000
qty = 3
Print:
Item       Price      Qty
Laptop     55000      3
using formatting so each column is aligned properly.'''

product = "Laptop"
price = 55000
qty = 3
print(f"{'Item':<10}{'price':<10}{'Qty':<10}")
print(f"{product:<10}{price:<10}{price:<10}")

'''Q9. Dynamic Width
Given:
word = "AI"
width = 10
Print the word centered inside a width of 10.
Example:
    AI
(with equal spaces on both sides as much as possible)'''

word = "AI"
width = 10
print(f"{word:^{width}}")

'''Q10. Combined Formatting
Question
name = "Ikrama"
marks = 89.4567
rank = 7
Output
Student : Ikrama
Marks   : 89.46
Rank    : 007'''

name3 = "Ikrama"
marks = 89.4567
rank = 7

print(f"Student:{name3}")
print(f"Marks:{marks:.2f}")
print(f"Rank:{rank:03d}")











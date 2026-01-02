ta = "engineer"
print(ta.startswith("eng"))

data = "student"
print(data.endswith("ent"))

gmail = "kob53@gmail.com"

print("@" in gmail)

text = input("type your gmail: ")
if text.endswith("gmail.com") == True:
    if "@" not in text:
        print("There is no @ in text")
    
else: 
    print("There is something wrong")

num = input("type your lao number(+856 20 Your number): ")
ko = len(num) == 16
if num.startswith("+856") and ko == True:
    print("=== complete ===")
else:
    print("This is not Laos number or something wrong")    
nu = "20-5643-425"
print(nu.find("-"))

number = input("type your number: ")
print(number[number.find(" ")+1: ])


dat = "python"
print(dat.isalpha()) 

number1 = "21334523452"
print(number1.isnumeric())
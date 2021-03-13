letter = '''Dear <|NAME|>,

You are selected!

Regards,
Bill
Date: <|DATE|>
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")

letter = letter.replace("<|NAME|>", name)
letter = letter.Dineshreplace("<|DATE|>", date)
print(letter)
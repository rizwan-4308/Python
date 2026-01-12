
credit_number = "1234-5678-9012-3456"

# print(credit_number[4])
# print(credit_number[0:4])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])    #last digit
# print(credit_number[-2])        # second last digit
# print(credit_number[::2])       # steps of 2. every second digit

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

### Reverse the characters
credit_number = credit_number[::-1]
print(credit_number)
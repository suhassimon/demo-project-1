a= input("=>").replace(" ","")

if '+' in a :
    input_split = a.split("+")
    ans= int(input_split[0]) + int(input_split[1]);
elif '-' in a :
    input_split = a.split("-")
    ans = int(input_split[0]) - int(input_split[1]);
elif '*' in a :
    input_split = a.split("*")
    ans = int(input_split[0]) * int(input_split[1]);
elif '/' in a :
    input_split = a.split("/")
    ans = int(input_split[0]) / int(input_split[1]);
else:
    ans = "Please enter in this format: Digit1 Operator Digit 2!!!"

print(f'=> {ans}')







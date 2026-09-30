#Austin White
#Date: 9/30/26
#desc: Temp converter part2 
print("===== Temperature Converter =====")
print()
print("1. Convert from Celsius to Fahrenheit")
print()
print("2. Convert from Fahrenheit to Celsius")
print()
#C to F
c_1 = int(input("Please choose from the above menu: "))
if c_1 == "1":
   tempc = float(input("Enter a temperature to convert: "))
   CtoF = tempc * 9/5 + 32
   print()
   print(f"{tempc} degrees Celsius is {CtoF} degrees Fahrenheit.")
#F to C
elif c_1 == "2":
    tempf = float(input("Enter a temperature to convert: "))
    ftoc = (tempf - 32 ) * 5/9
    print(f"{tempf} degrees Fahrenheit is {ftoc} degrees Celsius.")
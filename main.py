def calculate(h,w):
    result = w/(h**2)
    return result

def status(bmi) :
    if bmi <= 18.4 :
        result = "Under Weight"
    elif bmi >=18.5 and bmi <= 24.9 :
        result = "Normal Weight"
    elif bmi >= 25.0 and bmi <= 29.9 :
        result = "Over Weight"
    elif bmi >= 30.0 and bmi <= 34.9 :
        result = "Obese Class 1"
    elif bmi >= 35.0 and bmi <= 39.9 :
        result = "Obese Class 2"
    elif bmi >= 40.0 :
        result = "Obese Class 3"
    return result

h = float(input('Insert your height '))
kg = float(input('Insert your weight '))

bmi = calculate(h,kg)

print('your bmi is',bmi,' and you are',status(bmi))

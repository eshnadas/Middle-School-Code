def noOneLikesRomanNumerals(number):
    numbers = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
    if number < 4:
        return(number*"I")
    if number>4 and number<9:
        return("V" + (number-5)*"I")
    if number > 10 and number < 14:
        return("X" + (number-10) * "I")
    if number > 10 and number < 20:
        return(numbers[10] + noOneLikesRomanNumerals(number%10))
    if number > 20 and number < 39:
        return numbers[10] * (number//10) + noOneLikesRomanNumerals(number%10)
    if number > 39 and number < 50:
        return numbers[40] + noOneLikesRomanNumerals(number%10)
    if number > 50 and number < 90:
        return numbers[50] + numbers[10]* ((number - 50)//10) + noOneLikesRomanNumerals(number%10)
    if number > 90 and number < 100:
        return numbers[90] + noOneLikesRomanNumerals(number%10)
    if number >100 and number <400:
        return  numbers[100] * (number//100) + noOneLikesRomanNumerals(number%100)
    if number > 400 and number < 500:
        return numbers[400] + noOneLikesRomanNumerals(number%100)
    if number > 500 and number < 900:
        return numbers[500] + numbers[100]*((number-500)//100) + noOneLikesRomanNumerals(number%100)
    if number > 900 and number < 1000:
        return numbers[900] + noOneLikesRomanNumerals(number%100)
    if number > 1000 and number < 4000:
        return numbers[1000]*(number//1000)+ noOneLikesRomanNumerals(number%1000)
    if number > 4000:
        print("ur stupid ngl")
    else: 
        return(numbers[number])
print(noOneLikesRomanNumerals(412433526))
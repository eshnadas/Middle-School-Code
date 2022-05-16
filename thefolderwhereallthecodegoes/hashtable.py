def noOneLikesRomanNumerals(number):
    numbers = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
    if number < 4:
        return(number*"I")
    if number>4 and number<9:
        return("V" + (number-5)*"I")
    if number > 10 and number < 14:
        return("X" + (number-10) * "I")
    if number > 10 and number < 20:
        return(numbers[10] + noOneLikesRomanNumerals(number%10))
    else: 
        return(numbers[number])
print(noOneLikesRomanNumerals(19)) 

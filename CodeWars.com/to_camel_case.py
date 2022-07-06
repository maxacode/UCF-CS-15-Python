# DESCRIPTION:
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    #your code here
    listOfWords = []
    word = ''
    for x in text:
        if x.isalpha():
            x = x.lower()
            word = word + x
        else:
            listOfWords.append(word)
            word = ''

    listOfWords.append(word)   

    # loop through every word and on the second word on capitilize the first letter
    #      
    for x in range(len(listOfWords)):
        if x != 0:
            listOfWords[x] = listOfWords[x][0].upper() + listOfWords[x][1:]
        else:
            listOfWords[x] = listOfWords[x]

    return ''.join(listOfWords)

print(to_camel_case('the-stealth-warrior'))

print(to_camel_case('tHe-stealth-warrior'))
print(to_camel_case('tHe-stealth_warrior'))
print(to_camel_case('tHe+stealth_warrior'))



# def to_camel_case2(text):
#     list1 = []
#     word = ''

#     for x in text:





# print(to_camel_case2('the+stealth-warrior'))


## Tests

# test.describe("Testing function to_camel_case")
# test.it("Basic tests")
# test.assert_equals(to_camel_case(''), '', "An empty string was provided but not returned")
# test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
# test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
# test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")
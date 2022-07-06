# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case


"""


import codewars_test as test
from solution import count_bits

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(count_bits(0), 0)
        test.assert_equals(count_bits(4), 1)
        test.assert_equals(count_bits(7), 3)
        test.assert_equals(count_bits(9), 2)
        test.assert_equals(count_bits(10), 2)
        """

"""
Variable n should be passed in as INT

"""
def count_bits(n):

    print(n)

    binary = bin(n).replace("0b", "")
    print(binary)
    howManyOnes = binary.count("1")
    howManyZeros = binary.count("0")
     
    return print({"How many Ones": howManyOnes,"How many Zeros": howManyZeros})

def printHi():
    return print("__name__ = ", __name__)

if __name__ == "__main__":
    count_bits(1324)
    printHi()



# Best Solution:

# def countBits(n):
#     return bin(n).count("1")
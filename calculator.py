#!/bin/python3

print("""
 _________________________________
#                                 #
# PASSWORD COMBINATION CALCULATOR #
#_________________________________#
""")

try:
    total_char = int(input("> total characters : "))
    max_input = int(input("\n> max input : "))
    total_combination = 0

    i = 1
    while i <= max_input:
        total_combination += total_char**i
        i += 1

    print()
    print("# total combination :", total_combination)

except Exception as e:
    print()
    print(e)

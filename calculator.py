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

    for i, _ in enumerate(range(total_char)):
        total_combination += total_char**(i+1)

    print()
    print("# total combination :", total_combination)

except Exception as e:
    print()
    print(e)

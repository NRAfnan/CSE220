# def print_plus(n, current_n):
#     if current_n == n:
#         print(current_n)
#     else:
#         print(current_n, end=" ")
#     if current_n == n:
#         return current_n
#     print_plus(n, current_n + 5)
#
#
# def print_minus(current_n):
#     print(current_n, end=" ")
#     if current_n <= 0:
#         return current_n
#     return print_minus(current_n - 5)
#
#
# def print_pattern(n, num_spaces = 0):
#     if n <= 0:
#         return
#     space_str = " " * num_spaces
#     print(space_str, end="")
#     c_n = print_minus(n) + 5
#     print_plus(n, c_n)
#     print_pattern(n - 5, num_spaces + len(str(n)) + 1)


def print_p(n):
    if n <= 0:
        print(n, end=" ")
        return
    print(n, end=" ")
    print_p(n - 5)
    print(n, end=" ")




def print_pattern(n, num_spaces = 0):
    if n <= 0:
        return
    space_str = " " * num_spaces
    print(space_str, end="")
    print_p(n)
    print()
    print_pattern(n - 5, num_spaces + len(str(n)) + 1)



print('========1========')
n = 16
print_pattern(n)
#This should print

#16 11 6 1 -4 1 6 11 16
#   11 6 1 -4 1 6 11
#      6 1 -4 1 6
#        1 -4 1

print('========2========')
n = 10
print_pattern(n)
#This should print

#10 5 0 5 10
#   5 0 5
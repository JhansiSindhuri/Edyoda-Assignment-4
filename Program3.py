# Finding squares of given list :
# Python program to square the elements of a list using map() function.

def square_num(n):
  return n * n
nums = [4, 5, 2, 9]
print("Given List: ",nums)
result = map(square_num, nums)
print("Square of the elements of the list :")
print(list(result))

inputs = input("give inputs: ")
print(inputs.split(' '))
print(len(inputs.split(' ')) == 1)

def test(arr):
  zero = False
  for num in arr:
      if num == 0 and not zero:
          zero = True
      elif num == 0 and zero:
          return True
      elif num*2 in arr:
          return True
  return False
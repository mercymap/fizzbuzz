def fizzbuzz(list_1, list_2):
  lists = list_1 + list_2

  if len(lists) % 3 == 0 and len(lists) % 5 == 0:
     return "fizzbuzz"

  elif len(lists) % 3 == 0:
     return "fizz"

  elif len(lists) % 5 == 0:
     return "buzz"
  return (len(lists))


print(fizzbuzz( ['1', '2', '3', '4', '5'], ['1', '2', '3', '9']))
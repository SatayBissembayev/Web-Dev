def monkey_trouble(a_smile, b_smile):
  if a_smile == False and b_smile == False:
    return True
  elif a_smile == True and b_smile == False:
    return False
  elif a_smile == False and b_smile == True:
    return False
  else:
    return True

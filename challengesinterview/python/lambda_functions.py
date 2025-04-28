"They are small functions with anonymous name"

import numbers


def lambda_functions_example():
  # calculator
  add = lambda x: x + 1
  subtract = lambda x: x - 1
  multiply = lambda x: x * 2
  divide = lambda x: x / 2

  # sorting authors
  authors = ["Isaac Asimov", "Ray Bradbury", "Clarke Arthur", "Frank Herbert"]
  ordered_authors = sorted(authors, key=lambda name: name.split()[-1])
  
  # filtering numbers
  numbers = [1, 2, 3, 4, 5]
  odd_numbers = list(filter(lambda x: x % 2 !=0, numbers))
  even_numbers = list(filter(lambda x: x % 2 ==0, numbers))

# o operador % é o operador de módulo, que retorna o resto da divisão
# imagine fazendo o desenho de divisão do ensino médio, é a mesma coisa. 4 dividido por 2, da 2 e resta 0
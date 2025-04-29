def play_cards():
  results = []
  
  while True:
    try:
      n = int(input("Digite um número (0 para sair): "))

      if n == 0:
        break

      cards = list(range(n, 0, -1))
      print(f"Cards: {cards}")
      results.append(cards)
    except ValueError:
      print("Por favor, digite um número inteiro válido.")
  
  return results

if __name__ == "__main__":
  print("Iniciando programa...")
  all_results = play_cards()
  print("\nTodos os resultados:")
  for i, cards in enumerate(all_results):
    print(f"Resultado {i+1}: {cards}")
  print("Programa finalizado.")

try:
    with open("texto.txt", "r") as arquivo:
   
        conteudo = arquivo.read()
        
       
        palavras = conteudo.split()
        
       
        numero_palavras = len(palavras)
      
        print(f"O arquivo 'texto.txt' contém {numero_palavras} palavras.")
        
except FileNotFoundError:
    print("O arquivo 'texto.txt' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

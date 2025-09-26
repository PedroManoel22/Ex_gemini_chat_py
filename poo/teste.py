from deep_translator import GoogleTranslator

frase = "Life is better when you're laughing."

# Cria uma instância do tradutor com as línguas de origem e destino
# A linguagem de origem é opcional, mas boa prática para ser explícito
tradutor = GoogleTranslator(source='en', target='pt')

# Chama o método de tradução
texto_traduzido = tradutor.translate(frase)

print(texto_traduzido)
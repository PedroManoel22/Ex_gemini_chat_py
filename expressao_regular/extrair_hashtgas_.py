# Exercício 7: Extrair Hashtags de uma String
# Objetivo: Encontre todas as hashtags (palavras que começam com #) em um texto.

# Contexto: "Aprenda #Python com #projetos. Participe da #comunidade de #programação."
# Dica: Use re.findall() com um padrão que comece com # e seja seguido por caracteres de palavra.

import re 

texto = "Aprenda #Python com #projetos. Participe da #comunidade de #programação."

print(re.findall(r'#[a-zA-Z]+', texto))
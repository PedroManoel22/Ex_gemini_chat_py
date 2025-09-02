# Exercício 3: Extrair Endereços de Email
# Objetivo: Extraia todos os endereços de e-mail de um texto. Considere um formato simples nome@dominio.com.

# Contexto: "Fale conosco em contato@empresa.com.br ou suporte@minha-loja.com."
# Dica: Use re.findall(). O padrão pode ser \S+@\S+, que busca sequências de caracteres não-brancos.

import re

def extrair_emails(texto):

    emails = re.findall(r'\S+@\S+', texto)

    return emails

texto_1 = 'Fale conosco em contato@empresa.com.br ou suporte@minha-loja.com.'
print(extrair_emails(texto_1))

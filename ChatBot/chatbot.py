import openai

chave_api = "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"

openai.api_key = chave_api

def envia_mensagem(messagem):
    resposta = openai.ChatCompletion.create(
        model = "gpt-4-1106-preview",   
        mesagens = [
            {"role":"user", "content": messagem}
        ],
    )

    return resposta["choices"][0]["message"]["content"]

print(envia_mensagem("Qual foi o ultimo brasileiro campeão mundial"))
import streamlit as st

import openai

openai.api_key = "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"

def resposta_generica(pergunta):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # Ou outro modelo de sua escolha
        prompt=pergunta,  # Aqui você coloca a pergunta diretamente como um prompt
        max_tokens=150  # Limite de tokens na resposta, ajuste conforme necessário
    )
    return response.choices[0].text.strip()  # Pega a resposta e limpa espaços extras



# Função para obter resposta personalizada
def resposta_personalizada(pergunta):
    custom_prompt = (
        "Responda esta pergunta com base exclusivamente nas seguintes fontes: "
        "- Livro: 'A History of Israel' de Benny Morris. "
        "- Publicações da Universidade Hebraica de Jerusalém. "
        "- Artigos publicados por Alan Dershowitz, Samuel Feldberg e Ben Shapiro. "
        "Ignore quaisquer outras fontes ou interpretações."
        f"\n\nPergunta: {pergunta}"
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": custom_prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Interface do Streamlit
st.title("Protótipo de Perguntas e Respostas sobre Israel")
st.write("Compare respostas genéricas e personalizadas.")

# Campo de entrada para pergunta
pergunta = st.text_input("Digite sua pergunta aqui:")

if pergunta:
    # Resposta Genérica
    st.subheader("Resposta Genérica:")
    st.write(resposta_generica(pergunta))

    # Resposta Personalizada
    st.subheader("Resposta Personalizada:")
    st.write(resposta_personalizada(pergunta))

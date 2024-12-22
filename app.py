{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww19400\viewh12180\viewkind0
\deftab560
\pard\pardeftab560\slleading20\pardirnatural\partightenfactor0

\f0\fs26 \cf0 import streamlit as st\
import openai\
\
# Configura\'e7\'e3o da chave da API\
openai.api_key = "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"\
\
# Fun\'e7\'e3o para obter resposta gen\'e9rica\
def resposta_generica(pergunta):\
    response = openai.ChatCompletion.create(\
        model="gpt-3.5-turbo",\
        messages=[\
            \{"role": "user", "content": pergunta\}\
        ]\
    )\
    return response['choices'][0]['message']['content']\
\
# Fun\'e7\'e3o para obter resposta personalizada\
def resposta_personalizada(pergunta):\
    custom_prompt = (\
        "Responda esta pergunta com base exclusivamente nas seguintes fontes: "\
        "- Livro: 'A History of Israel' de Benny Morris. "\
        "- Publica\'e7\'f5es da Universidade Hebraica de Jerusal\'e9m. "\
        "- Artigos publicados por Alan Dershowitz, Samuel Feldberg e Ben Shapiro. "\
        "Ignore quaisquer outras fontes ou interpreta\'e7\'f5es."\
        f"\\n\\nPergunta: \{pergunta\}"\
    )\
    response = openai.ChatCompletion.create(\
        model="gpt-3.5-turbo",\
        messages=[\
            \{"role": "user", "content": custom_prompt\}\
        ]\
    )\
    return response['choices'][0]['message']['content']\
\
# Interface do Streamlit\
st.title("Prot\'f3tipo de Perguntas e Respostas sobre Israel")\
st.write("Compare respostas gen\'e9ricas e personalizadas.")\
\
# Campo de entrada para pergunta\
pergunta = st.text_input("Digite sua pergunta aqui:")\
\
if pergunta:\
    # Resposta Gen\'e9rica\
    st.subheader("Resposta Gen\'e9rica:")\
    st.write(resposta_generica(pergunta))\
\
    # Resposta Personalizada\
    st.subheader("Resposta Personalizada:")\
    st.write(resposta_personalizada(pergunta))\
}
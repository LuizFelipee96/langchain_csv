import streamlit as st
import os
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        st.error("A API da OpenAI não foi inserida")
        return
    
    st.set_page_config(page_title="Pergunte ao arquivo CSV")
    st.header("Perguntas ao CSV")
    
    csv_file = st.file_uploader("Faça o carregamento do seu arquivo", type="csv")
    
    if csv_file is not None:
        file_path = csv_file.name
        
        agent = create_csv_agent(OpenAI(temperature=0), file_path, verbose=True)
        
        user_question = st.text_input("Faça uma pergunta ao arquivo CSV: ")
        
        if user_question is not None and user_question != "":
            with st.spinner(text="Em progresso..."):
                st.write(agent.run(user_question))
        else:
            st.warning("Digite uma pergunta válida.")
        
if __name__ == "__main__":
    main()

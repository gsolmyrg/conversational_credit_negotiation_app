import random

import streamlit as st
from dotenv import load_dotenv

from services import CreditNegotiationService

load_dotenv()


def generate_random_persona():
    """Generate random persona values"""
    names = [
        "Ana Silva",
        "Carlos Santos",
        "Maria Oliveira",
        "João Costa",
        "Fernanda Lima",
        "Pedro Alves",
        "Juliana Rodrigues",
        "Rafael Pereira",
        "Camila Souza",
        "Lucas Ferreira",
    ]

    genders = ["Masculino", "Feminino", "Prefiro não especificar"]

    return {
        "name": random.choice(names),
        "gender": random.choice(genders),
        "age": random.randint(18, 75),
        "debt": random.randint(0, 100000),
        "yearly_revenue": random.randint(0, 200000),
    }


def main():
    st.set_page_config(page_title="Persona Definition", page_icon="👤", layout="wide")

    st.title("👩🏽‍💼 Negociação de Crédito")
    st.markdown("Simulação de negociação de crédito com agente virtual")

    # Initialize session state for persona data with randomized values
    if "persona" not in st.session_state:
        random_persona = generate_random_persona()
        # Add empty cellphone (not randomized)
        random_persona["cellphone"] = ""
        st.session_state.persona = random_persona

    # Create sidebar for persona configuration
    with st.sidebar:
        st.header("👤 Configuração da Persona")
        st.markdown("Configure os dados da persona para simulação")

        # Name input
        name = st.text_input(
            "Nome",
            value=st.session_state.persona["name"],
            placeholder="Digite o nome da persona",
        )

        # Cellphone input (required)
        cellphone = st.text_input(
            "Celular *",
            value=st.session_state.persona["cellphone"],
            placeholder="5511912345678 (sem o 9 inicial)",
            help="Campo obrigatório - não será alterado pela randomização",
        )

        # Gender selection
        gender = st.selectbox(
            "Gênero",
            options=["Masculino", "Feminino", "Prefiro não especificar"],
            index=["Masculino", "Feminino", "Prefiro não especificar"].index(
                st.session_state.persona["gender"]
            ),
        )

        # Age slider
        age = st.slider(
            "Idade",
            min_value=18,
            max_value=75,
            value=st.session_state.persona["age"],
            step=1,
        )

        st.markdown("---")
        st.subheader("💰 Informações Financeiras")

        # Debt slider
        debt = st.slider(
            "Dívida Atual",
            min_value=0,
            max_value=100000,
            value=st.session_state.persona["debt"],
            step=1000,
            format="R$ %d",
        )

        # Yearly Revenue slider
        yearly_revenue = st.slider(
            "Renda Anual",
            min_value=0,
            max_value=200000,
            value=st.session_state.persona["yearly_revenue"],
            step=1000,
            format="R$ %d",
        )

        st.markdown("---")
        st.subheader("⚙️ Opções")

        # Clear conversation history checkbox
        clear_history = st.checkbox(
            "🗑️ Limpar histórico de conversas",
            help="Marque esta opção para limpar todo o histórico de conversas e começar uma nova sessão",
        )

        st.markdown("---")

        # Buttons
        randomize_clicked = st.button(
            "🎲 Randomizar", type="secondary", use_container_width=True
        )

        trigger_clicked = st.button(
            "🚀 Processar", type="primary", use_container_width=True
        )

    # Handle randomize button click
    if randomize_clicked:
        random_persona = generate_random_persona()
        # Preserve the cellphone value (not affected by randomization)
        random_persona["cellphone"] = st.session_state.persona["cellphone"]
        st.session_state.persona = random_persona
        st.rerun()

    # Update session state with current values (only if not randomizing)
    if not randomize_clicked:
        st.session_state.persona = {
            "name": name,
            "cellphone": cellphone,
            "gender": gender,
            "age": age,
            "debt": debt,
            "yearly_revenue": yearly_revenue,
        }

    st.info(
        "🚧 Esta seção será implementada para simular a negociação de crédito com o agente virtual."
    )

    # Trigger action
    if trigger_clicked:
        if not st.session_state.persona["name"]:
            st.error("⚠️ Por favor, informe o nome da persona antes de processar.")
        elif not st.session_state.persona["cellphone"]:
            st.error("⚠️ Por favor, informe o número de celular antes de processar.")
        else:
            data = {
                "persona": st.session_state.persona,
                "options": {"clear_history": clear_history},
            }
            st.json(data)
            with st.spinner("Processando negociação de crédito..."):
                CreditNegotiationService().negotiate_credit(data)
                st.success(
                    "✅ Você receberá uma mensagem via WhatsApp no número informado em breve!"
                )


if __name__ == "__main__":
    main()

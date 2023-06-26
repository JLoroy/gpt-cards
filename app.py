# STREAMLIT Part
import streamlit as st
from chatbot_hot import create_card_with_gpt
from card import Card, card_from_json
from html_template import css_template
import os

st.session_state.card = None
st.session_state.deck = []

def open_card(filename):
    with open(f"cards/{filename}", 'r') as cardfile:
            cardjson = cardfile.read()
            return card_from_json(cardjson)


def main():
    st.set_page_config(layout="wide")

    deck = []
    for filename in os.listdir('cards'):
        if filename.endswith('.json'):
            deck.append(open_card(filename))
    
    deck_text = "DECK:"
    for c in deck:
        deck_text += f"\n{c.name}"

    st.title('GPT-Cards')
    st.markdown(css_template, unsafe_allow_html=True)
    control_col, cards_col = st.columns([1, 3])

    # Button
    prompt = control_col.text_input("Enter your card")
    if control_col.button("Generate" ) and prompt:
        with st.spinner('Wait for it...'):
            create_card_with_gpt(prompt, deck_text)

    if st.session_state.card:
        control_col.markdown(st.session_state.card.to_html(), unsafe_allow_html=True)
        control_col.info(st.session_state.card.illustration_description, icon="🖼")
    
    


    ether, arcane, chaos, nature, spirit = cards_col.tabs(["Ether", "Arcane", "Chaos", "Nature", "Spirit"])
    
    with ether:
        st.header("Ether")
        col_1, col_2, col_3 = st.columns(3)
        columns = [col_1, col_2, col_3]
        index = 0
        for card in deck:
            if card.type == "Ether":
                columns[index].markdown(card.to_html(),  unsafe_allow_html=True)
                index = (index+1)%3

    with arcane:
        st.header("Arcane")
        col_1, col_2, col_3 = st.columns(3)
        columns = [col_1, col_2, col_3]
        index = 0
        for card in deck:
            if card.type == "Arcane":
                columns[index].markdown(card.to_html(),  unsafe_allow_html=True)
                index = (index+1)%3

    with chaos:
        st.header("Chaos")
        col_1, col_2, col_3 = st.columns(3)
        columns = [col_1, col_2, col_3]
        index = 0
        for card in deck:
            if card.type == "Chaos":
                columns[index].markdown(card.to_html(),  unsafe_allow_html=True)
                index = (index+1)%3

    with nature:
        st.header("Nature")
        col_1, col_2, col_3 = st.columns(3)
        columns = [col_1, col_2, col_3]
        index = 0
        for card in deck:
            if card.type == "Nature":
                columns[index].markdown(card.to_html(),  unsafe_allow_html=True)
                index = (index+1)%3

    with spirit:
        st.header("Spirit")
        col_1, col_2, col_3 = st.columns(3)
        columns = [col_1, col_2, col_3]
        index = 0
        for card in deck:
            if card.type == "Spirit":
                columns[index].markdown(card.to_html(),  unsafe_allow_html=True)
                index = (index+1)%3

if __name__ == "__main__":
    main()
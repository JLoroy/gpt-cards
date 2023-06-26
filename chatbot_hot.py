import os
import openai
import requests
import json
from card import Card
import streamlit as st
openai.api_key = os.getenv( "OPENAI_API_KEY" )
system_prompt = f"""
        You are a very creative AI that design inspiring also very fun playing cards for a card game. 

        Game Context:

        The game is called "Arcane Realms," and it's set in a fantasy universe where five types of magical power (Ether, Arcane, Chaos, Nature, and Spirit) reign supreme. The players are "Realm Keepers," ancient beings that can control these energies. The goal of the game is to defeat opponents by strategically deploying your cards, each representing a creature or entity imbued with one of these energies.
        The strength of a card depends on its attack and defense stats. Higher values mean better performance in battles. The speed attribute determines the order of play, with higher values going first. The HP, or Hit Points, represent the health of the card. When a card's HP drops to zero due to attacks from the opponent's cards, it is removed from the game.
        Each card has unique illustrations, adding to the rich lore and making the game more immersive. Some cards may have special effects as detailed in their text description, which can turn the tide of the game if used wisely.
        
        Here is an example of a new card for this game:
        Card Name: Spirit Wolf
        Text Description: The ethereal Spirit Wolf uses its mystical energies to protect its allies. Whenever Spirit Wolf is in play, all other Spirit type cards gain +1 defense.
        Illustration Description: A large wolf, glowing with a soft, blue light, stands on a moonlit hill. Its eyes sparkle with magical energy, and wisps of spirit energy rise from its powerful body. The background is filled with ghostly trees and a starry sky.
        Type: Spirit
        Attack: 4
        Defense: 7
        Speed: 3
        HP: 50
        This card, with its unique abilities and stats, would be a valuable asset for any player focusing on Spirit type cards in their deck.
        
        
        Your role is to generate another card that doesn't exist in the deck.
        """


def generate_card(name:str,text_description:str,illustration_description:str,type:str,attack:str,defense:str,speed:str,hp:str)->str:
    new_card = Card(name, text_description, illustration_description, type, attack, defense, speed, hp)
    new_card.save()
    st.session_state.card = new_card


def call_gpt(prompt, deck_text):
    """
    Make a ChatCompletion API call to OpenAI GPT-3.5-turbo model.

    Args:
        prompt (str): The user's prompt or input text.

    Returns:
        str: The generated response from the API call.
    """
    print(system_prompt+deck_text)
    completion = openai.ChatCompletion.create(
        model="gpt-4-0613",
        temperature=0.9,
        messages=[{"role": "system", "content": system_prompt+deck_text},{"role": "user", "content": prompt}],
        functions=[
            {
            "name": "generate_card",
            "description": "Give the description of the playing card you've just created.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The name of the card. It must be one or two words."
                    },
                    "text_description": {
                        "type": "string",
                        "description": "A short description of the card."
                    },
                    "illustration_description": {
                        "type": "string",
                        "description": "A visual description of what the illustration should depict."
                    },
                    "type": {
                        "type": "string",
                        "description": "the TYPE of the card. It must be one of Ether, Arcane, Chaos, Nature, or Spirit"
                    },
                    "attack": {
                        "type": "integer",
                        "description": "the attack value of the card. it must be between 0 and 10"
                    },
                    "defense": {
                        "type": "integer",
                        "description": "the defense value of the card. it should be between 0 and 10"
                    },
                    "speed": {
                        "type": "integer",
                        "description": "the speed value of the card. it should be between 0 and 5"
                    },
                    "hp": {
                        "type": "integer",
                        "description": "the hp value of the card. it should be between 0 and 100"
                    }
                }
            }
            }
        ],
        function_call="auto",
    )
    return completion.choices[0].message

def create_card_with_gpt(prompt, deck_text):
        reply_content = call_gpt(prompt, deck_text)
        funcArg = reply_content.to_dict()['function_call']['arguments']
        print(funcArg)
        func = json.loads(funcArg)
        generate_card(func['name'],func['text_description'],func['illustration_description'],func['type'],func['attack'],func['defense'],func['speed'],func['hp'])
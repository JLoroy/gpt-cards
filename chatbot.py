# LANGCHAIN with FUNCTION CALLING
## Langchain part
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain_decorators import llm_prompt, llm_function
from langchain_decorators.common import GlobalSettings
from langchain_decorators import llm_prompt
from card import Card
import streamlit as st

from langchain_decorators import PromptTypes, PromptTypeSettings

PromptTypes.AGENT_REASONING.llm = ChatOpenAI()

# Or you can just define your own ones:
class MyCustomPromptTypes(PromptTypes):
    GPT4=PromptTypeSettings(llm=ChatOpenAI(model="gpt-4", temperature=0.9))

GlobalSettings.define_settings(verbose=True)

@llm_function
def generate_card(name:str,text_description:str,illustration_description:str,type:str,attack:str,defense:str,speed:str,hp:str)->str:
    """ 
    Give the description of the playing card you've just created. 

    Args:
        name (str): The name of the card. It must be one or two words.
        text_description (str): A short description of the card.
        illustration_description (str): A visual description of what the illustration should depict.
        type (str): the TYPE of the card. It must be one of Ether, Arcane, Chaos, Nature, or Spirit
        attack (int): the attack value of the card. it must be between 0 and 10
        defense (int): the defense value of the card. it should be between 0 and 10
        speed (int): the speed value of the card. it should be between 0 and 5
        hp  (int): the hp value of the card. it should be between 0 and 100
    """
    new_card = Card(name, text_description, illustration_description, type, attack, defense, speed, hp)
    new_card.save()
    st.session_state.card = new_card

class CardAgent:

    def __init__(self) -> None:
        self.todo_list=[]

    @llm_prompt(prompt_type=MyCustomPromptTypes.GPT4)
    def create_card(self, deck:str, functions=[generate_card]):
        """ 
        ``` <prompt:system>
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
        ```
        ``` <prompt:user>
        Please generate a new original card to add to my deck. 
        {deck}
        ```
        """


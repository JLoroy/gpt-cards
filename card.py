import json, os, shutil


def card_to_json(card):
    card_dict = {
        "name": card.name,
        "text_description": card.text_description,
        "illustration_description": card.illustration_description,
        "type": card.type,
        "attack": card.attack,
        "defense": card.defense,
        "speed": card.speed,
        "hp": card.hp
    }
    json_output = json.dumps(card_dict)
    return json_output

def card_from_json(json_input):
    card_dict = json.loads(json_input)
    return Card(
        card_dict["name"], 
        card_dict["text_description"], 
        card_dict["illustration_description"], 
        card_dict["type"], 
        card_dict["attack"], 
        card_dict["defense"], 
        card_dict["speed"], 
        card_dict["hp"]
    )

class Card():

    def __init__(self, name, text_description, illustration_description, type, attack, defense, speed, hp):
        self.name = name
        self.text_description = text_description
        self.illustration_description = illustration_description
        self.type = type
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.hp = hp
        self.filename = self.name.replace(" ", "_").lower()
        self.json = f"cards/{self.filename}.json"
        self.png = f"app/static/{self.filename}.png"
        self.pngfile = f"./static/{self.filename}.png"
        self.html = f"cards/{self.filename}.html"
    
    def save(self):
        with open(self.json, 'w') as card_file:
            card_file.write(card_to_json(self))
        if not os.path.exists(self.pngfile):
            shutil.copy("./static/template.png", self.pngfile)

    def show(self):
        result = []
        result.append(f"name: {self.name}")
        result.append(f"text_description: {self.text_description}")
        result.append(f"illustration_description: {self.illustration_description}")
        result.append(f"type: {self.type}")
        result.append(f"attack: {str(self.attack)}")
        result.append(f"defense: {str(self.defense)}")
        result.append(f"speed: {str(self.speed)}")
        result.append(f"hp: {str(self.hp)}")
        return result
    
    def to_html(self):
        picture = self.png
        if os.path.getsize(self.pngfile) == os.path.getsize("./static/template.png"):
            picture = "app/static/template.png"
        
        html_template = f"""
        <div class="container {self.type.lower()}">
            <div class="img-container">
                <img src='{picture}'>
            </div>
            <div class="info-container">
                <div class="info-row">
                    <span class="name">{self.name}</span>
                    <span class="hp">{self.hp}</span>
                </div>
                <div class="stats-row">
                    <span>Attack: {self.attack}</span>
                    <span>Defense: {self.defense}</span>
                    <span>Speed: {self.speed}</span>
                </div>
                <div class="description">{self.text_description}</div>
            </div>
        </div>
"""
        return html_template


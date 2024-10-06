import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="!", intents=intents)

# Parkour Alphabet Mapping
parkour_alphabet = {
    'a': '[ ] _ _ _ _',
    'b': '/ _ / _',
    'c': '{ } _ _ _',
    'd': '{ } _ _',
    'e': '[ ] _',
    'f': '/ _ // _',
    'g': '| | _',
    'h': '| _ _| _',
    'i': '[ ] _ _ _',
    'j': 'H _ [ ] _',
    'k': 'i _',
    'l': '{ } _',
    'm': '| | _| |',
    'n': 'L _ _',
    'o': 'L _ _ [ ] _',
    'p': '| | _| _',
    'q': 'HH _ _',
    'r': 'L _ _',
    's': '[ ] _ _',
    't': 'L _ [ ] _',
    'u': '{ } _ _ _ _',
    'v': '/ _ / _ /',
    'w': 'i _ _',
    'x': 'i _ _ [ ] _',
    'y': '// _ / _',
    'z': 'i _ [ ] _'
}

# Numbers Mapping
parkour_numbers = {
    '0': 'D',
    '1': 'D^',
    '2': 'D^^',
    '3': 'D^^^',
    '4': 'D^^^^',
    '5': 'D^^^^^',
    '6': 'D^^^^^^',
    '7': 'D^^^^^^^',
    '8': 'D^^^^^^^^',
    '9': 'D^^^^^^^^^'
}


def translate_to_parkour(text):
    translated = []
    for char in text.lower():
        if char in parkour_alphabet:
            translated.append(parkour_alphabet[char])
        elif char in parkour_numbers:
            translated.append(parkour_numbers[char])
        elif char == ' ':
            translated.append('*')  
        else:
            translated.append(char)  
    return ' '.join(translated)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def parkour(ctx, *, sentence):
    translated_sentence = translate_to_parkour(sentence)
    formatted_output = f"```python\n{translated_sentence}\n```"
    await ctx.send(f'Translated to Parkour language:\n{formatted_output}')


TOKEN = 'Add Bot Token'


bot.run(TOKEN)

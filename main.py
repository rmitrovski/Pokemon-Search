from pokebase import pokemon, ability
import textwrap

# Ask the user to enter a Pokémon name
pokemon_name = input("Enter the name of a Pokémon: ")

# Retrieve information about the Pokémon
try:
    pokemon_info = pokemon(pokemon_name.lower())
    print("Pokémon Details:")
    print("Name:", pokemon_info.name)
    print("ID:", pokemon_info.id)
    print("Base Experience:", pokemon_info.base_experience)
    print("Height:", pokemon_info.height)
    print("Weight:", pokemon_info.weight)
    
    abilities = []
    for ability_info in pokemon_info.abilities:
        ability_name = ability_info.ability.name
        ability_data = ability(ability_name)
        for entry in ability_data.effect_entries:
            if entry.language.name == 'en':
                # Wrap the ability description to 60 characters per line with an initial space
                wrapped_description = textwrap.fill(entry.short_effect, width=59, initial_indent=" ", subsequent_indent=" ")
                ability_desc = f"- Ability: {ability_name}\n Description: {wrapped_description}\n Effect: {entry.effect}"
                abilities.append(ability_desc)
                break
    
    print("Abilities:")
    print("\n".join(abilities))
    
    print("Types:", ", ".join([poke_type.type.name for poke_type in pokemon_info.types]))
    
    print("Stats:")
    for stat in pokemon_info.stats:
        print(f"- {stat.stat.name.capitalize()}: {stat.base_stat}")
except Exception as e:
    print("Error:", e)

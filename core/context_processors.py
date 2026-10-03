from twonumorg import eastereggs


# noinspection unused-parameter
def global_pokemon_question(request) -> dict[str, str]:
    return {
        "pokemon_question": eastereggs.pokemon_question(4)
    }

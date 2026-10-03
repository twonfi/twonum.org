"""Easter eggs for Cadence's website."""

from random import choice

POKEMON_QUESTION_COMMENTS = (
    # the ending song
    "you see, tonight, it could go either way",
    # pokemon_scarlet_spoilers.txt
    "select this for spoilers",
    # Ed Sheeran's music is bad anyway
    "to Ed Sheeran Celestial. Yes to YOASOBI Biri-Biri.",
    ", just why?",
    "supa luigi galaxy!!!!!",
    # Resetti
    (
        "You lied to official Pokémon League staff."
        " Your save file has been deleted."
    ),
    # YOASOBI -- Biri-Biri
    "fun, electrical",
)


def pokemon_question(pad: int = 0, comment: str | None = None, name: str = "Cadence") -> str:
    """Return the infamous "Do you like Pokémon?" question.

    For an example of the question from the Pokémon Scarlet game, see
    <https://www.twonum.org/static/pokemon_question.png>.

    This shouldn't be a major spoiler compared to what is described in
    pokemon_scarlet_spoilers.txt.

    :param pad: The number of spaces to add.  Defaults to 0.
    :param comment: Hardcode a comment for the "No" option.
    Defaults to a random comment.
    :param name: A name to be used.  Defaults to Cadence.
    :returns: A formatted, plain-text question with the ``name``.
    """
    # Example: pokemon_question(0, "%s", "Cadence")
    #                                                   -------
    #                                                  |> Yes |
    #                                                   | No  |  <-- %s
    #   ------------                                    -------
    #  |    Rika    | ____________________________________
    #   ------------                                     |
    #    |  Do you like Pokémon, Cadence?                |
    #    |                                               |
    #    |_______________________________________________|

    if not comment:
        comment = choice(POKEMON_QUESTION_COMMENTS)
    p = ' ' * pad

    return f"""{p}                                                 -------
{p}                                                |> Yes |
{p}                                                 | No  |  <-- {comment}
{p} ------------                                    -------
{p}|    Rika    |____________________________________
{p} ------------                                     |
{p}  |  Do you like Pokémon, {name+"?":<23} |
{p}  |                                               |
{p}  |_______________________________________________|"""

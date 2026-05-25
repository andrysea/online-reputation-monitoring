import re

def clean_text(text: str) -> str:
    """
    Pulisce minimamente un testo.

    La funzione non modifica URL, menzioni, hashtag o punteggiatura.
    Si limita a:
    - gestire input non testuali;
    - rimuovere spazi multipli;
    - eliminare spazi iniziali e finali.
    """

    if not isinstance(text, str):
        return ""

    # Rimuove spazi multipli
    text = re.sub(r"\s+", " ", text)

    # Rimuove spazi iniziali e finali
    text = text.strip()

    return text
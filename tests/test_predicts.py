import sys
import os

# Aggiunge la cartella principale del progetto al percorso di Python.
# Serve per importare correttamente i moduli presenti nella cartella src.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.predict import predict_sentiment


def test_predict_sentiment_returns_dictionary():
    # Esegue una predizione su un testo di esempio.
    result = predict_sentiment("I love this company!")

    # Verifica che il risultato sia un dizionario.
    assert isinstance(result, dict)


def test_predict_sentiment_returns_valid_sentiment():
    # Esegue una predizione su un testo di esempio.
    result = predict_sentiment("I love this company!")

    # Verifica che il sentiment restituito sia una delle classi previste.
    assert result["sentiment"] in ["Negative", "Neutral", "Positive"]


def test_predict_sentiment_confidence_between_zero_and_one():
    # Esegue una predizione su un testo di esempio.
    result = predict_sentiment("I love this company!")

    # Verifica che la confidence sia compresa tra 0 e 1.
    assert 0.0 <= result["confidence"] <= 1.0


def test_predict_sentiment_empty_text():
    # Esegue una predizione su un testo vuoto.
    result = predict_sentiment("")

    # Verifica che il sistema gestisca il testo vuoto senza errori.
    assert result["sentiment"] == "Neutral"
    assert result["confidence"] == 0.0
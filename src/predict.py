import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from src.preprocessing import clean_text


MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"

LABELS = {
    0: "Negative",
    1: "Neutral",
    2: "Positive"
}


tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)


def predict_sentiment(text: str) -> dict:
    """
    Predice il sentiment di un testo.

    Args:
        text (str): Testo da analizzare.

    Returns:
        dict: Dizionario contenente testo pulito, sentiment previsto e confidence.
    """

    cleaned_text = clean_text(text)

    # Testo vuoto
    if cleaned_text == "":
        return {
            "text": cleaned_text,
            "sentiment": "Neutral",
            "confidence": 0.0
        }

    # return_tensors="pt" -> Restituisce il risultato nel formato PyTorch
    # truncation=True     -> Se il testo è troppo lungo troncalo
    # max_length=512      -> Il testo può avere al massimo 512 token
    inputs = tokenizer(
        cleaned_text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    # Esegue la predizione senza aggiornare i pesi del modello.
    # Il modello viene solo usato per classificare il testo.
    with torch.no_grad():
        outputs = model(**inputs)

    # Trasforma i risultati grezzi del modello in probabilità per ciascuna classe.
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)

    # Seleziona la classe con la probabilità più alta.
    predicted_class = torch.argmax(probabilities, dim=-1).item()

    # Recupera il valore di probabilità associato alla classe scelta.
    confidence = probabilities[0][predicted_class].item()

    return {
        "text": cleaned_text,
        "sentiment": LABELS[predicted_class],
        "confidence": round(confidence, 4)
    }
import gradio as gr

from src.predict import predict_sentiment


def analyze_sentiment(text: str):
    """
    Analizza il sentiment del testo inserito dall'utente tramite l'interfaccia Gradio.

    Args:
        text (str): Testo scritto dall'utente.

    Returns:
        tuple: Sentiment previsto e confidence del modello.
    """

    # Usa il modello per classificare il testo inserito dall'utente.
    result = predict_sentiment(text)

    # Restituisce il sentiment previsto e il livello di confidenza.
    return result["sentiment"], result["confidence"]


demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(
        lines=5,
        placeholder="Scrivi qui un commento social da analizzare..."
    ),
    outputs=[
        gr.Label(label="Sentiment previsto"),
        gr.Number(label="Confidence")
    ],
    title="Online Reputation Monitoring - Sentiment Analysis",
    description=(
        "Questa applicazione analizza il sentiment di un testo social "
        "e lo classifica come Negative, Neutral o Positive."
    ),
    examples=[
        ["I love this company and their products are amazing!"],
        ["The service is okay, nothing special."],
        ["I had a terrible experience with customer support."]
    ]
)


if __name__ == "__main__":
    # Avvia l'app Gradio.
    demo.launch()
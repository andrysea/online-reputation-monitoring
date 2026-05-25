from sklearn.metrics import accuracy_score, classification_report


def evaluate_model_performance(y_true, y_pred) -> dict:
    """
    Valuta le performance del modello confrontando le etichette reali
    con le etichette predette.

    Args:
        y_true: Lista o serie contenente le etichette reali.
        y_pred: Lista o serie contenente le etichette predette.

    Returns:
        dict: Dizionario con accuracy e report di classificazione.
    """

    # Calcola quante predizioni del modello coincidono con le etichette reali.
    accuracy = accuracy_score(y_true, y_pred)

    # Crea un report dettagliato con precision, recall e f1-score per ogni classe.
    report = classification_report(y_true, y_pred, output_dict=True)

    return {
        "accuracy": round(accuracy, 4),
        "classification_report": report
    }


def should_retrain(current_accuracy: float, threshold: float = 0.75) -> bool:
    """
    Decide se è consigliato fare retraining del modello.

    Args:
        current_accuracy (float): Accuracy attuale del modello.
        threshold (float): Soglia minima accettabile di accuracy.

    Returns:
        bool: True se il retraining è consigliato, False altrimenti.
    """

    # Se l'accuracy scende sotto la soglia minima, il modello potrebbe non essere più affidabile.
    if current_accuracy < threshold:
        return True

    # Se l'accuracy è sopra la soglia, il retraining non è necessario in questo momento.
    return False
import pandas as pd


def sentiment_distribution(df: pd.DataFrame, sentiment_column: str = "predicted_sentiment") -> pd.DataFrame:
    """
    Calcola la distribuzione dei sentiment presenti nel dataset.

    Args:
        df (pd.DataFrame): Dataset contenente le predizioni del modello.
        sentiment_column (str): Nome della colonna che contiene i sentiment predetti.

    Returns:
        pd.DataFrame: Tabella con conteggio e percentuale per ogni sentiment.
    """

    if sentiment_column not in df.columns:
        raise ValueError(f"La colonna '{sentiment_column}' non esiste nel dataset.")

    # Conta quante volte compare ogni sentiment nel dataset.
    counts = df[sentiment_column].value_counts()

    # Calcola la percentuale di ogni sentiment rispetto al totale dei testi.
    percentages = df[sentiment_column].value_counts(normalize=True) * 100

    # Crea una tabella riassuntiva con conteggio e percentuale.
    distribution = pd.DataFrame({
        "count": counts,
        "percentage": percentages.round(2)
    })

    return distribution


def sentiment_over_time(
    df: pd.DataFrame,
    date_column: str = "date",
    sentiment_column: str = "predicted_sentiment"
) -> pd.DataFrame:
    """
    Calcola l'andamento dei sentiment nel tempo.

    Args:
        df (pd.DataFrame): Dataset contenente date e sentiment predetti.
        date_column (str): Nome della colonna con le date.
        sentiment_column (str): Nome della colonna con i sentiment predetti.

    Returns:
        pd.DataFrame: Tabella con il numero di sentiment per ogni data.
    """

    if date_column not in df.columns:
        raise ValueError(f"La colonna '{date_column}' non esiste nel dataset.")

    if sentiment_column not in df.columns:
        raise ValueError(f"La colonna '{sentiment_column}' non esiste nel dataset.")

    # Converte la colonna delle date in formato datetime.
    df[date_column] = pd.to_datetime(df[date_column])

    # Raggruppa i dati per data e sentiment, contando quante volte compare ogni classe.
    trend = (
        df.groupby([date_column, sentiment_column])
        .size()
        .reset_index(name="count")
    )

    return trend
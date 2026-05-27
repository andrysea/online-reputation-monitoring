---
title: Online Reputation Monitoring
sdk: gradio
app_file: app.py
pinned: false
---

# monitoraggio_reputazione_azienda
Progetto esame per il master di AI Engineering, modulo: MLOps e Machine Learning in Produzione

# MachineInnovators Inc. — Sentiment Analysis con MLOps

## Descrizione del Progetto

MachineInnovators Inc. è leader nello sviluppo di applicazioni di machine learning scalabili e pronte per la produzione.

Il focus principale del progetto è integrare metodologie **MLOps** per facilitare lo sviluppo, l'implementazione, il monitoraggio continuo e il retraining di modelli di analisi del sentiment.

L'obiettivo è abilitare l'azienda a migliorare e monitorare la propria reputazione sui social media attraverso l'analisi automatica dei sentiment degli utenti.

---

## Contesto

Le aziende si trovano spesso a fronteggiare la sfida di gestire e migliorare la propria reputazione sui social media in modo efficace e tempestivo.

Il monitoraggio manuale del sentiment degli utenti può risultare:

- inefficiente;
- soggetto a errori umani;
- poco scalabile;
- lento nel rilevare cambiamenti nella percezione del brand.

Rispondere rapidamente ai cambiamenti nel sentiment degli utenti è cruciale per mantenere un'immagine aziendale positiva e intervenire tempestivamente in caso di criticità.

---

## Benefici della Soluzione

### Automazione dell'Analisi del Sentiment

Implementando un modello di analisi del sentiment, MachineInnovators Inc. automatizzerà l'elaborazione dei dati provenienti dai social media per identificare sentiment:

- positivi;
- neutrali;
- negativi.

Questo permetterà una risposta più rapida e mirata ai feedback degli utenti.

### Monitoraggio Continuo della Reputazione

Utilizzando metodologie MLOps, l'azienda implementerà un sistema di monitoraggio continuo per valutare l'andamento del sentiment degli utenti nel tempo.

Ciò consentirà di:

- rilevare rapidamente cambiamenti nella percezione dell'azienda;
- monitorare l'evoluzione della reputazione online;
- intervenire prontamente in caso di aumento dei sentiment negativi.

### Retraining del Modello

L'introduzione di un sistema di retraining automatico permetterà al modello di adattarsi dinamicamente a:

- nuovi dati;
- variazioni nel linguaggio degli utenti;
- cambiamenti nei comportamenti sui social media;
- nuovi trend comunicativi.

Mantenere alta l'accuratezza predittiva del modello è essenziale per una valutazione corretta del sentiment.

---

## Dettagli del Progetto

## Fase 1 — Implementazione del Modello di Analisi del Sentiment

### Modello

Il progetto prevede l'utilizzo di un modello pre-addestrato per l'analisi del sentiment in grado di classificare testi provenienti dai social media in tre categorie:

- positivo;
- neutro;
- negativo.

Modello di riferimento:

[cardiffnlp/twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest)

### Dataset

Verranno utilizzati dataset pubblici contenenti testi e relative etichette di sentiment.

I dati saranno impiegati per:

- valutare le performance del modello;
- testare la pipeline di preprocessing;
- simulare scenari realistici di analisi sui social media.

---

## Fase 2 — Creazione della Pipeline CI/CD

La pipeline CI/CD sarà sviluppata per automatizzare le principali fasi del ciclo di vita del modello.

La pipeline comprenderà:

- training del modello;
- test di integrazione;
- validazione delle performance;
- deploy dell'applicazione;
- gestione del codice tramite repository GitHub.

L'obiettivo è garantire un processo di sviluppo riproducibile, scalabile e facilmente manutenibile.

---

## Fase 3 — Deploy e Monitoraggio Continuo

### Deploy su Hugging Face

Il deploy su Hugging Face è facoltativo, ma consigliato per facilitare:

- accessibilità del modello;
- integrazione con altre applicazioni;
- scalabilità;
- condivisione del progetto.

### Sistema di Monitoraggio

Il sistema di monitoraggio sarà configurato per valutare continuamente:

- performance del modello;
- distribuzione dei sentiment rilevati;
- variazioni nel tempo;
- eventuale degrado delle prestazioni;
- necessità di retraining.

---

## Documentazione delle Scelte Progettuali

Il progetto è stato strutturato seguendo un approccio MLOps, separando il codice in moduli dedicati a preprocessing, predizione, monitoraggio e retraining.

Il preprocessing è stato mantenuto minimo per non alterare eccessivamente i testi social, dato che il modello utilizzato è già addestrato su contenuti provenienti da Twitter/social media.

Il modello scelto è `cardiffnlp/twitter-roberta-base-sentiment-latest`, indicato nella traccia del progetto, basato su RoBERTa ed è stato utilizzato il modello Hugging Face indicato.

La pipeline CI/CD è stata implementata con GitHub Actions per eseguire automaticamente i test a ogni push o pull request, garantendo maggiore affidabilità del codice.

Il deploy è stato realizzato su Hugging Face Spaces tramite Gradio, così da rendere il modello accessibile tramite interfaccia web.

Il monitoraggio è stato progettato per analizzare la distribuzione dei sentiment e il loro andamento nel tempo, mentre la logica di retraining consente di stabilire quando il modello dovrebbe essere rivalutato o riaddestrato in base alle performance.

---

## Struttura della Repository

```text
online-reputation-monitoring/
│
├── app.py
├── src/
│   ├── predict.py
│   ├── preprocessing.py
│   ├── monitoring.py
│   └── retraining.py
│
├── tests/
│   └── test_predict.py
│
├── data/
│   └── sample_social_posts.csv
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
└── README.md
```
---

## Installazione

Clonare la repository:

```bash
git clone https://github.com/andrysea/online-reputation-monitoring
cd online-reputation-monitoring
```

Creare un ambiente virtuale:

```bash
python -m venv venv
source venv/bin/activate
```

Su Windows:

```bash
venv\Scripts\activate
```

Installare le dipendenze:

```bash
pip install -r requirements.txt
```

---

## Esecuzione dell'applicazione

Per avviare l'app Gradio in locale:

```bash
python app.py
```

Dopo l'avvio, l'app sarà accessibile dal browser tramite l'indirizzo mostrato nel terminale.

---

## Test

I test automatici si trovano nella cartella `tests/`.

Per eseguirli:

```bash
pytest
```

I test verificano che:

* il modello restituisca una classe valida;
* il sistema gestisca input testuali corretti;
* la pipeline di predizione non generi errori inattesi.

---

## Pipeline CI/CD

La pipeline CI/CD è configurata tramite GitHub Actions nel file:

```text
.github/workflows/ci.yml
```

A ogni push o pull request, la pipeline esegue automaticamente:

1. setup dell'ambiente Python;
2. installazione delle dipendenze;
3. esecuzione dei test automatici.

Questa automazione aiuta a garantire che il codice rimanga funzionante durante lo sviluppo.

---

## Deploy

Il deploy dell'applicazione viene effettuato su Hugging Face Spaces.

Link alla demo:

```text
https://huggingface.co/spaces/andrysea/online-reputation-monitoring
```

Lo Space permette di provare il modello direttamente online tramite interfaccia web.

---

## Risultati ottenuti

Il sistema permette di ottenere:

* classificazione automatica del sentiment;
* distribuzione dei commenti positivi, neutri e negativi;
* indicatori utili per monitorare la reputazione online;
* demo web accessibile online;
* pipeline automatizzata di test;
* base progettuale per retraining e monitoraggio continuo.

---

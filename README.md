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

La pipeline CI/CD è stata sviluppata per automatizzare la validazione del progetto.

La pipeline comprende:

- controllo del codice tramite test automatici;
- installazione delle dipendenze;
- verifica della pipeline di predizione;
- supporto al processo di deploy dell'applicazione su Hugging Face Spaces.

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

## Implementazioni Realizzate

Durante lo sviluppo del progetto sono stati implementati diversi componenti per coprire le principali fasi di un workflow MLOps.

### Preprocessing

Il modulo `src/preprocessing.py` contiene la funzione dedicata alla pulizia del testo.

Il preprocessing è stato mantenuto volutamente leggero, limitandosi alla gestione di input non testuali, alla rimozione di spazi multipli e alla normalizzazione degli spazi iniziali e finali.

Questa scelta è stata adottata perché il modello utilizzato è già stato addestrato su testi provenienti da Twitter/social media. Una pulizia troppo aggressiva, come la rimozione di hashtag, menzioni o punteggiatura, avrebbe potuto eliminare informazioni utili per la classificazione del sentiment.

### Predizione del Sentiment

Il modulo `src/predict.py` gestisce il caricamento del tokenizer e del modello pre-addestrato `cardiffnlp/twitter-roberta-base-sentiment-latest`.

La funzione principale `predict_sentiment()` riceve un testo in input e restituisce:

- testo analizzato;
- sentiment previsto;
- livello di confidenza della predizione.

Il modello classifica i testi in tre categorie:

- Negative;
- Neutral;
- Positive.

L'inferenza viene eseguita senza aggiornare i pesi del modello, utilizzando il modello esclusivamente per classificare il testo fornito dall'utente.

### Monitoraggio

Il modulo `src/monitoring.py` è stato progettato per supportare il monitoraggio della reputazione online.

Le funzionalità implementate permettono di analizzare:

- distribuzione dei sentiment;
- percentuale di commenti positivi, neutri e negativi;
- andamento del sentiment nel tempo.

Queste informazioni possono essere utilizzate per osservare eventuali variazioni nella percezione dell'azienda da parte degli utenti.

### Retraining e Rivalutazione

Il modulo `src/retraining.py` contiene una logica di supporto alla rivalutazione del modello.

Il sistema permette di confrontare le performance del modello con una soglia minima di accuratezza. Se le performance scendono sotto tale soglia, il sistema può segnalare la necessità di procedere con una nuova fase di valutazione o retraining.

Nel progetto attuale il retraining è rappresentato come logica progettuale e di controllo, non come addestramento automatico completo di un nuovo modello.

### Interfaccia Web

L'applicazione `app.py` utilizza Gradio per fornire una semplice interfaccia web.

L'utente può inserire un testo e ottenere in output:

- sentiment previsto;
- confidence score associato alla previsione.

L'applicazione è stata predisposta per il deploy su Hugging Face Spaces.

### Test Automatici

La cartella `tests/` contiene test automatici sviluppati con `pytest`.

I test verificano che:

- la funzione di predizione restituisca un dizionario;
- il sentiment previsto appartenga alle classi attese;
- la confidence sia compresa tra 0 e 1;
- gli input vuoti vengano gestiti senza generare errori.

### CI/CD

La pipeline CI/CD è stata configurata tramite GitHub Actions.

A ogni push o pull request sul branch principale, la pipeline installa le dipendenze ed esegue i test automatici. Questo consente di verificare che le modifiche al codice non compromettano il funzionamento della pipeline di predizione.

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

## Considerazioni sui Risultati

Il progetto ha permesso di realizzare un sistema funzionante per l'analisi automatica del sentiment applicata al monitoraggio della reputazione online.

I principali risultati ottenuti sono:

- implementazione di un modello pre-addestrato per la sentiment analysis;
- creazione di una pipeline di preprocessing e predizione;
- realizzazione di funzioni di monitoraggio della distribuzione dei sentiment;
- introduzione di una logica di supporto al retraining o alla rivalutazione del modello;
- sviluppo di un'interfaccia web con Gradio;
- deploy dell'applicazione su Hugging Face Spaces;
- configurazione di una pipeline CI/CD con GitHub Actions;
- creazione di test automatici per verificare il corretto funzionamento della predizione.

Il sistema rappresenta una base scalabile per un'applicazione MLOps più completa, nella quale potrebbero essere integrati in futuro nuovi dati reali, metriche di monitoraggio più avanzate e un processo di retraining completamente automatizzato.

## Limiti e Sviluppi Futuri

Il progetto utilizza un dataset dimostrativo e non un flusso continuo di dati reali provenienti dai social media.

In una possibile evoluzione futura, il sistema potrebbe essere esteso con:

- integrazione con API social o sorgenti dati esterne;
- salvataggio storico delle predizioni;
- dashboard di monitoraggio più avanzata;
- metriche di model drift e data drift;
- retraining automatico completo;
- confronto tra più modelli di sentiment analysis;
- supporto multilingua.

---

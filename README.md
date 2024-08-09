# 🛡️ SentiGuard-AI

A robust sentiment analysis tool using Google's Gemini AI with proxy support to leverage the free tier in supported countries and enhance privacy.

[English](#english) | [Italiano](#italiano)

---

## English

### 📝 Description
SentiGuard-AI is a Python script that performs sentiment analysis on text data using Google's Gemini AI. It features proxy support to utilize Gemini's free tier effectively in supported countries while also enhancing privacy. This makes it suitable for large-scale sentiment analysis tasks, allowing users to maximize the benefits of the free API tier while respecting rate limits.

### 🌟 Features
- 🧠 Utilizes Google's Gemini AI for accurate sentiment analysis
- 🌐 Implements proxy support via Webshare API to:
  - 🆓 Effectively use Gemini's free tier by routing requests through supported countries
  - 🕵️ Enhance privacy and anonymity of API requests
- 🔄 Handles multiple analyses with custom prompts
- ⏱️ Respects API rate limits to ensure uninterrupted operation within free tier constraints
- 📊 Provides real-time console output for monitoring
- 💾 Saves results progressively in CSV and final output in XLSX format

### 🛠️ Requirements
- Python 3.7+
- Required Python libraries (automatically installed by the script):
  ```
  pandas
  google-generativeai
  pillow
  requests
  openpyxl
  ```

### 🔑 API Keys Required

#### 1. Google Generative AI API Key
- 🔗 Obtain from [Google AI Studio](https://makersuite.google.com/app/apikey)
- 📋 Instructions:
  1. Visit the Google AI Studio link above
  2. Click on "Get API key"
  3. Create a new API key or use an existing one

> ⚠️ **Important:** Keep your API key secure. Review Google's guidelines on [API key security](https://cloud.google.com/docs/authentication/api-keys#securing_an_api_key) and check the [API quickstarts](https://ai.google.dev/tutorials/quickstarts) for language-specific best practices.

#### 2. Webshare API Key
- 🔗 Sign up at [Webshare](https://www.webshare.io/features/free-proxy)
- 📋 Instructions:
  1. Visit the Webshare link above
  2. Sign up for a free account
  3. Access your proxy list and API key from your dashboard

> 📢 **Note:** Webshare offers a free proxy server tier. However, the availability of proxies in countries supported by Gemini's free tier may vary. The script will attempt to use proxies from supported countries.

### 🌍 Gemini Free Tier Countries
The availability of Gemini's free tier is limited to certain countries. The script will attempt to use proxies from these countries to leverage the free tier. However, the actual availability depends on Webshare's proxy list at the time of execution.

### 🚀 How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SentiGuard-AI.git
   ```
2. Navigate to the project directory:
   ```bash
   cd SentiGuard-AI
   ```
3. Run the script:
   ```bash
   python sentiguard_ai.py
   ```
4. Follow the on-screen prompts to:
   - Enter your API keys
   - Select your input file (CSV or Excel)
   - Choose the column containing the text to analyze
   - Define the number of analyses and their respective prompts

### 📤 Output
- Interim results are saved in `sentiment_analysis_results.csv`
- Final results are saved in `sentiment_analysis_results_final.xlsx`
- Error logs, if any, are saved in `error_log.txt`

---

## Italiano

### 📝 Descrizione
SentiGuard-AI è uno script Python che esegue l'analisi del sentiment su dati testuali utilizzando l'AI Gemini di Google. Presenta il supporto proxy per utilizzare efficacemente il piano gratuito di Gemini nei paesi supportati, migliorando al contempo la privacy. Questo lo rende adatto per attività di analisi del sentiment su larga scala, permettendo agli utenti di massimizzare i benefici del piano API gratuito rispettando i limiti di utilizzo.

### 🌟 Caratteristiche
- 🧠 Utilizza l'AI Gemini di Google per un'analisi accurata del sentiment
- 🌐 Implementa il supporto proxy tramite API Webshare per:
  - 🆓 Utilizzare efficacemente il piano gratuito di Gemini instradando le richieste attraverso paesi supportati
  - 🕵️ Migliorare la privacy e l'anonimato delle richieste API
- 🔄 Gestisce analisi multiple con prompt personalizzati
- ⏱️ Rispetta i limiti di velocità delle API per garantire un funzionamento ininterrotto entro i vincoli del piano gratuito
- 📊 Fornisce output in console in tempo reale per il monitoraggio
- 💾 Salva i risultati progressivamente in formato CSV e l'output finale in formato XLSX

### 🛠️ Requisiti
- Python 3.7+
- Librerie Python richieste (installate automaticamente dallo script):
  ```
  pandas
  google-generativeai
  pillow
  requests
  openpyxl
  ```

### 🔑 Chiavi API Richieste

#### 1. Chiave API Google Generative AI
- 🔗 Ottenibile da [Google AI Studio](https://makersuite.google.com/app/apikey)
- 📋 Istruzioni:
  1. Visita il link di Google AI Studio sopra
  2. Clicca su "Ottieni chiave API"
  3. Crea una nuova chiave API o usa una esistente

> ⚠️ **Importante:** Mantieni la tua chiave API sicura. Rivedi le linee guida di Google sulla [sicurezza delle chiavi API](https://cloud.google.com/docs/authentication/api-keys#securing_an_api_key) e consulta le [guide rapide API](https://ai.google.dev/tutorials/quickstarts) per le migliori pratiche specifiche per linguaggio.

#### 2. Chiave API Webshare
- 🔗 Registrati su [Webshare](https://www.webshare.io/features/free-proxy)
- 📋 Istruzioni:
  1. Visita il link Webshare sopra
  2. Registrati per un account gratuito
  3. Accedi alla tua lista di proxy e alla chiave API dalla tua dashboard

> 📢 **Nota:** Webshare offre un piano gratuito di server proxy. Tuttavia, la disponibilità di proxy nei paesi supportati dal piano gratuito di Gemini può variare. Lo script tenterà di utilizzare proxy dai paesi supportati.

### 🌍 Paesi con Piano Gratuito Gemini
La disponibilità del piano gratuito di Gemini è limitata a certi paesi. Lo script tenterà di utilizzare proxy da questi paesi per sfruttare il piano gratuito. Tuttavia, l'effettiva disponibilità dipende dalla lista di proxy di Webshare al momento dell'esecuzione.

### 🚀 Come Utilizzare
1. Clona il repository:
   ```bash
   git clone https://github.com/tuousername/SentiGuard-AI.git
   ```
2. Naviga nella directory del progetto:
   ```bash
   cd SentiGuard-AI
   ```
3. Esegui lo script:
   ```bash
   python sentiguard_ai.py
   ```
4. Segui le istruzioni sullo schermo per:
   - Inserire le tue chiavi API
   - Selezionare il file di input (CSV o Excel)
   - Scegliere la colonna contenente il testo da analizzare
   - Definire il numero di analisi e i rispettivi prompt

### 📤 Output
- I risultati intermedi vengono salvati in `sentiment_analysis_results.csv`
- I risultati finali vengono salvati in `sentiment_analysis_results_final.xlsx`
- I log degli errori, se presenti, vengono salvati in `error_log.txt`

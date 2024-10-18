import sys
import subprocess
import os
import time
import requests
import pandas as pd
import tkinter as tk
from tkinter import simpledialog, filedialog
from google.ai import generativelanguage_v1beta2 as glm

# ASCII Art
ASCII_ART = """


███████ ███████ ███    ██ ████████ ██  ██████  ██    ██  █████  ██████  ██████       ██████  ███████ ███    ███ ██ ███    ██ ██ 
██      ██      ████   ██    ██    ██ ██       ██    ██ ██   ██ ██   ██ ██   ██     ██       ██      ████  ████ ██ ████   ██ ██ 
███████ █████   ██ ██  ██    ██    ██ ██   ███ ██    ██ ███████ ██████  ██   ██     ██   ███ █████   ██ ████ ██ ██ ██ ██  ██ ██ 
     ██ ██      ██  ██ ██    ██    ██ ██    ██ ██    ██ ██   ██ ██   ██ ██   ██     ██    ██ ██      ██  ██  ██ ██ ██  ██ ██ ██ 
███████ ███████ ██   ████    ██    ██  ██████   ██████  ██   ██ ██   ██ ██████       ██████  ███████ ██      ██ ██ ██   ████ ██ 
                                                                                                                                
                                                                                                                                

"""


def install(package):
    """Installs missing Python packages using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# Ensure all required libraries are installed
libraries = ['pandas', 'google-ai-generativelanguage', 'pillow', 'tkinter', 'requests', 'openpyxl']
for lib in libraries:
    try:
        __import__(lib)
    except ImportError:
        print(f"Installing {lib}...")
        install(lib)
        print(f"{lib} installed successfully.")


def get_proxies(webshare_api_key):
    """Fetches proxies filtered by US country code using the Webshare API."""
    headers = {"Authorization": f"Token {webshare_api_key}"}
    params = {"country_code__in": "US", "mode": "direct"}
    response = requests.get("https://proxy.webshare.io/api/v2/proxy/list/", headers=headers, params=params)
    if response.status_code == 200:
        proxies = response.json()['results']
        pd.DataFrame(proxies).to_csv("proxies_list.csv", index=False)
        print("Proxies fetched and saved to 'proxies_list.csv'.")
        return proxies
    else:
        print("Failed to fetch proxies:", response.text)
        return []


def test_proxy(gemini_api_key, proxies):
    """Tests each proxy to find one that can successfully make API requests to Google Generative AI."""
    test_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": "Explain how AI works"}]}]}
    for proxy in proxies:
        proxy_config = {
            "http": f"http://{proxy['username']}:{proxy['password']}@{proxy['proxy_address']}:{proxy['port']}",
            "https": f"http://{proxy['username']}:{proxy['password']}@{proxy['proxy_address']}:{proxy['port']}"
        }
        try:
            response = requests.post(test_url + f"?key={gemini_api_key}", headers=headers, json=data,
                                     proxies=proxy_config, timeout=10)
            if response.status_code == 200:
                print("Working proxy found:", proxy_config)
                return proxy_config
        except requests.RequestException as e:
            print(f"Proxy failed: {proxy}, Error: {e}")
    return None


def generate_content(prompt: str, working_proxy: dict, api_key: str) -> str:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, headers=headers, json=data, proxies=working_proxy)
    if response.ok:
        return response.json().get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text',
                                                                                                       'No response')
    else:
        raise Exception(f"API request failed: {response.text}")


def generate_prompt(base_prompt: str, review: str) -> str:
    return f"{base_prompt} Questo è il commento da analizzare: {review}"


def main():
    print(ASCII_ART)

    root = tk.Tk()
    root.withdraw()

    gemini_api_key = simpledialog.askstring("API Key", "Enter your Google Generative AI API key:")
    webshare_api_key = simpledialog.askstring("API Key", "Enter your Webshare API key:")

    if not gemini_api_key or not webshare_api_key:
        print("API keys are required to proceed.")
        return

    file_path = filedialog.askopenfilename(
        title="Seleziona il file CSV o Excel",
        filetypes=[("Excel Files", "*.xlsx;*.xls"), ("CSV Files", "*.csv")],
        initialdir=os.getcwd()
    )
    if not file_path:
        print("Nessun file selezionato. Operazione annullata.")
        return

    try:
        data = pd.read_csv(file_path) if file_path.endswith('.csv') else pd.read_excel(file_path)
    except Exception as e:
        print(f"Errore nel caricamento del file: {e}")
        return

    columns = list(data.columns)
    print("Colonne disponibili nel dataset:", columns)
    review_column = simpledialog.askstring("Input", "Indica il nome della colonna che contiene le recensioni:",
                                           initialvalue='review text')
    if not review_column or review_column not in columns:
        print(f"Colonna '{review_column}' non trovata. Operazione annullata.")
        return

    num_analyses = simpledialog.askinteger("Input", "Quante analisi desideri eseguire?")
    if not num_analyses or num_analyses <= 0:
        print("Numero di analisi non valido. Operazione annullata.")
        return

    for i in range(num_analyses):
        column_title = simpledialog.askstring("Input", f"Inserisci il titolo per l'analisi {i + 1}:")
        if column_title:
            data[column_title] = ''

    prompts = []
    for i in range(num_analyses):
        base_prompt = simpledialog.askstring("Input", f"Inserisci il prompt base per l'analisi {i + 1}:")
        prompts.append(base_prompt)

    print("Le seguenti colonne saranno popolate con i risultati dell'analisi:", data.columns[-num_analyses:])
    confirm = simpledialog.askstring("Input", "Confermi di voler procedere con l'analisi (sì/no)?", initialvalue='sì')
    if confirm.lower() != 'sì':
        print("Operazione annullata.")
        return

    proxies = get_proxies(webshare_api_key)
    working_proxy = test_proxy(gemini_api_key, proxies)
    if not working_proxy:
        print("No working proxy found.")
        return

    error_log = []

    for i, row in data.iterrows():
        print(f"\nProcessando riga {i + 1}")
        print(f"Contenuto della riga: {row[review_column]}")

        for j, prompt in enumerate(prompts):
            full_prompt = generate_prompt(prompt, row[review_column])
            try:
                print(f"Analisi {j + 1}...")
                response_text = generate_content(full_prompt, working_proxy, gemini_api_key)
                data.at[i, data.columns[-num_analyses + j]] = response_text

                print(f"Risposta dell'analisi {j + 1}:")
                print(response_text)

                # Salvataggio progressivo in formato CSV
                data.to_csv("sentiment_analysis_results.csv", index=False)
            except Exception as e:
                print(f"Errore durante la richiesta per la riga {i + 1}, analisi {j + 1}: {str(e)}")
                error_log.append(f"Riga {i + 1}, Analisi {j + 1}: {str(e)}")
            time.sleep(4)

    # Salvataggio finale in formato XLSX
    data.to_excel("sentiment_analysis_results_final.xlsx", index=False, engine='openpyxl')
    print("Analisi completata. Risultati salvati in 'sentiment_analysis_results_final.xlsx'")

    with open("error_log.txt", "w") as error_file:
        for error in error_log:
            error_file.write(error + "\n")
    if error_log:
        confirm_close = simpledialog.askstring("Input", "Sono stati riscontrati errori. Vuoi chiudere (sì/no)?",
                                               initialvalue='sì')
        if confirm_close.lower() != 'sì':
            print("Review gli errori nel file 'error_log.txt'.")
            return


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Errore: {str(e)}")
    finally:
        input("Premi invio per chiudere il terminale...")

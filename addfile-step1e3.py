import os
import shutil
import csv
import argparse

# Definisco le estensioni dei file per ciascuna tipologia
audio_est = ['.mp3', '.wav', '.flac']
docs_est = ['.txt', '.pdf', '.odt', '.docx']
images_est = ['.png', '.jpg', '.jpeg', '.gif']

# Funzione per determinare la categoria del file
def categoria_file(nome_file):
    est = os.path.splitext(nome_file)[1].lower()
    if est in audio_est:
        return 'audio'
    elif est in docs_est:
        return 'docs'
    elif est in images_est:
        return 'images'
    else:
        return None

# Funzione principale
def main(nome_file):
    # Percorso della cartella principale
    cartella_principale = r'C:\Users\adryc\files\files'

    # Cambio la directory corrente
    os.chdir(cartella_principale)

    # Percorso del file di recap
    recap_file = 'recap.csv'

    # Verifico l'esistenza del file da spostare
    if not os.path.exists(nome_file):
        print(f"Errore: il file '{nome_file}' non esiste.")
        return

    # Verifico l'esistenza del file recap.csv e creo l'intestazione se non esiste
    if not os.path.exists(recap_file):
        with open(recap_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'Tipo', 'Dimensione (byte)'])

    # Apro il file recap.csv in modalità append
    with open(recap_file, mode='a', newline='') as file:
        writer = csv.writer(file)

        file_path = os.path.join(cartella_principale, nome_file)
        file_type = categoria_file(nome_file)
        
        if file_type:
            target_folder = os.path.join(cartella_principale, file_type)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, nome_file))
            
            # Ottengo informazioni sul file
            file_size = os.path.getsize(os.path.join(target_folder, nome_file))
            
            # Stampo le informazioni sul file
            print(f"Nome: {nome_file}, Tipo: {file_type}, Dimensione: {file_size} byte")
            
            # Scrivo le informazioni nel file recap.csv
            writer.writerow([nome_file, file_type, file_size])

# Configurazione dell'interfaccia a linea di comando
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sposta un file nella sua sottocartella di competenza e aggiorna il recap.")
    parser.add_argument("nome_file", type=str, help="Nome del file da spostare ")
    args = parser.parse_args()
    
    main(args.nome_file)

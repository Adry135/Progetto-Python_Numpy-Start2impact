import argparse
import os
import csv
import sys
import shutil

#creo parser
parser = argparse.ArgumentParser()
#specifico unico argomento obbligatorio
parser.add_argument('filename', type=str, help='nome del file da aggiungere')
#parso e controllo argomenti
args = parser.parse_args()

#mi sposto nella cartella di lavoro
os.chdir('files')

#recupero argomento filename; se questo non si riferisce ad un file esistente...
filename = args.filename
if not os.path.exists(filename):
    print(f'Il file <{filename}> non esiste.')#...informo l'utente
    sys.exit(0)#ed esco

#se il file esiste, proseguo come nello script dello step 1
name, ext = os.path.splitext(filename)

for dirname in ['audio', 'docs', 'images']:
    if not os.path.exists(dirname):
        os.makedirs(dirname)

img_exts = ['.jpeg', '.jpg', '.png']
doc_exts = ['.txt', '.odt']
audio_exts = ['.mp3']

if not os.path.exists('recap.csv'):
    recap = open('recap.csv', 'w', newline='')
    writer = csv.writer(recap)
    writer.writerow(['name', 'type', 'size (B)'])
else:
    recap = open('recap.csv', 'a', newline='')
    writer = csv.writer(recap)

if ext in img_exts:    
    print(f'Aggiungo il file <{name}> alla cartella <images> e aggiorno il recap.')
    size = os.path.getsize(filename)
    writer.writerow([name, 'image', size])
    shutil.move(filename, 'images/')

elif ext in doc_exts:    
    print(f'Aggiungo il file <{name}> alla cartella <docs> e aggiorno il recap.')#informo l'utente dell'operazione
    size = os.path.getsize(filename)
    writer.writerow([name, 'docs', size])
    shutil.move(filename, 'docs/')

elif ext in audio_exts:    
    print(f'Aggiungo il file <{name}> alla cartella <audio> e aggiorno il recap.')
    size = os.path.getsize(filename)
    writer.writerow([name, 'audio', size])
    shutil.move(filename, 'audio/')

else:
    print('Formato non riconosciuto.')

recap.close()

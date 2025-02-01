import csv

# Specifica i nomi dei file di input e output
input_file = 'input.tsv'   # File sorgente con separatore tab
output_file = './TradingML/input.csv' # File di destinazione con separatore virgola

# Apriamo entrambi i file: in lettura per il file di input e in scrittura per il file di output
with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    
    # Leggiamo il file di input specificando che il delimitatore è il carattere di tabulazione
    tsv_reader = csv.reader(infile, delimiter='\t')
    # Creiamo il writer per il file di output con il delimitatore virgola
    csv_writer = csv.writer(outfile, delimiter=',')
    
    # Copiamo riga per riga
    for row in tsv_reader:
        csv_writer.writerow(row)

print(f"Conversione completata. File salvato come {output_file}")
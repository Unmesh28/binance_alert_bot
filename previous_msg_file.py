import csv

def createNewFile (filename) :
    with open(filename, 'x') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['tickerName', '1m', '5m', '15m', '1h', '4h', '6h', '12h', '1d', '1w', '1month'])
    output_file.close()
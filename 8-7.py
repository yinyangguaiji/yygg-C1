def make_album(name,album,number=''):
    singer = {}
    singer['name'] = name
    singer['album'] = album
    if number:
        singer['number of album'] = number
    return singer
print(make_album('Taylor Swift','Fearless'))
print(make_album('Madonna Ciccone','Vogue'))
print(make_album('Britney Sprars','Toxic','50'))

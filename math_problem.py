# La afirmación es la siguiente:
"""Si uno dobla una hoja de papel de 0.1 mm de grosor
y logra doblarla 50 veces, el grosor del resultado
ocuparía la distancia de la Tierra al sol."""
# Source: https://www.youtube.com/watch?v=jej8qlzlAGw&feature=youtu.be
# Distancia media desde la Tierra al sol: 149.597.870.700 m

distancia = 149597870700
grosor = 0.0001 # en metros.

for i in range(0, 50):
    grosor = grosor + grosor

print grosor > distancia

print distancia
print ("%.0f" % grosor)

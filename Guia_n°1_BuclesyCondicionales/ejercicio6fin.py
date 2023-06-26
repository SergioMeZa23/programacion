#ejercicio 6 reloj 
#se detiene a las 23:59:59

for hora in range(24):
    for minuto in range(60):
        for segundos in range(60):
            print(f"{hora:02}:{minuto:02}:{segundos:02}")
               
            
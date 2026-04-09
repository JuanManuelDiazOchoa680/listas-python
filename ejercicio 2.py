nombres = ['Rolando', 'Juan Diego', 'Andres', 'Ivdejel', 'Robinson']
edades = [15, 15, 15, 15, 17]
musica = ['Reggaeton', 'Cumbia', 'Vallenato', 'Salsa', 'Vocaloid']

promedio = sum(edades) / len(edades)
print('Promedio de edad:', promedio)

mayores = [edad for edad in edades if edad > 15]
print('Edades > 15:', mayores)

fans_rock = [gen for gen in musica if gen == 'Rock']
print('Total fans rock:', len(fans_rock))
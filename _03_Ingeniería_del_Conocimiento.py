peliculas = {
    'Pelicula1': ['Aventura', 'Acci�n'],
    'Pelicula2': ['Comedia'],
    'Pelicula3': ['Aventura', 'Fantas�a'],
    'Pelicula4': ['Comedia', 'Romance'],
    'Pelicula5': ['Acci�n']
}

# Base de conocimiento: Usuarios y sus preferencias
usuarios = {
    'Usuario1': {'Pelicula1', 'Pelicula3'},
    'Usuario2': {'Pelicula2', 'Pelicula4'},
    'Usuario3': {'Pelicula3', 'Pelicula5'}
}

# Recomendaci�n de pel�culas basada en intereses del usuario
def recomendar_peliculas(usuario):
    recomendaciones = set()
    for pelicula, generos in peliculas.items():
        if not peliculas_vistas(usuario, pelicula):
            for genero in generos:
                if tiene_interes(usuario, genero):
                    recomendaciones.add(pelicula)
                    break
    return recomendaciones

# Funci�n para verificar si un usuario ha visto una pel�cula
def peliculas_vistas(usuario, pelicula):
    return pelicula in usuarios.get(usuario, set())

# Funci�n para verificar si un usuario tiene inter�s en un g�nero
def tiene_interes(usuario, genero):
    for pelicula in usuarios.get(usuario, set()):
        if genero in peliculas[pelicula]:
            return True
    return False

# Ejemplo de recomendaci�n para Usuario1
usuario = 'Usuario1'
recomendaciones = recomendar_peliculas(usuario)
print(f"Recomendaciones para {usuario}: {recomendaciones}")

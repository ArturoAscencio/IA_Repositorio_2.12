reglas_diagnosticas = {
    "Regla 1": ["S�ntoma A", "S�ntoma B", "S�ntoma C"],
    "Regla 2": ["S�ntoma D", "S�ntoma E"],
    "Regla 3": ["S�ntoma F", "S�ntoma G", "S�ntoma H"]
}

reglas_causales = {
    "S�ntoma A": ["Causa X"],
    "S�ntoma B": ["Causa Y"],
    "S�ntoma C": ["Causa Z"],
    "S�ntoma D": ["Causa X"],
    "S�ntoma E": ["Causa Z"],
    "S�ntoma F": ["Causa Y"],
    "S�ntoma G": ["Causa X"],
    "S�ntoma H": ["Causa Z"]
}

# Funci�n para diagnosticar
def diagnosticar(sintomas):
    causas = set()
    for sintoma in sintomas:
        if sintoma in reglas_diagnosticas:
            causas.update(reglas_diagnosticas[sintoma])
    return causas

# Funci�n para encontrar causas
def encontrar_causas(sintoma):
    if sintoma in reglas_causales:
        return reglas_causales[sintoma]
    else:
        return [sintoma]

# Ejemplo de diagn�stico
sintomas_observados = ["S�ntoma A", "S�ntoma B"]
causas = diagnosticar(sintomas_observados)
print("Posibles causas basadas en los s�ntomas observados:", causas)

# Ejemplo de b�squeda de causas
sintoma = "S�ntoma A"
causas = encontrar_causas(sintoma)
print(f"Causas de {sintoma}:", causas)

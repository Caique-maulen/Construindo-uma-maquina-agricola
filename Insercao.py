from crud_operations import inserir_leitura, listar_leituras

# Simulação de dados do ESP32 (copiados manualmente do monitor serial)
dados_simulados = [
    ("L001", 6.5, "pH", "S01"),
    ("L002", 1, "Fósforo", "S02"),
    ("L003", 0, "Potássio", "S03"),
    ("L004", 40.3, "%", "S04")
]

for leitura in dados_simulados:
    inserir_leitura(*leitura)

print("Leituras inseridas:")
listar_leituras()
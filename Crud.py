import sqlite3
from datetime import datetime

def connect():
    return sqlite3.connect('farmtech.db')

def inserir_leitura(id_leitura, valor, unidade, id_sensor):
    conn = connect()
    cursor = conn.cursor()
    data_hora = datetime.now()
    cursor.execute("""
        INSERT INTO LEITURA_SENSOR (ID_Leitura, Data_Hora, Valor_Leitura, Unidade_Medida, ID_Sensor)
        VALUES (?, ?, ?, ?, ?)""",
        (id_leitura, data_hora, valor, unidade, id_sensor)
    )
    conn.commit()
    conn.close()

def listar_leituras():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM LEITURA_SENSOR")
    leituras = cursor.fetchall()
    for leitura in leituras:
        print(leitura)
    conn.close()

def atualizar_valor_leitura(id_leitura, novo_valor):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE LEITURA_SENSOR SET Valor_Leitura = ? WHERE ID_Leitura = ?
    """, (novo_valor, id_leitura))
    conn.commit()
    conn.close()

def remover_leitura(id_leitura):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM LEITURA_SENSOR WHERE ID_Leitura = ?", (id_leitura,))
    conn.commit()
    conn.close()

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

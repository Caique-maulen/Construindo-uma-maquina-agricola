import sqlite3

conn = sqlite3.connect('farmtech.db')
cursor = conn.cursor()

# Tabela Sensor
cursor.execute("""
CREATE TABLE IF NOT EXISTS Sensor (
    ID_Sensor TEXT PRIMARY KEY,
    Tipo TEXT,
    Numero_Serie TEXT,
    Data_Instalacao DATE,
    Status TEXT,
    ID_Cultura TEXT
)
""")

# Tabela Leitura Sensor
cursor.execute("""
CREATE TABLE IF NOT EXISTS LEITURA_SENSOR (
    ID_Leitura TEXT PRIMARY KEY,
    Data_Hora DATETIME,
    Valor_Leitura REAL,
    Unidade_Medida TEXT,
    ID_Sensor TEXT,
    FOREIGN KEY (ID_Sensor) REFERENCES Sensor(ID_Sensor)
)
""")

conn.commit()
conn.close()
print("Banco de dados e tabelas criados com sucesso.")

 1. Objetivo do Projeto
Desenvolver um sistema inteligente de irrigação baseado em sensores agrícolas simulados, com foco em:

Coleta de dados ambientais (pH, umidade, nutrientes).

Decisões automatizadas de irrigação.

Armazenamento e análise dos dados via banco de dados SQL.

Criação de interface de manipulação de dados (CRUD).

2. Plataforma de Simulação (Wokwi)
Componentes simulados:

Sensor de Umidade (DHT22) – simula a umidade do solo em tempo real.

Sensor de pH (LDR) – usa a variação de luz como analogia para valores de pH (0 a 14).

Sensor de Fósforo (botão) – representa a presença/ausência de fósforo (1/0).

Sensor de Potássio (botão) – funciona da mesma forma que o de fósforo.

ESP32 – microcontrolador central que processa os dados.

Relé + LED – simula o acionamento da bomba de irrigação.

Lógica embarcada:

Quando a umidade está abaixo de um limite ideal, o relé ativa a bomba.

O LED embutido acende quando a irrigação está ativa.

Os dados são enviados ao monitor serial.

 3. Modelagem de Dados (MER)
MER apresentado:

Entidade Cultura: define os parâmetros ideais (pH, umidade, nutrientes).

Entidade Sensor: identifica cada sensor vinculado a uma cultura.

Entidade LEITURA_SENSOR: armazena leituras em tempo real.

Entidade Irrigacao: representa eventos de irrigação registrados.

Entidade Aplicacao_Nutrientes: controla os registros de nutrientes aplicados.

Relacionamentos:

Cada sensor está vinculado a uma cultura.

Leituras de sensores estão associadas a sensores específicos.

As ações de irrigação e aplicação de nutrientes estão ligadas a culturas.

 4. Armazenamento SQL com Python
Tecnologia usada: SQLite + Python

Scripts desenvolvidos:

database_setup.py: cria a estrutura do banco de dados.

crud_operations.py: implementa as operações CRUD.

simular_insercao.py: simula inserções com dados vindos do ESP32.

Operações CRUD:

Operação	Explicação
Create	Inserção de leitura simulada (ID, valor, sensor, data)
Read	Consulta de todas as leituras armazenadas
Update	Atualização de valores incorretos ou corrigidos
Delete	Remoção de leituras obsoletas ou inválidas

 5. Justificativa da Estrutura do Banco
Por que usar essa estrutura?

O projeto exige rastreabilidade: cada leitura deve estar associada a um sensor e cultura.

As leituras são contínuas: o modelo relacional facilita consultas temporais e filtragens.

A normalização evita redundância: sensores, leituras, irrigação e nutrientes estão separados.

Facilita futuras integrações com painéis de visualização ou APIs.

 Conclusão
Este projeto mostra como a combinação de hardware embarcado, simulação e armazenamento em banco de dados pode criar uma solução realista e escalável para agricultura de precisão, mesmo com recursos limitados e utilizando ferramentas gratuitas como Wokwi e SQLite.




import pandas as pd
import zipfile as zip

directory = '/Users/marianamilhomem/Library/CloudStorage/OneDrive-Personal/Projects/Portfolio/bike-share-success-project/files/'
prefixes = ['202401', '202402', '202403', '202404', '202405', '202406', '202407', '202408', '202409', '202410', '202411', '202412']
sufix = '-divvy-tripdata.zip'

archives =[]

for i in range(len(prefixes)):
    archives.append(directory+prefixes[i]+sufix)
print(archives)

with zip.ZipFile(archives[0], mode='r') as myzip:
    myzip.printdir

## Próximos passos: 

# 1. Abrir os .zip e criar DataFrames pandas a partir dos .csv
# 2. Criar colunas de "tempo de viagem" e "dia da semana"
# 3. Verificar a integridade dos dados e documentar qualquer manipulação e limpeza feita.
# 4. Organize e formate os dados.
# 5. Realize cálculos descritivos, como médias e máximos de tempos de viagem.
# 6. Crie tabelas dinâmicas para visualizar padrões, como a média de tempo de viagem por tipo de usuário.
# importar as bibliotecaas

import pandas as pd              # manipulação e análise de dados. 
import matplotlib.pyplot as plt  #criar gráficos e figuras 
import seaborn as sns            # biblioteca de visualização de dados.
import re                        # biblioteca para manipulação de strings.

# importar dataframe 
caminho1 = r'C:\Users\RODRIGUES\Desktop\ANALISE_EXPLORATORIO\producao2017.csv'  
dados1 = pd.read_csv(caminho1)

# print(dados1.dtypes)
print(dados1.head())


# seleção e Limpeza de Dados

dadosespecificos = ['Ano', 'Produção de Óleo (m³)', 'Produção de Gás Não Associado (Mm³)', 'Produção de Água (m³)' ]
dataframe1 = dados1[dadosespecificos].copy() #cria uma cópia do dataframe para não afetar o original

# 1. Substituir vírgulas por pontos nas colunas e converter em numero
# Substituir vírgulas por pontos e converter para numérico
for coluna in dadosespecificos:
    dataframe1[coluna] = dataframe1[coluna].astype(str).str.replace(',', '.', regex=True)  # Substituir vírgulas por pontos
    dataframe1[coluna] = pd.to_numeric(dataframe1[coluna], errors='coerce')  # Converter para numérico

dataframe1.fillna(0, inplace=True)  # Substituir NaN por 0

print(dataframe1.dtypes)   
print (dataframe1.head(100))

# importar 2ª dataframe 

caminho2=r'C:\Users\RODRIGUES\Desktop\ANALISE_EXPLORATORIO\PRODUÇÃO_2018_4TRI.csv'
dados2= pd .read_csv(caminho2)

print(dados2.head())


# Seleção e limpeza de dados

# Seleção de colunas específicas e criação de um DataFrame com a cópia dos dados
dadosespecificos2 = ['Ano', 'Produção de Óleo (m³)', 'Produção de Gás Não Associado (Mm³)', 'Produção de Água (m³)']
dataframe2 = dados2[dadosespecificos2].copy()  # Cria a cópia com as colunas especificadas

 # mudar a coluna ano de caracter object para inteiro
dataframe2['Ano'] = dataframe2['Ano'].astype(int)

# 1. Substituir vírgulas por pontos nas colunas e converter em numero
# Substituir vírgulas por pontos e converter para numérico
for coluna in dadosespecificos2:
    dataframe2[coluna] = dataframe2[coluna].astype(str).str.replace(',', '.', regex=True)  # Substituir vírgulas por pontos
    dataframe2[coluna] = pd.to_numeric(dataframe2[coluna], errors='coerce')  # Converter para numérico

dataframe2.fillna(0, inplace=True)  # Substituir NaN por 0
 
print(dataframe2.dtypes)
# Exibir os primeiros registros para confirmar o filtro
print(dataframe2.head(10))


# Importar 3ª dataframe 

caminho3 =r'C:\Users\RODRIGUES\Desktop\ANALISE_EXPLORATORIO\PRODUCAO_FLUIDO_2019.csv'
dados3 = pd.read_csv(caminho3, sep=';')
print(dados3.head())

# Selecionar as colunas relevantes criando uma cópia explícita
dadosespecificos3 = ['Ano', 'Producao_Oleo(metro_cubico)', 'Produção de Gás Não Associado (Mm³)', 'Produção de Água (m³)']
dataframe3 = dados3[dadosespecificos3].copy()  # Use .copy() para evitar SettingWithCopyWarning


# 1. Substituir vírgulas por pontos nas colunas e converter em numero
# Substituir vírgulas por pontos e converter para numérico
for coluna in dadosespecificos3:
    dataframe3[coluna] = dataframe3[coluna].astype(str).str.replace(',', '.', regex=True)  # Substituir vírgulas por pontos
    dataframe3[coluna] = pd.to_numeric(dataframe3[coluna], errors='coerce')  # Converter para numérico

dataframe3.fillna(0, inplace=True)  # Substituir NaN por 0

# Renomear a coluna para manter consistência
dataframe3 = dataframe3.rename(columns={'Producao_Oleo(metro_cubico)': 'Produção de Óleo (m³)'})

print(dataframe3.dtypes)
# Exibir o DataFrame ajustado
print(dataframe3.head())


#Combine os dados dos três dataframes em um único dataframe
# Convertemos a lista em dataframe
df_2017 = pd.DataFrame(dataframe1)  
df_2018 = pd.DataFrame(dataframe2)
df_2019 = pd.DataFrame(dataframe3)


# 2. Concatenar os DataFrames
df_total = pd.concat([df_2017, df_2018, df_2019], ignore_index=True)

print(df_total.dtypes)  # Verificar os tipos de dados
print(df_total.head())  # Visualizar os primeiros registros


# Exportando o DataFrame para um arquivo CSV

df_total.to_csv('C:\\Users\\RODRIGUES\\Desktop\\ANALISE_EXPLORATORIO.csv', index=True)

# Análise Estatística
# 1. Estatísticas Descritivas
print(df_total.describe()

# Identificar Outliers
import matplotlib.pyplot as plt

plt.boxplot([df_total['Produção de Óleo (m³)'], df_total['Produção de Gás Não Associado (Mm³)'], df_total['Produção de Água (m³)']], tick_labels=['Óleo', 'Gás', 'Água'])
plt.title('Boxplot das Produções')
plt.show()


# Visualização com Gráficos

#  Gráfico de Linha

plt.figure(figsize=(10, 6))
plt.plot(df_total['Ano'], df_total['Produção de Óleo (m³)'], label='Produção de Óleo', color='blue')
plt.plot(df_total['Ano'], df_total['Produção de Gás Não Associado (Mm³)'], label='Produção de Gás', color='green')
plt.plot(df_total['Ano'], df_total['Produção de Água (m³)'], label='Produção de Água', color='orange')

plt.title('Tendência de Produções ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Produção')
plt.legend()
plt.grid(True)
plt.show()

# Série Temporal

# gráficos interativos para identificar padrões sazonais ou tendências de longo prazo.

plt.figure(figsize=(10, 6))
plt.scatter(df_total['Ano'], df_total['Produção de Óleo (m³)'], label='Produção de Óleo', color='blue')
plt.title("Distribuição anual dos Dados")
plt.show()


# Histograma

# visualizar a distribuição dos dados, como valores concentrados ou dispersos.

plt.figure(figsize=(10, 6))
plt.hist(df_total['Produção de Óleo (m³)'], bins=20, alpha=0.7, label='Óleo', color='blue')
plt.hist(df_total['Produção de Gás Não Associado (Mm³)'], bins=20, alpha=0.7, label='Gás', color='green')
plt.hist(df_total['Produção de Água (m³)'], bins=20, alpha=0.7, label='Água', color='orange')

plt.title('Distribuição de Produções')
plt.xlabel('Produção (m³)')
plt.ylabel('Frequência')
plt.legend()
plt.show()



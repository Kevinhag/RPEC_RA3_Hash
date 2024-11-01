import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

csv = pd.read_csv("dadosHash2.csv", encoding='utf-8')

def formatadorInt(x, pos):
    if x >= 1:
        return f'{int(x)}'
    else:
        return f'{x:.1f}'

csv.columns = csv.columns.str.strip().str.lower()

print("Colunas disponíveis no CSV:")
print(csv.columns.tolist())

csv.rename(columns={
    'funcaohash': 'FuncaoHash',
    'tamanhoconjunto': 'TamanhoConjunto',
    'tamanhotabela': 'TamanhoTabela',
    'tempoinsercao(ms)': 'TempoInsercao',
    'colisoesinsercao': 'ColisoesInsercao',
    'tempobusca(ms)': 'TempoBusca',
    'comparacoesbusca': 'ComparacoesBusca'
}, inplace=True)

csv['TempoInsercao'] = csv['TempoInsercao'].str.replace('ms', '').str.strip().astype(int)
csv['TempoBusca'] = csv['TempoBusca'].str.replace('ms', '').str.strip().astype(int)
csv['TamanhoConjunto'] = csv['TamanhoConjunto'].astype(int)
csv['TamanhoTabela'] = csv['TamanhoTabela'].astype(int)
csv['ColisoesInsercao'] = csv['ColisoesInsercao'].astype(int)
csv['ComparacoesBusca'] = csv['ComparacoesBusca'].astype(int)

if csv.isnull().values.any():
    print("\nRemovendo linhas com valores nulos...")
    csv.dropna(inplace=True)

# calcular a média 
csv_media = csv.groupby(['FuncaoHash', 'TamanhoConjunto', 'TamanhoTabela']).agg({
    'TempoInsercao': 'mean',
    'ColisoesInsercao': 'mean',
    'TempoBusca': 'mean',
    'ComparacoesBusca': 'mean'
}).reset_index()

print("\nDados com médias calculadas:")
print(csv_media.head())

sns.set_theme(style="whitegrid")

formatter = FuncFormatter(formatadorInt)

# ========================== MÉDIA DO TEMPO DE INSERÇÃO POR CONJUNTO ==========================

plt.figure(figsize=(12, 8))
sns.barplot(
    data=csv_media,
    x="TamanhoConjunto",
    y="TempoInsercao",
    hue="FuncaoHash",
    palette='muted',
    ci=95, 
    capsize=.4,
    errwidth=1
)

plt.title("Média do Tempo de Inserção", fontsize=16)
plt.xlabel("Tamanho do Conjunto", fontsize=14)
plt.ylabel("Média Tempo de Inserção (ms)", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Função Hash')
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(formatter)

# Anotações nas barras
for p in plt.gca().patches:
    height = p.get_height()
    if height > 0:
        plt.annotate(f'{int(height)}',
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=8, color='black',
                        xytext=(0, 5), textcoords='offset points', bbox=dict(facecolor='white', alpha=1, edgecolor='none'))
plt.tight_layout()
plt.show()

# ========================== MÉDIA DO TEMPO DE INSERÇÃO POR TABELA ==========================

plt.figure(figsize=(12, 8))
sns.barplot(
    data=csv_media,
    x="TamanhoTabela",
    y="TempoInsercao",
    hue="FuncaoHash",
    palette='muted',
    ci=95, 
    capsize=.4,
    errwidth=1
)

plt.title("Média do Tempo de Inserção", fontsize=16)
plt.xlabel("Tamanho da Tabela", fontsize=14)
plt.ylabel("Média Tempo de Inserção (ms)", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Função Hash')
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(formatter)

# Anotações nas barras
for p in plt.gca().patches:
    height = p.get_height()
    if height > 0:
        plt.annotate(f'{int(height)}',
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=8, color='black',
                        xytext=(0, 5), textcoords='offset points', bbox=dict(facecolor='white', alpha=1, edgecolor='none'))
plt.tight_layout()
plt.show()

# ========================== MÉDIA DO NÚMERO DE COLISÕES POR CONJUNTO ==========================

plt.figure(figsize=(12, 8))
sns.barplot(
    data=csv_media,
    x="TamanhoConjunto",
    y="ColisoesInsercao",
    hue="FuncaoHash",
    palette='muted',
    ci=95,
    capsize=.4,
    errwidth=1
)

plt.title("Média do Número de Colisões na Inserção", fontsize=16)
plt.xlabel("Tamanho do Conjunto", fontsize=14)
plt.ylabel("Média de Colisões na Inserção", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Função Hash')
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(formatter)

# Anotações nas barras
for p in plt.gca().patches:
    height = p.get_height()
    if height > 0:
        plt.annotate(f'{int(height)}',
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=8, color='black',
                        xytext=(0, 5), textcoords='offset points', bbox=dict(facecolor='white', alpha=1, edgecolor='none'))

plt.tight_layout()
plt.show()

# ========================== MÉDIA DO NÚMERO DE COLISÕES POR TABELA ==========================

plt.figure(figsize=(12, 8))
sns.barplot(
    data=csv_media,
    x="TamanhoTabela",
    y="ColisoesInsercao",
    hue="FuncaoHash",
    palette='muted',
    ci=95,
    capsize=.4,
    errwidth=1
)

plt.title("Média do Número de Colisões na Inserção", fontsize=16)
plt.xlabel("Tamanho da Tabela", fontsize=14)
plt.ylabel("Média de Colisões na Inserção", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Função Hash')
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(formatter)

# Anotações nas barras
for p in plt.gca().patches:
    height = p.get_height()
    if height > 0:
        plt.annotate(f'{int(height)}',
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=8, color='black',
                        xytext=(0, 5), textcoords='offset points', bbox=dict(facecolor='white', alpha=1, edgecolor='none'))

plt.tight_layout()
plt.show()

# ========================== MÉDIA DO TEMPO DE BUSCA POR CONJUNTO ==========================

plt.figure(figsize=(12, 8))
sns.barplot(
    data=csv_media,
    x="TamanhoConjunto",
    y="TempoBusca",
    hue="FuncaoHash",
    palette='muted',
    ci=95,
    capsize=.4,
    errwidth=1
)

plt.title("Média do Tempo de Busca", fontsize=16)
plt.xlabel("Tamanho do Conjunto", fontsize=14)
plt.ylabel("Média Tempo de Busca (ms)", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Função Hash')
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(formatter)

# Anotações nas barras
for p in plt.gca().patches:
    height = p.get_height()
    if height > 0:
        plt.annotate(f'{height:.2f}',
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=8, color='black',
                        xytext=(0, 5), textcoords='offset points', bbox=dict(facecolor='white', alpha=1, edgecolor='none'))

plt.tight_layout()
plt.show()

# ========================== MÉDIA DO TEMPO DE BUSCA POR TABELA ==========================

plt.figure(figsize=(12, 8))
sns.barplot(
    data=csv_media,
    x="TamanhoTabela",
    y="TempoBusca",
    hue="FuncaoHash",
    palette='muted',
    ci=95,
    capsize=.4,
    errwidth=1
)

plt.title("Média do Tempo de Busca", fontsize=16)
plt.xlabel("Tamanho da Tabela", fontsize=14)
plt.ylabel("Média Tempo de Busca (ms)", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Função Hash')
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(formatter)

# Anotações nas barras
for p in plt.gca().patches:
    height = p.get_height()
    if height > 0:
        plt.annotate(f'{height:.2f}',
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=8, color='black',
                        xytext=(0, 5), textcoords='offset points', bbox=dict(facecolor='white', alpha=1, edgecolor='none'))

plt.tight_layout()
plt.show()

# ========================== MÉDIA DO NÚMERO DE COMPARAÇÕES NA BUSCA POR CONJUNTO ==========================

plt.figure(figsize=(12, 8))
sns.barplot(
    data=csv_media,
    x="TamanhoConjunto",
    y="ComparacoesBusca",
    hue="FuncaoHash",
    palette='muted',
    ci=95,
    capsize=.4,
    errwidth=1
)

plt.title("Média do Número de Comparações na Busca", fontsize=16)
plt.xlabel("Tamanho do Conjunto", fontsize=14)
plt.ylabel("Média de Comparações na Busca", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Função Hash')
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(formatter)

# Anotações nas barras
for p in plt.gca().patches:
    height = p.get_height()
    if height > 0:
        plt.annotate(f'{int(height)}',
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=8, color='black',
                        xytext=(0, 5), textcoords='offset points', bbox=dict(facecolor='white', alpha=1, edgecolor='none'))

plt.tight_layout()
plt.show()
# ========================== MÉDIA DO NÚMERO DE COMPARAÇÕES NA BUSCA POR TABELA ==========================

plt.figure(figsize=(12, 8))
sns.barplot(
    data=csv_media,
    x="TamanhoTabela",
    y="ComparacoesBusca",
    hue="FuncaoHash",
    palette='muted',
    ci=95,
    capsize=.4,
    errwidth=1
)

plt.title("Média do Número de Comparações na Busca", fontsize=16)
plt.xlabel("Tamanho da Tabela", fontsize=14)
plt.ylabel("Média de Comparações na Busca", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Função Hash')
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(formatter)

# Anotações nas barras
for p in plt.gca().patches:
    height = p.get_height()
    if height > 0:
        plt.annotate(f'{int(height)}',
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=8, color='black',
                        xytext=(0, 5), textcoords='offset points', bbox=dict(facecolor='white', alpha=1, edgecolor='none'))

plt.tight_layout()
plt.show()

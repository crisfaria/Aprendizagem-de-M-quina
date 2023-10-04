import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv("dados4.csv")

# 1) Ajustar idades inválidas ou vazias para a moda da amostra
modaIdade = df["age"].mode()[0]
df["age"].fillna(modaIdade, inplace=True)

# Salvar a saída no arquivo Resposta01.txt
with open("Resposta01.txt", "w") as f:
    f.write(f"As idades foram ajustadas. Moda: {modaIdade}")

# 2) Somatório de homens e mulheres
somaHomens = df[df["sex"] == "male"].shape[0]
somaMulheres = df[df["sex"] == "female"].shape[0]

print(f"Somatório de Homens: {somaHomens}")
print(f"Somatório de Mulheres: {somaMulheres}")

# 3) Gráfico de pizza para porcentagem de sobreviventes e não sobreviventes
sobreviventes = df["survived"].value_counts()
labels = ["Não Sobreviventes", "Sobreviventes"]
colors = ["#FF6160", "#35D453"]

plt.pie(sobreviventes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
plt.axis("equal")
plt.title("Porcentagem de Sobreviventes e Não Sobreviventes")
plt.show()

# 4) Gráfico de dispersão de Idade pela Tarifa
plt.scatter(df["age"], df["fare"], alpha=0.5, c="#FF4500")
plt.xlabel("Idade")
plt.ylabel("Tarifa")
plt.title("Gráfico de Dispersão: Idade x Tarifa")
plt.show()

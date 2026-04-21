import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SQLite.csv")

print(df.head())

df.columns = df.columns.str.strip()

df["ca"] = df["prix"] * df["qte"]

ca_produit = df.groupby("produit")["ca"].sum()
ca_produit.plot(kind="bar")

plt.title("CA par produit")
plt.show()

ca_region = df.groupby("region")["ca"].sum()
ca_region.plot(kind="pie", autopct="%1.1f%%")

plt.title("CA par région")
plt.ylabel("")
plt.show()
# Script para carregar os dados de acidentes da PRF
import pandas as pd

# Caminho base dos arquivos
base_path = "data/"

# Leitura dos arquivos CSV
acidentes2021 = pd.read_csv(base_path + "datatran2021.csv", sep=";", encoding="latin1")
acidentes2022 = pd.read_csv(base_path + "datatran2022.csv", sep=";", encoding="latin1")
acidentes2023 = pd.read_csv(base_path + "datatran2023.csv", sep=";", encoding="latin1")
acidentes2024 = pd.read_csv(base_path + "datatran2024.csv", sep=";", encoding="latin1")
acidentes2025 = pd.read_csv(base_path + "datatran2025.csv", sep=";", encoding="latin1")

# Unir todos os datasets
acidentes_total = pd.concat([
    acidentes2021,
    acidentes2022,
    acidentes2023,
    acidentes2024,
    acidentes2025
])

# Mostrar dimensão final
print("Dimensão do dataset final:", acidentes_total.shape)
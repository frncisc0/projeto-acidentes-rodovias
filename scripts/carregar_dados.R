# Carregar datasets de acidentes da PRF
acidentes2021 <- read.csv2("data/datatran2021.csv", fileEncoding="ISO-8859-1")
acidentes2022 <- read.csv2("data/datatran2022.csv", fileEncoding="ISO-8859-1")
acidentes2023 <- read.csv2("data/datatran2023.csv", fileEncoding="ISO-8859-1")
acidentes2024 <- read.csv2("data/datatran2024.csv", fileEncoding="ISO-8859-1")
acidentes2025 <- read.csv2("data/datatran2025.csv", fileEncoding="ISO-8859-1")

# Verificar dimensões dos datasets
dim(acidentes2021)
dim(acidentes2022)
dim(acidentes2023)
dim(acidentes2024)
dim(acidentes2025)

# Unir todos os anos em um único dataset
acidentes_total <- rbind(
  acidentes2021,
  acidentes2022,
  acidentes2023,
  acidentes2024,
  acidentes2025
)

# Verificar dimensão final
dim(acidentes_total)


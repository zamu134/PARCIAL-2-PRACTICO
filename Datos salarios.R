library(readxl)
library(ggplot2)
library(dplyr)
library(httr)

# URL del archivo Excel en GitHub
url <- "https://github.com/zamu134/PARCIAL-2-PRACTICO/raw/main/Datos%20salarios.xlsx"

# Descargar el archivo desde GitHub y cargarlo en R
temp <- tempfile(fileext = ".xlsx")
download.file(url, temp, mode = "wb")
data <- read_excel(temp)

# Limpiar nombres de columnas
colnames(data) <- gsub(" ", "", colnames(data))

# Gráfico 1: Histograma de salarios
ggplot(data, aes(x = Salario)) +
  geom_histogram(binwidth = 1000, fill = "blue", color = "black") +
  theme_minimal() +
  labs(title = "Histograma de Salarios", x = "Salario", y = "Frecuencia")

# Gráfico 2: Gráfico de barras del promedio de salarios por facultad
data %>%
  group_by(Facultad) %>%
  summarize(promedio_salario = mean(Salario, na.rm = TRUE)) %>%
  ggplot(aes(x = Facultad, y = promedio_salario, fill = Facultad)) +
  geom_bar(stat = "identity") +
  theme_minimal() +
  labs(title = "Promedio de Salarios por Facultad", x = "Facultad", y = "Promedio de Salario")

# Gráfico 3: Diagrama de dispersión entre edad y salario
ggplot(data, aes(x = edad, y = Salario)) +
  geom_point(color = "red") +
  theme_minimal() +
  labs(title = "Diagrama de Dispersión: Edad vs Salario", x = "Edad", y = "Salario")

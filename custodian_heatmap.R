# custodian_heatmap.R
# Run with: Rscript custodian_heatmap.R

library(tidyverse)
library(ggplot2)
library(readr)

df <- read_csv("sample_data/custodians_sample.csv")
df$Date <- as.Date(df$Date)

ggplot(df, aes(x = Date, y = Custodian, fill = DocCount)) +
  geom_tile(color = "white", linewidth = 0.5) +
  scale_fill_gradient(low = "lightyellow", high = "darkred") +
  labs(title = "Custodian × Date Volume Heatmap",
       x = "Date", y = "Custodian", fill = "Doc Count") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

ggsave("sample_data/custodian_heatmap_R.png", width = 14, height = 8, dpi = 300)
cat("Heatmap saved as custodian_heatmap_R.png\n")

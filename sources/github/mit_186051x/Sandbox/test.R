library(ggplot2)

# Set value of t
t <- 2

# Create data for standard normal curve
x_vals <- seq(-4, 4, length.out = 1000)
y_vals <- dnorm(x_vals)

# Create a data frame
df <- data.frame(x = x_vals, y = y_vals)

# Plot with shaded area up to t
ggplot(df, aes(x, y)) +
  geom_line(color = "black") +
  geom_area(data = subset(df, x <= t), aes(x, y), fill = "skyblue", alpha = 0.5) +
  geom_vline(xintercept = t, linetype = "dashed", color = "blue") +
  labs(
    title = paste0("Visualizing Φ(", t, ")"),
    x = "Z",
    y = "Density"
  ) +
  theme_minimal()


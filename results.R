veri <- read.csv2(file.choose())
names(veri)

# Faz1
t.test(veri$Faz1_Manuel, veri$Faz1_DL, paired = TRUE)

# Faz2
t.test(veri$Faz1_DL, veri$Faz2_DL)

# BoxPlot
boxplot(veri$Faz1_Manuel,
        veri$Faz1_DL,
        veri$Faz2_DL,
        names = c("Faz1 Manual", "Faz1 DL", "Faz2 DL"),
        ylab = "Cycle Time (sec)",
        main = "Cycle Time Distribution Comparison")

# Scatter Plot
{
  plot(veri$Faz1_Manuel,
       veri$Faz1_DL,
       xlab = "Manual Measurement (sec)",
       ylab = "DL Measurement (sec)",
       main = "Manual vs DL Measurement Comparison",
       pch = 19)
  
  abline(0, 1, col = "red", lwd = 2)
}

# Bland-Altman Plot
avg <- (veri$Faz1_Manuel + veri$Faz1_DL) / 2
diff <- veri$Faz1_Manuel - veri$Faz1_DL

plot(avg, diff,
     xlab = "Average of Manual and DL (sec)",
     ylab = "Difference: Manual - DL (sec)",
     main = "Bland-Altman Plot",
     pch = 19)

abline(h = mean(diff), col = "blue", lwd = 2)
abline(h = mean(diff) + 1.96 * sd(diff), col = "red", lty = 2, lwd = 2)
abline(h = mean(diff) - 1.96 * sd(diff), col = "red", lty = 2, lwd = 2)

legend("topright",
       legend = c("Mean Difference", "95% Limits of Agreement"),
       col = c("blue", "red"),
       lty = c(1, 2),
       lwd = 2)

# Error Bar Plot
{
  means <- c(mean(veri$Faz1_Manuel),
             mean(veri$Faz1_DL),
             mean(veri$Faz2_DL))
  
  sds <- c(sd(veri$Faz1_Manuel),
           sd(veri$Faz1_DL),
           sd(veri$Faz2_DL))
  
  bp <- barplot(means,
                names.arg = c("Faz1 Manual", "Faz1 DL", "Faz2 DL"),
                ylim = c(0, max(means + sds) + 2),
                main = "Mean Cycle Time Comparison",
                ylab = "Seconds")
  
  arrows(bp,
         means - sds,
         bp,
         means + sds,
         angle = 90,
         code = 3,
         length = 0.08)
}

# Cohen's d for Faz 1 
library(effsize)

cohen.d(veri$Faz1_Manuel,
        veri$Faz1_DL,
        paired = TRUE)

# Cohen's d for Faz 2
cohen.d(veri$Faz1_DL,
        veri$Faz2_DL)

effects <- c(0.147, 0.669)

names <- c("Faz1 Manual vs DL", "Faz1 DL vs Faz2 DL")

barplot(effects,
        names.arg = names,
        main = "Effect Size Comparison (Cohen's d)",
        ylab = "Cohen's d",
        ylim = c(0, 1.2))

abline(h = 0.2, lty = 2)
abline(h = 0.5, lty = 2)
abline(h = 0.8, lty = 2)

text(1, 0.18, "Small", pos = 3)
text(1, 0.48, "Medium", pos = 3)
text(1, 0.78, "Large", pos = 3)

# Distribution Comparsion
plot(density(veri$Faz1_Manuel),
     main = "Density Comparison of Cycle Times",
     xlab = "Cycle Time (sec)",
     lwd = 2)

lines(density(veri$Faz1_DL), lwd = 2)
lines(density(veri$Faz2_DL), lwd = 2)

legend("topright",
       legend = c("Faz1 Manual", "Faz1 DL", "Faz2 DL"),
       lty = 1,
       lwd = 2)


bo <- read.csv("bo.csv")
bo_central <- read.csv("bo_central.csv")

bo_mat <- as.matrix(bo)
bo_central_mat <- as.matrix(bo_central)

View(friedman.test(bo_central_mat))
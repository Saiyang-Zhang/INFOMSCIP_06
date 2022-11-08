bo_central <- read.csv("bo_central.csv")

bo_central_mat <- as.matrix(bo_central)

# Part II Q3: Apply friedman test to the centralized BO data
# View(friedman.test(bo_central_mat))

# Part II Q3: Apply Wilcoxon test
ailen_hand <- bo_central["Alien.Hand"]
matched_hand <- bo_central["Matched.Hand"]
mismatched_hand <- bo_central["Mismatched.Hand"]

# View(wilcox.test(alien_hand[, 1], matched_hand[, 1]))
# View(res <- wilcox.test(alien_hand[, 1], mismatched_hand[, 1]))
# View(wilcox.test(matched_hand[, 1], mismatched_hand[, 1]))

# Part
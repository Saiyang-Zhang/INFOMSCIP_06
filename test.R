bo_central <- read.csv("bo_central_mean.csv")


PID <- bo_central["PID"][, 1]
alien_hand <- bo_central["Alien_Hand"][, 1]
matched_hand <- bo_central["Matched_Hand"][, 1]
mismatched_hand <- bo_central["Mismatched_Hand"][, 1]

# Part II Q3: Apply friedman test to the centralized BO data
bo_central_mat <- cbind(alien_hand, matched_hand, mismatched_hand)
rownames(bo_central_mat) <- PID

friedman_res <- friedman.test(bo_central_mat)

# Part II Q3: Apply Wilcoxon test

ah_mah_res <- wilcox.test(alien_hand, matched_hand)
ah_mih_res <- wilcox.test(alien_hand, mismatched_hand)
mah_mih_res <- wilcox.test(matched_hand, mismatched_hand)

View(friedman_res)

# Part
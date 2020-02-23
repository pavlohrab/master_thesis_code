library(dendextend)
library(ape)
library(phylogram)
library(dendsort)

normal <- read.tree("Norm_S136.txt.mafft.treefile") %>% as.phylo() %>%as.dendrogram.phylo()
anomal <- read.tree("Anomal_S136.txt.mafft.2.treefile") %>% as.dendrogram.phylo()

dend_list <- dendlist(normal,anomal)
dend_list %>%
  untangle(method = "ladderize") %>%
  tanglegram(
           lwd = 1.5,
           edge.lwd = 1, center = TRUE,
           margin_inner=19,
           rank_branches = T
           )

cor.dendlist(dend_list, method = "cophenetic")

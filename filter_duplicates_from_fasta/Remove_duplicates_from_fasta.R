library(seqinr)
library(rlist)

fasta <- read.fasta("Fasta.test")
dup <- read.delim("Duplicate.headers", header = F, stringsAsFactors = F)

fasta_new <- names(fasta)
fasta_keep <- c()
for (i in dup[[1]]){
  remove <- fasta_new[grep(paste0(i,'*'),fasta_new)]
  fasta_keep <- c(fasta_keep, fasta[remove[1]])
  fasta[grep(paste0(i,'*'),fasta_new)] = NULL
  fasta_new <- fasta_new[! fasta_new %in% remove]
}

fasta = c(fasta, fasta_keep)
write.fasta(fasta,names = names(fasta),file.out = "With_no_duplicates.fasta")


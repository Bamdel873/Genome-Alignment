from Bio import Align

# Create a pairwise aligner for global alignment
aligner = Align.PairwiseAligner(match_score=1.0)

# Define the sequences for global alignment
seq1 = "GAACT"
seq2 = "GAT"

# Calculate the global alignment score
score = aligner.score(seq1, seq2)
print(f"The score of the global alignment is {score}")

# Get the global alignments
alignments = aligner.align(seq1, seq2)
for alignment in alignments:
    print(alignment)

# Switch to local alignment mode
aligner.mode = 'local'

# Define the sequences for local alignment
seq3 = "AGAACTC"
seq4 = "GAACT"

# Calculate the local alignment score
scorelocal = aligner.score(seq3, seq4)
print(f"The local alignment score is {scorelocal}")

# Get the local alignments
alignlocal = aligner.align(seq3, seq4)
for alignment in alignlocal:
    print(alignment)

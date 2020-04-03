# Constructing Heat Maps to visualize ATAC-Seq results

##### Ravi Mandla

##### Last Updated on 04/03/2020

Heat maps are a great tool to compare the read counts of sequencing experiments in different populations, often used in RNA-seq experiments to visualize the gene expression differences between different populations (there's a great tutorial on doing through the [galaxy project](https://galaxyproject.github.io/training-material/topics/transcriptomics/tutorials/rna-seq-viz-with-heatmap2/tutorial.html)). However, the use of heat maps in such a way is not restricted to just RNA-seq experiments, and can be used in a wide range of sequencing experiments. I recently worked on a project where I was asked to create such a heat map comparing ATAC-seq data from two distinct cell populations, and struggled to find online resources on doing such experiments. I hope this tutorial will be useful for those in similar situations :)

## Steps

The general outline for conducting such an analysis goes as follows...

1. Obtain genomic coordinates for BAM peaks
2. Create a list of consensus sequences, with sequences present in all samples, as well as their read count
3. Use thresholds to limit the amount of consensus sequences one is analyzing
4. Normalize your read counts
5. Standardize the normal values to z-scores
6. Plot the data

## Example

I go through all of the above steps, as well as a tutorial using sampled data in the `tutorial.ipyng` file in Python. Check it out if you get stuck.

## Resources

Here are a bunch of resources I found which helped me with this project:

[The Galaxy Project's RNA-seq heatmap tutorial](https://galaxyproject.github.io/training-material/topics/transcriptomics/tutorials/rna-seq-viz-with-heatmap2/tutorial.html)

[EdgeR User Guide](https://www.bioconductor.org/packages/release/bioc/vignettes/edgeR/inst/doc/edgeRUsersGuide.pdf)

[Dave Tang's EdgeR Normalisation guide](https://davetang.org/muse/2011/01/24/normalisation-methods-for-dge-data/)

[Dave Tang's Pheatmap guide](https://davetang.org/muse/2018/05/15/making-a-heatmap-in-r-with-the-pheatmap-package/)

[Kamil Slowikowski's Pheatmap guide](https://slowkow.com/notes/pheatmap-tutorial/)

[Pheatmap documentation](https://cran.r-project.org/web/packages/pheatmap/pheatmap.pdf)

[Zuguang Gu's ComplexHeatmap Reference Book](https://jokergoo.github.io/ComplexHeatmap-reference/book/)

[Normalizing RNAseq Data](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2010-11-3-r25)

[DESeq2 tutorial](http://bioconductor.org/packages/devel/bioc/vignettes/DESeq2/inst/doc/DESeq2.html)


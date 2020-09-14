#  Data parsing exercise

The code in this repository was writen the next instructions:

The software Ariba is one piece of software that can be used to predict the presence of loci responsible for antimicrobial resistance in bacterial genomes.
After running the software on whole genome data from individual isolates the summary command can be used to summarize the presence and absence of loci across all the isolates. The output is described on this wiki page
Given a
 * [Ariba output file](ariba_amr_output.csv)
 * [NCBI acquired gene metadata file](ncbi_acquired_genes_metadata.csv)

Write code in the programming language of your choice that will parse this data to find those samples that contain loci responsible for conferring cephalosporin or carbapenem resistance.

These are defined as samples that
* contain a locus that has yes or yes_nonunique in the locus column with the `.assembled` suffix
* a coverage of at least 10 in the locus column with the `.ctg_cov` suffix
* the reference sequence described in the column with the `.ref_seq` suffix beginning `NG_*` is associated with a gene described in the NCBI metadata file that is associated with the `CEPHALOSPORIN` or `CARBAPENEM` subclass respectively 

# Multi-Omics Factor Analysis (MOFA) analysis for identifying dysregulated Transcription Factors in Cancer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![JupyterLab](https://img.shields.io/badge/JupyterLab-3.0%2B-orange?style=for-the-badge&logo=jupyter)

**Description**
MOFA is a factor analysis model that provides a general framework for the integration of multi-omic data sets in a completely unsupervised fashion. Intuitively, MOFA can be viewed as a versatile and statistically rigorous generalization of principal component analysis (PCA) to multi-omics data. Given several data matrices with measurements of multiple ‘omics data types on the same or on overlapping sets of samples, MOFA infers an interpretable low-dimensional data representation in terms of (hidden) factors. These learnt factors represent the driving sources of variation across data modalities, thus facilitating the identification of cellular states or disease subgroups.

Once trained, the model output can be used for a range of downstream analyses, including the visualisation of samples in factor space, the automatic annotation of factors using (gene set) enrichment analysis, the identification of outliers (e.g. due to sample swaps) and the imputation of missing values.

Here we use MOFA to perform multi-omic factor analysis on datasets from the CPTAC consortium


**For more details:**

MOFA paper: http://msb.embopress.org/cgi/doi/10.15252/msb.20178124 

site:https://biofam.github.io/MOFA2/

CPTAC: https://gdc.cancer.gov/about-gdc/contributed-genomic-data-cancer-research/clinical-proteomic-tumor-analysis-consortium-cptac

**Prequisites:**
To use the latest features of MOFA you can install the software from GitHub:

```python
pip install mofapy2
```
Download multiomic datasets from CPTAC

```python  
pip install cptac
```
**Structure:**
The repo is organized with jupyter notebooks that runs MOFA to determine dysregulated Transcription factors (TF) in cancer.
Every cancer indication is a MOFA run with its own multi-omic (transcriptomic, proteomic and phospho-proteomic) data to identify the dysregulated TFs in that particular indication (Colorectal, metastatic Colorectal and Bladder cancer)

* **`data/`**: The CPTAC datasets used for the mOFA runs (contains multi-omic data, clinical info and the TFs list)
* **`process_COAD_mofa.ipynb`**: Notebook that runs to extract TFs dysregulated in Colorectal cancer etc
* **`process_multiomics_for_mofa`**: Has functions needed to run the notebooks (needed as a custom dependency)
  
**Usage**

Each notebook runs stand alone in the Jupyterlab   


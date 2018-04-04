# Comparison of Vertex Componet Analysis (VCA) and Genetic Algorithm Endmember Extraction (GAEE) algorithms for Endmember Extraction

## Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |       PPI |    NFINDR |       VCA |      GAEE |   GAEE-IVFm |
|:-----------------|----------:|----------:|----------:|----------:|------------:|
| Alunite          | 0.374377  | 0.112191  | 0.09136   | 0.244162  |  0.333316   |
| Andradite        | 0.0757956 | 0.0912882 | 0.0858752 | 0.0710413 |  0.0747702  |
| Buddingtonite    | 0.20809   | 0.0761604 | 0.0897721 | 0.0937266 |  0.141666   |
| Dumortierite     | 0.190734  | 0.0706448 | 0.0701844 | 0.0965901 |  0.106933   |
| Kaolinite_1      | 0.0794624 | 0.0870056 | 0.0862021 | 0.115636  |  0.0950315  |
| Kaolinite_2      | 0.0819634 | 0.099195  | 0.0758247 | 0.0466318 |  0.0707981  |
| Muscovite        | 0.250633  | 0.158656  | 0.138526  | 0.094279  |  0.188539   |
| Montmonrillonite | 0.133816  | 0.0618906 | 0.0609575 | 0.0646271 |  0.0575392  |
| Nontronite       | 0.103292  | 0.0785457 | 0.0774903 | 0.0893713 |  0.0805585  |
| Pyrope           | 0.0578827 | 0.0850612 | 0.125747  | 0.0537088 |  0.0570572  |
| Sphene           | 0.0673108 | 0.140246  | 0.0769936 | 0.184264  |  0.113151   |
| Chalcedony       | 0.0871248 | 0.0934309 | 0.0760768 | 0.0861379 |  0.19593    |
| **Mean**         | 0.14254   | 0.096377  | 0.0932937 | 0.104077  |  0.12835    |
| **Std**          | 0         | 0.0138179 | 0.0134555 | 0.0175128 |  0.00699052 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |
|:-----------------|-----------:|-----------:|-----------:|-----------:|------------:|
| Alunite          | 0          | 0          | 0.018418   | 0          |  0          |
| Andradite        | 0          | 0.0319472  | 0.0155595  | 0          |  0          |
| Buddingtonite    | 0.047668   | 0.0071905  | 0.00765707 | 0.0106823  |  0          |
| Dumortierite     | 0.0562235  | 0.00711009 | 0.0114614  | 0.0141054  |  0.0217556  |
| Kaolinite_1      | 0.0113668  | 0.0130991  | 0.0129241  | 0.0152842  |  0.0130418  |
| Kaolinite_2      | 0.0113963  | 0.00712305 | 0.00570292 | 0.0029239  |  0.00708385 |
| Muscovite        | 0.096947   | 0.0259569  | 0.0187014  | 0.0103673  |  0.0464602  |
| Montmonrillonite | 0.0229949  | 0.00470432 | 0.00474685 | 0.00470432 |  0.00386881 |
| Nontronite       | 0.01264    | 0.0096385  | 0.00754401 | 0.00984283 |  0.00802697 |
| Pyrope           | 0.00713475 | 0.0102339  | 0.0075845  | 0.0280187  |  0.00454803 |
| Sphene           | 0.00756905 | 0.129301   | 0.0533127  | 0.0695174  |  0.0212323  |
| Chalcedony       | 0.00882676 | 0.0100621  | 0.00690701 | 0.00888408 |  0.0564801  |
| **Mean**         | 0.0235639  | 0.0235045  | 0.0188156  | 0.018264   |  0.0171429  |
| **Std**          | 0          | 0.00626792 | 0.00782176 | 0.00878088 |  0.00233611 |


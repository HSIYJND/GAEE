# Comparison of Vertex Componet Analysis (VCA) and Genetic Algorithm Endmember Extraction (GAEE) algorithms for Endmember Extraction

## Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

Envirionment Setup:

Monte Carlo runs: 2  Number of endmembers to estimate: 12  Number of skewers (PPI): 100  Maximum number of iterations (N-FINDR): 36 

Number of individuals in each generation: 100  Number of generations: 100  Crossover probability: 0.3  Mutation probability: 0.5 

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |       PPI |     NFINDR |       VCA |      GAEE |   GAEE-IVFm |
|:-----------------|----------:|-----------:|----------:|----------:|------------:|
| Alunite          | 0.374377  | 0.0926312  | 0.102462  | 0.112031  |   0.231736  |
| Andradite        | 0.0757956 | 0.0928352  | 0.07297   | 0.0960762 |   0.078295  |
| Buddingtonite    | 0.20809   | 0.0761604  | 0.121809  | 0.127309  |   0.112568  |
| Dumortierite     | 0.190734  | 0.0706448  | 0.0708485 | 0.0665961 |   0.100081  |
| Kaolinite_1      | 0.0794624 | 0.0917823  | 0.0862021 | 0.083056  |   0.076113  |
| Kaolinite_2      | 0.0819634 | 0.0757643  | 0.0751677 | 0.0647532 |   0.0601156 |
| Muscovite        | 0.250633  | 0.0960976  | 0.108403  | 0.167797  |   0.0965253 |
| Montmonrillonite | 0.133816  | 0.0618906  | 0.0656835 | 0.0663229 |   0.0669828 |
| Nontronite       | 0.103292  | 0.103292   | 0.0771623 | 0.0823558 |   0.0792332 |
| Pyrope           | 0.0578827 | 0.0619076  | 0.184073  | 0.0670503 |   0.0680813 |
| Sphene           | 0.0673108 | 0.285672   | 0.0633402 | 0.239992  |   0.146384  |
| Chalcedony       | 0.0871248 | 0.0919709  | 0.0760768 | 0.0676392 |   0.0690201 |
| **Mean**         | 0.14254   | 0.102959   | 0.10032   | 0.110813  |   0.106602  |
| **Std**          | 0         | 0.00687416 | 0.0160572 | 0.0164306 |   0.0156754 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |
|:-----------------|-----------:|-----------:|-----------:|-----------:|------------:|
| Alunite          | 0          | 0          | 0.0140103  | 0          |  0          |
| Andradite        | 0          | 0.0077595  | 0.00647544 | 0.0154143  |  0.00865414 |
| Buddingtonite    | 0.047668   | 0.0071905  | 0.0200077  | 0.010966   |  0.0147122  |
| Dumortierite     | 0.0562235  | 0.00689653 | 0.00718259 | 0.00606782 |  0.0122398  |
| Kaolinite_1      | 0.0113668  | 0.0130991  | 0.0129241  | 0.00938072 |  0.00809919 |
| Kaolinite_2      | 0.0113963  | 0.0095893  | 0.00591217 | 0.00627375 |  0.0062085  |
| Muscovite        | 0.096947   | 0.026671   | 0.0148187  | 0.0273533  |  0.0112208  |
| Montmonrillonite | 0.0229949  | 0.00489242 | 0.00489341 | 0.00501274 |  0.00507892 |
| Nontronite       | 0.01264    | 0.00684146 | 0.00866048 | 0.00887054 |  0.00809721 |
| Pyrope           | 0.00713475 | 0.062484   | 0.0359881  | 0.0379183  |  0.0119302  |
| Sphene           | 0.00756905 | 0.129301   | 0.00797184 | 0.0716476  |  0.0310442  |
| Chalcedony       | 0.00882676 | 0.00882676 | 0.00690701 | 0.00548343 |  0.00620729 |
| **Mean**         | 0.0235639  | 0.0256562  | 0.0148996  | 0.0191683  |  0.0133923  |
| **Std**          | 0          | 0.00308293 | 0.00638011 | 0.00555857 |  0.00376707 |


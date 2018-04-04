# Comparison of Vertex Componet Analysis (VCA) and Genetic Algorithm Endmember Extraction (GAEE) algorithms for Endmember Extraction

## Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

Envirionment Setup:

Monte Carlo runs: 2 
Number of endmembers to estimate: 12 
Number of skewers (PPI): 100 
Maximum number of iterations (N-FINDR): 36 

Number of individuals in each generation: 100 
Number of generations: 100 
Crossover probability: 0.3 
Mutation probability: 0.5 

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |       PPI |      NFINDR |       VCA |      GAEE |   GAEE-IVFm |
|:-----------------|----------:|------------:|----------:|----------:|------------:|
| Alunite          | 0.374377  | 0.0926312   | 0.09136   | 0.10747   |   0.104276  |
| Andradite        | 0.0757956 | 0.0911225   | 0.206736  | 0.124246  |   0.0707224 |
| Buddingtonite    | 0.20809   | 0.0761604   | 0.0785924 | 0.138821  |   0.1761    |
| Dumortierite     | 0.190734  | 0.0706448   | 0.0701844 | 0.082027  |   0.0665961 |
| Kaolinite_1      | 0.0794624 | 0.0870056   | 0.0862021 | 0.101255  |   0.0826539 |
| Kaolinite_2      | 0.0819634 | 0.0675381   | 0.0707858 | 0.0764603 |   0.0701803 |
| Muscovite        | 0.250633  | 0.124493    | 0.108403  | 0.203845  |   0.199636  |
| Montmonrillonite | 0.133816  | 0.0677506   | 0.0682226 | 0.066872  |   0.0587222 |
| Nontronite       | 0.103292  | 0.078045    | 0.112197  | 0.0738784 |   0.0752045 |
| Pyrope           | 0.0578827 | 0.0865489   | 0.0855351 | 0.0541151 |   0.0633292 |
| Sphene           | 0.0673108 | 0.285672    | 0.0633402 | 0.072489  |   0.119035  |
| Chalcedony       | 0.0871248 | 0.0947731   | 0.0877934 | 0.07451   |   0.140328  |
| **Mean**         | 0.14254   | 0.10215     | 0.101947  | 0.10347   |   0.105646  |
| **Std**          | 0         | 0.000953922 | 0.0210869 | 0.0202058 |   0.0140635 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |
|:-----------------|-----------:|-----------:|-----------:|-----------:|------------:|
| Alunite          | 0          | 0          | 0.0104872  | 0          |  0          |
| Andradite        | 0          | 0.00916246 | 0.0094222  | 0.0135296  |  0          |
| Buddingtonite    | 0.047668   | 0.0071905  | 0.00765707 | 0.0249317  |  0          |
| Dumortierite     | 0.0562235  | 0.00711009 | 0.00694232 | 0.00869794 |  0.00606782 |
| Kaolinite_1      | 0.0113668  | 0.0130991  | 0.0129241  | 0.0116238  |  0.0122267  |
| Kaolinite_2      | 0.0113963  | 0.00573363 | 0.010526   | 0.00883876 |  0.00624986 |
| Muscovite        | 0.096947   | 0.031699   | 0.0305828  | 0.026671   |  0.050114   |
| Montmonrillonite | 0.0229949  | 0.00531464 | 0.00535166 | 0.00533693 |  0.00384133 |
| Nontronite       | 0.01264    | 0.008296   | 0.0148909  | 0.00766549 |  0.0080744  |
| Pyrope           | 0.00713475 | 0.0300626  | 0.010077   | 0.00605452 |  0.0137243  |
| Sphene           | 0.00756905 | 0.0912113  | 0.00797184 | 0.0576356  |  0.0297292  |
| Chalcedony       | 0.00882676 | 0.0103525  | 0.0090267  | 0.00695196 |  0.0191864  |
| **Mean**         | 0.0235639  | 0.023149   | 0.0153463  | 0.0196878  |  0.0145699  |
| **Std**          | 0          | 0.0052986  | 0.00609868 | 0.0103672  |  0.00340021 |


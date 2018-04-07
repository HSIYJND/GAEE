# Comparison of Vertex Componet Analysis (VCA) and Genetic Algorithm Endmember Extraction (GAEE) algorithms for Endmember Extraction

## Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

**Envirionment Setup:**

Monte Carlo runs: 2 

Number of endmembers to estimate: 12 

Number of skewers (PPI): 100 

Maximum number of iterations (N-FINDR): 36 

Number of individuals in each generation: 100 

Number of generations: 100 

Crossover probability: 0.3 

Mutation probability: 0.5 

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |       PPI |    NFINDR |       VCA |      GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|----------:|----------:|----------:|----------:|------------:|-----------:|----------------:|
| Alunite          | 0.374377  | 0.112728  | 0.09136   | 0.253755  |   0.279273  | 0.104276   |      0.104276   |
| Andradite        | 0.0757956 | 0.206837  | 0.10341   | 0.078318  |   0.0947087 | 0.0912882  |      0.0912882  |
| Buddingtonite    | 0.20809   | 0.120508  | 0.0785924 | 0.104971  |   0.10771   | 0.0761598  |      0.0761598  |
| Dumortierite     | 0.190734  | 0.0720035 | 0.0724766 | 0.0915866 |   0.0853839 | 0.0720036  |      0.0720036  |
| Kaolinite_1      | 0.0794624 | 0.0870056 | 0.0862021 | 0.0872378 |   0.0825444 | 0.0870058  |      0.0870058  |
| Kaolinite_2      | 0.0819634 | 0.099195  | 0.0791532 | 0.0470788 |   0.0528539 | 0.0641441  |      0.0680958  |
| Muscovite        | 0.250633  | 0.0983345 | 0.0968199 | 0.132326  |   0.15248   | 0.138855   |      0.138855   |
| Montmonrillonite | 0.133816  | 0.0646271 | 0.0651032 | 0.0641655 |   0.0662506 | 0.0618903  |      0.0618903  |
| Nontronite       | 0.103292  | 0.0805545 | 0.112197  | 0.0727389 |   0.0835473 | 0.0825749  |      0.0825749  |
| Pyrope           | 0.0578827 | 0.0865489 | 0.21397   | 0.0599319 |   0.0526168 | 0.0678591  |      0.0785193  |
| Sphene           | 0.0673117 | 0.0542052 | 0.0769936 | 0.0633612 |   0.087449  | 0.151882   |      0.151882   |
| Chalcedony       | 0.0871248 | 0.0761879 | 0.0773462 | 0.0943611 |   0.0919799 | 0.0871248  |      0.0871248  |
| **Mean**         | 0.14254   | 0.103992  | 0.109728  | 0.0979445 |   0.106075  | 0.0905448  |      0.0925377  |
| **Std**          | 0         | 0.0194034 | 0.0161286 | 0.0155338 |   0.0105294 | 0.00958278 |      0.00245936 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-----------:|-----------:|-----------:|-----------:|------------:|-----------:|----------------:|
| Alunite          | 0          | 0          | 0.0164185  | 0          |  0          | 0          |      0          |
| Andradite        | 0          | 0.00916246 | 0.00810977 | 0          |  0          | 0.00976325 |      0          |
| Buddingtonite    | 0.047668   | 0.0211266  | 0.00765707 | 0.010966   |  0.014383   | 0.0071905  |      0.0071905  |
| Dumortierite     | 0.0562235  | 0.00711009 | 0.00718259 | 0.0121352  |  0.019749   | 0.00689653 |      0.00689653 |
| Kaolinite_1      | 0.0113668  | 0.0130991  | 0.0129241  | 0.0105637  |  0.0130991  | 0.0130991  |      0.0130991  |
| Kaolinite_2      | 0.0113963  | 0.00820605 | 0.00920191 | 0.00396682 |  0.00750405 | 0.00712305 |      0.00617913 |
| Muscovite        | 0.096947   | 0.026671   | 0.0257291  | 0.0355314  |  0.0404123  | 0.0275724  |      0.0239996  |
| Montmonrillonite | 0.0229949  | 0.00489242 | 0.00464996 | 0.00476634 |  0.00523934 | 0.00470432 |      0.00470432 |
| Nontronite       | 0.01264    | 0.008296   | 0.0120818  | 0.00774636 |  0.00939014 | 0.0081581  |      0.0081581  |
| Pyrope           | 0.00713475 | 0.062484   | 0.0292924  | 0.0148078  |  0.0131244  | 0.0889987  |      0.0291898  |
| Sphene           | 0.00756905 | 0.094298   | 0.0910914  | 0.0356481  |  0.0268377  | 0.0080519  |      0.159963   |
| Chalcedony       | 0.00882676 | 0.0103525  | 0.00690701 | 0.0241747  |  0.0106351  | 0.00882676 |      0.00882676 |
| **Mean**         | 0.0235639  | 0.0238933  | 0.0228589  | 0.0150472  |  0.0138277  | 0.0190925  |      0.0250309  |
| **Std**          | 0          | 0.0041777  | 0.0062353  | 0.00426228 |  0.00303145 | 0.00943218 |      0.00268023 |


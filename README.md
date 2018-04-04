# Hyperspectral Endmember Extraction

### Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |       PPI |    NFINDR |       VCA |      GAEE |   GAEE-IVFm |
|:-----------------|----------:|----------:|----------:|----------:|------------:|
| Alunite          | 0.374377  | 0.112728  | 0.09136   | 0.110624  |   0.151453  |
| Andradite        | 0.0757956 | 0.206837  | 0.0921267 | 0.0625078 |   0.107456  |
| Buddingtonite    | 0.20809   | 0.120508  | 0.151984  | 0.113614  |   0.121172  |
| Dumortierite     | 0.190734  | 0.0720035 | 0.0701844 | 0.0946749 |   0.0793365 |
| Kaolinite_1      | 0.0794624 | 0.0870056 | 0.0862021 | 0.0865925 |   0.101547  |
| Kaolinite_2      | 0.0819634 | 0.099195  | 0.0893595 | 0.0465472 |   0.0480251 |
| Muscovite        | 0.250633  | 0.0983345 | 0.0962291 | 0.196591  |   0.0959306 |
| Montmonrillonite | 0.133816  | 0.0646271 | 0.0645269 | 0.0692029 |   0.0700147 |
| Nontronite       | 0.103292  | 0.0805545 | 0.0771623 | 0.081329  |   0.0775539 |
| Pyrope           | 0.0578827 | 0.0865489 | 0.23665   | 0.107819  |   0.0614952 |
| Sphene           | 0.0673117 | 0.0542052 | 0.0633402 | 0.066538  |   0.0923917 |
| Chalcedony       | 0.0871248 | 0.0761879 | 0.0608225 | 0.0919799 |   0.0732091 |

|      |     PPI |    NFINDR |       VCA |      GAEE |   GAEE-IVFm |
|:-----|--------:|----------:|----------:|----------:|------------:|
| Mean | 0.14254 | 0.0992133 | 0.0983953 | 0.0961961 |   0.0970703 |
| Std  | 0       | 0.0206257 | 0.0123965 | 0.0098523 |   0.0115835 |

Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |
|:-----------------|-----------:|-----------:|-----------:|-----------:|------------:|
| Alunite          | 0          | 0          | 0.0104872  | 0          |  0.0294005  |
| Andradite        | 0          | 0.00916246 | 0.00884199 | 0          |  0.012498   |
| Buddingtonite    | 0.047668   | 0.0071905  | 0.0290442  | 0.0164024  |  0.01898    |
| Dumortierite     | 0.0562235  | 0.00711009 | 0.00694232 | 0.0125921  |  0.00816269 |
| Kaolinite_1      | 0.0113668  | 0.0130991  | 0.0129241  | 0.0131898  |  0.0130818  |
| Kaolinite_2      | 0.0113963  | 0.00573363 | 0.00952464 | 0.00331071 |  0.00376396 |
| Muscovite        | 0.096947   | 0.031699   | 0.0107897  | 0.0267404  |  0.0109214  |
| Montmonrillonite | 0.0229949  | 0.00531464 | 0.00474685 | 0.00592045 |  0.00514138 |
| Nontronite       | 0.01264    | 0.008296   | 0.00866048 | 0.0082386  |  0.00786584 |
| Pyrope           | 0.00713475 | 0.0300626  | 0.062435   | 0.00980904 |  0.00570679 |
| Sphene           | 0.00756905 | 0.0912113  | 0.00797184 | 0.0239994  |  0.0117273  |
| Chalcedony       | 0.00882676 | 0.0103525  | 0.00462902 | 0.0107626  |  0.00699113 |

|      |       PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |
|:-----|----------:|-----------:|-----------:|-----------:|------------:|
| Mean | 0.0235639 | 0.0219572  | 0.0158652  | 0.0130336  |  0.011671   |
| Std  | 0         | 0.00644016 | 0.00528309 | 0.00301049 |  0.00369823 |


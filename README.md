# Comparison of Vertex Componet Analysis (VCA) and Genetic Algorithm Endmember Extraction (GAEE) algorithms for Endmember Extraction

## Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

**Envirionment Setup:**

Monte Carlo runs: 2 

Number of endmembers to estimate: 12 

Number of skewers (PPI): 5 

Maximum number of iterations (N-FINDR): 5 

### Parameters used in each GAEE versions

| Parameters            |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:----------------------|-------:|------------:|-----------:|----------------:|
| Population Size       |   10   |        10   |       10   |            10   |
| Number of Generations |   10   |        10   |       10   |            10   |
| Crossover Probability |    1   |         1   |        1   |             1   |
| Mutation Probability  |    0.3 |         0.3 |        0.3 |             0.3 |

![alt text](Convergence.png)

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |       VCA |       GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-----------:|-----------:|----------:|-----------:|------------:|-----------:|----------------:|
| Alunite          |  0.3743766 |  0.1033697 | **0.1016300** |  0.3414486 |   0.1024535 |  0.1033697 |       0.1033697 |
| Andradite        |  0.0757956 |  0.0724709 | 0.0908270 |  0.0678708 |   0.0676371 |  0.0823914 |       **0.0592546** |
| Buddingtonite    |  0.2080900 |  0.0761604 | 0.0785924 |  0.1264569 |   0.1125306 |  **0.0761598** |       **0.0761598** |
| Dumortierite     |  0.1907338 |  **0.0720035** | 0.0951321 |  0.0777131 |   0.1512911 |  0.0720841 |       0.1052671 |
| Kaolinite_1      |  0.0794624 |  0.0870056 | 0.0862021 |  0.0922255 |   **0.0786868** |  0.0825444 |       0.0870058 |
| Kaolinite_2      |  0.0819634 |  0.0889228 | 0.0755032 |  **0.0587641** |   0.0627594 |  0.0763893 |       0.0953920 |
| Muscovite        |  0.2506333 |  0.1091060 | 0.1084029 |  0.1605602 |   0.2121529 |  0.1359533 |       **0.0960974** |
| Montmonrillonite |  0.1338156 |  0.0648080 | 0.0642589 |  0.0605655 |   **0.0590018** |  0.0657460 |       0.0657460 |
| Nontronite       |  0.1032919 |  0.0758386 | 0.1121975 |  0.0797934 |   **0.0735572** |  0.0762960 |       0.1150333 |
| Pyrope           |  0.0578827 |  0.1221578 | 0.1471749 |  **0.0461283** |   0.0644277 |  0.1941656 |       0.0964739 |
| Sphene           |  0.0673108 |  0.2856719 | 0.0834347 |  0.0741759 |   0.1528000 |  0.0770255 |       **0.0613746** |
| Chalcedony       |  0.0871248 |  0.0871248 | **0.0760768** |  0.2199309 |   0.1653366 |  0.0934307 |       0.0919706 |
| **Mean**         |  0.1425401 |  0.1057002 | 0.1005772 |  0.1210254 |   0.1096163 |  0.1054497 |       **0.0939173** |
| **Std**          |  **0.0000000** |  0.0053322 | 0.0158775 |  0.0112868 |   0.0228356 |  0.0209175 |       0.0118040 |
| **p-value**      | -5.7552679 | -0.6780580 | 0.0000000 | -2.4744633 |  -1.2267441 | **-0.3734411** |       0.6979624 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |       VCA |      GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-----------:|-----------:|----------:|----------:|------------:|-----------:|----------------:|
| Alunite          |  **0.0000000** |  **0.0000000** | **0.0000000** | **0.0000000** |   **0.0000000** |  **0.0000000** |       **0.0000000** |
| Andradite        |  **0.0000000** |  0.0061679 | 0.0080497 | **0.0000000** |   **0.0000000** |  0.0122536 |       0.0085121 |
| Buddingtonite    |  0.0476680 |  0.0071905 | 0.0076571 | **0.0000000** |   0.0270487 |  0.0071905 |       0.0071905 |
| Dumortierite     |  0.0562235 |  0.0068965 | 0.0178236 | **0.0000000** |   0.0092193 |  0.0075447 |       0.0119773 |
| Kaolinite_1      |  0.0113668 |  0.0130991 | 0.0129241 | 0.0217162 |   0.0098058 |  **0.0088126** |       0.0130991 |
| Kaolinite_2      |  0.0113963 |  0.0109124 | 0.0076261 | **0.0044164** |   0.0056577 |  0.0082711 |       0.0063615 |
| Muscovite        |  0.0969470 |  0.0300733 | **0.0148187** | 0.0280079 |   0.0524025 |  0.0300733 |       0.0300733 |
| Montmonrillonite |  0.0229949 |  0.0048775 | 0.0047469 | **0.0045035** |   0.0065401 |  0.0053146 |       0.0053146 |
| Nontronite       |  0.0126400 |  0.0076655 | 0.0081608 | 0.0080293 |   **0.0073461** |  0.0077239 |       0.0085682 |
| Pyrope           |  **0.0071348** |  0.0530846 | 0.1173103 | 0.0075062 |   0.0148324 |  0.0288032 |       0.0130515 |
| Sphene           |  **0.0075691** |  0.0912113 | 0.0095759 | 0.0295970 |   0.0528866 |  0.0528866 |       0.0912113 |
| Chalcedony       |  0.0088268 |  0.0088268 | **0.0069070** | 0.0231664 |   0.0090096 |  0.0100621 |       0.0100621 |
| **Mean**         |  0.0235639 |  0.0221020 | 0.0187293 | **0.0143122** |   0.0184279 |  0.0171611 |       0.0198158 |
| **Std**          |  **0.0000000** |  0.0024464 | 0.0107082 | 0.0057590 |   0.0071316 |  0.0041750 |       0.0042833 |
| **p-value**      | -6.3392612 | -1.5085898 | 0.0000000 | 1.1591285 |   0.1295330 |  0.6601739 |      **-0.3876038** |


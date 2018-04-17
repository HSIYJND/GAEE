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

| Endmembers       |         PPI |     NFINDR |       VCA |       GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|------------:|-----------:|----------:|-----------:|------------:|-----------:|----------------:|
| Alunite          |   0.3743766 |  0.1033697 | **0.0913600** |  0.3066626 |   0.2826150 |  0.0926313 |       0.0926313 |
| Andradite        |   0.0757956 |  **0.0724709** | 0.0868627 |  0.0802739 |   0.0862870 |  0.1644978 |       0.0752234 |
| Buddingtonite    |   0.2080900 |  **0.0761604** | 0.0823985 |  0.1181232 |   0.0874055 |  0.1193060 |       0.1602123 |
| Dumortierite     |   0.1907338 |  0.0720035 | 0.0708485 |  0.0718638 |   0.0899484 |  **0.0706448** |       **0.0706448** |
| Kaolinite_1      |   **0.0794624** |  0.0870056 | 0.0862021 |  0.0862734 |   0.0873382 |  0.0869072 |       0.0870058 |
| Kaolinite_2      |   0.0819634 |  0.0889228 | 0.0758247 |  **0.0638283** |   0.0732192 |  0.0730934 |       0.0861069 |
| Muscovite        |   0.2506333 |  0.1091060 | 0.1385263 |  0.1982286 |   0.1873132 |  0.1578801 |       **0.1091057** |
| Montmonrillonite |   0.1338156 |  0.0648080 | 0.0645269 |  0.0675177 |   **0.0617503** |  0.0646271 |       0.0646271 |
| Nontronite       |   0.1032919 |  0.0758386 | 0.0781925 |  0.0761649 |   **0.0729433** |  0.0797374 |       0.0779097 |
| Pyrope           |   0.0578827 |  0.1221578 | 0.2366504 |  0.0735907 |   **0.0509429** |  0.2377895 |       0.1217895 |
| Sphene           |   0.0673108 |  0.2856719 | **0.0633402** |  0.0675483 |   0.0959046 |  0.0770255 |       0.0640268 |
| Chalcedony       |   0.0871248 |  0.0871248 | 0.0938692 |  0.1504308 |   0.1512674 |  0.0919706 |       **0.0752052** |
| **Mean**         |   0.1425401 |  0.1057002 | 0.0987978 |  0.1151371 |   0.1135220 |  0.1141871 |       **0.0924109** |
| **Std**          |   **0.0000000** |  0.0053322 | 0.0186826 |  0.0066076 |   0.0067262 |  0.0182891 |       0.0132894 |
| **P-value**      | -30.9293928 | **-2.8365552** | 0.0000000 | -7.2328626 |  -4.5080643 | -3.2551426 |       2.5756814 |
| **Time**         |   **7.9611670** |  **7.9611670** | **7.9611670** |  **7.9611670** |   **7.9611670** |  **7.9611670** |       **7.9611670** |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |       VCA |      GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-----------:|-----------:|----------:|----------:|------------:|-----------:|----------------:|
| Alunite          |  **0.0000000** |  **0.0000000** | 0.0104872 | **0.0000000** |   **0.0000000** |  **0.0000000** |       **0.0000000** |
| Andradite        |  **0.0000000** |  0.0061679 | 0.0088420 | **0.0000000** |   **0.0000000** |  0.0194020 |       0.0074052 |
| Buddingtonite    |  0.0476680 |  0.0071905 | 0.0080367 | 0.0184321 |   **0.0000000** |  0.0267324 |       0.0071905 |
| Dumortierite     |  0.0562235 |  **0.0068965** | 0.0071826 | 0.0069057 |   0.0100143 |  0.0071101 |       0.0197490 |
| Kaolinite_1      |  0.0113668 |  0.0130991 | 0.0129241 | 0.0129120 |   0.0133009 |  **0.0108978** |       0.0130991 |
| Kaolinite_2      |  0.0113963 |  0.0109124 | 0.0084861 | **0.0046526** |   0.0073812 |  0.0059838 |       0.0109124 |
| Muscovite        |  0.0969470 |  0.0300733 | **0.0272276** | 0.0700768 |   0.0338296 |  0.0316990 |       0.0316990 |
| Montmonrillonite |  0.0229949 |  0.0048775 | 0.0048934 | 0.0050236 |   **0.0045624** |  0.0047043 |       0.0047043 |
| Nontronite       |  0.0126400 |  0.0076655 | 0.0109842 | 0.0074239 |   **0.0071590** |  0.0081465 |       0.0081465 |
| Pyrope           |  **0.0071348** |  0.0530846 | 0.0624350 | 0.0099261 |   0.0185373 |  0.0419685 |       0.0083235 |
| Sphene           |  **0.0075691** |  0.0912113 | 0.0079718 | 0.0082675 |   0.0363600 |  0.0912113 |       0.0241628 |
| Chalcedony       |  0.0088268 |  0.0088268 | 0.0102253 | 0.0316220 |   0.0198481 |  0.0130018 |       **0.0066897** |
| **Mean**         |  0.0235639 |  0.0221020 | 0.0211659 | 0.0206637 |   0.0137623 |  0.0229125 |       **0.0126264** |
| **Std**          |  **0.0000000** |  0.0024464 | 0.0082362 | 0.0075245 |   0.0035074 |  0.0036685 |       0.0024566 |
| **P-value**      | -0.3873310 | **-0.1431778** | 0.0000000 | 0.0579667 |   1.1746872 | -0.2771674 |       1.3682946 |
| **Time**         |  **7.9611670** |  **7.9611670** | **7.9611670** | **7.9611670** |   **7.9611670** |  **7.9611670** |       **7.9611670** |


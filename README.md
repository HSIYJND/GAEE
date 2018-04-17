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

| Endmembers       |        PPI |     NFINDR |       VCA |      GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-----------:|-----------:|----------:|----------:|------------:|-----------:|----------------:|
| Alunite          |  0.3743766 |  0.1033697 | **0.0913600** | 0.3039898 |   0.1138350 |  0.1025204 |       0.2127158 |
| Andradite        |  0.0757956 |  0.0724709 | 0.0925616 | 0.0817683 |   0.0660738 |  0.0781289 |       **0.0592546** |
| Buddingtonite    |  0.2080900 |  0.0761604 | 0.0785924 | 0.1107406 |   0.1239738 |  **0.0761598** |       **0.0761598** |
| Dumortierite     |  0.1907338 |  **0.0720035** | 0.0950507 | 0.0870930 |   0.0741464 |  0.0919245 |       0.0919245 |
| Kaolinite_1      |  **0.0794624** |  0.0870056 | 0.0862021 | 0.1346482 |   0.0924682 |  0.1241450 |       0.0870058 |
| Kaolinite_2      |  0.0819634 |  0.0889228 | 0.0707858 | **0.0518051** |   0.0596326 |  0.0812945 |       0.0631391 |
| Muscovite        |  0.2506333 |  **0.1091060** | 0.1205493 | 0.1501354 |   0.1708888 |  0.1388551 |       0.1431162 |
| Montmonrillonite |  0.1338156 |  0.0648080 | 0.0651032 | 0.0641974 |   0.0672974 |  **0.0618903** |       **0.0618903** |
| Nontronite       |  0.1032919 |  0.0758386 | 0.0902204 | 0.0771949 |   **0.0713363** |  0.0788187 |       0.0838923 |
| Pyrope           |  0.0578827 |  0.1221578 | 0.1751620 | **0.0551721** |   0.0655784 |  0.0685702 |       0.0851315 |
| Sphene           |  **0.0673108** |  0.2856719 | 0.2847472 | 0.0810005 |   0.1062639 |  0.1880035 |       0.2856719 |
| Chalcedony       |  0.0871248 |  0.0871248 | 0.0773462 | 0.1231989 |   0.1337771 |  **0.0752052** |       **0.0752052** |
| **Mean**         |  0.1425401 |  0.1057002 | 0.1150467 | 0.1108683 |   0.1037440 |  **0.1014401** |       0.1119390 |
| **Std**          |  **0.0000000** |  0.0053322 | 0.0059886 | 0.0106267 |   0.0092957 |  0.0089815 |       0.0048096 |
| **P-value**      | **-6.2391183** |  1.9346579 | 0.0000000 | 0.9333360 |   1.2022259 |  2.2065202 |       0.6670065 |
| **Time**         |  **0.2610414** | 44.9494044 | 0.5906152 | 0.4426334 |   0.4537501 |  0.4214742 |       0.4534234 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |       VCA |      GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-----------:|-----------:|----------:|----------:|------------:|-----------:|----------------:|
| Alunite          |  **0.0000000** |  **0.0000000** | 0.0104872 | **0.0000000** |   **0.0000000** |  0.0135685 |       0.0614333 |
| Andradite        |  **0.0000000** |  0.0061679 | 0.0108651 | **0.0000000** |   **0.0000000** |  0.0056619 |       0.0056619 |
| Buddingtonite    |  0.0476680 |  0.0071905 | 0.0076571 | **0.0000000** |   0.0191348 |  0.0071905 |       0.0071905 |
| Dumortierite     |  0.0562235 |  0.0068965 | 0.0122770 | **0.0000000** |   0.0069769 |  0.0113878 |       0.0113878 |
| Kaolinite_1      |  **0.0113668** |  0.0130991 | 0.0129241 | 0.0133890 |   0.0138912 |  0.0130991 |       0.0130991 |
| Kaolinite_2      |  0.0113963 |  0.0109124 | 0.0057029 | 0.0074352 |   **0.0050755** |  0.0092903 |       0.0056431 |
| Muscovite        |  0.0969470 |  0.0300733 | **0.0187014** | 0.0240166 |   0.0295499 |  0.0275724 |       0.0290227 |
| Montmonrillonite |  0.0229949 |  0.0048775 | 0.0047469 | **0.0039669** |   0.0051760 |  0.0048552 |       0.0048552 |
| Nontronite       |  0.0126400 |  0.0076655 | 0.0099309 | 0.0077983 |   **0.0071649** |  0.0090706 |       0.0090025 |
| Pyrope           |  **0.0071348** |  0.0530846 | 0.0334964 | 0.0121238 |   0.0122789 |  0.0185219 |       0.0084844 |
| Sphene           |  **0.0075691** |  0.0912113 | 0.0910914 | 0.0292876 |   0.0637404 |  0.0912113 |       0.0591837 |
| Chalcedony       |  0.0088268 |  0.0088268 | 0.0072431 | 0.0152404 |   0.0216808 |  **0.0066897** |       **0.0066897** |
| **Mean**         |  0.0235639 |  0.0221020 | 0.0205855 | **0.0106744** |   0.0173308 |  0.0205698 |       0.0194328 |
| **Std**          |  **0.0000000** |  0.0024464 | 0.0020932 | 0.0016942 |   0.0026817 |  0.0040195 |       0.0010093 |
| **P-value**      | -1.6317875 | **-0.5448024** | 0.0000000 | 4.4959139 |   1.2213106 |  0.0052408 |       0.5587635 |
| **Time**         |  **0.2610414** | 44.9494044 | 0.5906152 | 0.4426334 |   0.4537501 |  0.4214742 |       0.4534234 |


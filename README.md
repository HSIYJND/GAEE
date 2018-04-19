# Comparison of Vertex Componet Analysis (VCA) and Genetic Algorithm Endmember Extraction (GAEE) algorithms for Endmember Extraction

## Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

**Envirionment Setup:**

Monte Carlo runs: 2 

Number of endmembers to estimate: 12 

Number of skewers (PPI): 1 

Maximum number of iterations (N-FINDR): 1 

### Parameters used in each GAEE versions

| Parameters            |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:----------------------|-------:|------------:|-----------:|----------------:|
| Population Size       |   10   |        10   |       10   |            10   |
| Number of Generations |   10   |        10   |       10   |            10   |
| Crossover Probability |    1   |         1   |        1   |             1   |
| Mutation Probability  |    0.3 |         0.3 |        0.3 |             0.3 |

![alt text](./IMAGES/Convergence.png)

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |       PPI |    NFINDR |       VCA |      GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|----------:|----------:|----------:|----------:|------------:|-----------:|----------------:|
| Alunite          | 0.3743766 | **0.0926312** | 0.1024622 | 0.2298149 |   0.2702546 |  0.0926313 |       0.0926313 |
| Andradite        | 0.0757956 | **0.0724709** | 0.1341686 | 0.0781961 |   0.0764906 |  0.0910315 |       0.1486823 |
| Buddingtonite    | 0.2080900 | **0.0761604** | 0.0785924 | 0.0983172 |   0.1091044 |  0.0874055 |       0.0874055 |
| Dumortierite     | 0.1907338 | 0.0720035 | 0.0701844 | 0.1006342 |   **0.0696474** |  0.1200692 |       0.0720841 |
| Kaolinite_1      | **0.0794624** | 0.0870056 | 0.0893394 | 0.1146590 |   0.0938499 |  0.1196266 |       0.1005831 |
| Kaolinite_2      | 0.0819634 | 0.0889228 | 0.0961467 | 0.0669184 |   **0.0623641** |  0.0722893 |       0.0756588 |
| Muscovite        | 0.2506333 | **0.1091060** | 0.1584696 | 0.1524159 |   0.1513114 |  0.1210606 |       0.2039574 |
| Montmonrillonite | 0.1338156 | 0.0648080 | 0.0651032 | **0.0594497** |   0.0655744 |  0.0677500 |       0.0677500 |
| Nontronite       | 0.1032919 | 0.0758386 | 0.0794569 | 0.0967941 |   **0.0752045** |  0.0856076 |       0.0758600 |
| Pyrope           | 0.0578827 | 0.1221578 | 0.0814426 | **0.0499651** |   0.0574612 |  0.0753179 |       0.0654097 |
| Sphene           | 0.0673117 | 0.2856719 | **0.0530461** | 0.1176103 |   0.0845717 |  0.0697771 |       0.0697771 |
| Chalcedony       | 0.0871248 | 0.0871248 | 0.0760768 | 0.1181731 |   0.1100913 |  **0.0752052** |       **0.0752052** |

### SAM Statistics for Cuprite Dataset. 

| Statistics   |        PPI |     NFINDR |       VCA |       GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-------------|-----------:|-----------:|----------:|-----------:|------------:|-----------:|----------------:|
| _Mean_       |  0.1425401 |  0.1059427 | 0.0960657 |  0.1143145 |   0.1084843 |  **0.0904520** |       0.0951107 |
| _Std_        |  **0.0000000** |  0.0085976 | 0.0174209 |  0.0178741 |   0.0099003 |  0.0032332 |       0.0069262 |
| _p-value_    | -8.1654095 | -1.5219916 | 0.0000000 | -1.9543837 |  **-1.4596427** |  0.9801816 |       0.1670730 |
| _Time_       |  0.2364512 |  3.9212757 | 0.6464976 |  0.2375110 |   0.2222395 |  **0.2173737** |       0.2213006 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |       PPI |    NFINDR |       VCA |      GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|----------:|----------:|----------:|----------:|------------:|-----------:|----------------:|
| Alunite          | **0.0000000** | **0.0000000** | 0.0104872 | **0.0000000** |   **0.0000000** |  **0.0000000** |       0.0106528 |
| Andradite        | **0.0000000** | 0.0061679 | 0.0093155 | **0.0000000** |   **0.0000000** |  0.0100446 |       0.0214284 |
| Buddingtonite    | 0.0476680 | **0.0071905** | 0.0076571 | 0.0123924 |   0.0242026 |  0.0093362 |       0.0093362 |
| Dumortierite     | 0.0562235 | **0.0068965** | 0.0069423 | 0.0145629 |   0.0163066 |  0.0237962 |       0.0075447 |
| Kaolinite_1      | 0.0113668 | 0.0130991 | **0.0077023** | 0.0168440 |   0.0117205 |  0.0177103 |       0.0121350 |
| Kaolinite_2      | 0.0113963 | 0.0109124 | 0.0094397 | 0.0063159 |   **0.0054108** |  0.0101429 |       0.0153737 |
| Muscovite        | 0.0969470 | 0.0316990 | **0.0145920** | 0.0248155 |   0.0436349 |  0.0189268 |       0.0616666 |
| Montmonrillonite | 0.0229949 | 0.0048775 | 0.0047469 | **0.0044385** |   0.0080385 |  0.0053146 |       0.0053146 |
| Nontronite       | 0.0126400 | **0.0076655** | 0.0079970 | 0.0087722 |   0.0079852 |  0.0089198 |       0.0081462 |
| Pyrope           | **0.0071348** | 0.0530846 | 0.0359881 | 0.0083927 |   0.0080508 |  0.0086308 |       0.0071437 |
| Sphene           | **0.0075691** | 0.0912113 | 0.0530071 | 0.0655979 |   0.0172249 |  0.0092748 |       0.0092748 |
| Chalcedony       | 0.0088268 | 0.0088268 | 0.0072431 | 0.0202989 |   0.0091401 |  **0.0066897** |       **0.0066897** |

### SID Statistics for Cuprite Dataset. 

| Statistics   |        PPI |     NFINDR |       VCA |      GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-------------|-----------:|-----------:|----------:|----------:|------------:|-----------:|----------------:|
| _Mean_       |  0.0235639 |  0.0226774 | 0.0172418 | 0.0153289 |   0.0132147 |  **0.0108133** |       0.0151940 |
| _Std_        |  **0.0000000** |  0.0032907 | 0.0055583 | 0.0067291 |   0.0033858 |  0.0003602 |       0.0026051 |
| _p-value_    | -2.3869447 | **-1.4807902** | 0.0000000 | 0.7214021 |   1.4862128 |  2.4259642 |       0.7518609 |
| _Time_       |  0.2364512 |  3.9212757 | 0.6464976 | 0.2375110 |   0.2222395 |  **0.2173737** |       0.2213006 |

![alt text](./IMAGES/Alunite_Endmember.png)

![alt text](./IMAGES/Andradite_Endmember.png)

![alt text](./IMAGES/Buddingtonite_Endmember.png)

![alt text](./IMAGES/Dumortierite_Endmember.png)

![alt text](./IMAGES/Kaolinite_1_Endmember.png)

![alt text](./IMAGES/Kaolinite_2_Endmember.png)

![alt text](./IMAGES/Muscovite_Endmember.png)

![alt text](./IMAGES/Montmonrillonite_Endmember.png)

![alt text](./IMAGES/Nontronite_Endmember.png)

![alt text](./IMAGES/Pyrope_Endmember.png)

![alt text](./IMAGES/Sphene_Endmember.png)

![alt text](./IMAGES/Chalcedony_Endmember.png)


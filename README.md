# Comparison of Vertex Componet Analysis (VCA) and Genetic Algorithm Endmember Extraction (GAEE) algorithms for Endmember Extraction

## Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

**Envirionment Setup:**

Monte Carlo runs: 10 

Number of endmembers to estimate: 12 

Number of skewers (PPI): 1000 

Maximum number of iterations (N-FINDR): 36 

### Parameters used in each GAEE versions

| Parameters            |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:----------------------|-------:|------------:|-----------:|----------------:|
| Population Size       |  100   |      100    |      100   |           100   |
| Number of Generations |  250   |      250    |      250   |           250   |
| Crossover Probability |    0.7 |        1    |        0.7 |             0.7 |
| Mutation Probability  |    0.1 |        0.05 |        0.3 |             0.3 |

![alt text](./IMAGES/Convergence.png)

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |    PPI |   NFINDR |    VCA |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-------:|---------:|-------:|-------:|------------:|-----------:|----------------:|
| Alunite          | 0.3744 |   0.1075 | 0.1016 | 0.1112 |      0.1112 |     **0.0926** |          **0.0926** |
| Andradite        | 0.0758 |   0.0911 | 0.0778 | **0.0609** |      0.0796 |     0.0863 |          0.0917 |
| Buddingtonite    | 0.2081 |   **0.0762** | 0.0824 | 0.0937 |      0.0798 |     **0.0762** |          **0.0762** |
| Dumortierite     | 0.1907 |   0.0706 | **0.0702** | 0.0894 |      0.0835 |     0.0706 |          0.0706 |
| Kaolinite_1      | **0.0795** |   0.0870 | 0.0862 | 0.1140 |      0.0875 |     0.1014 |          0.1196 |
| Kaolinite_2      | 0.0820 |   0.0992 | 0.0811 | 0.0628 |      0.0813 |     0.0737 |          **0.0606** |
| Muscovite        | 0.2506 |   0.1587 | 0.1084 | 0.1531 |      **0.1009** |     0.1788 |          0.1548 |
| Montmonrillonite | 0.1338 |   0.0677 | 0.0698 | 0.0664 |      0.0664 |     **0.0619** |          **0.0619** |
| Nontronite       | 0.1033 |   0.0806 | **0.0722** | 0.0758 |      0.0823 |     0.0795 |          0.1011 |
| Pyrope           | 0.0579 |   0.0767 | 0.1729 | 0.0535 |      0.1028 |     **0.0509** |          0.0579 |
| Sphene           | 0.0673 |   **0.0654** | 0.0834 | 0.0814 |      0.0687 |     0.0826 |          0.0927 |
| Chalcedony       | 0.0871 |   0.0948 | 0.0761 | 0.0774 |      **0.0623** |     0.0752 |          0.0752 |

### SAM Statistics for Cuprite Dataset. 

| Statistics   |      PPI |   NFINDR |    VCA |    GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-------------|---------:|---------:|-------:|--------:|------------:|-----------:|----------------:|
| _Mean_       |   0.1425 |   0.1012 | 0.0996 |  0.1022 |      0.1004 |     **0.0966** |          0.1005 |
| _Std_        |   **0.0000** |   0.0227 | 0.0243 |  0.0256 |      0.0223 |     0.0148 |          0.0170 |
| _p-value_    | -15.9309 |  -0.4281 | 0.0000 | -0.7551 |     **-0.2328** |     0.8653 |         -0.2714 |
| Gain         |  32.2290 |   4.5119 | 3.0062 |  5.4635 |      3.8298 |     **0.0000** |          3.8609 |
| _Time_       |   2.2118 |   8.4757 | **0.5226** |  2.4932 |      5.7155 |     2.5397 |          5.7591 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |    PPI |   NFINDR |    VCA |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-------:|---------:|-------:|-------:|------------:|-----------:|----------------:|
| Alunite          | **0.0000** |   **0.0000** | 0.0133 | **0.0000** |      **0.0000** |     **0.0000** |          **0.0000** |
| Andradite        | **0.0000** |   0.0092 | 0.0071 | 0.0071 |      **0.0000** |     0.0082 |          0.0090 |
| Buddingtonite    | 0.0477 |   0.0211 | 0.0080 | 0.0193 |      0.0219 |     **0.0072** |          **0.0072** |
| Dumortierite     | 0.0562 |   0.0071 | **0.0069** | 0.0077 |      0.0125 |     0.0071 |          0.0071 |
| Kaolinite_1      | 0.0114 |   0.0131 | **0.0089** | 0.0133 |      0.0132 |     0.0166 |          0.0177 |
| Kaolinite_2      | 0.0114 |   0.0082 | 0.0076 | 0.0055 |      **0.0032** |     0.0101 |          0.0052 |
| Muscovite        | 0.0969 |   0.0267 | 0.0148 | 0.0284 |      **0.0113** |     0.0317 |          0.0317 |
| Montmonrillonite | 0.0230 |   **0.0049** | 0.0059 | 0.0051 |      0.0052 |     **0.0049** |          **0.0049** |
| Nontronite       | 0.0126 |   0.0083 | **0.0071** | 0.0088 |      0.0095 |     0.0119 |          0.0119 |
| Pyrope           | 0.0071 |   0.0625 | 0.0419 | **0.0061** |      0.0108 |     0.0438 |          0.0389 |
| Sphene           | **0.0076** |   0.0943 | 0.0096 | 0.0383 |      0.0408 |     0.0090 |          0.0104 |
| Chalcedony       | 0.0088 |   0.0104 | 0.0069 | **0.0042** |      0.0051 |     0.0067 |          0.0067 |

### SID Statistics for Cuprite Dataset. 

| Statistics   |     PPI |   NFINDR |     VCA |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-------------|--------:|---------:|--------:|-------:|------------:|-----------:|----------------:|
| _Mean_       |  0.0236 |   0.0258 |  0.0161 | **0.0148** |      0.0166 |     0.0163 |          0.0205 |
| _Std_        |  **0.0000** |   0.0056 |  0.0099 | 0.0071 |      0.0082 |     0.0060 |          0.0079 |
| _p-value_    | -4.6358 |  -5.6933 |  0.0000 | 0.7856 |     -0.2904 |    **-0.0764** |         -1.7339 |
| Gain         | 28.3124 |  **-1.0066** | -2.5993 | 0.0000 |     -1.7281 |    -5.7792 |         -1.6952 |
| _Time_       |  2.2118 |   8.4757 |  **0.5226** | 2.4932 |      5.7155 |     2.5397 |          5.7591 |

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


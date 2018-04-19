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

| Endmembers       |    PPI |   NFINDR |    VCA |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-------:|---------:|-------:|-------:|------------:|-----------:|----------------:|
| Alunite          | 0.3744 |   **0.0926** | 0.1283 | 0.1399 |      0.1025 |     0.1034 |          0.1034 |
| Andradite        | 0.0758 |   0.0725 | 0.0825 | 0.0730 |      0.0651 |     0.0843 |          **0.0586** |
| Buddingtonite    | 0.2081 |   **0.0762** | 0.0786 | 0.1224 |      0.1201 |     **0.0762** |          **0.0762** |
| Dumortierite     | 0.1907 |   0.0720 | 0.0951 | **0.0717** |      0.0724 |     0.0878 |          0.0767 |
| Kaolinite_1      | **0.0795** |   0.0870 | 0.0834 | 0.1146 |      0.1277 |     0.0892 |          0.1243 |
| Kaolinite_2      | 0.0820 |   0.0889 | 0.0876 | 0.0736 |      **0.0627** |     0.0775 |          0.0912 |
| Muscovite        | 0.2506 |   0.1091 | **0.0887** | 0.1689 |      0.1824 |     0.1205 |          0.1394 |
| Montmonrillonite | 0.1338 |   0.0648 | 0.0651 | **0.0603** |      0.0750 |     0.0628 |          0.0657 |
| Nontronite       | 0.1033 |   0.0758 | 0.1169 | 0.0779 |      **0.0644** |     0.0931 |          0.0818 |
| Pyrope           | **0.0579** |   0.1222 | 0.2306 | 0.1085 |      0.0605 |     0.2324 |          0.1025 |
| Sphene           | **0.0673** |   0.2857 | 0.0799 | 0.0692 |      0.0712 |     0.0826 |          0.0826 |
| Chalcedony       | 0.0871 |   0.0871 | **0.0761** | 0.1034 |      0.1183 |     0.0871 |          0.0871 |

### SAM Statistics for Cuprite Dataset. 

| Statistics   |      PPI |   NFINDR |    VCA |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-------------|---------:|---------:|-------:|-------:|------------:|-----------:|----------------:|
| _Mean_       |   0.1425 |   0.1059 | 0.1041 | 0.0996 |      0.1038 |     0.1050 |          **0.0928** |
| _Std_        |   **0.0000** |   0.0086 | 0.0088 | 0.0120 |      0.0120 |     0.0119 |          0.0070 |
| _p-value_    | -12.8149 |  -0.4327 | 0.0000 | 1.4136 |      0.0227 |    **-0.1543** |          3.1273 |
| _Time_       |   0.2225 |   4.0309 | 0.7839 | 0.2265 |      0.2204 |     **0.2022** |          0.2157 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |    PPI |   NFINDR |    VCA |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-------:|---------:|-------:|-------:|------------:|-----------:|----------------:|
| Alunite          | **0.0000** |   **0.0000** | 0.0113 | **0.0000** |      **0.0000** |     0.0137 |          0.0137 |
| Andradite        | **0.0000** |   0.0062 | 0.0080 | 0.0080 |      **0.0000** |     0.0085 |          0.0056 |
| Buddingtonite    | 0.0477 |   0.0072 | 0.0077 | 0.0197 |      **0.0000** |     0.0072 |          0.0072 |
| Dumortierite     | 0.0562 |   0.0069 | 0.0072 | 0.0077 |      **0.0066** |     0.0119 |          0.0230 |
| Kaolinite_1      | **0.0114** |   0.0131 | 0.0129 | 0.0156 |      0.0217 |     0.0150 |          0.0196 |
| Kaolinite_2      | 0.0114 |   0.0109 | 0.0117 | 0.0078 |      **0.0046** |     0.0067 |          0.0060 |
| Muscovite        | 0.0969 |   0.0317 | 0.0257 | 0.0304 |      0.0253 |     0.0339 |          **0.0152** |
| Montmonrillonite | 0.0230 |   0.0049 | 0.0049 | 0.0047 |      0.0073 |     0.0052 |          **0.0040** |
| Nontronite       | 0.0126 |   0.0077 | 0.0102 | 0.0077 |      **0.0064** |     0.0126 |          0.0075 |
| Pyrope           | **0.0071** |   0.0531 | 0.0187 | 0.0113 |      0.0085 |     0.0595 |          0.0249 |
| Sphene           | **0.0076** |   0.0912 | 0.0122 | 0.0299 |      0.0182 |     0.0090 |          0.0090 |
| Chalcedony       | **0.0088** |   **0.0088** | 0.0090 | 0.0140 |      0.0172 |     **0.0088** |          **0.0088** |

### SID Statistics for Cuprite Dataset. 

| Statistics   |     PPI |   NFINDR |    VCA |    GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-------------|--------:|---------:|-------:|--------:|------------:|-----------:|----------------:|
| _Mean_       |  0.0236 |   0.0227 | 0.0134 |  0.0144 |      **0.0115** |     0.0167 |          0.0130 |
| _Std_        |  **0.0000** |   0.0033 | 0.0041 |  0.0036 |      0.0028 |     0.0048 |          0.0036 |
| _p-value_    | -5.6963 |  -2.9857 | 0.0000 | **-0.4342** |      0.7537 |    -1.7150 |          0.1888 |
| _Time_       |  0.2225 |   4.0309 | 0.7839 |  0.2265 |      0.2204 |     **0.2022** |          0.2157 |

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


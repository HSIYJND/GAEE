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
| Alunite          | 0.3744 |   **0.0926** | 0.1025 | 0.2554 |      0.2839 |     0.1043 |          0.1043 |
| Andradite        | 0.0758 |   0.0725 | **0.0671** | 0.0717 |      0.0682 |     0.0791 |          0.0797 |
| Buddingtonite    | 0.2081 |   **0.0762** | 0.0786 | 0.1274 |      0.1255 |     **0.0762** |          **0.0762** |
| Dumortierite     | 0.1907 |   0.0720 | **0.0702** | 0.0899 |      0.0896 |     0.1198 |          0.0789 |
| Kaolinite_1      | **0.0795** |   0.0870 | 0.0862 | 0.1048 |      0.0883 |     0.0870 |          0.0870 |
| Kaolinite_2      | 0.0820 |   0.0889 | 0.0639 | 0.0708 |      **0.0593** |     0.0630 |          0.0758 |
| Muscovite        | 0.2506 |   **0.1091** | 0.1306 | 0.1633 |      0.1756 |     **0.1091** |          **0.1091** |
| Montmonrillonite | 0.1338 |   0.0648 | **0.0640** | 0.0670 |      0.0660 |     0.0726 |          0.0646 |
| Nontronite       | 0.1033 |   0.0758 | 0.0799 | 0.0783 |      **0.0728** |     0.0758 |          0.0826 |
| Pyrope           | **0.0579** |   0.1222 | 0.2933 | 0.0603 |      0.0636 |     0.0781 |          0.1105 |
| Sphene           | **0.0673** |   0.2857 | 0.0770 | 0.1127 |      0.0819 |     0.2154 |          0.0693 |
| Chalcedony       | 0.0871 |   0.0871 | 0.0953 | 0.1224 |      0.0853 |     **0.0752** |          **0.0752** |

### SAM Statistics for Cuprite Dataset. 

| Statistics   |     PPI |   NFINDR |     VCA |    GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-------------|--------:|---------:|--------:|--------:|------------:|-----------:|----------------:|
| _Mean_       |  0.1425 |   0.1059 |  0.1055 |  0.1191 |      0.1081 |     0.0969 |          **0.0867** |
| _Std_        |  **0.0000** |   0.0086 |  0.0177 |  0.0137 |      0.0100 |     0.0185 |          0.0046 |
| _p-value_    | -7.7174 |  **-0.0756** |  0.0000 | -1.3599 |     -0.4524 |     1.7790 |          3.5647 |
| Gain         | 39.2077 |  -2.0236 | -2.4421 |  9.2518 |      0.0000 |   **-11.5383** |        -24.7343 |
| _Time_       |  0.3415 |   4.0307 |  0.7263 |  0.3175 |      0.2477 |     0.2476 |          **0.2470** |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |    PPI |   NFINDR |    VCA |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-------:|---------:|-------:|-------:|------------:|-----------:|----------------:|
| Alunite          | **0.0000** |   **0.0000** | 0.0140 | **0.0000** |      **0.0000** |     **0.0000** |          **0.0000** |
| Andradite        | **0.0000** |   0.0062 | 0.0065 | **0.0000** |      0.0055 |     0.0131 |          **0.0000** |
| Buddingtonite    | 0.0477 |   0.0072 | 0.0200 | **0.0000** |      0.0204 |     0.0505 |          0.0072 |
| Dumortierite     | 0.0562 |   **0.0069** | 0.0072 | 0.0116 |      0.0117 |     0.0075 |          0.0207 |
| Kaolinite_1      | 0.0114 |   0.0131 | 0.0129 | 0.0137 |      0.0134 |     **0.0073** |          0.0131 |
| Kaolinite_2      | 0.0114 |   0.0109 | 0.0057 | 0.0062 |      **0.0052** |     0.0109 |          0.0064 |
| Muscovite        | 0.0969 |   0.0317 | 0.0217 | 0.0320 |      0.0384 |     0.0285 |          **0.0152** |
| Montmonrillonite | 0.0230 |   0.0049 | 0.0053 | 0.0051 |      0.0050 |     0.0052 |          **0.0047** |
| Nontronite       | 0.0126 |   0.0077 | 0.0102 | 0.0082 |      **0.0076** |     0.0077 |          0.0079 |
| Pyrope           | 0.0071 |   0.0531 | 0.0348 | 0.0112 |      **0.0068** |     0.0079 |          0.0115 |
| Sphene           | **0.0076** |   0.0912 | 0.0911 | 0.0462 |      0.0251 |     0.0529 |          0.0529 |
| Chalcedony       | 0.0088 |   0.0088 | 0.0070 | 0.0217 |      0.0093 |     **0.0067** |          **0.0067** |

### SID Statistics for Cuprite Dataset. 

| Statistics   |     PPI |   NFINDR |     VCA |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-------------|--------:|---------:|--------:|-------:|------------:|-----------:|----------------:|
| _Mean_       |  0.0236 |   0.0227 |  0.0242 | 0.0144 |      **0.0134** |     0.0191 |          0.0183 |
| _Std_        |  **0.0000** |   0.0033 |  0.0071 | 0.0044 |      0.0039 |     0.0081 |          0.0063 |
| _p-value_    |  0.1484 |   0.3000 |  **0.0000** | 2.0795 |      2.3326 |     0.9717 |          0.7844 |
| Gain         | 24.1712 |  -2.0236 | -2.4421 | 9.2518 |      0.0000 |   **-11.5383** |        -24.7343 |
| _Time_       |  0.3415 |   4.0307 |  0.7263 | 0.3175 |      0.2477 |     0.2476 |          **0.2470** |

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


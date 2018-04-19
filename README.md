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
| Alunite          | 0.3744 |   0.0926 | **0.0914** | 0.1433 |      0.2828 |     0.1043 |          0.1043 |
| Andradite        | 0.0758 |   **0.0725** | 0.0921 | 0.0750 |      0.0782 |     0.0947 |          0.0959 |
| Buddingtonite    | 0.2081 |   **0.0762** | 0.0786 | 0.1528 |      0.1181 |     **0.0762** |          **0.0762** |
| Dumortierite     | 0.1907 |   0.0720 | **0.0708** | 0.0757 |      0.0789 |     0.0721 |          0.0721 |
| Kaolinite_1      | **0.0795** |   0.0870 | 0.0862 | 0.1067 |      0.0876 |     0.0811 |          0.0811 |
| Kaolinite_2      | 0.0820 |   0.0889 | 0.0844 | 0.0809 |      **0.0619** |     0.0815 |          0.0835 |
| Muscovite        | 0.2506 |   **0.1091** | 0.1205 | 0.2084 |      0.1883 |     0.1211 |          0.1766 |
| Montmonrillonite | 0.1338 |   0.0648 | 0.0643 | 0.0953 |      **0.0625** |     0.0652 |          0.0704 |
| Nontronite       | 0.1033 |   0.0758 | 0.0930 | **0.0730** |      0.0844 |     0.0843 |          0.0744 |
| Pyrope           | 0.0579 |   0.1222 | 0.2768 | 0.0670 |      0.0700 |     **0.0516** |          0.0605 |
| Sphene           | **0.0673** |   0.2857 | 0.0686 | 0.0724 |      0.0727 |     0.2213 |          0.2213 |
| Chalcedony       | 0.0871 |   0.0871 | 0.0761 | 0.1301 |      0.1455 |     **0.0752** |          **0.0752** |

### SAM Statistics for Cuprite Dataset. 

| Statistics   |       PPI |   NFINDR |     VCA |     GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-------------|----------:|---------:|--------:|---------:|------------:|-----------:|----------------:|
| _Mean_       |    0.1425 |   0.1059 |  0.1003 |   0.1083 |      0.1147 |     **0.0950** |          0.1004 |
| _Std_        |    **0.0000** |   0.0086 |  0.0198 |   0.0142 |      0.0055 |     0.0070 |          0.0011 |
| _p-value_    | -406.5868 |  -1.7977 |  0.0000 |  -5.0958 |     -3.8004 |     5.4148 |         **-0.0812** |
| Gain         |  -33.3398 | **-10.3123** | -5.2998 | -12.2245 |    -17.1464 |     0.0000 |         -5.3879 |
| _Time_       |    0.2523 |   3.8492 |  0.7061 |   0.2528 |      0.2459 |     **0.2334** |          0.2467 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |    PPI |   NFINDR |    VCA |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-------:|---------:|-------:|-------:|------------:|-----------:|----------------:|
| Alunite          | **0.0000** |   **0.0000** | 0.0105 | **0.0000** |      **0.0000** |     0.0145 |          0.0145 |
| Andradite        | **0.0000** |   0.0062 | 0.0156 | 0.0055 |      **0.0000** |     0.0098 |          0.0139 |
| Buddingtonite    | 0.0477 |   0.0072 | 0.0077 | 0.0196 |      **0.0000** |     0.0072 |          0.0072 |
| Dumortierite     | 0.0562 |   0.0069 | 0.0075 | 0.0207 |      **0.0000** |     0.0143 |          0.0075 |
| Kaolinite_1      | 0.0114 |   0.0131 | **0.0108** | 0.0126 |      0.0113 |     0.0126 |          0.0126 |
| Kaolinite_2      | 0.0114 |   0.0109 | 0.0057 | 0.0046 |      **0.0040** |     0.0048 |          0.0098 |
| Muscovite        | 0.0969 |   0.0317 | **0.0187** | 0.0323 |      0.0272 |     0.0295 |          0.0420 |
| Montmonrillonite | 0.0230 |   0.0049 | **0.0047** | 0.0050 |      0.0053 |     0.0052 |          0.0055 |
| Nontronite       | 0.0126 |   0.0077 | 0.0087 | 0.0080 |      0.0082 |     0.0086 |          **0.0074** |
| Pyrope           | **0.0071** |   0.0531 | 0.0098 | 0.0190 |      0.0180 |     0.0123 |          **0.0071** |
| Sphene           | 0.0076 |   0.0912 | 0.0911 | **0.0075** |      0.0551 |     0.0303 |          0.0529 |
| Chalcedony       | 0.0088 |   0.0088 | 0.0069 | 0.0302 |      0.0206 |     **0.0067** |          **0.0067** |

### SID Statistics for Cuprite Dataset. 

| Statistics   |      PPI |   NFINDR |     VCA |     GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-------------|---------:|---------:|--------:|---------:|------------:|-----------:|----------------:|
| _Mean_       |   0.0236 |   0.0227 |  0.0233 |   0.0159 |      0.0137 |     **0.0131** |          0.0178 |
| _Std_        |   **0.0000** |   0.0033 |  0.0084 |   0.0042 |      0.0046 |     0.0026 |          0.0029 |
| _p-value_    |  **-0.0453** |   0.0800 |  0.0000 |   1.0388 |      1.3858 |     1.4958 |          0.7724 |
| Gain         | -33.3398 | **-10.3123** | -5.2998 | -12.2245 |    -17.1464 |     0.0000 |         -5.3879 |
| _Time_       |   0.2523 |   3.8492 |  0.7061 |   0.2528 |      0.2459 |     **0.2334** |          0.2467 |

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


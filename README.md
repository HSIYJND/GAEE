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
| Alunite          | 0.3744 |   **0.0926** | 0.1025 | 0.2242 |      0.3112 |     **0.0926** |          **0.0926** |
| Andradite        | 0.0758 |   0.0725 | 0.0825 | **0.0669** |      0.0701 |     0.0710 |          0.0789 |
| Buddingtonite    | 0.2081 |   **0.0762** | 0.0786 | 0.1266 |      0.0906 |     0.1550 |          **0.0762** |
| Dumortierite     | 0.1907 |   0.0720 | **0.0708** | 0.0896 |      0.0791 |     0.0755 |          0.1209 |
| Kaolinite_1      | **0.0795** |   0.0870 | 0.0862 | 0.0875 |      0.1053 |     0.0870 |          0.0870 |
| Kaolinite_2      | 0.0820 |   0.0889 | 0.0785 | **0.0628** |      0.0660 |     0.0936 |          0.0658 |
| Muscovite        | 0.2506 |   0.1091 | **0.1084** | 0.1752 |      0.1610 |     0.1825 |          0.1211 |
| Montmonrillonite | 0.1338 |   0.0648 | 0.0651 | 0.0656 |      0.0669 |     0.0657 |          **0.0646** |
| Nontronite       | 0.1033 |   0.0758 | 0.1122 | **0.0718** |      0.0795 |     0.0789 |          0.0801 |
| Pyrope           | **0.0579** |   0.1222 | 0.2768 | 0.0601 |      0.0778 |     0.0670 |          0.0588 |
| Sphene           | 0.0673 |   0.2857 | **0.0530** | 0.0990 |      0.0638 |     0.1000 |          0.2182 |
| Chalcedony       | **0.0871** |   **0.0871** | 0.0878 | 0.1388 |      0.1221 |     **0.0871** |          **0.0871** |

### SAM Statistics for Cuprite Dataset. 

| Statistics   |      PPI |   NFINDR |    VCA |    GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-------------|---------:|---------:|-------:|--------:|------------:|-----------:|----------------:|
| _Mean_       |   0.1425 |   0.1059 | 0.1030 |  0.1107 |      0.1126 |     0.1040 |          **0.0976** |
| _Std_        |   **0.0000** |   0.0086 | 0.0260 |  0.0061 |      0.0082 |     0.0142 |          0.0018 |
| _p-value_    | -13.9798 |  -0.6928 | 0.0000 | -1.3316 |     -1.7156 |    **-0.1215** |          1.6440 |
| Gain         |  31.5080 |   7.8477 | 5.2402 | 11.7820 |     13.2709 |     6.1464 |         **-0.0000** |
| _Time_       |   0.2455 |   3.9192 | 0.7190 |  0.2367 |      0.2436 |     **0.2148** |          0.2480 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |    PPI |   NFINDR |    VCA |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-------:|---------:|-------:|-------:|------------:|-----------:|----------------:|
| Alunite          | **0.0000** |   **0.0000** | 0.0140 | **0.0000** |      **0.0000** |     **0.0000** |          0.0107 |
| Andradite        | **0.0000** |   0.0062 | 0.0256 | **0.0000** |      **0.0000** |     **0.0000** |          0.0119 |
| Buddingtonite    | 0.0477 |   0.0072 | 0.0077 | **0.0000** |      0.0105 |     0.0325 |          0.0072 |
| Dumortierite     | 0.0562 |   0.0069 | **0.0056** | 0.0130 |      0.0084 |     0.0077 |          0.0197 |
| Kaolinite_1      | **0.0114** |   0.0131 | 0.0129 | 0.0180 |      0.0127 |     0.0131 |          0.0131 |
| Kaolinite_2      | 0.0114 |   0.0109 | 0.0132 | **0.0057** |      0.0059 |     0.0102 |          0.0061 |
| Muscovite        | 0.0969 |   0.0317 | **0.0108** | 0.0416 |      0.0320 |     0.0317 |          0.0189 |
| Montmonrillonite | 0.0230 |   0.0049 | 0.0054 | 0.0052 |      0.0053 |     0.0056 |          **0.0047** |
| Nontronite       | 0.0126 |   0.0077 | 0.0093 | **0.0073** |      0.0082 |     0.0076 |          0.0079 |
| Pyrope           | 0.0071 |   0.0531 | **0.0048** | 0.0073 |      0.0089 |     0.0144 |          0.0081 |
| Sphene           | **0.0076** |   0.0912 | 0.1187 | 0.0209 |      0.0241 |     0.0550 |          0.0550 |
| Chalcedony       | 0.0088 |   0.0088 | **0.0078** | 0.0272 |      0.0270 |     0.0088 |          0.0088 |

### SID Statistics for Cuprite Dataset. 

| Statistics   |     PPI |   NFINDR |     VCA |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-------------|--------:|---------:|--------:|-------:|------------:|-----------:|----------------:|
| _Mean_       |  0.0236 |   0.0227 |  0.0238 | **0.0130** |      0.0151 |     0.0160 |          0.0194 |
| _Std_        |  **0.0000** |   0.0033 |  0.0073 | 0.0031 |      0.0039 |     0.0029 |          0.0059 |
| _p-value_    |  0.0620 |   0.2344 |  **0.0000** | 2.5285 |      1.6629 |     1.8505 |          0.6786 |
| Gain         | 22.3605 |  -4.4597 | -7.4155 | 0.0000 |      1.6878 |    -6.3882 |        **-13.3555** |
| _Time_       |  0.2455 |   3.9192 |  0.7190 | 0.2367 |      0.2436 |     **0.2148** |          0.2480 |

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


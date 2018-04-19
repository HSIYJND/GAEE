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
| Alunite          | 0.3744 |   **0.0926** | 0.1016 | 0.2821 |      0.2495 |     0.2154 |          0.1433 |
| Andradite        | 0.0758 |   **0.0725** | 0.0874 | 0.0736 |      0.0763 |     0.0796 |          0.0832 |
| Buddingtonite    | 0.2081 |   **0.0762** | 0.0786 | 0.1115 |      0.1240 |     **0.0762** |          **0.0762** |
| Dumortierite     | 0.1907 |   0.0720 | **0.0708** | 0.0796 |      0.0905 |     0.1007 |          0.0721 |
| Kaolinite_1      | **0.0795** |   0.0870 | 0.1191 | 0.0851 |      0.1025 |     0.1242 |          0.1556 |
| Kaolinite_2      | 0.0820 |   0.0889 | 0.0811 | **0.0621** |      0.0657 |     0.0679 |          0.0886 |
| Muscovite        | 0.2506 |   0.1091 | **0.1065** | 0.1635 |      0.1774 |     0.1454 |          0.1211 |
| Montmonrillonite | 0.1338 |   0.0648 | **0.0640** | 0.0649 |      0.0804 |     0.0653 |          0.0646 |
| Nontronite       | 0.1033 |   **0.0758** | 0.0799 | 0.0781 |      0.0771 |     0.0820 |          0.0771 |
| Pyrope           | **0.0579** |   0.1222 | 0.2140 | 0.0695 |      0.0674 |     0.0616 |          0.2310 |
| Sphene           | **0.0673** |   0.2857 | 0.0834 | 0.0781 |      0.1147 |     0.0698 |          0.0698 |
| Chalcedony       | 0.0871 |   0.0871 | **0.0761** | 0.1175 |      0.1083 |     0.0765 |          0.0765 |

### SAM Statistics for Cuprite Dataset. 

| Statistics   |      PPI |   NFINDR |     VCA |    GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-------------|---------:|---------:|--------:|--------:|------------:|-----------:|----------------:|
| _Mean_       |   0.1425 |   0.1059 |  **0.0984** |  0.1106 |      0.1139 |     0.1054 |          0.1054 |
| _Std_        |   **0.0000** |   0.0086 |  0.0065 |  0.0094 |      0.0109 |     0.0131 |          0.0142 |
| _p-value_    | -28.8327 |  -2.1689 |  0.0000 | -2.2800 |     -4.8922 |    **-0.8218** |         -4.3537 |
| Gain         |  26.0739 |   0.5364 | **-7.0768** |  4.7203 |      7.5104 |     0.0000 |          0.0460 |
| _Time_       |   0.2686 |   4.0963 |  0.6955 |  0.2738 |      0.2505 |     0.2393 |          **0.2325** |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |    PPI |   NFINDR |    VCA |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-------:|---------:|-------:|-------:|------------:|-----------:|----------------:|
| Alunite          | **0.0000** |   **0.0000** | 0.0133 | **0.0000** |      **0.0000** |     **0.0000** |          **0.0000** |
| Andradite        | **0.0000** |   0.0062 | 0.0087 | 0.0063 |      **0.0000** |     0.0085 |          0.0119 |
| Buddingtonite    | 0.0477 |   **0.0072** | 0.0077 | 0.0197 |      0.0187 |     **0.0072** |          **0.0072** |
| Dumortierite     | 0.0562 |   **0.0069** | 0.0072 | 0.0084 |      0.0130 |     0.0151 |          0.0075 |
| Kaolinite_1      | 0.0114 |   0.0131 | 0.0167 | **0.0108** |      0.0175 |     0.0181 |          0.0256 |
| Kaolinite_2      | 0.0114 |   0.0109 | 0.0076 | 0.0064 |      **0.0039** |     0.0053 |          0.0078 |
| Muscovite        | 0.0969 |   0.0317 | **0.0143** | 0.0360 |      0.0390 |     0.0429 |          0.0313 |
| Montmonrillonite | 0.0230 |   0.0049 | 0.0049 | 0.0051 |      0.0049 |     0.0049 |          **0.0047** |
| Nontronite       | 0.0126 |   0.0077 | **0.0075** | 0.0077 |      0.0077 |     0.0094 |          0.0155 |
| Pyrope           | 0.0071 |   0.0531 | 0.0532 | **0.0065** |      0.0071 |     0.0071 |          0.0740 |
| Sphene           | **0.0076** |   0.0912 | 0.0096 | 0.0259 |      0.0308 |     0.0093 |          0.0093 |
| Chalcedony       | 0.0088 |   0.0088 | **0.0069** | 0.0190 |      0.0307 |     0.0070 |          0.0070 |

### SID Statistics for Cuprite Dataset. 

| Statistics   |     PPI |   NFINDR |      VCA |    GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-------------|--------:|---------:|---------:|--------:|------------:|-----------:|----------------:|
| _Mean_       |  0.0236 |   0.0227 |   0.0216 |  0.0167 |      **0.0159** |     0.0164 |          0.0170 |
| _Std_        |  **0.0000** |   0.0033 |   0.0102 |  0.0056 |      0.0020 |     0.0072 |          0.0026 |
| _p-value_    | -0.2377 |  **-0.1269** |   0.0000 |  0.5195 |      0.6644 |     0.5181 |          0.5412 |
| Gain         | 20.0709 |  -7.5403 | **-15.7717** | -3.0167 |      0.0000 |    -8.1203 |         -8.0706 |
| _Time_       |  0.2686 |   4.0963 |   0.6955 |  0.2738 |      0.2505 |     0.2393 |          **0.2325** |

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


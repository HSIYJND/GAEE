# Comparison of Vertex Componet Analysis (VCA) and Genetic Algorithm Endmember Extraction (GAEE) algorithms for Endmember Extraction

## Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

**Envirionment Setup:**

Monte Carlo runs: 1 

Number of endmembers to estimate: 12 

Number of skewers (PPI): 1000 

Maximum number of iterations (N-FINDR): 36 

### Parameters used in each GAEE versions

| Parameters            |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:----------------------|-------:|------------:|-----------:|----------------:|
| Population Size       |  100   |       100   |      100   |           100   |
| Number of Generations |  250   |       250   |      250   |           250   |
| Crossover Probability |    1   |         1   |        1   |             1   |
| Mutation Probability  |    0.3 |         0.3 |        0.3 |             0.3 |

![alt text](./IMAGES/Convergence.png)

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |    PPI |   NFINDR |    VCA |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-------:|---------:|-------:|-------:|------------:|-----------:|----------------:|
| Alunite          | 0.3744 |   0.1127 | 0.1086 | 0.0989 |      0.1043 |     **0.0952** |          **0.0952** |
| Andradite        | 0.0758 |   0.2068 | **0.0574** | 0.0693 |      0.0837 |     0.0732 |          0.0705 |
| Buddingtonite    | 0.2081 |   0.1205 | 0.0824 | 0.1225 |      0.1170 |     0.1502 |          **0.0762** |
| Dumortierite     | 0.1907 |   **0.0720** | 0.1167 | 0.0929 |      **0.0720** |     0.0721 |          0.0721 |
| Kaolinite_1      | **0.0795** |   0.0870 | 0.0893 | 0.1181 |      0.0870 |     0.0811 |          0.0811 |
| Kaolinite_2      | 0.0820 |   0.0992 | 0.0674 | **0.0480** |      0.0658 |     0.0936 |          0.0746 |
| Muscovite        | 0.2506 |   **0.0983** | 0.2288 | 0.1449 |      0.1694 |     0.2046 |          0.1766 |
| Montmonrillonite | 0.1338 |   **0.0646** | 0.0893 | 0.0658 |      0.0660 |     **0.0646** |          0.0694 |
| Nontronite       | 0.1033 |   0.0806 | 0.0799 | 0.0758 |      **0.0729** |     0.0806 |          0.0870 |
| Pyrope           | **0.0579** |   0.0865 | 0.1714 | 0.0714 |      0.0835 |     0.1942 |          0.0744 |
| Sphene           | 0.0673 |   **0.0542** | 0.0692 | 0.3481 |      0.2112 |     0.0770 |          0.2213 |
| Chalcedony       | 0.0871 |   0.0762 | 0.0878 | 0.0923 |      **0.0699** |     0.0752 |          0.0752 |

### SAM Statistics for Cuprite Dataset. 

| Statistics   |      PPI |   NFINDR |      VCA |     GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-------------|---------:|---------:|---------:|---------:|------------:|-----------:|----------------:|
| _Mean_       |   0.1425 |   **0.0966** |   0.1040 |   0.1123 |      0.1002 |     0.1051 |          0.0978 |
| _Std_        |   **0.0000** |   **0.0000** |   **0.0000** |   **0.0000** |      **0.0000** |     **0.0000** |          **0.0000** |
| _p-value_    | **nan**      | **nan**      | **nan**      | **nan**      |    **nan**      |   **nan**      |        **nan**      |
| Gain         |  31.3952 |  **-1.2719** |   5.9801 |  12.9356 |      2.4445 |     6.9874 |          0.0000 |
| _Time_       |   4.5994 |  57.5599 |   **0.5803** |   6.9029 |     15.6723 |     6.8193 |         15.9504 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |    PPI |   NFINDR |    VCA |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-------:|---------:|-------:|-------:|------------:|-----------:|----------------:|
| Alunite          | **0.0000** |   **0.0000** | 0.0147 | **0.0000** |      **0.0000** |     **0.0000** |          **0.0000** |
| Andradite        | **0.0000** |   **0.0000** | 0.0052 | 0.0061 |      **0.0000** |     0.0086 |          0.0060 |
| Buddingtonite    | 0.0477 |   0.0196 | 0.0080 | 0.0181 |      0.0165 |     0.0301 |          **0.0072** |
| Dumortierite     | 0.0562 |   **0.0069** | 0.0159 | 0.0120 |      **0.0069** |     0.0075 |          0.0075 |
| Kaolinite_1      | **0.0114** |   0.0131 | 0.0143 | 0.0164 |      0.0131 |     0.0126 |          0.0126 |
| Kaolinite_2      | 0.0114 |   0.0131 | 0.0055 | **0.0031** |      0.0061 |     0.0102 |          0.0084 |
| Muscovite        | 0.0969 |   **0.0113** | 0.1015 | 0.0250 |      0.0285 |     0.0290 |          0.0290 |
| Montmonrillonite | 0.0230 |   **0.0047** | 0.0103 | 0.0052 |      0.0050 |     **0.0047** |          0.0061 |
| Nontronite       | 0.0126 |   0.0093 | 0.0075 | 0.0078 |      **0.0072** |     0.0093 |          0.0100 |
| Pyrope           | **0.0071** |   0.0890 | 0.0335 | 0.0647 |      0.0270 |     0.0420 |          0.0209 |
| Sphene           | **0.0076** |   0.1331 | 0.0092 | 0.1581 |      0.0706 |     0.0652 |          0.0529 |
| Chalcedony       | 0.0088 |   0.0077 | 0.0090 | 0.0117 |      **0.0058** |     0.0067 |          0.0067 |

### SID Statistics for Cuprite Dataset. 

| Statistics   |      PPI |   NFINDR |      VCA |     GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-------------|---------:|---------:|---------:|---------:|------------:|-----------:|----------------:|
| _Mean_       |   0.0236 |   0.0256 |   0.0196 |   0.0273 |      0.0156 |     0.0188 |          **0.0139** |
| _Std_        |   **0.0000** |   **0.0000** |   **0.0000** |   **0.0000** |      **0.0000** |     **0.0000** |          **0.0000** |
| _p-value_    | **nan**      | **nan**      | **nan**      | **nan**      |    **nan**      |   **nan**      |        **nan**      |
| Gain         |  31.3952 |  **-1.2719** |   5.9801 |  12.9356 |      2.4445 |     6.9874 |          0.0000 |
| _Time_       |   4.5994 |  57.5599 |   **0.5803** |   6.9029 |     15.6723 |     6.8193 |         15.9504 |

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


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

| Endmembers       |       PPI |    NFINDR |       VCA |      GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|----------:|----------:|----------:|----------:|------------:|-----------:|----------------:|
| Alunite          | 0.3743766 | 0.1033697 | 0.1104500 | 0.1336420 |   0.2370752 |  **0.0926313** |       **0.0926313** |
| Andradite        | 0.0757956 | **0.0724709** | 0.1034098 | 0.0750778 |   0.0802386 |  0.0867231 |       0.0793889 |
| Buddingtonite    | 0.2080900 | 0.0761604 | 0.0785924 | 0.1365738 |   0.1049712 |  **0.0761598** |       **0.0761598** |
| Dumortierite     | 0.1907338 | 0.0720035 | **0.0708485** | 0.1047026 |   0.0916377 |  0.0754879 |       0.0754879 |
| Kaolinite_1      | **0.0794624** | 0.0870056 | 0.0969275 | 0.1230832 |   0.1006144 |  0.0870058 |       0.0870058 |
| Kaolinite_2      | 0.0819634 | 0.0889228 | 0.0657237 | **0.0615690** |   0.0767058 |  0.0938859 |       0.0641441 |
| Muscovite        | 0.2506333 | **0.1091060** | 0.1584696 | 0.2029566 |   0.1402789 |  0.1993443 |       0.1569993 |
| Montmonrillonite | 0.1338156 | 0.0648080 | 0.0650004 | 0.0652345 |   **0.0609964** |  0.0663206 |       0.0646198 |
| Nontronite       | 0.1032919 | 0.0758386 | **0.0754643** | 0.0782970 |   0.0761191 |  0.0780452 |       0.0780452 |
| Pyrope           | **0.0578827** | 0.1221578 | 0.2321769 | 0.0589776 |   0.0792559 |  0.0589284 |       0.0663260 |
| Sphene           | **0.0673108** | 0.2856719 | 0.0834347 | 0.0934243 |   0.0699057 |  0.1108873 |       0.2856719 |
| Chalcedony       | 0.0871248 | 0.0871248 | **0.0760768** | 0.1600500 |   0.0988815 |  0.0765022 |       0.0765022 |

### SAM Statistics for Cuprite Dataset. 

|    | Statistics     | PPI                 | NFINDR               | VCA                  | GAEE                | GAEE-IVFm            | GAEE-VCA             | GAEE-IVFm-VCA        |
|---:|:---------------|:--------------------|:---------------------|:---------------------|:--------------------|:---------------------|:---------------------|:---------------------|
|  0 | ****Statistics**** | PPI                 | NFINDR               | VCA                  | GAEE                | GAEE-IVFm            | GAEE-VCA             | GAEE-IVFm-VCA        |
|  1 | _Mean_         | 0.14254007446914863 | 0.10570019340318214  | 0.10200513677830932  | 0.10794469571082775 | 0.10239273206568295  | **0.0942018628573056**   | 0.10145221835725204  |
|  2 | _Std_          | **0.0**                 | 0.005332150046550546 | 0.018006586214343385 | 0.01742925447424214 | 0.014436726649944541 | 0.013009435994913984 | 0.008158837495002872 |
|  3 | _p-value_      | -64.96720910909326  | -1.7797427240750745  | 0.0                  | -9.270351874940559  | **-0.32820173681186643** | 3.1776968155557737   | 0.4078155669203638   |
|  4 | _Time_         | **0.295522753498517**   | 56.933022763507324   | 0.6149418420027359   | 0.441464971001551   | 0.453566853000666    | 0.4234358465037076   | 0.45532045199070126  |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |       PPI |    NFINDR |       VCA |      GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|----------:|----------:|----------:|----------:|------------:|-----------:|----------------:|
| Alunite          | **0.0000000** | **0.0000000** | **0.0000000** | **0.0000000** |   **0.0000000** |  **0.0000000** |       0.0106528 |
| Andradite        | **0.0000000** | 0.0061679 | 0.0119914 | 0.0081642 |   0.0068158 |  **0.0000000** |       0.0094214 |
| Buddingtonite    | 0.0476680 | **0.0071905** | 0.0076571 | 0.0147471 |   0.0372307 |  **0.0071905** |       **0.0071905** |
| Dumortierite     | 0.0562235 | **0.0068965** | 0.0071826 | 0.0071087 |   0.0110544 |  0.0077469 |       0.0077469 |
| Kaolinite_1      | 0.0113668 | 0.0130991 | 0.0166732 | 0.0142369 |   0.0128849 |  **0.0104453** |       0.0130991 |
| Kaolinite_2      | 0.0113963 | 0.0109124 | **0.0049449** | 0.0088764 |   0.0058211 |  0.0163145 |       0.0058072 |
| Muscovite        | 0.0969470 | 0.0300733 | **0.0257291** | 0.0389879 |   0.0298261 |  0.0316990 |       0.0316361 |
| Montmonrillonite | 0.0229949 | 0.0048775 | 0.0051814 | 0.0068398 |   0.0065041 |  0.0064747 |       **0.0047043** |
| Nontronite       | 0.0126400 | 0.0076655 | 0.0075440 | **0.0070716** |   0.0088840 |  0.0082960 |       0.0082960 |
| Pyrope           | 0.0071348 | 0.0530846 | 0.0891019 | 0.0169950 |   **0.0063414** |  0.0071907 |       0.0104577 |
| Sphene           | **0.0075691** | 0.0912113 | 0.0095759 | 0.0361263 |   0.0172372 |  0.0528866 |       0.0551972 |
| Chalcedony       | 0.0088268 | 0.0088268 | **0.0069070** | 0.0282016 |   0.0189973 |  0.0070255 |       0.0070255 |

### SID Statistics for Cuprite Dataset. 

|    | Statistics     | PPI                  | NFINDR                | VCA                  | GAEE                  | GAEE-IVFm            | GAEE-VCA             | GAEE-IVFm-VCA        |
|---:|:---------------|:---------------------|:----------------------|:---------------------|:----------------------|:---------------------|:---------------------|:---------------------|
|  0 | ****Statistics**** | PPI                  | NFINDR                | VCA                  | GAEE                  | GAEE-IVFm            | GAEE-VCA             | GAEE-IVFm-VCA        |
|  1 | _Mean_         | 0.02356391693807411  | 0.022101990537315905  | 0.0217683328315709   | 0.015619861447275564  | 0.015147188538679987 | **0.013302314713372591** | 0.020734380764811808 |
|  2 | _Std_          | **0.0**                  | 0.0024464315289225557 | 0.008378669068249906 | 0.0035835537012341243 | 0.003803994083899256 | 0.002828493367664799 | 0.008137670711107336 |
|  3 | _p-value_      | -0.31349528446097896 | **-0.05468902543361741**  | 0.0                  | 1.0734754132972841    | 1.1092277071908274   | 1.4751396539417356   | 0.11971045592537045  |
|  4 | _Time_         | **0.295522753498517**    | 56.933022763507324    | 0.6149418420027359   | 0.441464971001551     | 0.453566853000666    | 0.4234358465037076   | 0.45532045199070126  |


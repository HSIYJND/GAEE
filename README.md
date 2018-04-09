# Comparison of Vertex Componet Analysis (VCA) and Genetic Algorithm Endmember Extraction (GAEE) algorithms for Endmember Extraction

## Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

**Envirionment Setup:**

Monte Carlo runs: 2 

Number of endmembers to estimate: 12 

Number of skewers (PPI): 100 

Maximum number of iterations (N-FINDR): 36 

### Parameters used in each GAEE versions

| Parameters            |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:----------------------|-------:|------------:|-----------:|----------------:|
| Population Size       |   10   |        10   |       10   |           10    |
| Number of Generations |   10   |        10   |       10   |           10    |
| Crossover Probability |    1   |         0.7 |        1   |            1    |
| Mutation Probability  |    0.3 |         0.1 |        0.1 |            0.05 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |       PPI |     NFINDR |       VCA |      GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|----------:|-----------:|----------:|----------:|------------:|-----------:|----------------:|
| Alunite          | 0.374377  | 0.10337    | 0.10163   | 0.278911  |   0.230213  |  0.10337   |      0.10337    |
| Andradite        | 0.0757956 | 0.0724709  | 0.0574171 | 0.0725522 |   0.0736036 |  0.0791063 |      0.0763017  |
| Buddingtonite    | 0.20809   | 0.0761604  | 0.0785924 | 0.110206  |   0.113326  |  0.111295  |      0.111295   |
| Dumortierite     | 0.190734  | 0.0720035  | 0.101134  | 0.0918262 |   0.0701526 |  0.0754879 |      0.0754879  |
| Kaolinite_1      | 0.0794624 | 0.0870056  | 0.119055  | 0.105282  |   0.121893  |  0.0870058 |      0.0870058  |
| Kaolinite_2      | 0.0819634 | 0.0889228  | 0.0638501 | 0.0592271 |   0.0618574 |  0.0885846 |      0.0885846  |
| Muscovite        | 0.250633  | 0.109106   | 0.108403  | 0.173028  |   0.175364  |  0.158656  |      0.158656   |
| Montmonrillonite | 0.133816  | 0.064808   | 0.0651032 | 0.0560136 |   0.0719169 |  0.0651458 |      0.0651458  |
| Nontronite       | 0.103292  | 0.0758386  | 0.0925689 | 0.0772669 |   0.0783621 |  0.0811415 |      0.113673   |
| Pyrope           | 0.0578827 | 0.122158   | 0.231387  | 0.0504287 |   0.0656986 |  0.184205  |      0.0591833  |
| Sphene           | 0.0673108 | 0.285672   | 0.0834347 | 0.134303  |   0.0718936 |  0.0825881 |      0.0825881  |
| Chalcedony       | 0.0871248 | 0.0871248  | 0.0760768 | 0.15817   |   0.102459  |  0.0765022 |      0.0765022  |
| **Mean**         | 0.14254   | 0.1057     | 0.103168  | 0.116685  |   0.111034  |  0.100459  |      0.0954932  |
| **Std**          | 0         | 0.00533215 | 0.0157812 | 0.0117133 |   0.0115826 |  0.0019373 |      0.00680748 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-----------:|-----------:|-----------:|-----------:|------------:|-----------:|----------------:|
| Alunite          | 0          | 0          | 0.0132672  | 0          |  0          | 0.0137122  |     0           |
| Andradite        | 0          | 0.00616789 | 0.00519935 | 0          |  0.00604092 | 0.0118536  |     0.0118536   |
| Buddingtonite    | 0.047668   | 0.0071905  | 0.00765707 | 0          |  0.0268855  | 0.0195927  |     0.0150719   |
| Dumortierite     | 0.0562235  | 0.00689653 | 0.0131428  | 0.00867277 |  0.0101625  | 0.00774689 |     0.00774689  |
| Kaolinite_1      | 0.0113668  | 0.0130991  | 0.0166732  | 0.0186299  |  0.0138731  | 0.0130991  |     0.0130991   |
| Kaolinite_2      | 0.0113963  | 0.0109124  | 0.0057401  | 0.00572299 |  0.00676436 | 0.0102056  |     0.00579339  |
| Muscovite        | 0.096947   | 0.0300733  | 0.0148187  | 0.0337873  |  0.050349   | 0.0305958  |     0.0300733   |
| Montmonrillonite | 0.0229949  | 0.00487745 | 0.00474685 | 0.00679144 |  0.00549469 | 0.00483121 |     0.00483121  |
| Nontronite       | 0.01264    | 0.00766549 | 0.0104262  | 0.00844202 |  0.00802943 | 0.00757381 |     0.0152248   |
| Pyrope           | 0.00713475 | 0.0530846  | 0.0594321  | 0.00664267 |  0.00628618 | 0.0421579  |     0.0889987   |
| Sphene           | 0.00756905 | 0.0912113  | 0.00957585 | 0.00804378 |  0.0156273  | 0.00899202 |     0.00899202  |
| Chalcedony       | 0.00882676 | 0.00882676 | 0.00690701 | 0.0256791  |  0.0209392  | 0.00702554 |     0.00702554  |
| **Mean**         | 0.0235639  | 0.022102   | 0.0163164  | 0.0124111  |  0.0166699  | 0.016179   |     0.0174592   |
| **Std**          | 0          | 0.00244643 | 0.00504979 | 0.00263974 |  0.00494386 | 0.00258302 |     0.000677782 |


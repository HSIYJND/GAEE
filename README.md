# Comparison of Vertex Componet Analysis (VCA) and Genetic Algorithm Endmember Extraction (GAEE) algorithms for Endmember Extraction

## Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

**Envirionment Setup:**

Monte Carlo runs: 2 

Number of endmembers to estimate: 12 

Number of skewers (PPI): 100 

Maximum number of iterations (N-FINDR): 36 

### Parameters used in each GAEE versions|    | Parameters            |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|---:|:----------------------|-------:|------------:|-----------:|----------------:|
|  0 | Population Size       |  10    |       10    |      10    |           10    |
|  1 | Number of Generations |  10    |       10    |      10    |           10    |
|  2 | Crossover Probability |   1    |        1    |       1    |            1    |
|  3 | Mutation Probability  |   0.05 |        0.05 |       0.05 |            0.05 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |       PPI |    NFINDR |       VCA |      GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|----------:|----------:|----------:|----------:|------------:|-----------:|----------------:|
| Alunite          | 0.374377  | 0.112727  | 0.0998835 | 0.124794  |   0.243301  | 0.104276   |      0.104276   |
| Andradite        | 0.0757956 | 0.206837  | 0.0921267 | 0.089696  |   0.0709997 | 0.0912882  |      0.0835683  |
| Buddingtonite    | 0.20809   | 0.120508  | 0.0785924 | 0.129507  |   0.118418  | 0.0761598  |      0.0761598  |
| Dumortierite     | 0.190734  | 0.0720035 | 0.0708485 | 0.076523  |   0.104857  | 0.120902   |      0.0720036  |
| Kaolinite_1      | 0.0794624 | 0.0870056 | 0.100249  | 0.122803  |   0.112571  | 0.0870058  |      0.0870058  |
| Kaolinite_2      | 0.0819634 | 0.099195  | 0.0927827 | 0.0680451 |   0.0655493 | 0.0658336  |      0.0658336  |
| Muscovite        | 0.250633  | 0.0983345 | 0.164724  | 0.190312  |   0.179554  | 0.0960974  |      0.0960974  |
| Montmonrillonite | 0.133816  | 0.0646271 | 0.0609575 | 0.067253  |   0.067885  | 0.0620456  |      0.0646271  |
| Nontronite       | 0.103292  | 0.0805545 | 0.0799378 | 0.0740895 |   0.0742218 | 0.08013    |      0.08013    |
| Pyrope           | 0.0578827 | 0.0865489 | 0.206878  | 0.066966  |   0.0549642 | 0.0556809  |      0.0850606  |
| Sphene           | 0.0673108 | 0.0542064 | 0.0781701 | 0.0964598 |   0.102925  | 0.218232   |      0.285672   |
| Chalcedony       | 0.0871248 | 0.0761866 | 0.0760768 | 0.107935  |   0.151445  | 0.0731364  |      0.0731364  |
| **Mean**         | 0.14254   | 0.10663   | 0.103761  | 0.107186  |   0.116165  | 0.100225   |      0.100854   |
| **Std**          | 0         | 0.0225456 | 0.0172563 | 0.0143764 |   0.0101719 | 0.00860126 |      0.00325426 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-----------:|-----------:|-----------:|-----------:|------------:|-----------:|----------------:|
| Alunite          | 0          | 0          | 0.0130738  | 0          |  0          | 0.0145061  |      0          |
| Andradite        | 0          | 0          | 0.00904997 | 0.00549676 |  0          | 0.00757018 |      0.0319473  |
| Buddingtonite    | 0.047668   | 0.0195927  | 0.00765707 | 0.0161583  |  0.0170231  | 0.0071905  |      0.0071905  |
| Dumortierite     | 0.0562235  | 0.00689653 | 0.00718259 | 0.00905426 |  0.0158393  | 0.0121307  |      0.00689653 |
| Kaolinite_1      | 0.0113668  | 0.0130991  | 0.015911   | 0.0154226  |  0.015538   | 0.0130991  |      0.0130991  |
| Kaolinite_2      | 0.0113963  | 0.0131021  | 0.00939455 | 0.00724293 |  0.00516156 | 0.00610629 |      0.00610629 |
| Muscovite        | 0.096947   | 0.0113106  | 0.0300883  | 0.0258853  |  0.036661   | 0.0107204  |      0.0107204  |
| Montmonrillonite | 0.0229949  | 0.00470432 | 0.00464996 | 0.00486497 |  0.00515576 | 0.00470432 |      0.00470432 |
| Nontronite       | 0.01264    | 0.00927976 | 0.00754401 | 0.00778165 |  0.00785    | 0.00976177 |      0.00976177 |
| Pyrope           | 0.00713475 | 0.0889987  | 0.0469881  | 0.0174765  |  0.0108758  | 0.0291898  |      0.0102339  |
| Sphene           | 0.00756905 | 0.133057   | 0.00859687 | 0.0849334  |  0.0253533  | 0.0912113  |      0.159963   |
| Chalcedony       | 0.00882676 | 0.00769969 | 0.00690701 | 0.0158696  |  0.0489771  | 0.00681987 |      0.00681987 |
| **Mean**         | 0.0235639  | 0.0259477  | 0.0196321  | 0.0194202  |  0.0232174  | 0.0206567  |      0.0236268  |
| **Std**          | 0          | 0.00292633 | 0.00894753 | 0.00292264 |  0.00863323 | 0.00423197 |      0.00301432 |


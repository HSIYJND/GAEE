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
| Population Size       |  10    |       10    |      10    |           10    |
| Number of Generations |  10    |       10    |      10    |           10    |
| Crossover Probability |   1    |        1    |       1    |            1    |
| Mutation Probability  |   0.05 |        0.05 |       0.05 |            0.05 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |       PPI |    NFINDR |       VCA |       GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|----------:|----------:|----------:|-----------:|------------:|-----------:|----------------:|
| Alunite          | 0.374377  | 0.112727  | 0.09136   | 0.282093   |   0.129032  | 0.104276   |      0.104276   |
| Andradite        | 0.0757956 | 0.206837  | 0.0925616 | 0.0731793  |   0.076452  | 0.0785992  |      0.073309   |
| Buddingtonite    | 0.20809   | 0.120508  | 0.0785924 | 0.140967   |   0.12486   | 0.0761598  |      0.0761598  |
| Dumortierite     | 0.190734  | 0.0720035 | 0.0749538 | 0.0797063  |   0.0740043 | 0.0720841  |      0.0717506  |
| Kaolinite_1      | 0.0794624 | 0.0870056 | 0.0862021 | 0.109471   |   0.119916  | 0.0870058  |      0.0870058  |
| Kaolinite_2      | 0.0819634 | 0.099195  | 0.0740539 | 0.0649451  |   0.0731602 | 0.0757646  |      0.0757646  |
| Muscovite        | 0.250633  | 0.0983345 | 0.120549  | 0.157837   |   0.163845  | 0.168116   |      0.125328   |
| Montmonrillonite | 0.133816  | 0.0646271 | 0.066696  | 0.0641655  |   0.0723196 | 0.0646271  |      0.0646271  |
| Nontronite       | 0.103292  | 0.0805545 | 0.105974  | 0.0767448  |   0.0746511 | 0.0849654  |      0.101394   |
| Pyrope           | 0.0578827 | 0.0865489 | 0.23665   | 0.0547798  |   0.0821261 | 0.085637   |      0.085637   |
| Sphene           | 0.0673108 | 0.0542064 | 0.0761215 | 0.0959763  |   0.169246  | 0.0641609  |      0.0641609  |
| Chalcedony       | 0.0871248 | 0.0761866 | 0.0938692 | 0.115784   |   0.132687  | 0.0934307  |      0.0934307  |
| **Mean**         | 0.14254   | 0.10663   | 0.10298   | 0.113812   |   0.113372  | 0.0897705  |      0.0902273  |
| **Std**          | 0         | 0.0225456 | 0.0224441 | 0.00726876 |   0.0112101 | 0.00229854 |      0.00792103 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |    GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-----------:|-----------:|-----------:|-----------:|------------:|------------:|----------------:|
| Alunite          | 0          | 0          | 0.0104872  | 0          |  0          | 0.0145061   |      0.0145061  |
| Andradite        | 0          | 0          | 0.0108651  | 0          |  0.00773852 | 0.0105869   |      0.00878716 |
| Buddingtonite    | 0.047668   | 0.0195927  | 0.00765707 | 0.0248653  |  0.0259459  | 0.0071905   |      0.0071905  |
| Dumortierite     | 0.0562235  | 0.00689653 | 0.00754412 | 0.00833856 |  0.00768892 | 0.00754467  |      0.00754467 |
| Kaolinite_1      | 0.0113668  | 0.0130991  | 0.0129241  | 0.0168745  |  0.0136135  | 0.0130991   |      0.0130991  |
| Kaolinite_2      | 0.0113963  | 0.0131021  | 0.00798409 | 0.00642447 |  0.00732859 | 0.00846287  |      0.00846287 |
| Muscovite        | 0.096947   | 0.0113106  | 0.0187014  | 0.0461662  |  0.0351905  | 0.0365677   |      0.0338066  |
| Montmonrillonite | 0.0229949  | 0.00470432 | 0.00493426 | 0.00476634 |  0.00713089 | 0.00470432  |      0.00470432 |
| Nontronite       | 0.01264    | 0.00927976 | 0.0132864  | 0.00817066 |  0.00698936 | 0.00762265  |      0.0117582  |
| Pyrope           | 0.00713475 | 0.0889987  | 0.062435   | 0.00932598 |  0.0113287  | 0.00979028  |      0.00979028 |
| Sphene           | 0.00756905 | 0.133057   | 0.0164143  | 0.0351085  |  0.0251163  | 0.0080519   |      0.0080519  |
| Chalcedony       | 0.00882676 | 0.00769969 | 0.0102253  | 0.0244858  |  0.0236029  | 0.0100621   |      0.0100621  |
| **Mean**         | 0.0235639  | 0.0259477  | 0.0174932  | 0.0196505  |  0.0153604  | 0.0115755   |      0.012645   |
| **Std**          | 0          | 0.00292633 | 0.00840723 | 0.00679262 |  0.00197607 | 0.000270245 |      0.00162052 |


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

![alt text](Convergence.eps)

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |       PPI |     NFINDR |        VCA |      GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|----------:|-----------:|-----------:|----------:|------------:|-----------:|----------------:|
| Alunite          | 0.374377  | 0.10337    | 0.0939242  | 0.0941522 |   0.184046  |  0.10747   |      0.10747    |
| Andradite        | 0.0757956 | 0.0724709  | 0.1033     | 0.0772989 |   0.0735839 |  0.086105  |      0.134304   |
| Buddingtonite    | 0.20809   | 0.0761604  | 0.0785924  | 0.135739  |   0.104952  |  0.079849  |      0.079849   |
| Dumortierite     | 0.190734  | 0.0720035  | 0.0701844  | 0.105699  |   0.0899518 |  0.0754879 |      0.0754879  |
| Kaolinite_1      | 0.0794624 | 0.0870056  | 0.0862021  | 0.110118  |   0.119083  |  0.0870058 |      0.0870058  |
| Kaolinite_2      | 0.0819634 | 0.0889228  | 0.0740539  | 0.061046  |   0.0668798 |  0.0734972 |      0.0936411  |
| Muscovite        | 0.250633  | 0.109106   | 0.125684   | 0.203627  |   0.157214  |  0.121061  |      0.158656   |
| Montmonrillonite | 0.133816  | 0.064808   | 0.0651032  | 0.0657027 |   0.0621043 |  0.0646271 |      0.0646271  |
| Nontronite       | 0.103292  | 0.0758386  | 0.0781925  | 0.0781344 |   0.0724971 |  0.0836579 |      0.0745189  |
| Pyrope           | 0.0578827 | 0.122158   | 0.191832   | 0.0679378 |   0.0700864 |  0.237789  |      0.0619178  |
| Sphene           | 0.0673108 | 0.285672   | 0.0633402  | 0.0855421 |   0.240786  |  0.0684115 |      0.0654388  |
| Chalcedony       | 0.0871248 | 0.0871248  | 0.0760768  | 0.158967  |   0.111339  |  0.0871248 |      0.0871248  |
| **Mean**         | 0.14254   | 0.1057     | 0.0924954  | 0.104282  |   0.113312  |  0.100414  |      0.0916227  |
| **Std**          | 0         | 0.00533215 | 0.00354505 | 0.0161118 |   0.0178854 |  0.0199823 |      0.00576149 |
| **t-test**       | 1.99903   | 1.99423    | 0          | 1.95759   |   1.96941   |  1.94519   |      1.98879    |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-----------:|-----------:|-----------:|-----------:|------------:|-----------:|----------------:|
| Alunite          | 0          | 0          | 0.0104872  | 0          |  0          | 0.0155754  |      0          |
| Andradite        | 0          | 0.00616789 | 0.0170589  | 0.00749918 |  0          | 0.0164639  |      0.0167878  |
| Buddingtonite    | 0.047668   | 0.0071905  | 0.00765707 | 0.02676    |  0.0182685  | 0.0075562  |      0.0075562  |
| Dumortierite     | 0.0562235  | 0.00689653 | 0.00681985 | 0.0185697  |  0.0168243  | 0.019749   |      0.00774689 |
| Kaolinite_1      | 0.0113668  | 0.0130991  | 0.0149764  | 0.0170484  |  0.0116615  | 0.0109827  |      0.0130991  |
| Kaolinite_2      | 0.0113963  | 0.0109124  | 0.00638055 | 0.00550296 |  0.0065122  | 0.00635805 |      0.00837022 |
| Muscovite        | 0.096947   | 0.0300733  | 0.00985296 | 0.0454891  |  0.0368247  | 0.0189268  |      0.026671   |
| Montmonrillonite | 0.0229949  | 0.00487745 | 0.00495034 | 0.00484846 |  0.00416649 | 0.00470432 |      0.00470432 |
| Nontronite       | 0.01264    | 0.00766549 | 0.00866048 | 0.00759495 |  0.00819142 | 0.00791139 |      0.00927976 |
| Pyrope           | 0.00713475 | 0.0530846  | 0.0469881  | 0.00659649 |  0.00693477 | 0.00954521 |      0.006423   |
| Sphene           | 0.00756905 | 0.0912113  | 0.00924357 | 0.00830329 |  0.0293081  | 0.0528866  |      0.129301   |
| Chalcedony       | 0.00882676 | 0.00882676 | 0.00690701 | 0.0174433  |  0.0476768  | 0.00882676 |      0.00882676 |
| **Mean**         | 0.0235639  | 0.022102   | 0.0136084  | 0.0178156  |  0.0163237  | 0.0192624  |      0.0229521  |
| **Std**          | 0          | 0.00244643 | 0.00315458 | 0.00586874 |  0.00481091 | 0.00725007 |      0.00572888 |
| **t-test**       | 1.95272    | 1.91923    | 0          | 1.69212    |  1.83207    | 1.7467     |      1.84033    |


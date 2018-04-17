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

| Endmembers       |       PPI |     NFINDR |       VCA |      GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|----------:|-----------:|----------:|----------:|------------:|-----------:|----------------:|
| Alunite          | 0.374377  | 0.10337    | 0.09136   | 0.29477   |   0.0988756 |  0.0951658 |      0.0951658  |
| Andradite        | 0.0757956 | 0.0724709  | 0.0938516 | 0.0732537 |   0.106114  |  0.0784494 |      0.0849071  |
| Buddingtonite    | 0.20809   | 0.0761604  | 0.0785924 | 0.136212  |   0.149265  |  0.0761598 |      0.0761598  |
| Dumortierite     | 0.190734  | 0.0720035  | 0.0708485 | 0.0769125 |   0.0967679 |  0.0720841 |      0.0720841  |
| Kaolinite_1      | 0.0794624 | 0.0870056  | 0.0862021 | 0.0929558 |   0.0873443 |  0.0870058 |      0.0870058  |
| Kaolinite_2      | 0.0819634 | 0.0889228  | 0.0876237 | 0.0756971 |   0.0592781 |  0.0885846 |      0.0658336  |
| Muscovite        | 0.250633  | 0.109106   | 0.120549  | 0.187004  |   0.260077  |  0.216763  |      0.165173   |
| Montmonrillonite | 0.133816  | 0.064808   | 0.0642589 | 0.0645813 |   0.0664523 |  0.0664311 |      0.05903    |
| Nontronite       | 0.103292  | 0.0758386  | 0.0929608 | 0.0805874 |   0.0778562 |  0.115033  |      0.0780452  |
| Pyrope           | 0.0578827 | 0.122158   | 0.276787  | 0.0617028 |   0.0626181 |  0.058842  |      0.0606743  |
| Sphene           | 0.0673108 | 0.285672   | 0.0769936 | 0.0846362 |   0.06846   |  0.098202  |      0.285672   |
| Chalcedony       | 0.0871248 | 0.0871248  | 0.0760768 | 0.127536  |   0.195646  |  0.0871248 |      0.0871248  |
| **Mean**         | 0.14254   | 0.1057     | 0.104686  | 0.115877  |   0.110793  |  0.100012  |      0.104079   |
| **Std**          | 0         | 0.00533215 | 0.0149713 | 0.0113225 |   0.0203239 |  0.0176732 |      0.00668595 |
| **t-test**       | 1.97397   | 1.9499     | 0         | 1.94961   |   1.91621   |  1.90411   |      1.94044    |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-----------:|-----------:|-----------:|-----------:|------------:|-----------:|----------------:|
| Alunite          | 0          | 0          | 0.0104872  | 0          |  0          | 0.011496   |      0.011496   |
| Andradite        | 0          | 0.00616789 | 0.00773993 | 0.00689982 |  0.00717946 | 0.00764555 |      0.0128857  |
| Buddingtonite    | 0.047668   | 0.0071905  | 0.00765707 | 0.0205497  |  0.0170227  | 0.0071905  |      0.0071905  |
| Dumortierite     | 0.0562235  | 0.00689653 | 0.00754412 | 0.00886082 |  0.0054884  | 0.00754467 |      0.00754467 |
| Kaolinite_1      | 0.0113668  | 0.0130991  | 0.0125057  | 0.0169809  |  0.0148153  | 0.0130991  |      0.0130991  |
| Kaolinite_2      | 0.0113963  | 0.0109124  | 0.00974023 | 0.00628592 |  0.0040087  | 0.0113932  |      0.00610629 |
| Muscovite        | 0.096947   | 0.0300733  | 0.0107897  | 0.0386027  |  0.0357739  | 0.0657069  |      0.0189268  |
| Montmonrillonite | 0.0229949  | 0.00487745 | 0.00535166 | 0.00492942 |  0.00602144 | 0.00498531 |      0.00465124 |
| Nontronite       | 0.01264    | 0.00766549 | 0.00918988 | 0.00801433 |  0.00785371 | 0.0155032  |      0.00815511 |
| Pyrope           | 0.00713475 | 0.0530846  | 0.0418798  | 0.00780804 |  0.00696181 | 0.00613064 |      0.0331924  |
| Sphene           | 0.00756905 | 0.0912113  | 0.0910914  | 0.0184249  |  0.0220709  | 0.0120016  |      0.0912113  |
| Chalcedony       | 0.00882676 | 0.00882676 | 0.00861385 | 0.0516843  |  0.0329762  | 0.00882676 |      0.00882676 |
| **Mean**         | 0.0235639  | 0.022102   | 0.0225147  | 0.0161085  |  0.0149651  | 0.0208502  |      0.0188413  |
| **Std**          | 0          | 0.00244643 | 0.00530314 | 0.00352063 |  0.00413781 | 0.0123771  |      0.00122644 |
| **t-test**       | 1.87424    | 1.83918    | 0          | 1.73523    |  1.7108     | 1.58385    |      1.81604    |


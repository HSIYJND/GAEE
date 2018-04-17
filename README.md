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

| Endmembers       |        PPI |      NFINDR |       VCA |        GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-----------:|------------:|----------:|------------:|------------:|-----------:|----------------:|
| Alunite          |  0.374377  |  0.10337    | 0.10163   |  0.249431   |  0.232623   | 0.104276   |     0.104276    |
| Andradite        |  0.0757956 |  0.0724709  | 0.0777159 |  0.0760611  |  0.074694   | 0.0693223  |     0.0752277   |
| Buddingtonite    |  0.20809   |  0.0761604  | 0.0785924 |  0.111314   |  0.121688   | 0.0761598  |     0.0761598   |
| Dumortierite     |  0.190734  |  0.0720035  | 0.0683267 |  0.0824781  |  0.0853791  | 0.0754879  |     0.0754879   |
| Kaolinite_1      |  0.0794624 |  0.0870056  | 0.0862021 |  0.0806436  |  0.0990143  | 0.0870058  |     0.0870058   |
| Kaolinite_2      |  0.0819634 |  0.0889228  | 0.0799621 |  0.074103   |  0.0714376  | 0.0750258  |     0.0641441   |
| Muscovite        |  0.250633  |  0.109106   | 0.0928138 |  0.162383   |  0.169709   | 0.134367   |     0.134172    |
| Montmonrillonite |  0.133816  |  0.064808   | 0.0688709 |  0.0595697  |  0.0676279  | 0.0632861  |     0.0651458   |
| Nontronite       |  0.103292  |  0.0758386  | 0.0929608 |  0.0763732  |  0.0813641  | 0.0892534  |     0.0857129   |
| Pyrope           |  0.0578827 |  0.122158   | 0.160893  |  0.0558766  |  0.0657798  | 0.0682974  |     0.0954414   |
| Sphene           |  0.0673108 |  0.285672   | 0.0781701 |  0.0910653  |  0.118747   | 0.285672   |     0.285672    |
| Chalcedony       |  0.0871248 |  0.0871248  | 0.0640846 |  0.150035   |  0.0827149  | 0.0752052  |     0.0752052   |
| **Mean**         |  0.14254   |  0.1057     | 0.103117  |  0.111946   |  0.106926   | 0.10098    |     0.102141    |
| **Std**          |  0         |  0.00533215 | 0.0230409 |  0.00894601 |  0.00629223 | 0.00179384 |     0.000766907 |
| **p-value**      | -2.52739   | -0.164293   | 0         | -0.526381   | -0.243653   | 0.136858   |     0.0625914   |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |         PPI |      NFINDR |        VCA |        GAEE |   GAEE-IVFm |    GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|------------:|------------:|-----------:|------------:|------------:|------------:|----------------:|
| Alunite          |  0          |  0          | 0.0132672  |  0          |  0          |  0.0145061  |      0.0145061  |
| Andradite        |  0          |  0.00616789 | 0.00924583 |  0.00800466 |  0          |  0.00567641 |      0.00693028 |
| Buddingtonite    |  0.047668   |  0.0071905  | 0.00765707 |  0.0153772  |  0.0180597  |  0.0071905  |      0.0071905  |
| Dumortierite     |  0.0562235  |  0.00689653 | 0.00615763 |  0.00909567 |  0.0137228  |  0.00774689 |      0.00774689 |
| Kaolinite_1      |  0.0113668  |  0.0130991  | 0.00942634 |  0.00756614 |  0.0168275  |  0.0130991  |      0.0130991  |
| Kaolinite_2      |  0.0113963  |  0.0109124  | 0.0104449  |  0.00808734 |  0.00536273 |  0.00809942 |      0.004838   |
| Muscovite        |  0.096947   |  0.0300733  | 0.0100394  |  0.0361145  |  0.0375192  |  0.0428566  |      0.0269789  |
| Montmonrillonite |  0.0229949  |  0.00487745 | 0.00603923 |  0.00424995 |  0.00457033 |  0.00483121 |      0.00483121 |
| Nontronite       |  0.01264    |  0.00766549 | 0.0132864  |  0.00726825 |  0.00755031 |  0.00961848 |      0.00914114 |
| Pyrope           |  0.00713475 |  0.0530846  | 0.0418798  |  0.00607869 |  0.00469253 |  0.00772668 |      0.0125333  |
| Sphene           |  0.00756905 |  0.0912113  | 0.00859687 |  0.0210532  |  0.0170983  |  0.0225175  |      0.0912113  |
| Chalcedony       |  0.00882676 |  0.00882676 | 0.00526383 |  0.0408248  |  0.0105087  |  0.00668973 |      0.00668973 |
| **Mean**         |  0.0235639  |  0.022102   | 0.0176508  |  0.0193861  |  0.0141586  |  0.0193138  |      0.0216543  |
| **Std**          |  0          |  0.00244643 | 0.0101539  |  0.00720557 |  0.00340848 |  0.00951891 |      0.00572175 |
| **p-value**      | -1.00642    | -0.713336   | 0          | -0.211216   |  0.535411   | -0.185562   |     -0.540386   |


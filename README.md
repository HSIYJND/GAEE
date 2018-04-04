# Comparison of Vertex Componet Analysis (VCA) and Genetic Algorithm Endmember Extraction (GAEE) algorithms for Endmember Extraction

## Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

Envirionment Setup:

Monte Carlo runs: 2 

Number of endmembers to estimate: 12 

Number of skewers (PPI): 100 

Maximum number of iterations (N-FINDR): 36 

Number of individuals in each generation: 100 

Number of generations: 100 

Crossover probability: 0.3 

Mutation probability: 0.5 

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |       PPI |     NFINDR |       VCA |      GAEE |   GAEE-IVFm |
|:-----------------|----------:|-----------:|----------:|----------:|------------:|
| Alunite          | 0.374377  | 0.0926312  | 0.116273  | 0.243281  |  0.104276   |
| Andradite        | 0.0757956 | 0.132235   | 0.0921267 | 0.0874728 |  0.0699908  |
| Buddingtonite    | 0.20809   | 0.124654   | 0.0785924 | 0.121932  |  0.118162   |
| Dumortierite     | 0.190734  | 0.0706448  | 0.0984941 | 0.0907707 |  0.0952892  |
| Kaolinite_1      | 0.0794624 | 0.0870056  | 0.110158  | 0.0873798 |  0.0895541  |
| Kaolinite_2      | 0.0819634 | 0.0757643  | 0.0585269 | 0.0569941 |  0.0723325  |
| Muscovite        | 0.250633  | 0.0983345  | 0.138526  | 0.152419  |  0.204244   |
| Montmonrillonite | 0.133816  | 0.06607    | 0.0642589 | 0.0562996 |  0.0676078  |
| Nontronite       | 0.103292  | 0.078045   | 0.0783853 | 0.078946  |  0.0843987  |
| Pyrope           | 0.0578827 | 0.0865489  | 0.200634  | 0.0629272 |  0.0949175  |
| Sphene           | 0.0673108 | 0.228527   | 0.0834347 | 0.146924  |  0.0726093  |
| Chalcedony       | 0.0871248 | 0.0853271  | 0.0760768 | 0.0991994 |  0.0922141  |
| **Mean**         | 0.14254   | 0.10792    | 0.100666  | 0.108628  |  0.0992362  |
| **Std**          | 0         | 0.00720477 | 0.0098402 | 0.0151924 |  0.00844481 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |
|:-----------------|-----------:|-----------:|-----------:|-----------:|------------:|
| Alunite          | 0          | 0          | 0.018418   | 0          |  0          |
| Andradite        | 0          | 0.0184827  | 0.00804972 | 0          |  0          |
| Buddingtonite    | 0.047668   | 0.0211266  | 0.00765707 | 0          |  0.0130865  |
| Dumortierite     | 0.0562235  | 0.00711009 | 0.0143246  | 0.0108984  |  0.00898544 |
| Kaolinite_1      | 0.0113668  | 0.0130991  | 0.0142435  | 0.0176115  |  0.0143884  |
| Kaolinite_2      | 0.0113963  | 0.00820605 | 0.00424712 | 0.00401825 |  0.00886319 |
| Muscovite        | 0.096947   | 0.0113106  | 0.0272276  | 0.027127   |  0.030583   |
| Montmonrillonite | 0.0229949  | 0.00486723 | 0.00474685 | 0.00385766 |  0.00498441 |
| Nontronite       | 0.01264    | 0.0081581  | 0.00967855 | 0.00808751 |  0.00790604 |
| Pyrope           | 0.00713475 | 0.0331924  | 0.0436597  | 0.0225615  |  0.00888816 |
| Sphene           | 0.00756905 | 0.178019   | 0.00957585 | 0.0594911  |  0.0462191  |
| Chalcedony       | 0.00882676 | 0.00933356 | 0.00690701 | 0.0141375  |  0.00679747 |
| **Mean**         | 0.0235639  | 0.0282201  | 0.0153046  | 0.0154854  |  0.0147281  |
| **Std**          | 0          | 0.00386866 | 0.00343143 | 0.0038388  |  0.00579512 |


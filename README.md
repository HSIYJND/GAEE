# Comparison of Vertex Componet Analysis (VCA) and Genetic Algorithm Endmember Extraction (GAEE) algorithms for Endmember Extraction

## Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

**Envirionment Setup:**

Monte Carlo runs: 2 

Number of endmembers to estimate: 12 

Number of skewers (PPI): 100 

Maximum number of iterations (N-FINDR): 36 

Number of individuals in each generation: 100 

Number of generations: 100 

Crossover probability: 0.3 

Mutation probability: 0.5 

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |       PPI |    NFINDR |       VCA |      GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|----------:|----------:|----------:|----------:|------------:|-----------:|----------------:|
| Alunite          | 0.374377  | 0.112191  | 0.102462  | 0.105842  |   0.104749  | 0.104276   |      0.104276   |
| Andradite        | 0.0757956 | 0.0912882 | 0.120798  | 0.0707363 |   0.0962507 | 0.0724714  |      0.0724714  |
| Buddingtonite    | 0.20809   | 0.0761604 | 0.0785924 | 0.104372  |   0.108081  | 0.0761598  |      0.0761598  |
| Dumortierite     | 0.190734  | 0.0706448 | 0.0708485 | 0.0824232 |   0.0921744 | 0.0754879  |      0.0754879  |
| Kaolinite_1      | 0.0794624 | 0.0870056 | 0.0862021 | 0.108627  |   0.10268   | 0.0870058  |      0.0870058  |
| Kaolinite_2      | 0.0819634 | 0.099195  | 0.0707858 | 0.0635    |   0.0704023 | 0.0754461  |      0.0754461  |
| Muscovite        | 0.250633  | 0.158656  | 0.106516  | 0.158468  |   0.189482  | 0.203776   |      0.203776   |
| Montmonrillonite | 0.133816  | 0.0618906 | 0.0651032 | 0.0663045 |   0.0675647 | 0.05903    |      0.05903    |
| Nontronite       | 0.103292  | 0.0785457 | 0.0893511 | 0.0717927 |   0.0757989 | 0.0780452  |      0.0780452  |
| Pyrope           | 0.0578827 | 0.0850612 | 0.104951  | 0.0547739 |   0.0666672 | 0.0734482  |      0.0589092  |
| Sphene           | 0.0673117 | 0.140246  | 0.0633402 | 0.160286  |   0.0953859 | 0.153709   |      0.153709   |
| Chalcedony       | 0.0871248 | 0.0934309 | 0.0938692 | 0.0643781 |   0.128843  | 0.0765022  |      0.0765022  |
| **Mean**         | 0.14254   | 0.100138  | 0.0971799 | 0.102007  |   0.103277  | 0.0970388  |      0.0935638  |
| **Std**          | 0         | 0.0126496 | 0.0144155 | 0.0113695 |   0.0131684 | 0.00592139 |      0.00016231 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|-----------:|-----------:|-----------:|-----------:|------------:|-----------:|----------------:|
| Alunite          | 0          | 0          | 0.0140103  | 0          |  0          | 0          |      0          |
| Andradite        | 0          | 0.0319472  | 0.0134001  | 0.0066622  |  0.00948798 | 0.00616789 |      0.00616789 |
| Buddingtonite    | 0.047668   | 0.0071905  | 0.00765707 | 0.0150047  |  0.021832   | 0.0071905  |      0.0071905  |
| Dumortierite     | 0.0562235  | 0.00711009 | 0.00718259 | 0.0135765  |  0.00921706 | 0.00774689 |      0.00774689 |
| Kaolinite_1      | 0.0113668  | 0.0130991  | 0.0129241  | 0.0151036  |  0.0111605  | 0.0130991  |      0.0130991  |
| Kaolinite_2      | 0.0113963  | 0.00712305 | 0.00570292 | 0.00613689 |  0.00346816 | 0.0077546  |      0.0077546  |
| Muscovite        | 0.096947   | 0.0259569  | 0.0391311  | 0.0302634  |  0.0307999  | 0.0285336  |      0.0285336  |
| Montmonrillonite | 0.0229949  | 0.00470432 | 0.00474685 | 0.00472609 |  0.00485521 | 0.00423954 |      0.00423954 |
| Nontronite       | 0.01264    | 0.0096385  | 0.00929175 | 0.00733574 |  0.00877505 | 0.0081581  |      0.0081581  |
| Pyrope           | 0.00713475 | 0.0102339  | 0.0127728  | 0.0144838  |  0.0210325  | 0.0122869  |      0.0122869  |
| Sphene           | 0.00756905 | 0.129301   | 0.00797184 | 0.0389911  |  0.0408364  | 0.053228   |      0.053228   |
| Chalcedony       | 0.00882676 | 0.0100621  | 0.0102253  | 0.00506394 |  0.00985663 | 0.00702554 |      0.00702554 |
| **Mean**         | 0.0235639  | 0.0244884  | 0.017135   | 0.0139345  |  0.01542    | 0.0139262  |      0.0129526  |
| **Std**          | 0          | 0.00649615 | 0.00834293 | 0.00208992 |  0.00260821 | 0.0024081  |      0          |


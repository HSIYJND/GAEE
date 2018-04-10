# Comparison of Vertex Componet Analysis (VCA) and Genetic Algorithm Endmember Extraction (GAEE) algorithms for Endmember Extraction

## Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

**Envirionment Setup:**

Monte Carlo runs: 100 

Number of endmembers to estimate: 12 

Number of skewers (PPI): 100 

Maximum number of iterations (N-FINDR): 36 

### Parameters used in each GAEE versions

| Parameters            |   GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:----------------------|-------:|------------:|-----------:|----------------:|
| Population Size       |  100   |       100   |      100   |           100   |
| Number of Generations |  100   |       100   |      100   |           100   |
| Crossover Probability |    1   |         0.5 |        1   |             0.5 |
| Mutation Probability  |    0.3 |         0.3 |        0.1 |             0.3 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |         PPI |    NFINDR |       VCA |      GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|------------:|----------:|----------:|----------:|------------:|-----------:|----------------:|
| Alunite          | 0.374377    | 0.0926312 | 0.102462  | 0.102454  |   0.136259  |  0.104276  |       0.104276  |
| Andradite        | 0.0757956   | 0.16815   | 0.0574171 | 0.0553758 |   0.0799768 |  0.0843278 |       0.0843278 |
| Buddingtonite    | 0.20809     | 0.0761604 | 0.0785924 | 0.135751  |   0.0897498 |  0.0761598 |       0.0761598 |
| Dumortierite     | 0.190734    | 0.0706448 | 0.0708485 | 0.0808311 |   0.0686588 |  0.10066   |       0.0706448 |
| Kaolinite_1      | 0.0794624   | 0.0870056 | 0.0862021 | 0.104985  |   0.113432  |  0.0958325 |       0.119627  |
| Kaolinite_2      | 0.0819634   | 0.0669077 | 0.0791371 | 0.0738762 |   0.0709747 |  0.0679695 |       0.0739498 |
| Muscovite        | 0.250633    | 0.109106  | 0.108403  | 0.0983258 |   0.102821  |  0.138855  |       0.138855  |
| Montmonrillonite | 0.133816    | 0.0671111 | 0.066696  | 0.067225  |   0.0671108 |  0.0646271 |       0.0646271 |
| Nontronite       | 0.103292    | 0.0767601 | 0.0763078 | 0.0825749 |   0.0905499 |  0.0780037 |       0.0780037 |
| Pyrope           | 0.0578827   | 0.0767272 | 0.111714  | 0.0693814 |   0.0790294 |  0.0589284 |       0.0680463 |
| Sphene           | 0.0673108   | 0.0654395 | 0.0834347 | 0.125547  |   0.0649052 |  0.0825881 |       0.0825881 |
| Chalcedony       | 0.0871248   | 0.0699061 | 0.0705023 | 0.0643781 |   0.0731364 |  0.0752052 |       0.0752052 |
| **Mean**         | 0.14254     | 0.102426  | 0.0999777 | 0.102626  |   0.102904  |  0.0959233 |       0.0932983 |
| **Std**          | 1.09866e-16 | 0.0227061 | 0.0243778 | 0.0267735 |   0.0268529 |  0.0201638 |       0.0167166 |

### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |         PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |   GAEE-VCA |   GAEE-IVFm-VCA |
|:-----------------|------------:|-----------:|-----------:|-----------:|------------:|-----------:|----------------:|
| Alunite          | 0           | 0          | 0.0140103  | 0          |  0          | 0.0145061  |      0.0145061  |
| Andradite        | 0           | 0.0116519  | 0.00519935 | 0          |  0          | 0.0118536  |      0.0118536  |
| Buddingtonite    | 0.047668    | 0.0071905  | 0.00765707 | 0.0246649  |  0.0086128  | 0.0071905  |      0.0071905  |
| Dumortierite     | 0.0562235   | 0.00711009 | 0.00718259 | 0.016296   |  0.0123425  | 0.00711009 |      0.00711009 |
| Kaolinite_1      | 0.0113668   | 0.0130991  | 0.0129241  | 0.0116728  |  0.0110228  | 0.0107053  |      0.0177103  |
| Kaolinite_2      | 0.0113963   | 0.00846287 | 0.00981524 | 0.00540784 |  0.0059545  | 0.0082711  |      0.0082711  |
| Muscovite        | 0.096947    | 0.031699   | 0.0148187  | 0.026671   |  0.0128302  | 0.0312945  |      0.0312945  |
| Montmonrillonite | 0.0229949   | 0.00486723 | 0.00493426 | 0.00473553 |  0.00610006 | 0.00470432 |      0.00542261 |
| Nontronite       | 0.01264     | 0.0081581  | 0.00918988 | 0.0081264  |  0.00716092 | 0.00928682 |      0.00928682 |
| Pyrope           | 0.00713475  | 0.0338687  | 0.0141579  | 0.0153263  |  0.0188316  | 0.00899719 |      0.00559692 |
| Sphene           | 0.00756905  | 0.0674551  | 0.00957585 | 0.00674719 |  0.00612192 | 0.00899202 |      0.00899202 |
| Chalcedony       | 0.00882676  | 0.00933356 | 0.00599773 | 0.00864444 |  0.00504781 | 0.00668973 |      0.00668973 |
| **Mean**         | 0.0235639   | 0.0252484  | 0.0180916  | 0.0170422  |  0.0158775  | 0.0150359  |      0.0157127  |
| **Std**          | 2.29128e-17 | 0.00708007 | 0.0107126  | 0.0120706  |  0.0093716  | 0.00780647 |      0.00729529 |


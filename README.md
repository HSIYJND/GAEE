# Hyperspectral Endmember Extraction

### Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

#### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |       PPI |    NFINDR |       VCA |      GAEE |   GAEE-IVFm |
|:-----------------|----------:|----------:|----------:|----------:|------------:|
| Alunite          | 0.374377  | 0.112728  | 0.09136   | 0.109894  |   0.156501  |
| Andradite        | 0.0757956 | 0.206837  | 0.110177  | 0.0815806 |   0.0800569 |
| Buddingtonite    | 0.20809   | 0.120508  | 0.0785924 | 0.126616  |   0.112219  |
| Dumortierite     | 0.190734  | 0.0720035 | 0.0708485 | 0.0991473 |   0.0787475 |
| Kaolinite_1      | 0.0794624 | 0.0870056 | 0.0862021 | 0.119179  |   0.100331  |
| Kaolinite_2      | 0.0819634 | 0.099195  | 0.0654264 | 0.0480802 |   0.0649107 |
| Muscovite        | 0.250633  | 0.0983345 | 0.0962291 | 0.153509  |   0.159613  |
| Montmonrillonite | 0.133816  | 0.0646271 | 0.0651032 | 0.0665078 |   0.0625816 |
| Nontronite       | 0.103292  | 0.0805545 | 0.080055  | 0.0728827 |   0.0770503 |
| Pyrope           | 0.0578827 | 0.0865489 | 0.23665   | 0.060406  |   0.0578766 |
| Sphene           | 0.0673117 | 0.0542052 | 0.0590917 | 0.230576  |   0.218844  |
| Chalcedony       | 0.0871248 | 0.0761879 | 0.0918181 | 0.0948662 |   0.137143  |

|      |     PPI |    NFINDR |       VCA |      GAEE |   GAEE-IVFm |
|:-----|--------:|----------:|----------:|----------:|------------:|
| Mean | 0.14254 | 0.0965612 | 0.100926  | 0.113945  |   0.115556  |
| Std  | 0       | 0         | 0.0162188 | 0.0248599 |   0.0144456 |

#### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |
|:-----------------|-----------:|-----------:|-----------:|-----------:|------------:|
| Alunite          | 0          | 0          | 0.0104872  | 0          |  0          |
| Andradite        | 0          | 0          | 0.00904997 | 0          |  0.00818497 |
| Buddingtonite    | 0.047668   | 0.0195927  | 0.00765707 | 0.0204392  |  0.0191228  |
| Dumortierite     | 0.0562235  | 0.00689653 | 0.012277   | 0.0140924  |  0.00860972 |
| Kaolinite_1      | 0.0113668  | 0.0130991  | 0.0129241  | 0.0160207  |  0.0141039  |
| Kaolinite_2      | 0.0113963  | 0.0131021  | 0.00602154 | 0.00413981 |  0.00669393 |
| Muscovite        | 0.096947   | 0.0113106  | 0.0187014  | 0.0300075  |  0.0332484  |
| Montmonrillonite | 0.0229949  | 0.00470432 | 0.00465983 | 0.00489888 |  0.00482202 |
| Nontronite       | 0.01264    | 0.00927976 | 0.00866048 | 0.00678564 |  0.00756494 |
| Pyrope           | 0.00713475 | 0.0889987  | 0.0292924  | 0.0319008  |  0.0059653  |
| Sphene           | 0.00756905 | 0.133057   | 0.0910914  | 0.0574906  |  0.0560187  |
| Chalcedony       | 0.00882676 | 0.00769969 | 0.00724313 | 0.0103934  |  0.0283285  |

|      |       PPI |   NFINDR |        VCA |       GAEE |   GAEE-IVFm |
|:-----|----------:|---------:|-----------:|-----------:|------------:|
| Mean | 0.0235639 | 0.025645 | 0.0228493  | 0.0178983  |  0.0216428  |
| Std  | 0         | 0        | 0.00632572 | 0.00393895 |  0.00830362 |


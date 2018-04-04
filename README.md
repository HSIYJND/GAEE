# Hyperspectral Endmember Extraction

### Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

| Endmembers       |       VCA |
|:-----------------|----------:|
| Alunite          | 0.10163   |
| Andradite        | 0.10341   |
| Buddingtonite    | 0.0785924 |
| Dumortierite     | 0.0721547 |
| Kaolinite_1      | 0.0893394 |
| Kaolinite_2      | 0.0739628 |
| Muscovite        | 0.0968199 |
| Montmonrillonite | 0.0688709 |
| Nontronite       | 0.102521  |
| Pyrope           | 0.23665   |
| Sphene           | 0.0691669 |
| Chalcedony       | 0.0773462 |

|    |      |       VCA |
|---:|:-----|----------:|
|  0 | Mean | 0.102137  |
|  1 | Std  | 0.0207509 |

|    | Endmembers       |        VCA |
|---:|:-----------------|-----------:|
|  0 | Alunite          | 0.0104872  |
|  1 | Andradite        | 0.00893583 |
|  2 | Buddingtonite    | 0.00765707 |
|  3 | Dumortierite     | 0.00754412 |
|  4 | Kaolinite_1      | 0.0129241  |
|  5 | Kaolinite_2      | 0.0102169  |
|  6 | Muscovite        | 0.0216937  |
|  7 | Montmonrillonite | 0.00474685 |
|  8 | Nontronite       | 0.00754401 |
|  9 | Pyrope           | 0.00958286 |
| 10 | Sphene           | 0.0229165  |
| 11 | Chalcedony       | 0.00704778 |

|    |      |        VCA |
|---:|:-----|-----------:|
|  0 | Mean | 0.012608   |
|  1 | Std  | 0.00405393 |


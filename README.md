# Comparison of Vertex Componet Analysis (VCA) and Genetic Algorithm Endmember Extraction (GAEE) algorithms for Endmember Extraction

### Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.

Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.

#### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.

| Endmembers       |       PPI |    NFINDR |       VCA |      GAEE |   GAEE-IVFm |
|:-----------------|----------:|----------:|----------:|----------:|------------:|
| Alunite          | 0.374377  | 0.112728  | 0.10163   | 0.13109   |   0.194066  |
| Andradite        | 0.0757956 | 0.206837  | 0.0921267 | 0.0786324 |   0.0897853 |
| Buddingtonite    | 0.20809   | 0.120508  | 0.0785924 | 0.0967349 |   0.104839  |
| Dumortierite     | 0.190734  | 0.0720035 | 0.0701844 | 0.072418  |   0.07619   |
| Kaolinite_1      | 0.0794624 | 0.0870056 | 0.119055  | 0.0859543 |   0.0856323 |
| Kaolinite_2      | 0.0819634 | 0.099195  | 0.0791371 | 0.072289  |   0.0592072 |
| Muscovite        | 0.250633  | 0.0983345 | 0.120549  | 0.182511  |   0.15308   |
| Montmonrillonite | 0.133816  | 0.0646271 | 0.0642589 | 0.0706499 |   0.0644545 |
| Nontronite       | 0.103292  | 0.0805545 | 0.105974  | 0.0803328 |   0.0845656 |
| Pyrope           | 0.0578827 | 0.0865489 | 0.23665   | 0.0562707 |   0.0558586 |
| Sphene           | 0.0673117 | 0.0542052 | 0.0834347 | 0.159265  |   0.155453  |
| Chalcedony       | 0.0871248 | 0.0761879 | 0.0760768 | 0.0609167 |   0.0652931 |

|      |     PPI |    NFINDR |      VCA |      GAEE |   GAEE-IVFm |
|:-----|--------:|----------:|---------:|----------:|------------:|
| Mean | 0.14254 | 0.0996848 | 0.110612 | 0.101423  |   0.109928  |
| Std  | 0       | 0.0177408 | 0.015789 | 0.0140034 |   0.0183288 |

#### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.

| Endmembers       |        PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |
|:-----------------|-----------:|-----------:|-----------:|-----------:|------------:|
| Alunite          | 0          | 0          | 0.0132672  | 0          |  0          |
| Andradite        | 0          | 0          | 0.00804972 | 0.00789313 |  0.00881242 |
| Buddingtonite    | 0.047668   | 0.0195927  | 0.00765707 | 0.0108714  |  0.014383   |
| Dumortierite     | 0.0562235  | 0.00689653 | 0.00694232 | 0.0122289  |  0.00787504 |
| Kaolinite_1      | 0.0113668  | 0.0130991  | 0.0166732  | 0.0111147  |  0.0129185  |
| Kaolinite_2      | 0.0113963  | 0.0131021  | 0.00990345 | 0.00684811 |  0.00496879 |
| Muscovite        | 0.096947   | 0.0113106  | 0.0272276  | 0.0428566  |  0.0294954  |
| Montmonrillonite | 0.0229949  | 0.00470432 | 0.00474685 | 0.00627479 |  0.00525684 |
| Nontronite       | 0.01264    | 0.00927976 | 0.00929175 | 0.00812354 |  0.00912811 |
| Pyrope           | 0.00713475 | 0.0889987  | 0.062435   | 0.0252067  |  0.00506366 |
| Sphene           | 0.00756905 | 0.133057   | 0.00957585 | 0.0444819  |  0.0600064  |
| Chalcedony       | 0.00882676 | 0.00769969 | 0.00690701 | 0.0046536  |  0.00525543 |

|      |       PPI |     NFINDR |        VCA |       GAEE |   GAEE-IVFm |
|:-----|----------:|-----------:|-----------:|-----------:|------------:|
| Mean | 0.0235639 | 0.0266034  | 0.0165093  | 0.0156716  |  0.0175931  |
| Std  | 0         | 0.00489742 | 0.00606592 | 0.00352267 |  0.00760883 |


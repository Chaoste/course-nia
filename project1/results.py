import numpy as np
from matplotlib import pyplot as plt

def get_one_lambda_2():
    title = r'(1+$\lambda$)-EA [$\lambda = 2$]'
    labels = ["one_max", "leading_ones", "jump", "royal_roads"]
    all_runtimes = np.array([
      [
        [  70,  58,  33,  87,  35,  95,  99, 200,  55,  87],
        [ 250, 162, 149, 236, 188, 188, 212, 199, 142, 215],
        [ 285, 288, 476, 311, 622, 360, 556, 522, 322, 326],
        [ 602, 671, 777, 611, 606, 774, 436, 329, 554, 432],
        [ 491, 778, 894, 750, 704, 668, 630, 830, 396, 906],
        [  817,  980,  610,  716,  631, 1282,  927,  661,  529,  925],
        [ 1082,  763, 1201, 1435, 1840,  992, 1350,  777,  647, 1190],
      ],
      [
        [ 277, 320, 316, 323, 264, 180, 228, 329, 330, 185],
        [  878, 1025,  910, 1100, 1006,  818, 1081,  987, 1217, 1164],
        [ 1933, 1695, 1962, 3218, 2453, 2113, 2759, 2896, 2203, 1556],
        [ 6070, 3545, 3479, 3165, 4252, 4032, 4341, 4446, 4906, 3851],
        [ 6634, 5953, 5820, 5226, 6026, 6370, 5473, 6333, 6862, 5844],
        [  9317,  9212, 12151,  7477, 10060,  8748, 12568,  7827,  9804, 8495],
        [ 10595, 10569, 11654, 13029, 14117, 12532, 12405, 12047, 13355,13186],
      ],
      [
        [ 1102,  923,   72, 2530,  908,   54, 1363, 4796,  278,  726],
        [ 12198,  2052, 21847, 12090, 29900, 15720, 18706, 50700,  5356, 1945],
        [  92429,   5314,  36680,  54606, 104392, 133565,   6849,  24582,   364,  62528],
        [ 224700, 105805, 419391,  30359, 178083,  25435,  30255, 336082,152799, 161500],
        [ 132697,   2469, 123575, 815934, 393088,  43869, 149194,  32699,442863,  75324],
        [ 1459874,  704981,  124828,  106169,  622779,  809321,   44526, 106922,  952008,  118197],
        [ 1053086, 1847529,   43834,  100659,   44468,  785764,  109447,   8953, 1962699,  852949],
      ],
      [
        [  388,  358, 1190,  337,  352,  397,  873,  702,  503,  627],
        [ 1112, 1631, 1215, 1591,  896, 2125, 1360, 1083, 1599,  711],
        [ 3165, 3124, 2262,  859, 1019, 1821, 2117, 3209, 1165,  927],
        [ 4336, 3359, 2253, 2064, 4359, 4034, 2062, 4422, 3295, 3804],
        [ 4427, 3999, 4801, 5027, 6213, 2928, 1734, 2072, 2938, 2271],
        [ 5311, 4277, 3893, 5850, 4055, 3220, 8180, 7561, 4820, 5793],
        [ 10878,  6926, 13148,  3978,  3664,  4791,  4167,  8150,  7739, 3938],
      ],
    ])
    return title, labels, all_runtimes

def get_one_lambda_10():
    title = r'(1+$\lambda$)-EA [$\lambda = 10$]'
    labels = ["one_max", "leading_ones", "jump", "royal_roads"]
    all_runtimes = np.array([
        [
            [ 16, 15, 33, 19, 21, 14, 29, 17, 18, 20],
            [ 54, 57, 85, 71, 29, 36, 55, 46, 39, 41],
            [ 77, 111,  59,  71,  62, 112, 143,  85, 109,  72],
            [ 83, 120, 174,  92, 100, 178,  92,  98, 123, 169],
            [ 158, 268, 237, 152, 152, 178, 164, 189, 195, 153],
            [ 144, 179, 219, 189, 180, 200, 348, 295, 303, 169],
            [ 252, 314, 178, 155, 264, 263, 276, 211, 199, 255],
        ],
        [
            [ 72,  61,  58,  33,  36,  73,  56, 112,  46,  43],
            [ 219, 236, 316, 122, 203, 162, 157, 218, 235, 193],
            [ 584, 403, 418, 551, 479, 598, 503, 416, 693, 547],
            [ 725,  889,  844,  581,  743,  970,  776,  941,  809, 1061],
            [ 1414, 1587, 1155, 1299, 1347, 1280, 1371, 1600, 1242, 1624],
            [ 2062, 2458, 1982, 1690, 2122, 1962, 1751, 1894, 2347, 2154],
            [ 2870, 2911, 2687, 2368, 2821, 2642, 2507, 2000, 2817, 2210],
        ],
        [
            [ 153,  22,  14, 100, 324, 412,  41,  32, 202, 716.],
            [ 2383, 2809,  189, 2468,  740,  763, 3215, 2436,  472,  982.],
            [  1878, 10897,  4260,  1687,  2715,  2901,   682, 33557, 14734,890.],
            [ 16815,  3437,  2807, 13148,  2425, 16309,  3132, 61294, 18871,16775.],
            [  1633,  6770, 21692, 13787,  3139, 34537, 18310, 96308,  8614,21043.],
            [  46554,  67896,   1371,  54225, 140748,  52637,  15171,  22122,56537,21420.],
            [  60117,  22599, 120371,  77789,  14348,   3515,   8685,  67879,71441,21354.],
        ],
        [
            [ 245, 183,  68,  44, 191,  23,  68, 110,  90,  92.],
            [  399, 1274,  244,  317,  299,  139,  175,  358,  357,  362.],
            [ 622, 978, 523, 941, 820, 394, 342, 624, 732, 758.],
            [ 1000, 1229,  595, 1254,  690,  918, 1095,  923, 1275,  764.],
            [  731, 1232, 1267, 1191,  833, 1589, 1039, 2047, 2904, 1676.],
            [ 2137, 1176, 1457, 1187, 1052, 1273, 1715, 1131, 1259, 1654.],
            [ 1884, 1995, 1661, 2465, 2173, 2006, 3278, 2211, 3010, 1567.],
        ],
    ])
    return title, labels, all_runtimes

def get_one_lambda_50():
    title = r'(1+$\lambda$)-EA [$\lambda = 50$]'
    labels = ["one_max", "leading_ones", "jump", "royal_roads"]
    all_runtimes = np.array([
      [
        [ 10,  9,  9,  8, 10, 10,  8,  8,  8,  6],
        [ 21, 27, 25, 22, 16, 19, 16, 20, 24, 24],
        [ 25, 33, 28, 27, 34, 27, 29, 29, 33, 34],
        [ 50, 31, 40, 39, 36, 35, 47, 43, 41, 49],
        [ 60, 54, 62, 54, 60, 54, 65, 66, 60, 60],
        [ 66, 78, 64, 73, 74, 61, 73, 71, 69, 82],
        [  74, 100,  87,  65,  98,  90,  89,  72,  94,  93],
      ],
      [
        [ 19, 20, 14, 10, 16, 16, 20, 14, 15, 25],
        [ 68, 58, 73, 41, 46, 54, 74, 75, 78, 57],
        [ 128, 138, 136, 107, 115, 123, 125, 127, 131,  97],
        [ 172, 177, 193, 205, 167, 175, 163, 150, 228, 178],
        [ 350, 314, 252, 307, 278, 277, 276, 332, 271, 240],
        [ 482, 336, 441, 381, 394, 455, 336, 280, 526, 332],
        [ 648, 588, 608, 574, 605, 557, 570, 628, 506, 564],
      ],
      [
        [ 256,  45,  59, 118,  71, 105, 102,  34,  90,  57],
        [  617,   21,  534,  137,  146,  619, 1019,   77, 2410,  548],
        [ 4066,  197,  977,   44, 1404,  130, 2978,  685,  691,   37],
        [  236, 5176, 1981,   62, 1256, 2443,  601, 1567,  825, 1960],
        [ 11517,  1747,  3393,  1254, 45631,  3804,  3001,  1692,  4468,1546],
        [  3180, 21740,  2205,  8098,  6084,  3285,  2408,  4840,  8186, 949],
        [  7804,  7660, 15181, 23214, 20704, 16453, 55112, 10633,   822,6745],
      ],
      [
        [  91,  48,  26, 198,  29, 159, 101,  65,  29,  23],
        [ 310, 274, 106, 339, 116, 214, 174, 133, 236, 236],
        [ 309, 245, 361, 213, 408, 264, 409, 372, 275, 557],
        [ 829, 367, 501, 545, 288, 909, 852, 314, 631, 970],
        [  433,  430,  647,  725, 1235,  986,  737, 1155,  873, 1066],
        [  968,  770,  690, 1457, 1213, 1276, 1428, 1311,  731, 1060],
        [ 2634, 1849,  610, 1305, 1315, 1591, 1179, 1678,  870, 2834],
      ],
    ])
    return title, labels, all_runtimes

def get_one_one():
    title = '(1+1)-EA'
    labels = ["one_max", "leading_ones", "jump", "royal_roads"]
    all_runtimes = np.array([
        [
            [ 179, 145, 144, 221, 198, 360, 177,  77, 366, 133],
            [ 201, 831, 220, 390, 517, 446, 402, 276, 329, 286],
            [  770,  416,  568,  746,  927,  369,  571, 1005,  772,  280],
            [ 1097, 1194, 1028,  660,  975, 1367,  964,  746, 1621, 2050],
            [ 1748, 1219, 1492, 1221,  782, 2615, 1140, 1276, 1156, 2014],
            [ 1194, 1770, 1366, 1438, 2703, 1561, 2576, 2260, 1696, 1714],
            [ 2102, 2086, 1816, 2279, 1494, 1734, 1977, 1672, 2142, 1976],
        ],
        [
            [ 445, 573, 534, 348, 266, 618, 284, 361, 592, 476],
            [ 2631, 1754, 2740, 1596, 2677, 1906, 1562, 1813, 2128, 2106],
            [ 5909, 4593, 3948, 5747, 4987, 2851, 5022, 4986, 4177, 4336],
            [ 11957, 10579, 10288,  7843,  9908,  9120,  7308,  7826,  8187,  7551],
            [ 13979, 12909,  7096, 12926, 13660, 14364, 12755, 12791, 17163, 14486],
            [ 20018, 19244, 17335, 20259, 18163, 19095, 17707, 17070, 20151, 19718],
            [ 23765, 24955, 27303, 19854, 15262, 24756, 27619, 26550, 27931, 31341],
        ],
        [
            [  4191,  3572, 13712,  2393,  3188,  1722,   117,  2931,  4096,  4468],
            [ 45137, 39838, 38733, 38629,   377, 28602, 12223, 43482, 25881, 18512],
            [  14469,  14326,  41223, 177453, 202046,  59979,  15737,  55560,  67125, 222441],
            [  76836,   1898, 455345,  30055, 158321, 168294, 108086, 121794, 253348, 765475],
            [ 142030, 470468, 221122, 526112,  42753,  93279, 288115, 425435, 222477, 984517],
            [  354423,  167149,  807574,  465129,  370740,  233419,  358949, 642123, 1998640,  500811],
            [ 1572967,  163251, 2245867,   65852, 1363897,  165105, 2226003, 1212024,   11740,  660502],
        ],
        [
            [  506,  811,  853, 1202,  210,  530, 1931,  805, 3684,  609],
            [ 1043, 3940, 4211, 1045, 3223, 3411, 2756, 1681, 1280, 2865],
            [ 4136, 4093, 4468, 2583, 4757, 2672, 4319, 4863, 3991, 3860],
            [ 3695, 5691, 5596, 4032, 8628, 3167, 5612, 5322, 4107, 3100],
            [ 10933,  8518,  7566,  6139,  6646,  9079,  5525,  4616,  7042, 11744],
            [  9336,  4921, 12416,  8118, 16699,  7776, 12535, 12809, 11422, 8216],
            [ 30953,  8628, 10519, 11042,  9285, 11632, 17687, 10372,  8278, 12959],
        ],
    ])
    return title, labels, all_runtimes

def get_rls():
    title = 'Random Local Search'
    labels = ["one_max", "leading_ones", "jump", "royal_roads"]
    all_runtimes = np.array([
        [
          [ 122,  68, 150,  44,  98,  80, 138,  50,  51,  46],
          [ 107, 124, 178, 221, 332, 178, 230, 125, 297, 173],
          [ 333, 306, 252, 437, 330, 390, 248, 327, 193, 255],
          [ 334, 328, 481, 358, 466, 308, 341, 332, 267, 488],
          [ 522, 832, 542, 503, 422, 702, 618, 445, 500, 625],
          [ 873, 588, 550, 834, 679, 673, 545, 803, 832, 669],
          [ 1226, 1251,  664, 1222,  889,  663, 1051,  831,  906, 1199],
        ],
        [
          [ 383, 357, 140, 337, 277, 269, 487, 325, 329, 213],
          [ 1665, 1055, 1389, 1389, 1803, 2223, 1727,  925, 1113,  775],
          [ 2370, 2134, 1900, 3105, 3351, 2967, 1863, 2066, 2627, 2571],
          [ 6788, 4760, 5192, 6110, 5855, 3864, 4189, 4715, 4219, 4105],
          [  7632,  7397,  8563,  6806,  8538,  8639, 10966,  8731,  7272, 10026],
          [  9977, 11846, 12054, 12054,  9028, 13765, 12730,  8909, 10788, 9904],
          [ 18969, 12634, 14743, 17664, 18319, 12674, 15360, 14269, 15791, 16160],
        ],
        [
          [ 1454, 4786,  375,  869, 1507, 1222, 2314, 2415, 6359, 2164],
          [ 50000, 26320,  1963,  2727,  1250,  2934,  5947,   688,  4038, 4122],
          [  94474,  45483, 123571,   5478,  97237,   1558,  46063, 102430, 199933,   8441],
          [  76115,  45397,  21826,   7244,  18020, 268549,  13183, 389647, 73079,  75977],
          [ 132583, 299540, 179617, 533644, 130309, 122477, 116704,  11339, 19395, 157612],
          [ 331143, 348260, 457149, 120690, 460176, 119481, 596873,  11790, 38030, 285275],
          [   44003,  634787,  605356,  768204,  405428,  493772,  824501, 3072497, 2590259,   83822],
        ],
        [
          [ 341, 471, 384, 558, 177, 294, 193, 132, 444, 415],
          [ 1118, 1360,  693, 1781,  578, 1017,  780,  479, 1028, 1080],
          [ 1060, 1799,  930, 1936, 1976, 2721, 1470, 1491, 2360, 2076],
          [ 2484, 2200, 3169, 2378, 2494, 2883, 1717, 2889, 1981, 1541],
          [ 5196, 3428, 4755, 3668, 4081, 2859, 3632, 4590, 3202, 3384],
          [  2582,  3079, 13784,  5346,  3140,  5610,  5078,  3136,  3686, 4187],
          [ 4901, 8951, 5082, 5492, 6797, 5029, 3518, 7627, 5071, 3689],
        ],
    ])
    return title, labels, all_runtimes


def get_rls_go():
    title = r'Random Local Search ($greater_only=True$)'
    labels = ["one_max", "leading_ones"]
    all_runtimes = np.array([

    ])
    return title, labels, all_runtimes

def get_one_one_go():
    title = r'(1+1)-EA ($greater_only=True$)'
    labels = ["one_max", "leading_ones"]
    all_runtimes = np.array([

    ])
    return title, labels, all_runtimes

def get_one_lambda_2_go():
    title = r'(1+$\lambda$)-EA  [$\lambda = 2$] ($greater_only=True$)'
    labels = ["one_max", "leading_ones"]
    all_runtimes = np.array([

    ])
    return title, labels, all_runtimes

def get_one_lambda_10_go():
    title = r'(1+$\lambda$)-EA  [$\lambda = 10$] ($greater_only=True$)'
    labels = ["one_max", "leading_ones"]
    all_runtimes = np.array([

    ])
    return title, labels, all_runtimes

def get_one_lambda_50_go():
    title = r'(1+$\lambda$)-EA  [$\lambda = 50$] ($greater_only=True$)'
    labels = ["one_max", "leading_ones"]
    all_runtimes = np.array([

    ])
    return title, labels, all_runtimes
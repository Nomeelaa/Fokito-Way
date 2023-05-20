"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the definitions of the tiles.
"""
from typing import Dict, Any

TILES: Dict[int, Dict[str, Any]] = {
    # Border of world
    0: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    74: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    75: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    96: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    97: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    118: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    119: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    140: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    141: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    244: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    245: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    266: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    267: {"solidness": dict(top=True, right=True, bottom=True, left=True)},

    242: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    243: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    264: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    265: {"solidness": dict(top=True, right=True, bottom=True, left=True)},

    320: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    321: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    322: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    323: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    324: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    325: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    326: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    327: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    328: {"solidness": dict(top=True, right=True, bottom=True, left=True)},

    342: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    343: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    344: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    345: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    346: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    347: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    348: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    349: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    350: {"solidness": dict(top=True, right=True, bottom=True, left=True)},

    365: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    366: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    367: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    368: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    369: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    370: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    371: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    372: {"solidness": dict(top=True, right=True, bottom=True, left=True)},

######## arbol group
    
    145: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    146: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    147: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    148: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    149: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    150: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    151: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    

    166: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    167: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    168: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    169: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    170: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    171: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    172: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    173: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    174: {"solidness": dict(top=True, right=True, bottom=True, left=True)},

    188: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    189: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    190: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    191: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    192: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    193: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    194: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    195: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    196: {"solidness": dict(top=True, right=True, bottom=True, left=True)},

    210: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    211: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    212: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    213: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    214: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    215: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    216: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    217: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    218: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
##########################

######## arbol group
    
    233: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    234: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    235: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    236: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    237: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    238: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    239: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    

    254: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    255: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    256: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    257: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    258: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    259: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    260: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    261: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    262: {"solidness": dict(top=True, right=True, bottom=True, left=True)},

    276: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    277: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    278: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    279: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    280: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    281: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    282: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    283: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    284: {"solidness": dict(top=True, right=True, bottom=True, left=True)},

    285: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    286: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    287: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    288: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    289: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    290: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    291: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    292: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    293: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
##########################

    176: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    177: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    178: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    179: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    180: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    181: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    182: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    183: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    184: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    185: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    186: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    187: {"solidness": dict(top=True, right=True, bottom=True, left=True)},

    198: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    199: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    200: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    201: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    202: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    203: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    204: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    205: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    206: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    207: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    208: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    209: {"solidness": dict(top=True, right=True, bottom=True, left=True)},

    220: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    221: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    222: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    223: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    224: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    225: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    226: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    227: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    228: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    229: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    230: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    231: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    





}

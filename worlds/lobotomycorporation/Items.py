
from BaseClasses import ItemClassification

item_table = {
    'ZAYIN WEAPON':         [ItemClassification.useful,         17,    10000],
    'ZAYIN ARMOR':          [ItemClassification.useful,    15,    11000],
    'TETH WEAPON':          [ItemClassification.useful,         40,    20000],
    'TETH ARMOR':           [ItemClassification.useful,    59,    21000],
    'HE WEAPON':            [ItemClassification.useful,         42,    30000],
    'HE ARMOR':             [ItemClassification.useful,    43,    31000],
    'WAW WEAPON':           [ItemClassification.useful,         58,    40000],
    'WAW ARMOR':            [ItemClassification.useful,    50,    41000],
    'ALEPH WEAPON':         [ItemClassification.progression,         20,    50000],
    'ALEPH ARMOR':          [ItemClassification.progression,    16,    51000],



    'SEED OF LIGHT':        [ItemClassification.progression,    20,    70000],
    

    'LOB POINTS':           [ItemClassification.filler,         1,     80000],
    'DAILY LOB INCOME':     [ItemClassification.useful,         50,    80001],
    'DAILY AGENT TRAINING': [ItemClassification.useful,         50,    80002],
    'STARTING LOB':         [ItemClassification.useful,         50,    80003],
    
    'RESEARCH TT2 PROTOCOL' :                              [ItemClassification.useful,         1,     90001],      
    'RESEARCH JOINT COMMAND' :                             [ItemClassification.useful,         1,     90002],   
    'RESEARCH ASSEMBLY SUMMONS' :                          [ItemClassification.useful,         1,     90103], 

    'RESEARCH REGENERATOR MK2' :                           [ItemClassification.useful,         1,     90006], 
    'RESEARCH MENTAL CORRUPTION NEUTRALIZING GAS' :        [ItemClassification.useful,         1,     90007], 
    'RESEARCH REGENERATOR DISTINGUISHER MODIFICATION' :    [ItemClassification.useful,         1,     90203], 

    'RESEARCH SUPPLY EDUCATION MANUALS' :                  [ItemClassification.useful,         1,     90008], 
    'RESEARCH IMPROVE WORK EDUCATION' :                    [ItemClassification.useful,         1,     90009], 
    'RESEARCH IMPROVE HIRING PROCEDURES' :                 [ItemClassification.useful,         1,     90010], 

    'RESEARCH G.O Visualization' :                         [ItemClassification.useful,         1,     90003], 
    'RESEARCH DAMAGE NORMALIZATION' :                      [ItemClassification.useful,         1,     90004], 
    'RESEARCH ABNORMALITY COUNTERMEASURES MANUAL' :        [ItemClassification.useful,         1,     90005], 

    'RESEARCH PHYSICAL INTERVENTION SHIELD' :              [ItemClassification.useful,         1,     90501], 
    'RESEARCH TRAUMA SHIELD' :                             [ItemClassification.useful,         1,     90502], 
    'RESEARCH EROSION SHIELD' :                            [ItemClassification.useful,         1,     90503], 

    'RESEARCH EXECUTION BULLET' :                          [ItemClassification.useful,         1,     90701], 
    'RESEARCH QLIPOTH INTERVENTION FIELD' :                [ItemClassification.useful,         1,     90702], 
    'RESEARCH THE RABBIT TEAM' :                           [ItemClassification.useful,         1,     90703], 

    'RESEARCH HP-N BULLETS' :                              [ItemClassification.useful,         1,     90801], 
    'RESEARCH SP-E BULLETS' :                              [ItemClassification.useful,         1,     90802], 
    'RESEARCH HP & SP BULLET REFINING' :                   [ItemClassification.useful,         1,     90803],

    'RESEARCH MELTDOWN PREVENTION' :                       [ItemClassification.useful,         1,     90901],  
    'RESEARCH RE-EXTRACTION' :                             [ItemClassification.useful,         1,     90902], 
    'RESEARCH GIFT DIVISION' :                             [ItemClassification.useful,         1,     90903], 

    'RESEARCH LIMIT BREAK: THE VIRTUE OF PROTECTION' :     [ItemClassification.useful,         1,     91001], 
    'RESEARCH LIMIT BREAK: THE VIRTUE OF GOVERNANCE' :     [ItemClassification.useful,         1,     91002], 
    'RESEARCH LIMIT BREAK: THE VIRTUE OF CREATION' :       [ItemClassification.useful,         1,     91003], 

    'SEPHIRA MELTDOWN REWARD: MALKUTH' :                   [ItemClassification.useful,         1,     91100],
    'SEPHIRA MELTDOWN REWARD: YESOD' :                     [ItemClassification.useful,         1,     91101],
    'SEPHIRA MELTDOWN REWARD: HOD' :                       [ItemClassification.useful,         1,     91102],
    'SEPHIRA MELTDOWN REWARD: NETZACH' :                   [ItemClassification.useful,         1,     91103],
    'SEPHIRA MELTDOWN REWARD: TIPHERETH' :                  [ItemClassification.useful,         1,     91104],
    'SEPHIRA MELTDOWN REWARD: GEBURA' :                    [ItemClassification.progression,    1,     91105],
    'SEPHIRA MELTDOWN REWARD: CHESED' :                    [ItemClassification.useful,         1,     91106],
    'SEPHIRA MELTDOWN REWARD: BINAH' :                     [ItemClassification.useful,         1,     91107],
    'SEPHIRA MELTDOWN REWARD: HOKMA' :                     [ItemClassification.useful,         1,     91108],

    'ZAYIN ABNORMALITY':                                   [ItemClassification.progression,    6,    100000],
    'TETH ABNORMALITY':                                    [ItemClassification.progression,    15,   100001],
    'HE ABNORMALITY':                                      [ItemClassification.progression,    15,   100002],
    'WAW ABNORMALITY':                                     [ItemClassification.progression,    19,   100003],
    'ALEPH ABNORMALITY':                                   [ItemClassification.progression,    6,    100004],

    'TOOL ABNORMALITY':                                    [ItemClassification.progression,         17,   100005],

    'SMALL BIRD':                                          [ItemClassification.progression,    1,    110000],
    'BIG BIRD':                                            [ItemClassification.progression,    1,    111000],
    'LONG BIRD':                                           [ItemClassification.progression,    1,    112000],
    'PLAGUE DOCTOR':                                       [ItemClassification.progression,    1,    120000],

    'ENERGY TRAP':                                          [ItemClassification.trap,          25,    200000],
    'CHOO CHOO TRAP':                                       [ItemClassification.trap,          25,    200001],
    'MELTDOWN TRAP':                                        [ItemClassification.trap,          25,    200002],
    'NAP TRAP':                                             [ItemClassification.trap,          25,    200003],
    'FALSE ALARM TRAP':                                     [ItemClassification.trap,          25,    200004],
    'QLIPHOTH MALFUNCTION TRAP':                            [ItemClassification.trap,          25,    200005],
    'MIDNIGHT TRAP':                                        [ItemClassification.trap,          25,    200006],

    'Victory':                                              [ItemClassification.progression,          0,    90000],
}

trap_table ={
    'ENERGY TRAP',
    'CHOO CHOO TRAP',
    'MELTDOWN TRAP',
    'NAP TRAP',
    'FALSE ALARM TRAP',
    'QLIPHOTH MALFUNCTION TRAP',
    'MIDNIGHT TRAP'
}


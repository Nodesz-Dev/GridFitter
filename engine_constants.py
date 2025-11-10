# Arrays that represent the active squares that main reactors give to the main grid

BLANK_REACTOR = [[0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0]]

SPLIT_REACTOR = [[1,1,0,0,0,0,1,1],
                 [1,1,1,0,0,1,1,1],
                 [1,1,1,0,0,1,1,1],
                 [1,1,1,0,0,1,1,1]]

SOLID_STATE_REACTOR = [ [0,0,1,1,1,1,0,0],
                        [0,0,1,1,1,1,0,0],
                        [0,0,1,1,1,1,0,0],
                        [0,0,1,1,1,1,0,0]]

MATERIA_SCATTER_REACTOR = [ [1,1,1,1,1,1,1,1],
                            [0,1,0,1,1,0,1,0],
                            [1,1,1,1,1,1,1,1],
                            [1,0,1,0,0,1,0,1]]

NULL_WAVE_REACTOR = [   [1,1,0,0,0,0,1,1],
                        [1,1,1,0,0,1,1,1],
                        [0,1,1,1,1,1,1,0],
                        [0,0,1,1,1,1,0,0]]

# Array to store Engine names for the drop down menu
REACTOR_OPTIONS = ["None", 
                  "Split Reactor", 
                  "Solid State Reactor",
                  "Materia Scatter Reactor",
                  "Null Wave Reactor"]

REACTOR_ARRAYS = [BLANK_REACTOR,
                 SPLIT_REACTOR,
                 SOLID_STATE_REACTOR,
                 MATERIA_SCATTER_REACTOR,
                 NULL_WAVE_REACTOR]

# Arrays that represent the active squares that aux generators give to the main grid

BLANK_AUX_GENERATOR = [ [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0]]

BIO_FISSION_GENERATOR_MK1 = [   [0,0,1,1,1,1,0,0],
                                [0,0,1,0,0,1,0,0]]

BIO_FISSION_GENERATOR_MK2 = [   [0,1,1,1,1,1,1,0],
                                [0,1,0,0,0,0,1,0]]

BIO_FISSION_GENERATOR_MK3 = [   [1,1,1,1,1,1,1,1],
                                [1,0,0,0,0,0,0,1]]

NULL_TENSION_GENERATOR = [  [0,0,1,1,1,1,0,0],
                            [0,0,1,1,1,1,0,0]]

MATERIA_SHIFT_GENERATOR = [ [0,1,1,0,0,1,1,0],
                            [0,1,1,0,0,1,1,0]]


# Array to store generator names for the drop down menu
GENERATOR_OPTIONS = ["None",
                     "Bio-Fission Generator Mk1",
                     "Bio-Fission Generator Mk2",
                     "Bio-Fission Generator Mk3",
                     "Null Tension Generator",
                     "Materia Shift Generator"]

GENERATOR_ARRAYS = [BLANK_AUX_GENERATOR,
                    BIO_FISSION_GENERATOR_MK1,
                    BIO_FISSION_GENERATOR_MK2,
                    BIO_FISSION_GENERATOR_MK3,
                    NULL_TENSION_GENERATOR,
                    MATERIA_SHIFT_GENERATOR]
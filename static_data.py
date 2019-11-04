#PYTHON IMPORT
import math

ACKLEY_MIN_RANGE = -4  #-32768
ACKLEY_MAX_RANGE = 4   #32768
ACKLEY_RANGE = 0.2

LEVY_MIN_RANGE = -10
LEVY_MAX_RANGE = 10
LEVY_RANGE = 0.2

GRIEWANK_MIN_RANGE = -10    #-600
GRIEWANK_MAX_RANGE = 10     #600
GRIEWANK_RANGE = 0.2

RASTRIGIN_MIN_RANGE = -5.12
RASTRIGIN_MAX_RANGE = 5.12
RASTRIGIN_RANGE = 0.1

SCHWEFEL_MIN_RANGE = -500
SCHWEFEL_MAX_RANGE = 500
SCHWEFEL_RANGE = 5

ZAKHAROV_MIN_RANGE = -10
ZAKHAROV_MAX_RANGE = 10
ZAKHAROV_RANGE = 0.2

SPHERE_MIN_RANGE = -5.12
SPHERE_MAX_RANGE = 5.12
SPHERE_RANGE = 0.1

MICHALEWICZ_MIN_RANGE = 0
MICHALEWICZ_MAX_RANGE = math.pi
MICHALEWICZ_RANGE = 0.1

def get_min_range(name_function):
    if name_function == "ackley":
        return ACKLEY_MIN_RANGE
    elif name_function == "levy":
        return LEVY_MIN_RANGE
    elif name_function == "griewank":
        return GRIEWANK_MIN_RANGE
    elif name_function == "schwefel":
        return SCHWEFEL_MIN_RANGE
    elif name_function == "zakharov":
        return ZAKHAROV_MIN_RANGE
    elif name_function == "sphere":
        return SPHERE_MIN_RANGE
    elif name_function == "michalewicz":
        return MICHALEWICZ_MIN_RANGE
    else:
        return 0

def get_max_range(name_function):
    if name_function == "ackley":
        return ACKLEY_MAX_RANGE
    elif name_function == "levy":
        return LEVY_MAX_RANGE
    elif name_function == "griewank":
        return GRIEWANK_MAX_RANGE
    elif name_function == "schwefel":
        return SCHWEFEL_MAX_RANGE
    elif name_function == "zakharov":
        return ZAKHAROV_MAX_RANGE
    elif name_function == "sphere":
        return SPHERE_MAX_RANGE
    elif name_function == "michalewicz":
        return MICHALEWICZ_MAX_RANGE
    else:
        return 0

def get_range(name_function):
    if name_function == "ackley":
        return ACKLEY_RANGE
    elif name_function == "levy":
        return LEVY_RANGE
    elif name_function == "griewank":
        return GRIEWANK_RANGE
    elif name_function == "schwefel":
        return SCHWEFEL_RANGE
    elif name_function == "zakharov":
        return ZAKHAROV_RANGE
    elif name_function == "sphere":
        return SPHERE_RANGE
    elif name_function == "michalewicz":
        return MICHALEWICZ_RANGE
    else:
        return 0






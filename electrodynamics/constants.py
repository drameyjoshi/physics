# Speed of light in vacuum in cm/s
c = 2.998 * 1E10

# Magnitude of electronic charge in esu.
e = 4.803 * 1E-10

# Mass of electron in g.
m_e = 9.110 * 1E-28

# Mass of proton in g.
m_p = 1.673 * 1E-24

# Avogadro number in per mol.
N_A = 6.023 * 1E23

# Boltzmann constant in erg/K.
k = 1.381 * 1E-16

# Planck constant in erg s
h = 6.626 * 1E-27

# Gravitational constant in dynes cm^2/g^2.
G = 6.672 * 1E-8

# Electron magnetic moment in erg/gauss.
mu_e = 9.285 * 1E-21

# Proton magnetic moment in erg/gauss.
mu_p = 1.411 * 1E-21

# Acceleration due to earth's gravity im cm/s^2
g = 980

def toSI(quantity: str, value: float) -> float:
    match quantity:
        case 'charge': return value / 3 * 1E-9
        case 'pd': return value * 300
        case 'magnetic induction': return value/10000
        case 'capacitance': return value / 9 * 1E-11
        case 'current': return value / 3 * 1E-9
        case 'electric field': return value * 3 * 1E4
        case 'resistance': return value / 1.113 * 1E12
        case 'inductance': return value / 1.113 * 1E12
        case _: raise ValueError(f'{quantity} cannot be converted to SI.')

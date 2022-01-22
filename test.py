from pymatgen.ext.matproj import MPRester

if __name__ == "__main__":
    MAPI_KEY = 'vitvGcsFqw8QTTDZ5L'  # You must change this to your Materials API key! (or set MAPI_KEY env variable)
    # QUERY = "mp-1203"  # change this to the mp-id of your compound of interest
    QUERY = "TiO"  # change this to a formula of interest
    # QUERY = "Ti-O"  # change this to a chemical system of interest

    mpr = MPRester(MAPI_KEY)  # object for connecting to MP Rest interface

    structures = mpr.get_structures(QUERY)
    for s in structures:
        print(s)
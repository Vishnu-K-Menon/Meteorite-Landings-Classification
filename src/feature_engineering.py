def map_recclass_to_macro(df):
    mapping = {
        "Chondrite": ["L", "H", "LL", "CH", "CM", "CO", "CV", "CK", "CR"],
        "Achondrite": ["Aubrite", "Howardite", "Diogenite", "Eucrite", "Ureilite"],
        "Iron": ["Iron", "IAB", "IIAB", "IIIAB", "IVA"],
        "Stony-Iron": ["Pallasite", "Mesosiderite"],
        "Lunar": ["Lunar"],
        "Martian": ["Martian"]
    }

    def map_class(x):
        for macro, substrings in mapping.items():
            if any(sub in str(x) for sub in substrings):
                return macro
        return "Other"

    df["classification_type"] = df["recclass"].apply(map_class)
    return df

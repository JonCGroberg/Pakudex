import pakudex

if __name__ == '__main__':
    dex = pakudex.Pakudex()
    dex.add_pakuri("Meep")
    dex.add_pakuri("Bear")
    dex.add_pakuri("Tiger")

    print(dex)

    print(dex.evolve_species("Tiger"))

    print("\n" + str(dex))

    print(dex.get_stats("Tiger"))

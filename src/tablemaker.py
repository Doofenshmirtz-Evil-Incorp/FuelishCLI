def tablemaker(data):  # OPTIMIZED VARIANT
    l = len(data[0])
    lf = [max(len(str(i[p])) for i in data) for p in range(l)]

    print("+" + "-" * ((len(lf) * 4) + sum(lf) - 2) + "+")
    for p in data:
        for i in range(l):
            print("|", " ", p[i], " " * (lf[i] - len(str(p[i]))), "|", end="", sep="")
        if data[0] == p:
            print()
            print("+" + "-" * ((len(lf) * 4) + sum(lf) - 2) + "+", end="")
        print()
    print("+" + "-" * ((len(lf) * 4) + sum(lf) - 2) + "+")  # table making end



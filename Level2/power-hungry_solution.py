def solution(xs):
    positives = []
    negatives = []
    product = max(xs)
    xs.remove(product)
    for panel in xs:
        if panel > 0:
            positives.append(panel)
        if panel < 0:
            negatives.append(panel)
    if (len(positives) > 0):
        for panel in positives:
            product = product * panel
    if (len(negatives) > 0):
        if (len(negatives)%2==0):
            for panel in negatives:
                product = product * panel
        if (len(negatives)%2==1):
            negatives.remove(sorted(negatives, reverse=True)[0])
            for panel in negatives:
                product = product * panel
    return str(product)

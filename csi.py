suspects = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

haircolor = {"Black": "CCAGCAATCGC", "Brown": "GCCAGTGCCG", "Blonde": "TTAGCTATCGC"}
facialshape = {"Square": "GCCACGG", "Round": "ACCACAA", "Oval": "AGGCCTCA"}
eyecolor = {"Blue": "TTGTGGTGGC", "Green": "GGGAGGTGGC", "Brown": "AAGTAGTGAC"}
gender = {"Female": "TGAAGGACCTTC", "Male": "TGCAGGAACTTC"}
race = {"White": "AAAACCTCA", "Black": "CGACTACAG", "Asian": "CGCGGGCCG"}

eva = [gender["Female"], race["White"], haircolor["Blonde"], eyecolor["Blue"], facialshape["Oval"]]
larisa = [gender["Female"], race["White"], haircolor["Brown"], eyecolor["Brown"], facialshape["Oval"]]
matej = [gender["Male"], race["White"], haircolor["Black"], eyecolor["Blue"], facialshape["Oval"]]
miha = [gender["Male"], race["White"], haircolor["Brown"], eyecolor["Green"], facialshape["Square"]]

persons = {"eva": eva, "larisa": larisa, "matej": matej, "miha": miha}

def untersuchung(name):
    for x in persons[name]:
        if x not in suspects:
            return False
    #print "Der Verdaechtige ist " + name
    return True

for name in persons:
    if untersuchung(name):
        print "der Taeter ist " + name
    else:
        print name + " ist unschuldig"

#print untersuchung("eva")
#print untersuchung("larisa")
#print untersuchung("matej")
#print untersuchung("miha")

"""
def untersuchung2(person):
    i = 0
    e = len(person)
    for x in person:
        if x in suspects:
            i = i + 1
    return i == e

print untersuchung2(miha)
print untersuchung2(eva)
"""
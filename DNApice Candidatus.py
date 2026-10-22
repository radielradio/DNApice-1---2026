def calc(serie):
    total = len(serie)
    for q in ["A", "T", "G", "U", "C"]:
        quant_letra = serie.count(q)
        porcent = (quant_letra/total)*100
        print(f"{q}: {porcent:.1f}%")
        
bases = {"A" : "T",     "T" : "A",    "C" : "G",    "G" : "C"}
rnabases = {"A" : "U",    "U" : "A",    "C" : "G",    "G" : "C"}
cores = {
    "A" : "\033[34mA\033[0m",
    "T" : "\033[33mT\033[0m",
    "C" : "\033[35mC\033[0m",
    "G" : "\033[32mG\033[0m",
    "U" : "\033[33mU\033[0m",
    "\u2261" : "\033[36m\u2261\033[0m",
    "=" : "\033[31m=\033[0m"
}

input("\nAperte ENTER para gerar o DNA da bactéria Candidatus Carsonella: ")

bac_dna = ["A", "A", "G", "T", "T", "A", "T", "T", "C", "T", "T", "A", "T", "A", "G", "T", "T", "C", "C", "A", "G"]
bac_dna2 = ["T", "T", "C", "A", "A", "T", "A", "A", "G", "A", "A", "T", "A", "T", "C", "A", "A", "G", "G", "T", "C"]

dadosbacteria = bac_dna + bac_dna2

dnacompleto = list(zip(bac_dna, bac_dna2))
for base, basepar in dnacompleto:
    if base in ["A", "T"]:
        pontes = "="
    else:
        pontes = "\u2261"
    
    print(f"| {cores[base]} {cores[pontes]} {cores[basepar]} |")

print("\nPorcentagens da fita de DNA da bactéria Candidatus Carsonella: ")
calc(dadosbacteria)



rnabacteria = input("\nO usuário deseja ver o RNA da bactéria? S/N ")

if rnabacteria.lower() in ["s", "sim"]:
    bac_rna = []
    for base, basepar in dnacompleto:
        base_rna = "U" if base == "T" else base
        basepar_rna = "U" if basepar == "T" else basepar
        bac_rna.append(base_rna)
        bac_rna.append(basepar_rna)
    
        if base in ["A", "U"]:
            pontes = "="        
        else:
            pontes = "\u2261"
            
        print(f"| {cores[base_rna]} {cores[pontes]} {cores[basepar_rna]} |")
    
    print("\nPorcentagem da fita de RNA da bactéria: ")
    calc(bac_rna)
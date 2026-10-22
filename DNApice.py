from random import choice

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

print("\033[96m\nDNAPICE: GERADOR DE DNA E RNA EM PYTHON\033[0m")


quant = int(input("\nDigite a quantidade desejada de bases nitrogenadas: "))
vezes = int(input("\nQuantos pares de bases o usuário deseja gerar por vez? Digite 0 para ver o total. "))
fita = []



for num in range(quant):
    base = choice(list(bases.keys()))
    fita.append(base) 
    basepar = bases[base]
    fita.append(basepar)
        
    if base in ["A" , "T"]:
        pontes = "="
    else:
        pontes = "\u2261"
    
    print(f"| {cores[base]} {cores[pontes]} {cores[basepar]} |")
    
    if vezes > 0 and (num + 1) % vezes == 0 and (num + 1) < quant:
        restantes = quant - (num + 1)
        input(f"Pressione a tecla ENTER para gerar as próximas bases. {restantes}/{quant} restantes. ")
          
print("\nPorcentagens da fita de DNA:")  
calc(fita)



rnapergunta = input("\nO usuario deseja ver esta fita em RNA? S/N ")
vezes_rna = int(input("\nQuantos pares de bases do RNA o usuário deseja gerar por vez? Digite 0 para ver o total. "))

if rnapergunta.lower() in ["s", "sim"]:
    fita_rna = []
    transcricao = {"A": "U", "T": "A", "C": "G", "G": "C"}
    
    for i, base in enumerate (fita[::2]):
        base_rna = transcricao[base]
        fita_rna.append(base_rna)
        basepar_dna = bases[base]
        basepar_rna = transcricao[basepar_dna]
        fita_rna.append(basepar_rna)
                 
        if base_rna in ["A" , "U"]:
                pontes = "="
        else:
            pontes = "\u2261"
        
        print(f"| {cores[base_rna]} {cores[pontes]} {cores[basepar_rna]} |")
        
        
        if vezes_rna > 0 and (i + 1) % vezes_rna == 0 and (i + 1) < quant:
            restantes = quant - (i + 1)
            input(f"Pressione a tecla ENTER para gerar as próximas bases. {restantes}/{quant} restantes. ")
        
    print("\nPorcentagens da fita de RNA: ")
    calc(fita_rna)
    
    
    

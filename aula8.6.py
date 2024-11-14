#Tabela de tradução dos aminoácidos
tabela_de_traducao = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

# Função para obter o complemento reverso de uma sequência de DNA
def complemento_reverso(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(sequence))

# Função para traduzir uma sequência de códons em aminoácidos
def traduzir_codons(sequence):
    aminoacidos = []
    for i in range(0, len(sequence) - len(sequence) % 3, 3):
        codon = sequence[i:i+3]
        if codon in tabela_de_traducao:
            aminoacidos.append(tabela_de_traducao[codon])
        else:
            aminoacidos.append('X')  # Se o códon não for encontrado, marca com 'X'
    return ''.join(aminoacidos)

# Função para encontrar o peptídeo mais longo (M => Stop)
def encontrar_peptideo_longest(aa_sequence):
    peptideos = aa_sequence.split('*')  # Divide a sequência em peptídeos
    peptideo_longest = ""
    for peptideo in peptideos:
        if peptideo.startswith('M') and len(peptideo) > len(peptideo_longest):
            peptideo_longest = peptideo
    return peptideo_longest

# Solicita o nome do arquivo ao usuário
arquivo_fasta = input("Digite o nome do arquivo FASTA: ")

# Define os nomes dos arquivos de saída
arquivo_codons = "Python_08.codons-6frames.nt"
arquivo_traduzido = "Python_08.translated.aa"
arquivo_peptideo = "Python_08.translated-longest.aa"

try:
    # Inicializa um dicionário para armazenar as sequências
    sequencias = {}
    sequencia_atual = None

    # Abre e processa o arquivo FASTA
    with open(arquivo_fasta, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                sequencia_atual = line[1:]
                sequencias[sequencia_atual] = ""
            else:
                sequencias[sequencia_atual] += line

    # Abre os arquivos de saída no modo escrita
    with open(arquivo_codons, "w") as saida_codons, open(arquivo_traduzido, "w") as saida_traduzido, open(arquivo_peptideo, "w") as saida_peptideo:
        # Para cada sequência, gere os 6 quadros de leitura
        for seq_name, sequence in sequencias.items():
            # Para os 3 quadros de leitura da sequência original
            for frame in range(3):
                saida_codons.write(f"{seq_name}-frame-{frame+1}-codons\n")
                codons = []
                for i in range(frame, len(sequence) - len(sequence) % 3, 3):
                    codon = sequence[i:i+3]
                    codons.append(codon)
                saida_codons.write(" ".join(codons) + "\n")
                
                # Traduz para aminoácidos
                aminoacidos = traduzir_codons(sequence[frame:])
                saida_traduzido.write(f"{seq_name}-frame-{frame+1}-aa\n")
                saida_traduzido.write(aminoacidos + "\n")

                # Encontra o peptídeo mais longo
                peptideo_longest = encontrar_peptideo_longest(aminoacidos)
                saida_peptideo.write(f">{seq_name}-frame-{frame+1}-longest-peptideo\n")
                saida_peptideo.write(peptideo_longest + "\n")

            # Obter o complemento reverso da sequência
            complement_sequence = complemento_reverso(sequence)

            # Para os 3 quadros de leitura do complemento reverso
            for frame in range(3):
                saida_codons.write(f"{seq_name}-frame-{frame+4}-codons\n")
                codons = []
                for i in range(frame, len(complement_sequence) - len(complement_sequence) % 3, 3):
                    codon = complement_sequence[i:i+3]
                    codons.append(codon)
                saida_codons.write(" ".join(codons) + "\n")
                
                # Traduz para aminoácidos
                aminoacidos = traduzir_codons(complement_sequence[frame:])
                saida_traduzido.write(f"{seq_name}-frame-{frame+4}-aa\n")
                saida_traduzido.write(aminoacidos + "\n")

                # Encontra o peptídeo mais longo
                peptideo_longest = encontrar_peptideo_longest(aminoacidos)
                saida_peptideo.write(f">{seq_name}-frame-{frame+4}-longest-peptideo\n")
                saida_peptideo.write(peptideo_longest + "\n")

            saida_codons.write("\n")  # Pula uma linha entre as sequências
            saida_traduzido.write("\n")  # Pula uma linha entre as sequências
            saida_peptideo.write("\n")  # Pula uma linha entre as sequências

    print(f"A saída dos códons foi gravada no arquivo '{arquivo_codons}'.")
    print(f"A tradução dos códons foi gravada no arquivo '{arquivo_traduzido}'.")
    print(f"O peptídeo mais longo foi gravado no arquivo '{arquivo_peptideo}'.")

except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o nome e tente novamente.")
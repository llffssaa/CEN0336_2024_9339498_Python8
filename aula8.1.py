# Solicita o nome do arquivo ao usuário
arquivo_fasta = input("Digite o nome do arquivo FASTA: ")

try:
    # Tenta abrir o arquivo no modo leitura e exibir seu conteúdo
    with open(arquivo_fasta, "r") as arquivo:
        print("Conteúdo do arquivo:")
        for linha in arquivo:
            print(linha.strip())  # remove espaços em branco extras

    # Inicializa variáveis para armazenar dados
    sequences = {}
    current_sequence_name = None

    # Abre e processa o arquivo FASTA para contar nucleotídeos
    with open(arquivo_fasta, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                # Identifica o nome da sequência
                current_sequence_name = line[1:]
                sequences[current_sequence_name] = {"A": 0, "T": 0, "G": 0, "C": 0}
            else:
                # Conta nucleotídeos na sequência
                for nucleotide in line:
                    if nucleotide in sequences[current_sequence_name]:
                        sequences[current_sequence_name][nucleotide] += 1

    # Exibe os resultados
    print("\nContagem de nucleotídeos:")
    for seq_name, counts in sequences.items():
        print(f"{seq_name}\tA:{counts['A']}\tT:{counts['T']}\tG:{counts['G']}\tC:{counts['C']}")

except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o nome e tente novamente.")
#Solicita o nome do arquivo ao usuário
arquivo_fasta = input("Digite o nome do arquivo FASTA: ")

# Define o nome do arquivo de saída
arquivo_saida = "Python_08.codons-frame-1.nt"

try:
    # Inicializa um dicionário para armazenar as sequências
    sequencias = {}
    sequencia_atual = None

    # Abre e processa o arquivo FASTA
    with open(arquivo_fasta, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                # Identifica o nome da sequência
                sequencia_atual = line[1:]
                sequencias[sequencia_atual] = ""
            else:
                # Adiciona a linha de sequência (sem o identificador ">")
                sequencias[sequencia_atual] += line

    # Abre o arquivo de saída no modo escrita
    with open(arquivo_saida, "w") as saida:
        # Divide cada sequência em códons no primeiro quadro de leitura e escreve no arquivo
        for seq_name, sequence in sequencias.items():
            saida.write(f"{seq_name}-frame-1-codons\n")
            # Loop para iterar pela sequência em blocos de 3
            for i in range(0, len(sequence) - len(sequence) % 3, 3):
                codon = sequence[i:i+3]
                saida.write(f"{codon} ")
            saida.write("\n")  # Pula uma linha entre cada sequência

    print(f"A saída foi gravada no arquivo '{arquivo_saida}'.")

except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o nome e tente novamente.")
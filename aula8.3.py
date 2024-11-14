# Solicita o nome do arquivo ao usuário
arquivo_fasta = input("Digite o nome do arquivo FASTA: ")

# Define o nome do arquivo de saída
arquivo_saida = "Python_08.codons-3frames.nt"

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
        # Para cada sequência, gere os 3 quadros de leitura
        for seq_name, sequence in sequencias.items():
            for frame in range(3):  # Para os 3 quadros de leitura
                saida.write(f"{seq_name}-frame-{frame+1}-codons\n")
                # Divide a sequência em códons considerando o quadro de leitura
                for i in range(frame, len(sequence) - len(sequence) % 3, 3):
                    codon = sequence[i:i+3]
                    saida.write(f"{codon} ")
                saida.write("\n")  # Pula uma linha entre os quadros de leitura
            saida.write("\n")  # Pula uma linha entre as sequências

    print(f"A saída foi gravada no arquivo '{arquivo_saida}'.")

except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o nome e tente novamente.")
import itertools
import time

def gerar_wordlist():
    print("— Gerador de Wordlist para Auditoria —")
    
    palavras = input("Digite palavras-chave (ex: admin,teste,msfadmin): ").split(',')
    numeros = input("Digite números (ex: 2024,123): ").split(',')
    caracteres = ['!', '@', '#']

    palavras = [p.strip() for p in palavras]
    numeros = [n.strip() for n in numeros]

    filename = "wordlist_custom.txt"
    
    inicio = time.time()

    try:
        with open(filename, 'w') as arquivo:
            combinacoes = list(itertools.product(palavras, numeros, caracteres))
            for combo in combinacoes:
                senha = "".join(combo)
                arquivo.write(senha + "\n")
        
        fim = time.time()
        tempo_total = fim - inicio
        
        print(f"\n[Sucesso] {len(combinacoes)} senhas geradas em: {filename}")
        print(f"[Tempo] Processo concluído em {tempo_total:.4f} segundos.")

    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")

if __name__ == "__main__":
    gerar_wordlist()

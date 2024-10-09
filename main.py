import cryptos
# Rode este arquivo aqui!

automode = False
content = "RSA eh um algoritmo que leva o nome de 3 professores do MIT: Rivest, Shamir e Adleman"
algos = ["RSA-1024", "RSA-2048", "RSA-4096", "RSA-8192", "AES-128", "AES-256"]
algo_functions = [cryptos.rsa_test, cryptos.rsa_test, cryptos.rsa_test, cryptos.rsa_test, cryptos.aes_test, cryptos.aes_test]
algo_bits = [1024, 2048, 4096, 8192, 128, 256]
encryption_timings = []

print("Gostária de rodar no teste no modo automático? (s/n)")
if input().lower() == 's':
    automode = True

if automode:
    print("Rodando no modo automático...\n")
else:
    print("Rodando no modo manual...\n")

for i in range(len(algos)):
    if not automode:
        print("Pressione uma tecla para começar a execução do algoritmo", algos[i])
        input()
    else:
        print("Cifrando a mensagem com o algoritmo", algos[i])
    
    print("Processando...\n")
    
    # Convert content to bytes
    content_bytes = content.encode('utf-8')
    
    encryption_time = algo_functions[i](algo_bits[i], content_bytes)
    
    print(encryption_time)
    encryption_timings.append(encryption_time)
    print(encryption_timings[i])
    
    print("Pronto!\n")
    print("Movendo para o próximo algoritmo...\n")
    

print("Processando dados...")


for i in range(len(algos)):
    print(algos[i], encryption_timings[i])

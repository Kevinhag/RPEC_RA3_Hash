import subprocess

tamanhoConjuntos = ["1000000", "5000000", "20000000"]
tamanhoTabelas = ["10000000", "50000000", "100000000"]
funcoesHash = ["modulo", "multiplicacao", "dobra"]
seed = 123

for i in range(len(funcoesHash)):
    print(f"\nRodando a função hash: {i}\n")
    for j in range(len(tamanhoConjuntos)):
        seeds = 123
        for k in range(len(tamanhoTabelas)): 
            for k2 in range(10):
                compileCommand = ["javac", "tabelasHash.java"]
                argumentos = [tamanhoConjuntos[j], tamanhoTabelas[k], str(seed), funcoesHash[i]]
                print(funcoesHash[i], tamanhoConjuntos[j], tamanhoTabelas[k],  f"seed={seed}")
                runCommand = ["java", "tabelasHash"] + argumentos
                seed += 1

                runProcess = subprocess.run(compileCommand, capture_output=True, text=True)
                runProcess = subprocess.run(runCommand, capture_output=True, text=True)

                if runProcess.returncode != 0:
                    print(runProcess)
                    print("Erro na compilação:")
                    print(runProcess.stderr)
                else:
                    print("Compilação bem-sucedida.")
                    print(runProcess.stdout)

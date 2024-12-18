def main():
    #declaracao de variaveis
    codigo_disciplina = str()
    quantidade_alunos = int()
    peso_um = float()
    peso_dois = float()
    peso_tres = float()
    matricula = str()
    n_um = float()
    n_dois = float()
    n_tres = float()
    frequencia = int()
    nota_parcial = float()
    soma = float()
    maior = float()
    menor = float()
    aluno_maior = str()
    aluno_menor = str()
    contA = int()
    contP = int()
    contR = int()
    
    #processamento
    codigo_disciplina = input()
    while(codigo_disciplina != "FIM"):
        quantidade_alunos = int(input())
        peso_um = float(input())
        peso_dois = float(input())
        peso_tres = float(input())
        print(f"DISC {codigo_disciplina}")
        soma = 0
        contA = 0
        contP = 0
        contR = 0
        maior = -1
        menor = 101
        for i in range(quantidade_alunos):
            
            matricula = input()
            n_um = float(input())
            n_dois = float(input())
            n_tres = float(input())
            frequencia = int(input())
            
            nota_parcial = ((n_um*peso_um)+(n_dois*peso_dois)+(n_tres*peso_tres))/(peso_um+peso_dois+peso_tres)
            soma = soma + nota_parcial
            if(nota_parcial >= 60 and frequencia >= 72):
                
                print(f"MATRI {matricula} NOTA PARCIAL={nota_parcial:.2f} SITUACAO FINAL=APROVADO")
                contA+=1
            if(nota_parcial <= 60 and frequencia >= 72):
                nota_minima = (nota_parcial + (60 + nota_parcial))/2
                print(f"MATRI {matricula} NOTA PARCIAL={nota_parcial:.2f} SITUACAO FINAL=PROVA FINAL NOTA MÍNIMA NA PROVA FINAL={nota_minima}")
                contP+=1
            if(frequencia < 72):
                print(f"MATRI {matricula} NOTA PARCIAL={nota_parcial:.2f} SITUACAO FINAL=REPROVADO POR FALTA")
                contR+=1
            

            if(nota_parcial > maior):
                maior = nota_parcial
                maior_aluno = matricula
            if(nota_parcial < menor):
                menor = nota_parcial
                aluno_menor = matricula
        codigo_disciplina = input()
        if(quantidade_alunos == 0):
            print(f"{codigo_disciplina}")
            print(f"NOTA MEDIA=0")
            print(f"0% APROVADOS")
            print(f"0% PROVA FINAL")
            print(f"0% REPROVADOS POR FALTA")
        else:
            print(f"{codigo_disciplina}")
            print(f"NOTA MEDIA={(soma/quantidade_alunos):.2f}")
            print(f"{((contA/quantidade_alunos)*100):.2f}% APROVADOS")
            print(f"{((contP/quantidade_alunos)*100):.2f}% PROVA FINAL")
            print(f"{((contR/quantidade_alunos)*100):.2f}% REPROVADOS POR FALTA")


if __name__ == "__main__":
    main()

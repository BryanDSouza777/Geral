class CPF:
    def UltimosDigitos(self, lista):
        m1 = []
        for e in range(9):  
            m1.append(int(lista[e]) * (10 - e))
        mt1 = (sum(m1) * 10) % 11
        if mt1 >= 10:
            mt1 = 0

        m2 = []
        for a in range(10):
            m2.append(int(lista[a]) * (11 - a))
        mt2 = (sum(m2)* 10) % 11
        if mt2 >= 10:
            mt2 = 0
        
        if lista[9] == str(mt1) and lista[10] == str(mt2):
            print('\nCPF Válido!')
            return lista
        elif lista[9] != str(mt1) or lista[10] != str(mt2):
            print('\nCPF Inválido')
            exit()

    def escreverCPF(self,seucpf):
        self.seucpf = seucpf
        while True:
            try:
                self.seucpf
            except:
                print('CPF não pode conter letras ou sinais, apenas números')
            if str(self.seucpf) == str(self.seucpf)[::-1]:#anti falsa validação
                print('CPF com caracteres repetidos é inválido!')
                continue
            else:
                break
            
        if len(str(self.seucpf)) != 11:
            print ("\nCPF está incorreto, digite sem '.' e '-'")
        cpf.UltimosDigitos(self.seucpf)
cpf = CPF()
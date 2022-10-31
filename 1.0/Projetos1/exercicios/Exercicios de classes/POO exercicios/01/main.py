from classes import Funcionarios
from classes import Departamento
from classes import Empresa
emp = Empresa
print('Empresa Valhalla Store\n')
emp = Empresa('Valhalla Store')
cnpj = emp.generate_cnpj()
cnpjv = True
if cnpjv == True:
    print ('%s%s.%s%s%s.%s%s%s/%s%s%s%s-%s%s' % tuple(cnpj[::-1]))

print('\nDepartamento de Moveis\n')
emp.inserirDepartamento('Moveis')
dp = emp.departamentos[-1]
dp.contratar('Cleber',1500,'10/07/2019')
dp.contratar('João',2050,'29/05/2018')
dp.contratar('Lan',1750,'15/08/2020')
dp.aumento()
dp.lista()

print('\nDepartamento de Tecnologia\n')
emp.inserirDepartamento('Tecnologia')
dp1 = emp.departamentos[-1]
dp1.contratar('Zezin',2350,'20/06/2018')
dp1.contratar('Paulo',4805,'30/02/2016')
dp1.contratar('Connor',3980,'25/03/2017')
dp1.aumento()
dp1.lista()

print('\nDepartamento de Roupas\n')
emp.inserirDepartamento('Roupas')
dp2 = emp.departamentos[-1]
dp2.contratar('Felipe',3000,'28/12/2017')
dp2.contratar('Paulo',2800,'16/09/2018')
dp2.contratar('Claudio',2482,'19/11/2019')
dp2.lista()

print('\nDepartamento de Materiais Artisticos\n')
emp.inserirDepartamento('Materiais Artisticos')
dp3 = emp.departamentos[-1]
dp3.contratar('Clebin',4192,'31/08/2017')
dp3.contratar('Mayara',4307,'02/09/2018')
dp3.contratar('Junior',2092,'05/05/2019')
dp3.lista()

while True:
    try:
        djs = (input("Deseja contratar algum funcionario?\n\n1 = Sim\n2 = Não"))
    except:
        print("\nDigite apenas 1 ou 2")

    if djs != '1' and djs != '2':
        print('\nDigite apenas 1 ou 2')

    elif djs == '1':
        contdep = input('\nDigite em qual departamento deseja contratar seu funcionario: \n\n1 = Moveis\n2 = Tecnologia\n3 = Roupas\n4 = Materiais Artisticos\n')
        if contdep == 1:
            contdep = 'Moveis'
        contnom = input('\nDigite o nome do funcionario: ')
        contsal = int(input('\nDigite o salario do seu funcionario: '))
        contdat = input('\nDigite quando seu funcionario sera contratado: ')
        Departamento.contratar(contdep,contnom,contsal,contdat)
    elif djs == '2':
        break
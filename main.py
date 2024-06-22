# ## Desafio 2

# Você é um analista de dados, e decidiu trocar de emprego.

# Utilize a media, moda, mediana e o desvio padrão 

#para decidir qual empresa faz sentido para você:

# Justificar por que decidiu por essa empresa.

# ***Verifique isso através dos salários:***


from  media import media1

from mediana import mediana1

from varianca import varianca1

from desvio import desvio1

from moda import moda1


from matplotlib import pyplot as plt


empresa1 = [1000,6000,1200,8000,1400]

empresa1.sort()

empresa2 = [5000,4000,3000,2000,7000]

empresa2.sort()

empresa3 = [1200,1300,8000,3000,15000]

empresa3.sort()

empresa4 = [1400,1750,2000,4500,5900]

empresa4.sort()


cargos = ['estagiario','tecnico','assistente','analista','supervisor']



def hadle(lista, salarios):


    print('EMPRESA', salarios)
    print('----------------------------')
    media1(lista)
    mediana1(lista)
    moda1(lista)
    varianca1(lista)
    desvio1(lista)



hadle(empresa1, empresa1)  

hadle(empresa2, empresa2)   

hadle(empresa3, empresa3) 

hadle(empresa4, empresa4) 

plt.title('CARGOS E SALARIOS')
plt.xlabel('CARGOS')
plt.ylabel('SALARIOS')


plt.plot(cargos, empresa1, linestyle = '--', marker='o')

plt.plot(cargos, empresa2, linestyle = '--', marker='o')

plt.plot(cargos, empresa3, linestyle = '--', marker='o')

plt.plot(cargos, empresa4, linestyle = '--', marker='o')

plt.grid(True)

plt.show()
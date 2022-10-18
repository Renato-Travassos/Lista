lista=list()
n=r=h=select=nome=search=0
def programalista(n):
   n=int(n)
   for c in range(n):
      r=input('nome:').upper().strip()
      lista.append(r)
while select!='4': 
 select=input('SELECIONE \n0 =apaga,1=adiciona,2=pesquisa,3=ver lista,4=terminar')
 if select=='0':  
    print('-'*20)
    for c,v in enumerate(lista):       
       print(f'{c} {v}')
    print('-'*20)
    while nome!='999':
     nome=input('digite o número do nome') 
     if nome.isnumeric() and nome!='999':
        nome=int(nome)
        nome<=len(lista)-1     
        lista.remove(lista[nome])
     else:
        print('nome não encontrado',nome)
 elif select=='1':
    while True:
     n=input('quantos?')
     if n.isnumeric():        
        programalista(n)          
        break    
 elif select=='2':
    print('para sair digite 999\n') 
    while search!='999':
     search=input('ver se existe tal nome: ').upper().strip()
     if search in lista:
         print(f'{search} está na lista')
     else:
         print(f'{search}  não está na lista')           
 elif select=='3' or select=='4':
      print('-'*20)
      for nome in lista:
         print(nome,end='\n') 
      print('-'*20)     

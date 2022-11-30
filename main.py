lista=list()
n=r=h=select=nome=search=edit=0
def adicionar(select):
      n=input('quantos?')
      if n.isnumeric():            
         n=int(n)                 
         for c in range(n):
             r=input('nome:').upper().strip()
             lista.append(r)          
      else:
         print('somente números')  
           
def ver(select):
    for nome,n in enumerate(lista):
         print(nome,n) 
               
def apagar(select): 
    print('-'*20)   
    while True:
     nome=input('digite o número do nome: ') 
     if nome.isnumeric() and nome!='999':
        nome=int(nome)
        if nome<=len(lista)-1:
           print(f'{lista[nome]},removido\n')    
           lista.remove(lista[nome])
     if nome=='999':
        break
        print('saindo')
        
def editar(select):
    while True:       
       nome=input('digite o nome que quer colocar').upper().strip()
       edit=input('numero')
       if len(nome)>3 and edit.isnumeric():
          edit=int(edit)
          if edit<=len(lista)-1:
             lista[edit]=nome
             print('editado')
       elif nome=='999':
            print('saindo')
            break
       return 'número inexistente'      
            
while select!='5': 
 select=input('SELECIONE \n0 =apaga,1=adiciona,2=pesquisa,3=ver lista,4=editar,5=terminar')
 if select=='0':
    ver(select)
    apagar(select)
 elif select=='1':
      adicionar(select)
 elif select=='2':
    ver(select)
    search=' '
    while search!='999':
     search=input('ver se existe tal nome: ').upper().strip()
     print(f'{search} está na lista?',search in lista)
 elif select=='3':
      ver(select)
 elif select=='4':
      ver(select)
      editar(select)    
with open('lista.txt','w+') as file:
     for nomes in lista:
         print(nomes)
         file.write(nomes+'\n')

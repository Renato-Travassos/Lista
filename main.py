lista=list()
n=r=h=select=nome=search=edit=0
def programalista(n):
   n=int(n)
   for c in range(n):
      r=input('nome:').upper().strip()
      lista.append(r)
      
def listas(nome):
     print('para sair digite 999\n') 
     for c,v in enumerate(lista):       
        print(f'{c} {v}')
     print('-'*20)
      
while select!='5': 
 select=input('SELECIONE \n0 =apaga,1=adiciona,2=pesquisa,3=ver lista,4=editar,5=terminar')
 if select=='0':  
    print('-'*20)
    while nome!='999':    
     listas(nome)
     nome=input('digite o número do nome: ') 
     if nome.isnumeric() and nome!='999':
        nome=int(nome)
        if nome<=len(lista)-1:
           print(f'{lista[nome]},removido\n')    
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
    search=' '
    while search!='999':
     search=input('ver se existe tal nome: ').upper().strip()
     print(f'{search} está na lista?',search in lista)
 elif select=='4':
      while nome!='999':
       listas(nome)        
       nome=input('digite o nome que quer colocar').upper().strip()
       edit=input('numero')
       if len(nome)>3 and edit.isnumeric():
          edit=int(edit)
          if edit<=len(lista)-1:
             lista[edit]=nome
             print('editado')
       else:
          print('número inexistente')       
 elif select in '35' :
      print('-'*20)
      for nome in lista:
         print(nome) 
      print('-'*20)     

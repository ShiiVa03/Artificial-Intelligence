% transporte: Tipo,Classificacao,PesoMax,VelMax
transporte(1,bicicleta,5,10).
transporte(2,moto,20,35).
transporte(3,carro,100,25).


freguesia(povoa,[rua1,rua2,rua3]).

% encomenda: IdEncomenda, Peso, Volume
encomenda(1,10,10).
encomenda(2,20,5).
encomenda(3,60,30).
encomenda(4,25,10).
encomenda(5,40,40).
encomenda(6,90,90).

% entrega : IdEnt,Rua,HoraPedido,PrazoEntrega,IdEstafeta,Transporte,IdCliente,Rating,IdEnc,Entregue.
entrega(1,rua3,10/03/2010-14:30,10/03/2010-14:40,1,carro,jose,2,4,entregue).
entrega(2,rua1,10/03/2010-13:30,10/03/2010-14:50,2,moto,antonio,3,2,nao_entregue).
entrega(3,rua2,10/03/2010-15:30,10/03/2010-16:30,3,moto,antonio,5,3,entregue).
entrega(4,rua2,11/03/2010-15:30,11/03/2010-16:30,4,bicicleta,novais,5,1,entregue).
entrega(5,rua2,20/05/2021-15:10,20/05/2021-16:10,4,bicicleta,jose,5,5,entregue).
entrega(6,rua2,20/05/2021-15:10,20/05/2021-16:30,2,carro,manuel,5,6,entregue).

% Cria factos através do conhecimento ja obtido mas desta vez com o preço
entrega(_,_,D1,D2,_,T,_,_,Id,_,Preco) :- 
    entrega(_,_,D1,D2,_,T,_,_,Id,_),
    encomenda(Id,Peso,Volume),
    calculateHours(D1,D2,Hours),
    calculaPrecoHora(T,Hours,P),
    Preco is (Peso*Volume)/10 + P.


% cliente: Nome
cliente(jose).
cliente(antonio).
cliente(manuel).
cliente(novais).

% estafeta: IdEstafeta, Nome
estafeta(1,tiago).
estafeta(2,zeca).
estafeta(3,pedro).
estafeta(4,joaquim).
% transporte: Tipo,Classificacao,PesoMax,VelMax
transporte(1,bicicleta,5,10).
transporte(2,moto,20,35).
transporte(3,carro,100,25).


freguesia(povoa_de_varzim,[largo_do_cruzeiro, avenida_dos_pescadores, rua_31_de_janeiro]).
freguesia(gualtar,[rua_da_universidade, avenida_da_paz, rua_do_sol, rua_igreja_velha]).

% encomenda: IdEncomenda, Peso, Volume, IdEstafeta
:- dynamic encomenda/4.
:- dynamic entrega/10.
encomenda(1,10,10,4).
encomenda(2,20,5,2).
encomenda(3,60,30,3).
encomenda(4,25,10,1).
encomenda(5,40,40,4).
encomenda(6,90,90,2).

% entrega : IdEnt,Rua,HoraPedido,PrazoEntrega,IdEstafeta,Transporte,IdCliente,Rating,IdEnc,Entregue.
entrega(1,largo_do_cruzeiro,10/03/2010-14:30,10/03/2010-14:40,1,carro,jose,2,4,(entregue,1)).
entrega(2,rua_do_sol,10/03/2010-13:30,10/03/2010-14:50,2,moto,antonio,3,2,nao_entregue).
entrega(3,rua_da_universidade,10/03/2010-15:30,10/03/2010-16:30,3,moto,antonio,5,3,(entregue,0)).
entrega(4,rua_igreja_velha,11/03/2010-15:30,11/03/2010-16:30,4,bicicleta,joao,5,1,(entregue,0)).
entrega(5,avenida_dos_pescadores,20/05/2021-15:10,20/05/2021-16:10,4,bicicleta,jose,5,5,(entregue,1)).
entrega(6,rua_da_universidade,20/05/2021-15:10,20/05/2021-16:30,2,carro,manuel,5,6,(entregue,1)).

% Cria factos através do conhecimento ja obtido mas desta vez com o preço
entrega(_,_,D1,D2,_,T,_,_,Id,_,Preco) :- 
    entrega(_,_,D1,D2,_,T,_,_,Id,_),
    encomenda(Id,Peso,Volume,_),
    calculateHours(D1,D2,Hours),
    calculaPrecoHora(T,Hours,P),
    Preco is (Peso*Volume)/10 + P.


% cliente: Nome
cliente(jose).
cliente(antonio).
cliente(manuel).
cliente(joao).

% estafeta: IdEstafeta, Nome, Penalizacoes
estafeta(1,tiago,5).
estafeta(2,zeca,5).
estafeta(3,pedro,1).
estafeta(4,joaquim,3).

% Trasportes classificados pela vertente ecologica
% transporte: Tipo,Classificacao

transporte(1,bicicleta,5,10).
transporte(2,moto,20,35).
transporte(3,carro,100,25).

freguesia(povoa,[rua1,rua2,rua3]).
encomenda(1,10,30).
encomenda(2,20,40).
encomenda(3,60,80).

% entrega : IdEnt,Rua,Data,IdEstafeta,Transporte,IdCliente,PreÃ§o,Rating,IdEnc).
entrega(3,rua3,10/03/2001-14:30,3,carro,cli,10,2,1,entregue).
entrega(4,rua1,10/03/2001-13:30,1,bicicleta,cli,20,3,2,nao_entregue).
entrega(5,rua2,10/03/2001-15:30,2,moto,cli,30,5,3,entregue).
entrega(5,rua2,10/03/2001-15:30,3,carro,cli,30,5,3,entregue).
cliente(cli).

estafeta(1,tiago).
estafeta(2,zeca).
estafeta(3,pedro).


compare_tuples_descending('<', (_, X), (_, Y)) :- 
    transporte(A,X,_,_),
    transporte(B,Y,_,_),
    A < B, !.
compare_tuples_descending('>', _, _).

sort_tuples_descending(Unsorted, Sorted) :-
    predsort(compare_tuples_descending, Unsorted, Sorted).

remove_list([], _, []).
remove_list([X|Tail], L2, Result):- member(X, L2), !, remove_list(Tail, L2, Result). 
remove_list([X|Tail], L2, [X|Result]):- remove_list(Tail, L2, Result).

count(L,E, N,Result) :-
    include(=(E), L, L2), length(L2, N),
    remove_list(L,L2,Result).


countList([],Resu,Resu).
countList([(X,T)|Tail],Resu,L):- 
    count(Tail,(X,T),Res,L1),
    R is Res +1,
    append([((X,T),R)],Resu,L2),
    countList(L1,L2,L).

maxL([],(Res,Id),(Res,Id)).
maxL([((Id,T),N)| Tail], (Max,MaxId), (Res,IdF)) :- 
    N > Max,
    maxL(Tail,(N,Id),(Res,IdF)).
maxL([((Id,T),N)| Tail], (Max,MaxId), (Res,IdF)):- 
    N =< Max,
    maxL(Tail,(Max,MaxId),(Res,IdF)).

maxLWrapper([((Id,T),N)|Tail], R) :- maxL(Tail,(Id,N),R).

are_different((X,T), (Y,T1)) :-
    T \= T1.

filterList(A, In, Out) :-
    exclude(are_different(A), In, Out).

eco(Id) :-
    findall((Id, T), entrega(_,_,_,Id,T,_,_,_,_,_),Transportes),
    sort_tuples_descending(Transportes,[Head|TT]),
    filterList(Head,[Head|TT],Sol),
    countList(Sol,[],Li),
    maxLWrapper(Li,(Res,Id)).

estafeta_enc(IdCliente, List, Res) :- 
    findall((IdEnc,IdT), entrega(_,_,_,IdT,_,IdCliente,_,_,IdEnc,_), Entregas),
    estafeta_enc_aux(Entregas, List, [], Res).


estafeta_enc_aux([], _, Result,Result).
estafeta_enc_aux([(IdEnc,IdT)|Tail], List, Result,Re) :- 
    member(IdEnc, List),
    estafeta_enc_aux(Tail,List, [IdT|Result],Re),!.
estafeta_enc_aux([X|Tail],List,Result,Re) :- estafeta_enc_aux(Tail,List,Result,Re).


valor_faturado(D/M/A,Result) :- 
    findall(P,entrega(_,_,D/M/A-_:_,_,_,_,P,_,_,_),PriceList),
    sumlist(PriceList,Result).

calcula_rating([],_) :- !,fail.
calcula_rating(L,Result) :- 
    length(L,Len),
    sumlist(L,S),
    Result is S/Len.

rating_medio(IdEstafeta,Result) :-
    findall(R, entrega(_,_,_,IdEstafeta,_,_,_,R,_,_),RatingList),
    calcula_rating(RatingList,Result).

get_list_by_trans_aux([],Result,Result).
get_list_by_trans_aux([X|Tail], Res,R) :-
    count(Tail,X,Count,LWithoutRep),
    Total is Count + 1,
    append([(X,Total)],Res,L2),
    get_list_by_trans_aux(LWithoutRep,L2,R).

get_list_by_trans(List,Result) :- get_list_by_trans_aux(List,[],Result).
total_by_transport(DataIn, DataFin, Res) :-
    findall(Trans,(entrega(_,_,D,_,Trans,_,_,_,_,_),dataEntreDatas(DataIn,D,DataFin)),TransList),
    get_list_by_trans(TransList,Res).


total_deliveries(DataIn,DataFin,Res) :-
    findall(Id,(entrega(Id,_,D,_,_,_,_,_,_,_),dataEntreDatas(DataIn,D,DataFin)),List),
    length(List,Res).


dataMaiorQueData(D1/M1/A1-H1:MIN1, D2/M2/A2-H2:MIN2) :-
	(A1 > A2, !);
    (A1 =:= A2, M1 > M2, !);
    (A1 =:= A2, M1 =:= M2, D1 > D2, !);
    (A1 =:= A2, M1 =:= M2, D1 =:= D2, H1 > H2, !);
    (A1 =:= A2, M1 =:= M2, D1 =:= D2, H1 =:= H2, MIN1 > MIN2, !).

dataMenorQueData(X, Y) :- not(dataMaiorQueData(X,Y)).

dataEntreDatas(A, B, C) :- 
    dataMaiorQueData(B, A),
    dataMenorQueData(B, C).

% Ex 9

contarEncomendasEntregues(Data1,Data2,R) :-
	findall(1, (entrega(_,_,X,_,_,_,_,_,_,entregue), dataEntreDatas(Data1,X,Data2)), L),
	length(L,R).

contarEncomendasNaoEntregues(Data1,Data2,R) :-
	findall(1, (entrega(_,_,X,_,_,_,_,_,_,nao_entregue), dataEntreDatas(Data1,X,Data2)), L),
	length(L,R).

% Ex 10


getPesoEncomenda(Id,P) :-
	encomenda(Id,P,_).

calcularPesoTotal(Estafeta, Resultado) :-
	estafeta(IdEstafeta, Estafeta),
	findall(X, entrega(_,_,_,IdEstafeta,_,_,_,_,X,_), L),
	maplist(getPesoEncomenda, L, T),
	sumlist(T, Resultado).
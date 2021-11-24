:- style_check(-singleton).
:- include('database.pl').
:- include('funcoes_auxiliares.pl').


% Ex 1
eco(R) :-
    findall((Id, T), entrega(_,_,_,_,Id,T,_,_,_,_),Transportes),
    sort_tuples_descending(Transportes,[Head|TT]),
    filterList(Head,[Head|TT],Sol),
    countList(Sol,[],Li),
    maxLWrapper(Li,(Res,Re)),
    estafeta(Re,R),!.

maxLWrapper([((Id,T),N)|Tail], R) :- maxL(Tail,(N,Id),R).


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


% Ex 2
estafeta_enc(IdCliente, List, Res) :- 
    findall((IdEnc,IdT), entrega(_,_,_,_,IdT,_,IdCliente,_,IdEnc,_), Entregas),
    estafeta_enc_aux(Entregas, List, [], Res).


estafeta_enc_aux([], _, Result,Result).
estafeta_enc_aux([(IdEnc,IdT)|Tail], List, Result,Re) :- 
    member(IdEnc, List),
    estafeta(IdT,Nome),
    estafeta_enc_aux(Tail,List, [Nome|Result],Re),!.
estafeta_enc_aux([X|Tail],List,Result,Re) :- estafeta_enc_aux(Tail,List,Result,Re).


% Ex 3
servidoEstafeta(IdEstafeta, Res) :-
    findall(IdCliente, entrega(_,_,_,_,IdEstafeta,_,IdCliente,_,_,_), Res).


% Ex 4
valor_faturado(D/M/A,Result) :- 
    findall(P,entrega(_,_,D/M/A-_:_,_,_,_,_,_,_,_,P),PriceList),
    sumlist(PriceList,Result).


% Ex 5
zonaComMaisEntregasAux([], Z/N, Z/N).
zonaComMaisEntregasAux([Z|T], X/N, Res) :-
    count(T, Z, N1, _),
    N2 is N1 + 1,
    N2 >= N,
    zonaComMaisEntregasAux(T, Z/N2, Res).
zonaComMaisEntregasAux([H|T], X/N, Res) :-
    zonaComMaisEntregasAux(T, X/N, Res).
    
zonaComMaisEntregas(L, R) :-
    zonaComMaisEntregasAux(L, _/0, R), !.

findFreguesia(Rua, F) :-
    freguesia(F, L),
    member(Rua, L), !.

ruaComMaisEntregas(Result) :-
    findall(Rua, entrega(_, Rua, _, _, _, _, _, _, _, _), Ruas),
    zonaComMaisEntregas(Ruas, Result).

freguesiaComMaisEntregas(Result) :-
    findall(Freguesia, (entrega(_, Rua, _, _, _, _, _, _, _, _), findFreguesia(Rua, Freguesia)), Freguesias),
    zonaComMaisEntregas(Freguesias, Result).


% Ex 6
rating_medio(IdEstafeta,Result) :-
    findall(R, entrega(_,_,_,_,IdEstafeta,_,_,R,_,_),RatingList),
    calcula_rating(RatingList,Result).

calcula_rating([],_) :- !,fail.
calcula_rating(L,Result) :- 
    length(L,Len),
    sumlist(L,S),
    Result is S/Len.


% Ex 7
total_by_transport(DataIn, DataFin, Res) :-
    findall(Trans,(entrega(_,_,D,_,_,Trans,_,_,_,_),dataEntreDatas(DataIn,D,DataFin)),TransList),
    get_list_by_trans(TransList,Res).

get_list_by_trans(List,Result) :- get_list_by_trans_aux(List,[],Result).

get_list_by_trans_aux([],Result,Result).
get_list_by_trans_aux([X|Tail], Res,R) :-
    count(Tail,X,Count,LWithoutRep),
    Total is Count + 1,
    append([(X,Total)],Res,L2),
    get_list_by_trans_aux(LWithoutRep,L2,R).


% Ex 8
total_by_est(DataIn, DataFin, Res) :-
    findall(IdEs,(entrega(_,_,D,_,IdEs,_,_,_,_,_),dataEntreDatas(DataIn,D,DataFin)),EstList),
    get_list_by_est(EstList,Res).

get_list_by_est(List,Result) :- get_list_by_est_aux(List,[],Result).

get_list_by_est_aux([],Result,Result).
get_list_by_est_aux([X|Tail], Res,R) :-
    count(Tail,X,Count,LWithoutRep),
    Total is Count + 1,
    estafeta(X,Nome),
    append([(Nome,Total)],Res,L2),
    get_list_by_est_aux(LWithoutRep,L2,R).


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

calcularPesoTotal(Estafeta,D/M/A, Resultado) :-
	estafeta(IdEstafeta, Estafeta),
	findall(X, (entrega(_,_,DataIn,_,IdEstafeta,_,_,_,X,_),dataEntreDatas(D/M/A-00:00,DataIn,D/M/A-23:59)), L),
	maplist(getPesoEncomenda, L, T),
	sumlist(T, Resultado).

% Calcula o preco baseado no prazo de entrega
calculaPrecoHora(T,Hours,P) :-
    transporte(N,T,_,_),
    P is ((15/N)/Hours),!.

calculateHours(D/M/A-H:Mi,D1/M1/A1-H1:Mi1,Hours) :- 
    timediff(date(A,M,D,H,Mi,0,0,-,-), date(A1,M1,D1,H1,Mi1,0,0,-,-),Res),
    Hours is Res/3600,!.

timediff(DateTime1, DateTime2, Sec) :-
        date_time_stamp(DateTime1, TimeStamp1),
        date_time_stamp(DateTime2, TimeStamp2),
        Sec is abs(TimeStamp2 - TimeStamp1),!.


% Metodo para comparar os niveis de transporte
compare_tuples_descending('<', (_, X), (_, Y)) :- 
    transporte(A,X,_,_),
    transporte(B,Y,_,_),
    A < B, !.
compare_tuples_descending('>', _, _).

sort_tuples_descending(Unsorted, Sorted) :-
    predsort(compare_tuples_descending, Unsorted, Sorted).

% Contar quantos elementos são iguais a E e depois removê-los da cauda
count(L,E, N,Result) :-
    include(=(E), L, L2), length(L2, N),
    remove_list(L,L2,Result).


remove_list([], _, []).
remove_list([X|Tail], L2, Result):- member(X, L2), !, remove_list(Tail, L2, Result). 
remove_list([X|Tail], L2, [X|Result]):- remove_list(Tail, L2, Result).



% Remove os elementos diferentes de A, em que A é um tuplo
filterList(A, In, Out) :-
    exclude(are_different(A), In, Out).

are_different((X,T), (Y,T1)) :-
    T \= T1.


% Verifica se uma dada data está entre outras
dataEntreDatas(A, B, C) :- 
    dataMaiorQueData(B, A),
    dataMenorQueData(B, C).

dataMaiorQueData(D1/M1/A1-H1:MIN1, D2/M2/A2-H2:MIN2) :-
	(A1 > A2, !);
    (A1 =:= A2, M1 > M2, !);
    (A1 =:= A2, M1 =:= M2, D1 > D2, !);
    (A1 =:= A2, M1 =:= M2, D1 =:= D2, H1 > H2, !);
    (A1 =:= A2, M1 =:= M2, D1 =:= D2, H1 =:= H2, MIN1 > MIN2, !).

dataMenorQueData(X, Y) :- not(dataMaiorQueData(X,Y)).
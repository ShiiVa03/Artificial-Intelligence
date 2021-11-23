% Calcula o preco baseado no prazo de entrega
calculaPrecoHora(T,H1:M1,H2:M2,P) :-
    H1 =< H2,
    H is abs(H2 - H1),
    M is abs(M2 - M1),
    transporte(N,T,_,_),
    P is (H*(15/N) + (M*(15/N))/60),!.
calculaPrecoHora(T,H1:M1,H2:M2,P) :-
    H is abs((H1-24) - H2),
    M is abs(M2 - M1),
    transporte(N,T,_,_),
    P is (H*(15/N) + (M*(15/N))/60),!.

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
:-include('trabalho.pl').

:- use_module(library(print_table)).

main_menu :-
    repeat,
    write('\33\[2J'),
    write('-------MENU-------'), nl,
    write('1. Conhecimento'), nl,
    write('2. Queries'), nl,
    write('0. Sair'), nl,
    read(Z),
    ( Z = 0 -> !, fail; true ),  % fail without backtrack if Z = 0
    ( Z = 1 -> !, facts_menu; true ),
    ( Z = 2 -> !, queries_menu; true ),
    fail.

facts_menu :-
    write('\33\[2J'),
    write('---CONHECIMENTO---'), nl,
    write('1. Transportes'), nl,
    write('2. Freguesias'), nl,
    write('3. Clientes'), nl,
    write('4. Estafetas'), nl,
    write('5. Encomendas'), nl,
    write('6. Entregas'), nl,
    write('0. Voltar a trás'), nl,
    read(Z),
    ( Z = 0 -> !, main_menu; true ),
    ( Z = 1 -> !, facts(transporte); true ),
    ( Z = 2 -> !, facts(freguesia); true ),
    ( Z = 3 -> !, facts(cliente); true ),
    ( Z = 4 -> !, facts(estafeta); true ),
    ( Z = 5 -> !, facts(encomenda); true ),
    ( Z = 6 -> !, facts(entrega); true ),
    fail.

facts(X) :-
    repeat,
    write('\33\[2J'),
    facts_table(X),
    write('0. Voltar a trás'), nl,
    read(Z),
    ( Z = 0 -> !, facts_menu; true ),
    fail.

facts_table(transporte) :-
    findall(
        row{'Tipo':A, 'Classificação':B, 'Peso Máximo':C, 'Velocidade Máxima':D},
        transporte(A, B, C, D),
        Data
    ),
    Keys = ['Tipo', 'Classificação', 'Peso Máximo', 'Velocidade Máxima'],
    print_table(Data, Keys, _{}, "Transportes", mysql, 50).

facts_table(freguesia) :-
    findall(
        row{'Nome':A, 'Ruas':C},
        (freguesia(A, B), atomic_list_concat(B, ', ', C)),
        Data
    ),
    Keys = ['Nome', 'Ruas'],
    print_table(Data, Keys, _{}, "Freguesias", mysql, 50).

facts_table(cliente) :-
    findall(
        row{'Nome':A},
        cliente(A),
        Data
    ),
    Keys = ['Nome'],
    print_table(Data, Keys, _{}, "Clientes", mysql, 50).

facts_table(estafeta) :-
    findall(
        row{'ID':A, 'Nome':B, 'Penalizações':C},
        estafeta(A, B, C),
        Data
    ),
    Keys = ['ID', 'Nome', 'Penalizações'],
    print_table(Data, Keys, _{}, "Estafetas", mysql, 50).

facts_table(encomenda) :-
    findall(row{'ID':A, 'Peso':B, 'Volume':C, 'ID Estafeta':D}, encomenda(A, B, C, D), Data),
    Keys = ['ID', 'Peso', 'Volume', 'ID Estafeta'],
    print_table(Data, Keys, _{}, "Encomendas", mysql, 50).

facts_table(entrega) :-
    findall(
        row{'ID':A, 'Rua':B, 'Data do Pedido':C, 'Prazo de Entrega':D, 'ID Estafeta':E, 'Transporte Usado':F, 'Nome do Cliente':G, 'Rating':H, 'ID Encomenda':I, 'Estado':J},
        entrega(A, B, C, D, E, F, G, H, I, J),
        Data
    ),
    Keys = ['ID', 'Rua', 'Data do Pedido', 'Prazo de Entrega', 'ID Estafeta', 'Transporte Usado', 'Nome do Cliente', 'Rating', 'ID Encomenda', 'Estado'],
    print_table(Data, Keys, _{}, "Entregas", mysql, 200).

queries_menu :-
    write('\33\[2J'),
    write('------QUERIES------'), nl,
    write('1.  Query 1'), nl,
    write('2.  Query 2'), nl,
    write('3.  Query 3'), nl,
    write('4.  Query 4'), nl,
    write('5.  Query 5'), nl,
    write('6.  Query 6'), nl,
    write('7.  Query 7'), nl,
    write('8.  Query 8'), nl,
    write('9.  Query 9'), nl,
    write('10. Query 10'), nl,
    write('0.  Voltar a trás'), nl,
    read(Z),
    ( Z = 0 -> !, main_menu; true ),
    ( Z = 1 -> !, query(1); true ),
    ( Z = 2 -> !, query(2); true ),
    ( Z = 3 -> !, query(3); true ),
    ( Z = 4 -> !, query(4); true ),
    ( Z = 5 -> !, query(5); true ),
    ( Z = 6 -> !, query(6); true ),
    ( Z = 6 -> !, query(7); true ),
    ( Z = 6 -> !, query(8); true ),
    ( Z = 6 -> !, query(9); true ),
    ( Z = 6 -> !, query(10); true ),
    fail.

query(X) :-
    write('\33\[2J'),
    write('0. Voltar a trás'), nl,
    query_body(X),
    read(Z),
    ( Z = 0 -> !, queries_menu; true ),
    fail.

query_body(1) :-
    write('------QUERY 1------'), nl, nl,
    write('Descrição:'), nl,
    write('Identificar o estafeta que utilizou mais vezes um meio de transporte mais ecológico.'), nl, nl,
    write('Resultado:'), nl,
    eco(R),
    write(R), nl, nl.

query_body(2) :-
    write('------QUERY 2------'), nl, nl,
    write('Descrição:'), nl,
    write('Identificar que estafetas entregaram determinada(s) encomenda(s) a um cliente.'), nl, nl,
    facts_table(cliente), nl,
    facts_table(encomenda), nl,
    write('Nome do Cliente:'), nl,
    read(Nome), nl,
    write('Lista de IDs das encomendas: '), nl,
    read(L), nl,
    write('Resultado:'), nl,
    estafeta_enc(Nome, L, R),
    write(R), nl, nl.
    
query_body(3) :-
    write('------QUERY 3------'), nl, nl,
    write('Descrição:'), nl,
    write('Identificar os clientes servidos por um determinado estafeta.'), nl, nl,
    facts_table(estafeta), nl,
    write('ID do Estafeta:'), nl,
    read(ID), nl,
    write('Resultado:'), nl,
    servidoEstafeta(ID, R),
    write(R), nl, nl.

query_body(4) :-
    write('------QUERY 4------'), nl, nl,
    write('Descrição:'), nl,
    write('Calcular o valor faturado pela Green Distribution num determinado dia.'), nl, nl,
    write('Dia/Mês/Ano:'), nl,
    read(ID), nl,
    write('Resultado:'), nl,
    valor_faturado(ID, R),
    write(R), nl, nl.

query_body(5) :-
    write('------QUERY 5------'), nl, nl,
    write('Descrição:'), nl,
    write('Identificar quais as zonas com maior volume de entregas por parte da Green Distribution.'), nl, nl,
    write('Resultado:'), nl,
    write('Rua com mais entregas:'), nl,
    ruaComMaisEntregas(R),
    write(R), nl, nl,
    write('Freguesia com mais entregas:'), nl,
    freguesiaComMaisEntregas(F),
    write(F), nl, nl.

query_body(6) :-
    write('------QUERY 6------'), nl, nl,
    write('Descrição:'), nl,
    write('Calcular a classificação média de satisfação de cliente para um determinado estafeta.'), nl, nl,
    facts_table(estafeta), nl,
    write('ID do Estafeta:'), nl,
    read(ID), nl,
    write('Resultado:'), nl,
    rating_medio(ID, R),
    write(R), nl, nl.

query_body(7) :-
    write('------QUERY 7------'), nl, nl,
    write('Descrição:'), nl,
    write('Identificar o número total de entregas pelos diferentes meios de transporte, num determinado intervalo de tempo.'), nl, nl,
    write('Dia/Mês/Ano-H:M inicial:'), nl,
    read(DataIn), nl,
    write('Dia/Mês/Ano-H:M final:'), nl,
    read(DataFin), nl,
    write('Resultado:'), nl,
    total_by_transport(DataIn, DataFin, R),
    write(R), nl, nl.

query_body(8) :-
    write('------QUERY 8------'), nl, nl,
    write('Descrição:'), nl,
    write('Identificar o número total de entregas pelos estafetas, num determinado intervalo de tempo.'), nl, nl,
    write('Dia/Mês/Ano-H:M inicial:'), nl,
    read(DataIn), nl,
    write('Dia/Mês/Ano-H:M final:'), nl,
    read(DataFin), nl,
    write('Resultado:'), nl,
    total_by_est(DataIn, DataFin, R),
    write(R), nl, nl.

query_body(9) :-
    write('------QUERY 9------'), nl, nl,
    write('Descrição:'), nl,
    write('Identificar o número total de entregas pelos estafetas, num determinado intervalo de tempo.'), nl, nl,
    write('Dia/Mês/Ano-H:M inicial:'), nl,
    read(DataIn), nl,
    write('Dia/Mês/Ano-H:M final:'), nl,
    read(DataFin), nl,
    write('Resultado:'), nl,
    write('Número de Encomendas Entregues:'), nl,
    contarEncomendasEntregues(DataIn, DataFin, R),
    write(R), nl, nl,
    write('Número de Encomendas Não Entregues:'), nl,
    contarEncomendasNaoEntregues(DataIn, DataFin, F),
    write(F), nl, nl.

query_body(10) :-
    write('-----QUERY 10-----'), nl, nl,
    write('Descrição:'), nl,
    write('Calcular o peso total transportado por estafeta num determinado dia.'), nl, nl,
    facts_table(estafeta),
    write('Resultado:'), nl,
    write('ID Estafeta:'), nl,
    read(ID), nl,
    write('Dia/Mês/Ano:'), nl,
    read(Date), nl,
    write('Resultado:'), nl,
    calcularPesoTotal(ID, Date, R),
    write(R), nl, nl.

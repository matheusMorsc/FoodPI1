/*create table pedido (
   id int NOT NULL,
   id_cliente int NOT NULL,
   endereco varchar(300) NOT NULL,
   descricao varchar(300) NOT NULL,
   horario time NOT NULL DEFAULT CURRENT_TIMESTAMP,
   tipo_pagamento varchar(16) NOT NULL DEFAULT 'Carteira',
   valor_total int NOT NULL,
   status varchar(25) NOT NULL DEFAULT 'Ainda a ser entregue'
);

INSERT INTO pedido (id, id_cliente, endereco, descricao, horario, tipo_pagamento, valor_total, status)
VALUES
(1, 2, 'Rua Jõao 2', 'Casa amarela', '2017-03-28 17:32:41', 'Carteira', 150, 'Ainda a ser entregue'),
(2, 2, 'Avenida Maria', '', '2017-03-28 17:43:05', 'Carteira', 130, 'Cancelado pelo cliente'),
(3, 3, 'Rua Tiago', '3º andar prédio azul', '2017-03-28 19:49:33', 'Dinheiro', 130, 'Ainda a ser entregue'),
(4, 3, 'Rua Vitor', '', '2017-03-28 19:52:01', 'Dinheiro', 130, 'Cancelado pelo cliente'),
(5, 3, 'Rua Flávia', '', '2017-03-28 20:47:28', 'Carteira', 285, 'Pausado'),
(6, 3, 'Rua Gabriela', '', '2017-03-30 00:43:31', 'Carteira', 325, 'Cancelado pelo cliente');*/


select * from pedido;




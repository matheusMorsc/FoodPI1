CREATE TABLE items (
  rId int,
  idItem int NOT NULL,
  nome varchar(20) NOT NULL,
  preco double precision NOT NULL,
  primary key(idItem),
  foreign key (rId) references Restaurantes (rId)
) ;

Create table Pedidos ( 
  uId int,
  rId int,  
  PedidosId  int, 
  horario_pedido      Date, 
  total  double precision,
  hora_entregada Date,
  primary key   (PedidosId),
  foreign key   (uId) references usuarios (uId),
  foreign key   (rId) references Restaurantes (rId)
);

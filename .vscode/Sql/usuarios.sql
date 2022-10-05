
Create table usuarios (
  uId      int not null,
  uNome   varchar(20),
  uTelefone   char(10), 
  uEndereco varchar(25), 
  uEmail varchar(35) not null,
  uUsername varchar(10) not null,
  uSenha varchar(12) not null,
  primary key (uId)
); 


create database BancaElectronica;
use BancaElectronica;
#create table TIPO_EMPRESA(
#IdEmpresa int primary key not null auto_increment,
#Nombre varchar(50)
#);
#Creando tabla Usuario para el Login
create table USUARIO(
IdUsuario int primary key not null auto_increment,
Usuario varchar(50) not null,
Contraseña varchar(50) not null,
TipoUsuario varchar(14) not null,
IngresosFallidos int not null
);
#creamos la tabla Empresa
#Rlegal = Representante Legal
create table EMPRESA(
NitEmpresa numeric(8,0) primary key not null,
TipoEmpresa varchar(50) not null,
NombreEmpresa varchar(50) not null,
NombreComercial varchar(50) not null,
RLegal varchar(75) not null,
Dirreccion varchar(250) not null,
TelefonoEmpresa numeric(8,0) not null,
TelefonoRLegal numeric(8,0) not null,
Email Varchar(50) not null,
Usuario int,
foreign key (Usuario) references USUARIO(IdUsuario)
#TipoEmpresa int not null,
#foreign key(TipoEmpresa) references TIPO_EMPRESA(IdEmpresa)
);
#drop database BancaElectronica; #eliminar Base de dato
#creando tabla Persona
create table PERSONA(
NitPersona numeric(8,0) primary Key not null,
CuiPersona numeric(13,0) not null,
Nombre varchar(50) not null,
Apellido varchar(50) not null,
FechaNacimiento date not null,
Telefono1 numeric(8,0) not null,
Telefono2 numeric(8,0) null,
Dirrecion varchar(250) not null,
Email varchar(50) not null,
Usuario int,
foreign key (Usuario) references USUARIO(IdUsuario)
)ENGINE=InnoDB;
#constraint persona foreign key (Usuario) references USUARIO(IdUsuario)
#drop table CUENTA;
#Drop table TRANSACCION;
#Creando la tabla cuenta
create table CUENTA(
NoCuenta bigint(10) unsigned zerofill primary key not null auto_increment,
TipoCuenta varchar(50) not null,
TipoMoneda varchar(50) not null ,
Monto numeric(10,2) null,
FechaApertura date  not null,
Estado varchar(11)  null,
ManejoCuenta numeric(10,0),
Interes decimal(4,4),
Clienteempresa numeric(8,0) null,
ClientePersona numeric(8,0) null,
Usuario int null,
foreign key (Clienteempresa) references EMPRESA(NitEmpresa),
foreign key (ClientePersona) references PERSONA(NitPersona),
foreign key (Usuario) references USUARIO(IdUsuario)
)ENGINE=InnoDB;
#Cliente numeric(8,0) not null,
#creando la tabla transaccion
create table TRANSACCION(
IdTransaccion  int primary key not null auto_increment,
TipoCuenta varchar(50) not null,
Monto numeric(10,2) not null,
MontoActual numeric(10,2) not null,
fecha date not null,
#hora time not null,
Cuenta bigint(10) unsigned zerofill,
foreign key (Cuenta) references CUENTA(NoCuenta)
);
# creando la tabla Servicio
create table SERVICIO(
IdServicio int primary key not null auto_increment,
NombreComercial varchar (60) not null, 
CuentaServicio int(10) not null,
TipoServicio varchar(50) not null
);
create table TRANSERVICE(
IdTransaccion int,
IdServicio int,
primary key(IdTransaccion,IdServicio),
foreign key (IdTransaccion) references TRANSACCION(IdTransaccion),
foreign key (IdServicio) references SERVICIO(IdServicio)
);
create table AUTORIZACION(
IdAutorizacion int primary key auto_increment not null,
nombre varchar(50)
);
create table PRESTAMO(
IdPrestamo int primary key not null auto_increment,
FechaEmision date not null,
interes decimal(4,4) null,
TiempoPagar varchar(50) not null,
MontoPrestamo numeric(6,2),
Motivo varchar(250),
Autorizacion int,
UsuarioSolicitante int,
foreign key (UsuarioSolicitante) references USUARIO(IdUsuario),
foreign key (Autorizacion) references AUTORIZACION(IdAutorizacion)
);
create table TRANSPRESTAMO(
Transaccion int,
Prestamo int,
primary key (Transaccion,Prestamo),
foreign key (Transaccion) references TRANSACCION(IdTransaccion),
foreign key (Prestamo) references Prestamo(IdPrestamo)
);
create table TERCEROS(
idTerceros int primary key not null auto_increment,
TipoMoneda varchar(50) not null,
NoCuenta numeric(10,0) not null,
TipoCuenta varchar(50) not null,
Alia varchar(50) not null,
CuentaEmisora numeric(10,0) not null
);
create table PAGO_EMPRESARIAL(
IdPagoEmpresarial int primary key not null auto_increment,
TipoPago varchar(50) not null,
Nombre varchar(50) not null,
TiempoPago varchar(50) not null,
MontoPago numeric(14,2) not null,
CuentaReceptora bigint(10) unsigned zerofill not null,
NitEmpresa numeric(8,0) not null
);
create table TRNSPAGO(
PagoEmpresarial int,
Transaccion int,
primary key (PagoEmpresarial,Transaccion),
foreign key (PagoEmpresarial) references PAGO_EMPRESARIAL(IdPagoEmpresarial),
foreign key (Transaccion) references TRANSACCION(IdTransaccion)
);
#drop table TRNSPAGO;
#drop table PAGO_EMPRESARIAL;

create table CHEQUERA(
NoChequera int primary key not null auto_increment,
CantidadCheque int not null,
CuentaAsociada bigint(10) unsigned zerofill,
foreign key (CuentaAsociada) references CUENTA(NoCuenta)
);
create table PRE_AUTORIZACION(
IdAutorizacion int primary key not null auto_increment,
EstadoAutorizacion varchar(50) not null
);
create table CHEQUE(
NoCheque bigint(8) unsigned zerofill primary key not null auto_increment,
MontoCheque numeric(4,2) not null,
NombreReceptor varchar(100) not null,
Autorizacion int,
Chequera int ,
foreign key (Chequera) references CHEQUERA(NoChequera),
foreign key (Autorizacion) references PRE_AUTORIZACION(IdAutorizacion)
);
create table TRANSCHEQUE(
ChequeNumero bigint(8) unsigned zerofill,
Transaccion int,
primary key (ChequeNumero,Transaccion),
foreign key (ChequeNumero) references CHEQUE(NoCheque),
foreign key (Transaccion) references TRANSACCION(IdTransaccion)
);

create table CREDITCARD(
NoTarjeta numeric(16,0) primary key not null,
Marca varchar(50) not null,
Moneda varchar(50) not null,
Limite numeric(7,2) not null,
MesVencimiento int not null,
AñoVencimiento int not null,
Cvv numeric(3,0) not null,
Puntos int not null,
cashbak numeric(10,4) not null,
Tipo varchar(50) not null,
CuentaAsociada bigint(10) unsigned zerofill,
foreign key (CuentaAsociada) references CUENTA(NoCuenta)
);
CREATE TABLE TRANSTARJETA(
NoTarjeta numeric(16,0),
Transaccion int,
primary key (Transaccion,NoTarjeta),
foreign key (Transaccion) references TRANSACCION(IdTransaccion),
foreign key(NoTarjeta) references CREDITCARD(NoTarjeta)
);
#editar el nombre de la columna contraseña por pasword
ALTER TABLE USUARIO RENAME COLUMN Contraseña to Pasword;
ALTER TABLE cuenta ADD PlazoPagar int AFTER Monto;
alter table transaccion add TipoTransaccion varchar(50) after IdTransaccion;
alter table transaccion add Descripcion varchar(50) after IdTransaccion;
#alter table transaccion add TipoMoneda varchar(10) after TipoCuenta;
#ALTER TABLE transaccion RENAME COLUMN Tipo to TipoCuenta;
#ALTER TABLE transaccion DROP COLUMN hora;
#ALTER TABLE transaccion DROP COLUMN TipoCuenta;
#ALTER TABLE creditcard ADD PuntosCash int AFTER Tipo;
#drop table creditcard;

#------------------------------------------ Tipo de Autorizacion---------------------------------------------------------------------------
insert into autorizacion values
(null,'Pendiente'),
(null,'Rechazado'),
(null,'Autorizado');

#--------------------------------------Registro----------------------------------------------------------------------------------------------------------------------------------------------------------
insert into usuario values
(null,'admin','Option65.la','Administrador',0),
(null,'empresa1','Option65.la','Empresa',0),
(null,'empresa2','Option65.la','Empresa',0),
(null,'empresa3','Option65.la','Empresa',0),
(null,'empresa4','Option65.la','Empresa',0),
(null,'empresa5','Option65.la','Empresa',0),
(null,'empresa6','Option65.la','Empresa',0),
(null,'empresa7','Option65.la','Empresa',0),
(null,'empresa8','Option65.la','Empresa',0),
(null,'usuario1','Option65.la','Individual',0),
(null,'usuario2','Option65.la','Individual',0);
#insert into empresa values(70851069,'Sociedad Anonima','Miselanea la pala','Miselanea la pala','Jaime Alejandro Armira Us','colonia san rafael zona 2',54689562,56458689,'alejoar@gmail.com',2);
insert into empresa values
(00000000,'Sociedad Anonima','Banco el Ahorro','Banco Centro Americano','Jaime Alejandro Armira Us','centro america',22222222,25896321,'alejoar@gmail.com',1),
(71851069,'Sociedad Anonima','Miselanea la pala','Miselanea la pala','Jaime Alejandro Armira Us','colonia san rafael zona 2',54689562,56458689,'alejoar@gmail.com',2),
(90851069,'Sociedad Anonima','El ahorro','zapateria el ahorro','Juan Francico Castro','colonia san rafael zona 2',54689562,56458689,'JfCastro@gmail.com',3),
('90861069','Sociedad Anonima','J.Elias','Ventas Hierrro en Forma J.Elias','Jose Alvarez','colonia san rafael zona 2',54689562,56458689,'JElias@gmail.com',4),
('90861061','Sociedad Anonima','Sega S.A','SEGA','Antonio Rotterford','colonia san rafael zona 2',54685562,56458689,'ejecutivo@sega.com.gt',5),
('10861061','Sociedad Anonima','Multiperfiles S.A','SEGA','Antonio Rotterford','colonia san rafael zona 2',54685562,56458689,'ejecutivo@sega.com.gt',6),
('10861062','Sociedad Anonima','FFACSA S.A','FFACSA','Luis Velasquez','colonia san rafael zona 2',54685562,56458689,'ffacsa@ffacsa.com.gt',7),
('10861063','Sociedad Anonima','Distun S.A','Distub','Rafael rodriguez','colonia san rafael zona 2',54685562,56458689,'distun@distun.com.gt',8);

insert into persona values
(70861069,1764988500401,'Jaimea Alejandro','Armira Us',19890518,50800129,null,'san rafael zona 2','alejoarmira@gmail.com',9),
(70841068,1865988510301,'Juan Manuel',' Villalvaso','19890607',50800129,null,'porvenir 2 chinautla','JMvilla@gmail.com',10);

insert into cuenta values
(null,'Monetaria','Q',30000,null,19890520,'Activo','0',0,0,null,1),
(null,'Monetaria','Q',30000,null,19890520,'Activo','0',0,71851069,null,2),
(null,'Ahorro','Q',30000,null,19890520,'Activo','0',0,71851069,null,2),
(null,'Monetaria','Q',30000,null,19890520,'Activo','0',0,90851069,null,3),
(null,'Monetaria','Q',30000,null,19890520,'Activo','0',0,90861069,null,4),
(null,'Monetaria','Q',30000,null,19890520,'Activo','0',0,90861061,null,5),
(null,'Monetaria','Q',30000,null,19890520,'Activo','0',0,10861061,null,6),
(null,'Monetaria','Q',30000,null,19890520,'Activo','0',0,10861062,null,7),
(null,'Monetaria','Q',30000,null,19890520,'Activo','0',0,10861063,null,8),
(null,'Monetaria','Q',250,null,19890520,'Activo','15',0,null,70861069,9),
(null,'Ahorro','Q',250,null,19890520,'Activo','15',0,null,70861069,9),
(null,'Monetaria','Q',250,null,19890520,'Activo','15',0,null,70841068,10);
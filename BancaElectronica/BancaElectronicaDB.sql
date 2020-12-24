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
)ENGINE=InnoDB;
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
Monto numeric(10,2) not null,
FechaApertura date not null,
Estado varchar(11) not null,
ManejoCuenta numeric(10,0),
Interes numeric(4,4),
ClienteEmpresa numeric(8,0) null,
ClientePersona numeric(8,0) null,
#Cliente numeric(8,0) not null,
Usuario int null,
foreign key (ClienteEmpresa) references EMPRESA(NitEmpresa),
foreign key (ClientePersona) references PERSONA(NitPersona),
foreign key (Usuario) references USUARIO(IdUsuario)
);
#creando la tabla transaccion
create table TRANSACCION(
IdTransaccion  int primary key not null auto_increment,
Tipo varchar(50) not null,
Monto numeric(10,2) not null,
MontoActual numeric(10,2) not null,
fecha date not null,
hora time not null,
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
create table PRESTAMO(
IdPrestamo int primary key not null auto_increment,
Cui numeric(13,0) not null,
FechaEmision date not null,
Nombre varchar(50) not null,
Apellido varchar(50) not null,
TiempoPagar varchar(50) not null,
MontoPrestamo numeric(6,2),
CuentaSolicitante bigint(10) unsigned zerofill,
foreign key (cuentaSolicitante) references CUENTA(NoCuenta)
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
TiempoPago varchar(50) not null,
MontoPago numeric(6,2) not null,
CuentaReceptora numeric(10,0) not null,
CuentaPagadora numeric(10,0) not null
);
create table TRNSPAGO(
PagoEmpresarial int,
Transaccion int,
primary key (PagoEmpresarial,Transaccion),
foreign key (PagoEmpresarial) references PAGO_EMPRESARIAL(IdPagoEmpresarial),
foreign key (Transaccion) references TRANSACCION(IdTransaccion)
);
create table CHEQUERA(
NoChequera int primary key not null auto_increment,
CantidadCheque int not null,
CuentaAsociada bigint(8) unsigned zerofill,
foreign key (CuentaAsociada) references CUENTA(NoCuenta)
);
create table AUTORIZACION(
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
foreign key (Autorizacion) references AUTORIZACION(IdAutorizacion)
);

create table TRANSCHEQUE(
ChequeNumero bigint(8) unsigned zerofill,
Transaccion int,
primary key (ChequeNumero,Transaccion),
foreign key (ChequeNumero) references CHEQUE(NoCheque),
foreign key (Transaccion) references TRANSACCION(IdTransaccion)
);

#editar el nombre de la columna contraseña por pasword
ALTER TABLE USUARIO RENAME COLUMN Contraseña to Pasword;
	
ALTER TABLE cuenta ADD PlazoPagar int AFTER Monto;

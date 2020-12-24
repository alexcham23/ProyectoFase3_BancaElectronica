# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Autorizacion(models.Model):
    idautorizacion = models.AutoField(db_column='IdAutorizacion', primary_key=True)  # Field name made lowercase.
    estadoautorizacion = models.CharField(db_column='EstadoAutorizacion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'autorizacion'


class Cheque(models.Model):
    nocheque = models.BigAutoField(db_column='NoCheque', primary_key=True)  # Field name made lowercase.
    montocheque = models.DecimalField(db_column='MontoCheque', max_digits=4, decimal_places=2)  # Field name made lowercase.
    nombrereceptor = models.CharField(db_column='NombreReceptor', max_length=100)  # Field name made lowercase.
    autorizacion = models.ForeignKey(Autorizacion, models.DO_NOTHING, db_column='Autorizacion', blank=True, null=True)  # Field name made lowercase.
    chequera = models.ForeignKey('Chequera', models.DO_NOTHING, db_column='Chequera', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cheque'


class Chequera(models.Model):
    nochequera = models.AutoField(db_column='NoChequera', primary_key=True)  # Field name made lowercase.
    cantidadcheque = models.IntegerField(db_column='CantidadCheque')  # Field name made lowercase.
    cuentaasociada = models.ForeignKey('Cuenta', models.DO_NOTHING, db_column='CuentaAsociada', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chequera'


class Cuenta(models.Model):
    nocuenta = models.BigAutoField(db_column='NoCuenta', primary_key=True)  # Field name made lowercase.
    tipocuenta = models.CharField(db_column='TipoCuenta', max_length=50)  # Field name made lowercase.
    tipomoneda = models.CharField(db_column='TipoMoneda', max_length=50)  # Field name made lowercase.
    monto = models.DecimalField(db_column='Monto', max_digits=10, decimal_places=2)  # Field name made lowercase.
    fechaapertura = models.DateField(db_column='FechaApertura')  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=11)  # Field name made lowercase.
    manejocuenta = models.DecimalField(db_column='ManejoCuenta', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    interes = models.DecimalField(db_column='Interes', max_digits=4, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    clienteempresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='ClienteEmpresa', blank=True, null=True)  # Field name made lowercase.
    clientepersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='ClientePersona', blank=True, null=True)  # Field name made lowercase.
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuenta'


class Empresa(models.Model):
    nitempresa = models.DecimalField(db_column='NitEmpresa', primary_key=True, max_digits=8, decimal_places=0)  # Field name made lowercase.
    tipoempresa = models.CharField(db_column='TipoEmpresa', max_length=50)  # Field name made lowercase.
    nombreempresa = models.CharField(db_column='NombreEmpresa', max_length=50)  # Field name made lowercase.
    nombrecomercial = models.CharField(db_column='NombreComercial', max_length=50)  # Field name made lowercase.
    rlegal = models.CharField(db_column='RLegal', max_length=75)  # Field name made lowercase.
    dirreccion = models.CharField(db_column='Dirreccion', max_length=250)  # Field name made lowercase.
    telefonoempresa = models.DecimalField(db_column='TelefonoEmpresa', max_digits=8, decimal_places=0)  # Field name made lowercase.
    telefonorlegal = models.DecimalField(db_column='TelefonoRLegal', max_digits=8, decimal_places=0)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa'


class PagoEmpresarial(models.Model):
    idpagoempresarial = models.AutoField(db_column='IdPagoEmpresarial', primary_key=True)  # Field name made lowercase.
    tipopago = models.CharField(db_column='TipoPago', max_length=50)  # Field name made lowercase.
    tiempopago = models.CharField(db_column='TiempoPago', max_length=50)  # Field name made lowercase.
    montopago = models.DecimalField(db_column='MontoPago', max_digits=6, decimal_places=2)  # Field name made lowercase.
    cuentareceptora = models.DecimalField(db_column='CuentaReceptora', max_digits=10, decimal_places=0)  # Field name made lowercase.
    cuentapagadora = models.DecimalField(db_column='CuentaPagadora', max_digits=10, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pago_empresarial'


class Persona(models.Model):
    nitpersona = models.DecimalField(db_column='NitPersona', primary_key=True, max_digits=8, decimal_places=0)  # Field name made lowercase.
    cuipersona = models.DecimalField(db_column='CuiPersona', max_digits=13, decimal_places=0)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=50)  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='FechaNacimiento')  # Field name made lowercase.
    telefono1 = models.DecimalField(db_column='Telefono1', max_digits=8, decimal_places=0)  # Field name made lowercase.
    telefono2 = models.DecimalField(db_column='Telefono2', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dirrecion = models.CharField(db_column='Dirrecion', max_length=250)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persona'


class Prestamo(models.Model):
    idprestamo = models.AutoField(db_column='IdPrestamo', primary_key=True)  # Field name made lowercase.
    cui = models.DecimalField(db_column='Cui', max_digits=13, decimal_places=0)  # Field name made lowercase.
    fechaemision = models.DateField(db_column='FechaEmision')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=50)  # Field name made lowercase.
    tiempopagar = models.CharField(db_column='TiempoPagar', max_length=50)  # Field name made lowercase.
    montoprestamo = models.DecimalField(db_column='MontoPrestamo', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cuentasolicitante = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='CuentaSolicitante', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prestamo'


class Servicio(models.Model):
    idservicio = models.AutoField(db_column='IdServicio', primary_key=True)  # Field name made lowercase.
    nombrecomercial = models.CharField(db_column='NombreComercial', max_length=60)  # Field name made lowercase.
    cuentaservicio = models.IntegerField(db_column='CuentaServicio')  # Field name made lowercase.
    tiposervicio = models.CharField(db_column='TipoServicio', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicio'


class Terceros(models.Model):
    idterceros = models.AutoField(db_column='idTerceros', primary_key=True)  # Field name made lowercase.
    tipomoneda = models.CharField(db_column='TipoMoneda', max_length=50)  # Field name made lowercase.
    nocuenta = models.DecimalField(db_column='NoCuenta', max_digits=10, decimal_places=0)  # Field name made lowercase.
    tipocuenta = models.CharField(db_column='TipoCuenta', max_length=50)  # Field name made lowercase.
    alia = models.CharField(db_column='Alia', max_length=50)  # Field name made lowercase.
    cuentaemisora = models.DecimalField(db_column='CuentaEmisora', max_digits=10, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'terceros'


class Transaccion(models.Model):
    idtransaccion = models.AutoField(db_column='IdTransaccion', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=50)  # Field name made lowercase.
    monto = models.DecimalField(db_column='Monto', max_digits=10, decimal_places=2)  # Field name made lowercase.
    montoactual = models.DecimalField(db_column='MontoActual', max_digits=10, decimal_places=2)  # Field name made lowercase.
    fecha = models.DateField()
    hora = models.TimeField()
    cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='Cuenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transaccion'


class Transcheque(models.Model):
    chequenumero = models.OneToOneField(Cheque, models.DO_NOTHING, db_column='ChequeNumero', primary_key=True)  # Field name made lowercase.
    transaccion = models.ForeignKey(Transaccion, models.DO_NOTHING, db_column='Transaccion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transcheque'
        unique_together = (('chequenumero', 'transaccion'),)


class Transervice(models.Model):
    idtransaccion = models.OneToOneField(Transaccion, models.DO_NOTHING, db_column='IdTransaccion', primary_key=True)  # Field name made lowercase.
    idservicio = models.ForeignKey(Servicio, models.DO_NOTHING, db_column='IdServicio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transervice'
        unique_together = (('idtransaccion', 'idservicio'),)


class Transprestamo(models.Model):
    transaccion = models.OneToOneField(Transaccion, models.DO_NOTHING, db_column='Transaccion', primary_key=True)  # Field name made lowercase.
    prestamo = models.ForeignKey(Prestamo, models.DO_NOTHING, db_column='Prestamo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transprestamo'
        unique_together = (('transaccion', 'prestamo'),)


class Trnspago(models.Model):
    pagoempresarial = models.OneToOneField(PagoEmpresarial, models.DO_NOTHING, db_column='PagoEmpresarial', primary_key=True)  # Field name made lowercase.
    transaccion = models.ForeignKey(Transaccion, models.DO_NOTHING, db_column='Transaccion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trnspago'
        unique_together = (('pagoempresarial', 'transaccion'),)


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='IdUsuario', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=50)  # Field name made lowercase.
    pasword = models.CharField(db_column='Pasword', max_length=50)  # Field name made lowercase.
    tipousuario = models.CharField(db_column='TipoUsuario', max_length=14)  # Field name made lowercase.
    ingresosfallidos = models.IntegerField(db_column='IngresosFallidos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'

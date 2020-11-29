# Es necesario importar las depencendias necesarias
from datetime import date, datetime, timedelta

# from datetime import datetime
# from datetime import timedelta

# Día actual
today = date.today()
# Fecha actual
now = datetime.now()
print("today", today)
print("now", now)

# Date
print("El día actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El año actual es {}".format(today.year))
# Datetime
print("El día actual es {}".format(now.day))
print("El mes actual es {}".format(now.month))
print("El año actual es {}".format(now.year))
print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))

# Los argumentos serán: Año, Mes, Día, Hora, Minutos, Segundos,
# Milisegundos.
new_date = datetime(2019, 2, 28, 10, 15, 00, 00000)
print("new_Date", new_date)

# Sumar dos días a la fecha actual
now = datetime.now()
new_date = now + timedelta(days=2)
print("new_date + 2 days", new_date)

format = new_date.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos')
print('new_date formateada', format)

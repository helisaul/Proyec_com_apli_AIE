

pkg load database
conn = pq_connect(setdbopts('dbname','pro3','host','localhost','port','5432','user','postgres','password','1234'));
precio = input("Ingrese el Precio de su producto : Q ")
IVA = precio *0.12;
precio_sin_iva =  precio - IVA;
fprintf("el precio del producto sin iva es Q%0.0f ,por lo que el IVA es de Q%0.0f\n ",precio_sin_iva,IVA);

try
  Ins1 = 'insert into productos(precio) values (';
  Ins2 = ");";
  Instruccion = strcat(Ins1,num2str(precio),Ins2);
  Registro = pq_exec_params(conn,Instruccion);
catch e
    disp(['Error dunate la conexion a DB, consulte sobre el error  ' e.message]);

end


USE restaurante;
-- Se usa la palabra DELIMITER que sirve pra indicar que hasta que no vuelva a encontrar la palabra
-- todo será parte del comando
DELIMITER //
CREATE PROCEDURE DevolverTodosLosUsuarios()
BEGIN
	SELECT * FROM usuarios;
    -- El procedimiento almacenado (stored procedure) sirve para un conjunto de operaciones
    -- INSERT INTO platos (... 
END //

DELIMITER ;

-- Ahora un SP con parámetros
-- en este caso declaramos un parámetro de entrada(IN) y a su vez le ponemos un nombre al delimitador
-- Si queremos indicar un parámetro de saldia (OUT)
DROP PROCEDURE DevolverUsuariosSegunTipo;
DELIMITER //
CREATE PROCEDURE DevolverUsuariosSegunTipo(IN tipo varchar(40), OUT usuarioID INT)
BEGIN
	-- Funciones de agregación (cont, sum, avg, max, min, )
    -- https://www.mysqltutorial.org/mysql-aggregate-functions.aspx
    -- COUNT > contabilice cuántos usuarios hay de ese tipo
	SELECT COUNT(id) INTO usuarioID FROM usuarios WHERE tipo_usuario = tipo;
END //

DELIMITER ;

CALL DevolverTodosLosUsuarios();
CALL DevolverUsuariosSegunTipo('ADMIN', @usuarioId);
SELECT @usuarioId;

CALL DevolverUsuariosSegunTipo('USER', @usuarioUser);
SELECT @usuarioUser;
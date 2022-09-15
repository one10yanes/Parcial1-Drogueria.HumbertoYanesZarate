/*
SQLyog Professional v12.5.1 (64 bit)
MySQL - 8.0.28 : Database - drogueria
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`drogueria` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `drogueria`;

/*Table structure for table `clientes` */

DROP TABLE IF EXISTS `clientes`;

CREATE TABLE `clientes` (
  `clienteId` int NOT NULL AUTO_INCREMENT,
  `nombreCliente` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `telefonoCliente` varchar(50) NOT NULL,
  PRIMARY KEY (`clienteId`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `clientes` */

insert  into `clientes`(`clienteId`,`nombreCliente`,`telefonoCliente`) values 
(1,'Humberto Yanes','323725'),
(2,'Elisa Solano','3345099'),
(3,'Juan Perez','3245690'),
(4,'Pedro Marsol','3665544');

/*Table structure for table `productos` */

DROP TABLE IF EXISTS `productos`;

CREATE TABLE `productos` (
  `productoId` int NOT NULL AUTO_INCREMENT,
  `codigoProducto` int NOT NULL,
  `nombreProducto` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `clienteId` int NOT NULL,
  `proveedorId` int NOT NULL,
  PRIMARY KEY (`productoId`),
  KEY `productoId` (`productoId`),
  KEY `fk-clienteId` (`clienteId`),
  KEY `fk-proveedorId` (`proveedorId`),
  CONSTRAINT `fk-clienteId` FOREIGN KEY (`clienteId`) REFERENCES `clientes` (`clienteId`),
  CONSTRAINT `fk-proveedorId` FOREIGN KEY (`proveedorId`) REFERENCES `proveedores` (`proveedorId`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `productos` */

insert  into `productos`(`productoId`,`codigoProducto`,`nombreProducto`,`clienteId`,`proveedorId`) values 
(1,2222,'Dipirona',1,1),
(2,43558,'Tramadol',2,2),
(3,343483,'Dolex',3,1),
(4,45576,'Dexametazona',1,1),
(5,565784,'Dolex Gripa',2,1),
(7,999999,'Ibuprofeno',4,2);

/*Table structure for table `proveedores` */

DROP TABLE IF EXISTS `proveedores`;

CREATE TABLE `proveedores` (
  `proveedorId` int NOT NULL AUTO_INCREMENT,
  `nombreProveedor` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `telefonoProveedor` varchar(50) NOT NULL,
  PRIMARY KEY (`proveedorId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `proveedores` */

insert  into `proveedores`(`proveedorId`,`nombreProveedor`,`telefonoProveedor`) values 
(1,'Drogueria la carpita roja','444444'),
(2,'Farmacenter','3244423'),
(3,'Farmatodo','223345');

/* Procedure structure for procedure `listar_clientes` */

/*!50003 DROP PROCEDURE IF EXISTS  `listar_clientes` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `listar_clientes`()
BEGIN
		SELECT * FROM clientes;
	END */$$
DELIMITER ;

/* Procedure structure for procedure `crear_cliente` */

/*!50003 DROP PROCEDURE IF EXISTS  `crear_cliente` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `crear_cliente`(in PnombreCliente varchar(50), in pTelefonoCliente varchar(50))
BEGIN
		INSERT INTO clientes (nombreCliente, telefonoCliente) VALUES (PnombreCliente, pTelefonoCliente);
	END */$$
DELIMITER ;

/* Procedure structure for procedure `eliminar_cliente` */

/*!50003 DROP PROCEDURE IF EXISTS  `eliminar_cliente` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `eliminar_cliente`(IN pId INT(50))
BEGIN
	DELETE FROM clientes WHERE clienteId = pId;
	END */$$
DELIMITER ;

/* Procedure structure for procedure `actualizar_cliente` */

/*!50003 DROP PROCEDURE IF EXISTS  `actualizar_cliente` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `actualizar_cliente`(IN pNombreCl varchar(50), in pTelefonoCl varchar(50), IN pId INT(50))
BEGIN
	UPDATE clientes SET nombreCliente=pNombreCl, telefonoCliente=pTelefonoCl WHERE clienteId=pId;
	END */$$
DELIMITER ;

/* Procedure structure for procedure `listar_proveedores` */

/*!50003 DROP PROCEDURE IF EXISTS  `listar_proveedores` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `listar_proveedores`()
BEGIN
	SELECT * FROM proveedores;
		
	END */$$
DELIMITER ;

/* Procedure structure for procedure `crear_proveedor` */

/*!50003 DROP PROCEDURE IF EXISTS  `crear_proveedor` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `crear_proveedor`(IN PnombreProveedor VARCHAR(50), IN pTelefonoProveedor VARCHAR(50))
BEGIN
		INSERT INTO proveedores (nombreProveedor, telefonoProveedor) VALUES (PnombreProveedor, pTelefonoProveedor);
	END */$$
DELIMITER ;

/* Procedure structure for procedure `eliminar_proveedor` */

/*!50003 DROP PROCEDURE IF EXISTS  `eliminar_proveedor` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `eliminar_proveedor`(IN pId INT(50))
BEGIN
	DELETE FROM proveedores WHERE proveedorId = pId;
	END */$$
DELIMITER ;

/* Procedure structure for procedure `actualizar_proveedor` */

/*!50003 DROP PROCEDURE IF EXISTS  `actualizar_proveedor` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `actualizar_proveedor`(IN pNombrePr VARCHAR(50), IN pTelefonoPr VARCHAR(50), IN pId INT(50))
BEGIN
	UPDATE proveedores SET nombreProveedor=pNombrePr, telefonoProveedor=pTelefonoPr WHERE proveedorId=pId;
	END */$$
DELIMITER ;

/* Procedure structure for procedure `listar_productos` */

/*!50003 DROP PROCEDURE IF EXISTS  `listar_productos` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `listar_productos`()
BEGIN
		SELECT pr.`productoId`,pr.`codigoProducto`,pr.`nombreProducto`,cl.`nombreCliente` cliente,pro.`nombreProveedor` proveedor FROM productos pr JOIN clientes cl ON pr.`clienteId` = cl.`clienteId` JOIN proveedores pro ON pr.`proveedorId` = pro.`proveedorId`;
		
	END */$$
DELIMITER ;

/* Procedure structure for procedure `crear_producto` */

/*!50003 DROP PROCEDURE IF EXISTS  `crear_producto` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `crear_producto`(IN pcodigoProducto int(10), IN pnombreProducto VARCHAR(50), in pclienteId int(10), pproveedorId int(10))
BEGIN
	INSERT INTO productos(codigoProducto, nombreProducto, clienteId, proveedorId) VALUES (pcodigoProducto, pnombreProducto, pclienteId, pproveedorId);
	END */$$
DELIMITER ;

/* Procedure structure for procedure `eliminar_producto` */

/*!50003 DROP PROCEDURE IF EXISTS  `eliminar_producto` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `eliminar_producto`(IN pId INT(50))
BEGIN
	DELETE FROM productos WHERE productoId = pId;
	END */$$
DELIMITER ;

/* Procedure structure for procedure `actualizar_producto` */

/*!50003 DROP PROCEDURE IF EXISTS  `actualizar_producto` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `actualizar_producto`(IN pcodigoProducto INT(10), IN pnombreProducto VARCHAR(50), IN pclienteId INT(10), pproveedorId INT(10), IN pId INT(50))
BEGIN
	UPDATE productos SEt codigoProducto=pcodigoProducto, nombreProducto=pnombreProducto, clienteId=pclienteId, proveedorId=pproveedorId WHERE productoId=pId;
	END */$$
DELIMITER ;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydbf
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Proveedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Proveedor` (
  `idProvedor` INT NOT NULL,
  `nombreProvedor` VARCHAR(45) NULL,
  `direccion` VARCHAR(45) NULL,
  `telefono` VARCHAR(45) NULL,
  PRIMARY KEY (`idProvedor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`MateriaPrima`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`MateriaPrima` (
  `idMateriaPrima` INT NOT NULL,
  `nombreMateriaPrima` VARCHAR(45) NULL,
  `costo` INT NULL,
  `proveedor` INT NULL,
  `cantidad` INT NULL,
  `unidadMedida` VARCHAR(10) NULL,
  `categoria` VARCHAR(45) NULL,
  `marca` VARCHAR(45) NULL,
  `fechaLlegada` DATETIME NULL,
  `fechaVencimiento` DATETIME NULL,
  PRIMARY KEY (`idMateriaPrima`),
  INDEX `fk_MateriaPrima_Provedor_idx` (`proveedor` ASC) VISIBLE,
  CONSTRAINT `fk_MateriaPrima_Provedor`
    FOREIGN KEY (`proveedor`)
    REFERENCES `mydb`.`Proveedor` (`idProvedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Usuarios` (
  `idUsuarios` INT NOT NULL,
  `usuario` VARCHAR(45) NULL,
  `contrasenaUsuario` VARCHAR(45) NULL,
  `rol` VARCHAR(45) NULL,
  `correoElectronico` VARCHAR(45) NULL,
  PRIMARY KEY (`idUsuarios`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`MateriaPrima_has_Usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`MateriaPrima_has_Usuarios` (
  `MateriaPrimaIdMateriaPrima` INT NOT NULL,
  `Usuarios_idUsuarios` INT NOT NULL,
  PRIMARY KEY (`MateriaPrimaIdMateriaPrima`, `Usuarios_idUsuarios`),
  INDEX `fk_MateriaPrima_has_Usuarios_Usuarios1_idx` (`Usuarios_idUsuarios` ASC) VISIBLE,
  INDEX `fk_MateriaPrima_has_Usuarios_MateriaPrima1_idx` (`MateriaPrimaIdMateriaPrima` ASC) VISIBLE,
  CONSTRAINT `fk_MateriaPrima_has_Usuarios_MateriaPrima1`
    FOREIGN KEY (`MateriaPrimaIdMateriaPrima`)
    REFERENCES `mydb`.`MateriaPrima` (`idMateriaPrima`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_MateriaPrima_has_Usuarios_Usuarios1`
    FOREIGN KEY (`Usuarios_idUsuarios`)
    REFERENCES `mydb`.`Usuarios` (`idUsuarios`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ProveedorAuditoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ProveedorAuditoria` (
  `idProveedorAuditoria` INT NOT NULL,
  `nombreAnterior` VARCHAR(45) NULL,
  `direccionAnterior` VARCHAR(45) NULL,
  `telefonoAnterior` INT NULL,
  PRIMARY KEY (`idProveedorAuditoria`),
  CONSTRAINT `fk_Proveedor_Auditoria_1`
    FOREIGN KEY (`idProveedorAuditoria`)
    REFERENCES `mydb`.`Proveedor` (`idProvedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`MateriaPrimaAuditoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`MateriaPrimaAuditoria` (
  `idMateriaPrima` INT NOT NULL,
  `nombreMateriaPrimaAnterior` VARCHAR(45) NULL,
  `costoAnterior` INT NULL,
  `proveedorAnterior` INT NULL,
  `cantidadAnterior` INT NULL,
  `unidadMedidaAnterior` VARCHAR(10) NULL,
  `categoriaAnterior` VARCHAR(45) NULL,
  `marcaAnterior` VARCHAR(45) NULL,
  `fechaLlegadaAnterior` DATETIME NULL,
  `fechaVencimientoAnterior` DATETIME NULL,
  `fechaModificacion` DATETIME NULL,
  PRIMARY KEY (`idMateriaPrima`),
  CONSTRAINT `fk_MateriaPrimaAuditoria_1`
    FOREIGN KEY (`idMateriaPrima`)
    REFERENCES `mydb`.`MateriaPrima` (`idMateriaPrima`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`UsuariosAuditoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`UsuariosAuditoria` (
  `idUsuario` INT NOT NULL,
  `usuarioAnterior` VARCHAR(45) NULL,
  `contrasenaUsuarioAnterior` VARCHAR(45) NULL,
  `rol` VARCHAR(45) NULL,
  `correoElectronico` VARCHAR(45) NULL,
  `fechaModificacion` DATETIME NULL,
  PRIMARY KEY (`idUsuario`),
  CONSTRAINT `fk_UsuariosAuditoria_1`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `mydb`.`Usuarios` (`idUsuarios`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `mydb`;


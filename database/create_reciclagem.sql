-- MySQL Script generated by MySQL Workbench
-- Wed Feb  1 08:36:37 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema reciclagem
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema reciclagem
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `reciclagem` DEFAULT CHARACTER SET utf8 ;
USE `reciclagem` ;

-- -----------------------------------------------------
-- Table `reciclagem`.`Cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reciclagem`.`Cliente` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(250) NOT NULL,
  `ultimo_nome` VARCHAR(45) NOT NULL,
  `primeiro_nome` VARCHAR(200) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  `cidade` VARCHAR(60) NOT NULL,
  `bairro` VARCHAR(100) NOT NULL,
  `rua` VARCHAR(60) NOT NULL,
  `numero` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `reciclagem`.`Funcionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reciclagem`.`Funcionario` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `primeiro_nome` VARCHAR(200) NOT NULL,
  `ultimo_nome` VARCHAR(200) NOT NULL,
  `data_de_nasc` DATE NOT NULL,
  `email` VARCHAR(200) NOT NULL,
  `senha` VARCHAR(100) NOT NULL,
  `cidade` VARCHAR(200) NULL,
  `bairro` VARCHAR(200) NULL,
  `rua` VARCHAR(200) NULL,
  `numero` VARCHAR(200) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `reciclagem`.`Tipo_de_Material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reciclagem`.`Tipo_de_Material` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `descricao` VARCHAR(300) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `reciclagem`.`Material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reciclagem`.`Material` (
  `lote` BIGINT NOT NULL AUTO_INCREMENT,
  `valor` DOUBLE NOT NULL,
  `peso` DOUBLE NOT NULL,
  `tipo` VARCHAR(45) NOT NULL,
  `data` DATETIME NOT NULL,
  `Cliente_id` BIGINT NOT NULL,
  `Funcionario_id` BIGINT NOT NULL,
  `Tipo_de_Material_id` BIGINT NOT NULL,
  PRIMARY KEY (`lote`),
  INDEX `fk_Material_Cliente1_idx` (`Cliente_id` ASC),
  INDEX `fk_Material_Funcionario1_idx` (`Funcionario_id` ASC),
  INDEX `fk_Material_Tipo_de_Material1_idx` (`Tipo_de_Material_id` ASC),
  CONSTRAINT `fk_Material_Cliente1`
    FOREIGN KEY (`Cliente_id`)
    REFERENCES `reciclagem`.`Cliente` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Material_Funcionario1`
    FOREIGN KEY (`Funcionario_id`)
    REFERENCES `reciclagem`.`Funcionario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Material_Tipo_de_Material1`
    FOREIGN KEY (`Tipo_de_Material_id`)
    REFERENCES `reciclagem`.`Tipo_de_Material` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `reciclagem`.`TelefoneCliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reciclagem`.`TelefoneCliente` (
  `telefone` VARCHAR(20) NOT NULL,
  `Cliente_id` BIGINT NOT NULL,
  PRIMARY KEY (`telefone`, `Cliente_id`),
  INDEX `fk_TelefoneCliente_Cliente1_idx` (`Cliente_id` ASC),
  CONSTRAINT `fk_TelefoneCliente_Cliente1`
    FOREIGN KEY (`Cliente_id`)
    REFERENCES `reciclagem`.`Cliente` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

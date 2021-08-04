/*
 Navicat Premium Data Transfer

 Source Server         : sql_test
 Source Server Type    : MySQL
 Source Server Version : 100413
 Source Host           : localhost:3306
 Source Schema         : sql_test_sql

 Target Server Type    : MySQL
 Target Server Version : 100413
 File Encoding         : 65001

 Date: 03/08/2021 06:43:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for country_tb
-- ----------------------------
DROP TABLE IF EXISTS `country_tb`;
CREATE TABLE `country_tb`  (
  `Id` int(11) NOT NULL,
  `country_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`Id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for university_tb
-- ----------------------------
DROP TABLE IF EXISTS `university_tb`;
CREATE TABLE `university_tb`  (
  `Id` int(11) NOT NULL,
  `university_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `country` int(255) NULL DEFAULT NULL,
  PRIMARY KEY (`Id`) USING BTREE,
  INDEX `fk_3`(`country`) USING BTREE,
  CONSTRAINT `fk_3` FOREIGN KEY (`country`) REFERENCES `country_tb` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for user_tb
-- ----------------------------
DROP TABLE IF EXISTS `user_tb`;
CREATE TABLE `user_tb`  (
  `ID` int(11) NOT NULL,
  `Name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `University` int(11) NULL DEFAULT NULL,
  `Sex` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Age` int(11) NULL DEFAULT NULL,
  `Country` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `fk_1`(`University`) USING BTREE,
  INDEX `fk_2`(`Country`) USING BTREE,
  CONSTRAINT `fk_1` FOREIGN KEY (`University`) REFERENCES `university_tb` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_2` FOREIGN KEY (`Country`) REFERENCES `country_tb` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

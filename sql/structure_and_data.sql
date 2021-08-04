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

 Date: 01/08/2021 17:19:31
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for city_tb
-- ----------------------------
DROP TABLE IF EXISTS `city_tb`;
CREATE TABLE `city_tb`  (
  `ID` int(11) NOT NULL,
  `City_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

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
-- Records of country_tb
-- ----------------------------
INSERT INTO `country_tb` VALUES (1, 'United States');
INSERT INTO `country_tb` VALUES (2, 'United Kingdom');
INSERT INTO `country_tb` VALUES (3, 'Canada');
INSERT INTO `country_tb` VALUES (4, 'Russia');
INSERT INTO `country_tb` VALUES (5, 'China');
INSERT INTO `country_tb` VALUES (6, 'France');
INSERT INTO `country_tb` VALUES (7, 'Germany');
INSERT INTO `country_tb` VALUES (8, 'Australia');
INSERT INTO `country_tb` VALUES (9, 'South Africa');

-- ----------------------------
-- Table structure for email_tb
-- ----------------------------
DROP TABLE IF EXISTS `email_tb`;
CREATE TABLE `email_tb`  (
  `ID` int(11) NOT NULL,
  `Email_addr` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for job_tb
-- ----------------------------
DROP TABLE IF EXISTS `job_tb`;
CREATE TABLE `job_tb`  (
  `ID` int(11) NOT NULL,
  `Job_type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
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
-- Records of university_tb
-- ----------------------------
INSERT INTO `university_tb` VALUES (1, 'Harvard University', 1);
INSERT INTO `university_tb` VALUES (2, 'California Institute of Technology (Caltech)', 1);
INSERT INTO `university_tb` VALUES (3, 'Stanford University', 1);
INSERT INTO `university_tb` VALUES (4, 'Massachusetts Institute of Technology ', 1);
INSERT INTO `university_tb` VALUES (5, 'Stanford University', 1);
INSERT INTO `university_tb` VALUES (6, 'University of Oxford', 2);
INSERT INTO `university_tb` VALUES (7, 'University of Cambridge', 2);
INSERT INTO `university_tb` VALUES (8, 'UCL', 2);
INSERT INTO `university_tb` VALUES (9, 'University of Toronto', 3);

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
  `City` int(11) NULL DEFAULT NULL,
  `Email` int(255) NULL DEFAULT NULL,
  `Job` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `fk_1`(`University`) USING BTREE,
  INDEX `fk_2`(`Country`) USING BTREE,
  INDEX `fk4`(`City`) USING BTREE,
  INDEX `fk5`(`Email`) USING BTREE,
  INDEX `fk6`(`Job`) USING BTREE,
  CONSTRAINT `fk_1` FOREIGN KEY (`University`) REFERENCES `university_tb` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_2` FOREIGN KEY (`Country`) REFERENCES `country_tb` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk4` FOREIGN KEY (`City`) REFERENCES `city_tb` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk5` FOREIGN KEY (`Email`) REFERENCES `email_tb` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk6` FOREIGN KEY (`Job`) REFERENCES `job_tb` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80013
 Source Host           : localhost:3306
 Source Schema         : beer

 Target Server Type    : MySQL
 Target Server Version : 80013
 File Encoding         : 65001

 Date: 02/04/2019 18:11:17
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 54 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (5, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (8, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (9, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (10, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (11, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (12, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (17, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (18, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (19, 'Can add material_ inventory', 7, 'add_material_inventory');
INSERT INTO `auth_permission` VALUES (20, 'Can change material_ inventory', 7, 'change_material_inventory');
INSERT INTO `auth_permission` VALUES (21, 'Can delete material_ inventory', 7, 'delete_material_inventory');
INSERT INTO `auth_permission` VALUES (22, 'Can add production_ activity', 8, 'add_production_activity');
INSERT INTO `auth_permission` VALUES (23, 'Can change production_ activity', 8, 'change_production_activity');
INSERT INTO `auth_permission` VALUES (24, 'Can delete production_ activity', 8, 'delete_production_activity');
INSERT INTO `auth_permission` VALUES (25, 'Can add customers', 9, 'add_customers');
INSERT INTO `auth_permission` VALUES (26, 'Can change customers', 9, 'change_customers');
INSERT INTO `auth_permission` VALUES (27, 'Can delete customers', 9, 'delete_customers');
INSERT INTO `auth_permission` VALUES (28, 'Can add product_ inventory', 10, 'add_product_inventory');
INSERT INTO `auth_permission` VALUES (29, 'Can change product_ inventory', 10, 'change_product_inventory');
INSERT INTO `auth_permission` VALUES (30, 'Can delete product_ inventory', 10, 'delete_product_inventory');
INSERT INTO `auth_permission` VALUES (31, 'Can add equipments', 11, 'add_equipments');
INSERT INTO `auth_permission` VALUES (32, 'Can change equipments', 11, 'change_equipments');
INSERT INTO `auth_permission` VALUES (33, 'Can delete equipments', 11, 'delete_equipments');
INSERT INTO `auth_permission` VALUES (34, 'Can add administrators', 12, 'add_administrators');
INSERT INTO `auth_permission` VALUES (35, 'Can change administrators', 12, 'change_administrators');
INSERT INTO `auth_permission` VALUES (36, 'Can delete administrators', 12, 'delete_administrators');
INSERT INTO `auth_permission` VALUES (37, 'Can add orders', 13, 'add_orders');
INSERT INTO `auth_permission` VALUES (38, 'Can change orders', 13, 'change_orders');
INSERT INTO `auth_permission` VALUES (39, 'Can delete orders', 13, 'delete_orders');
INSERT INTO `auth_permission` VALUES (40, 'Can add procurement', 14, 'add_procurement');
INSERT INTO `auth_permission` VALUES (41, 'Can change procurement', 14, 'change_procurement');
INSERT INTO `auth_permission` VALUES (42, 'Can delete procurement', 14, 'delete_procurement');
INSERT INTO `auth_permission` VALUES (43, 'Can add warehouse', 15, 'add_warehouse');
INSERT INTO `auth_permission` VALUES (44, 'Can change warehouse', 15, 'change_warehouse');
INSERT INTO `auth_permission` VALUES (45, 'Can delete warehouse', 15, 'delete_warehouse');
INSERT INTO `auth_permission` VALUES (46, 'Can add staff', 16, 'add_staff');
INSERT INTO `auth_permission` VALUES (47, 'Can change staff', 16, 'change_staff');
INSERT INTO `auth_permission` VALUES (48, 'Can delete staff', 16, 'delete_staff');
INSERT INTO `auth_permission` VALUES (49, 'Can add maintenances', 17, 'add_maintenances');
INSERT INTO `auth_permission` VALUES (50, 'Can change maintenances', 17, 'change_maintenances');
INSERT INTO `auth_permission` VALUES (51, 'Can delete maintenances', 17, 'delete_maintenances');
INSERT INTO `auth_permission` VALUES (52, 'Can add suppliers', 18, 'add_suppliers');
INSERT INTO `auth_permission` VALUES (53, 'Can change suppliers', 18, 'change_suppliers');
INSERT INTO `auth_permission` VALUES (54, 'Can delete suppliers', 18, 'delete_suppliers');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for beer_administrators
-- ----------------------------
DROP TABLE IF EXISTS `beer_administrators`;
CREATE TABLE `beer_administrators`  (
  `Admin_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Admin_Username` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Admin_Password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `WorkNum_id` int(11) NOT NULL,
  PRIMARY KEY (`Admin_Id`) USING BTREE,
  INDEX `Beer_administrators_WorkNum_id_55f0d66d_fk_Beer_staff_WorkNum`(`WorkNum_id`) USING BTREE,
  CONSTRAINT `Beer_administrators_WorkNum_id_55f0d66d_fk_Beer_staff_WorkNum` FOREIGN KEY (`WorkNum_id`) REFERENCES `beer_staff` (`worknum`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of beer_administrators
-- ----------------------------
INSERT INTO `beer_administrators` VALUES (1, 'wedon', '123', 1001);
INSERT INTO `beer_administrators` VALUES (2, 'fkayal', '888888', 1003);
INSERT INTO `beer_administrators` VALUES (3, 'csales', 'csales1010', 1010);
INSERT INTO `beer_administrators` VALUES (4, 'zproduction', 'zproduction1025', 1025);
INSERT INTO `beer_administrators` VALUES (5, 'xpurchase', 'xpurchase1027', 1027);
INSERT INTO `beer_administrators` VALUES (6, 'lmarketing', 'lmarketing1030', 1030);
INSERT INTO `beer_administrators` VALUES (7, 'wmarketing', 'wmarketing1031', 1031);
INSERT INTO `beer_administrators` VALUES (8, 'zsales', 'zsales1035', 1035);
INSERT INTO `beer_administrators` VALUES (9, 'sproduction', 'sproduction1040', 1040);
INSERT INTO `beer_administrators` VALUES (10, 'cpurchase', 'cpurchase1042', 1042);

-- ----------------------------
-- Table structure for beer_customers
-- ----------------------------
DROP TABLE IF EXISTS `beer_customers`;
CREATE TABLE `beer_customers`  (
  `Customer_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Customer_Name` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Customer_Category` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `PhoneNum` int(11) NOT NULL,
  `Customer_Address` varchar(250) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`Customer_Id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20180010 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of beer_customers
-- ----------------------------
INSERT INTO `beer_customers` VALUES (20180001, 'Hilton', 'hotel', 123456, 'Beijing');
INSERT INTO `beer_customers` VALUES (20180002, 'Zoom', 'bar', 234567, 'Beijing');
INSERT INTO `beer_customers` VALUES (20180003, 'Kempinski', 'hotel', 123457, 'Beijing');
INSERT INTO `beer_customers` VALUES (20180004, 'Party World', 'ktv', 345677, 'Nanjing');
INSERT INTO `beer_customers` VALUES (20180005, 'Yanqi', 'hotel', 999990, 'Beijing');
INSERT INTO `beer_customers` VALUES (20180006, 'Da City', 'bar', 222220, 'Changsha');
INSERT INTO `beer_customers` VALUES (20180007, 'Marriott', 'hotel', 444440, 'Xiamen');
INSERT INTO `beer_customers` VALUES (20180008, 'Bret', 'retailer', 442220, 'Guangzhou');
INSERT INTO `beer_customers` VALUES (20180009, 'ABC', 'others', 355770, 'Shanghai');
INSERT INTO `beer_customers` VALUES (20180010, 'Sedco', 'restaurant', 666770, 'Shanghai');

-- ----------------------------
-- Table structure for beer_equipments
-- ----------------------------
DROP TABLE IF EXISTS `beer_equipments`;
CREATE TABLE `beer_equipments`  (
  `Equip_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Equip_Name` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Warehouse_id` int(11) NOT NULL,
  PRIMARY KEY (`Equip_Id`) USING BTREE,
  INDEX `Beer_equipments_Warehouse_id_445477d8_fk_Beer_ware`(`Warehouse_id`) USING BTREE,
  CONSTRAINT `Beer_equipments_Warehouse_id_445477d8_fk_Beer_ware` FOREIGN KEY (`Warehouse_id`) REFERENCES `beer_warehouse` (`warehouse_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of beer_equipments
-- ----------------------------
INSERT INTO `beer_equipments` VALUES (1, 'A fermentation cylinder', 2);
INSERT INTO `beer_equipments` VALUES (2, 'B saccharifying system', 2);
INSERT INTO `beer_equipments` VALUES (3, 'C craft equipment', 2);
INSERT INTO `beer_equipments` VALUES (4, 'D fermentation system', 2);
INSERT INTO `beer_equipments` VALUES (5, 'E fermentation tank', 2);
INSERT INTO `beer_equipments` VALUES (6, 'F Saccharifying system', 8);
INSERT INTO `beer_equipments` VALUES (7, 'G fermentation system', 8);
INSERT INTO `beer_equipments` VALUES (8, 'H craft equipment', 8);
INSERT INTO `beer_equipments` VALUES (9, 'I fermentation cylinder', 8);
INSERT INTO `beer_equipments` VALUES (10, 'J Fermentation tank', 8);

-- ----------------------------
-- Table structure for beer_maintenances
-- ----------------------------
DROP TABLE IF EXISTS `beer_maintenances`;
CREATE TABLE `beer_maintenances`  (
  `Mainten_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Mainten_Date` date NOT NULL,
  `Deprecation` varchar(250) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Equip_id` int(11) NOT NULL,
  `MaintenStaff_id` int(11) NOT NULL,
  PRIMARY KEY (`Mainten_Id`) USING BTREE,
  INDEX `Beer_maintenances_Equip_id_a09009bf_fk_Beer_equipments_Equip_Id`(`Equip_id`) USING BTREE,
  INDEX `Beer_maintenances_MaintenStaff_id_f876c0a9_fk_Beer_staff_WorkNum`(`MaintenStaff_id`) USING BTREE,
  CONSTRAINT `Beer_maintenances_Equip_id_a09009bf_fk_Beer_equipments_Equip_Id` FOREIGN KEY (`Equip_id`) REFERENCES `beer_equipments` (`equip_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Beer_maintenances_MaintenStaff_id_f876c0a9_fk_Beer_staff_WorkNum` FOREIGN KEY (`MaintenStaff_id`) REFERENCES `beer_staff` (`worknum`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 201808002 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of beer_maintenances
-- ----------------------------
INSERT INTO `beer_maintenances` VALUES (201801001, '2018-01-12', 'broken', 1, 1010);
INSERT INTO `beer_maintenances` VALUES (201801002, '2018-01-26', 'deformation', 4, 1010);
INSERT INTO `beer_maintenances` VALUES (201802001, '2018-02-17', 'fell apart', 6, 1035);
INSERT INTO `beer_maintenances` VALUES (201803001, '2018-03-23', 'lack of parts', 8, 1035);
INSERT INTO `beer_maintenances` VALUES (201804001, '2018-04-06', 'broken', 2, 1010);
INSERT INTO `beer_maintenances` VALUES (201805001, '2018-05-17', 'broken', 5, 1010);
INSERT INTO `beer_maintenances` VALUES (201806001, '2018-06-22', 'deformation', 10, 1035);
INSERT INTO `beer_maintenances` VALUES (201807001, '2018-07-19', 'fell apart', 3, 1010);
INSERT INTO `beer_maintenances` VALUES (201807002, '2018-07-31', 'lack of parts', 7, 1035);
INSERT INTO `beer_maintenances` VALUES (201808001, '2018-08-18', 'fell apart', 9, 1035);
INSERT INTO `beer_maintenances` VALUES (201808002, '2018-12-23', 'A', 1, 1001);

-- ----------------------------
-- Table structure for beer_material_inventory
-- ----------------------------
DROP TABLE IF EXISTS `beer_material_inventory`;
CREATE TABLE `beer_material_inventory`  (
  `Material_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Material_Name` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Material_Category` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Material_Surplus` int(11) NOT NULL,
  `Warehouse_id` int(11) NOT NULL,
  PRIMARY KEY (`Material_Id`) USING BTREE,
  INDEX `Beer_material_invent_Warehouse_id_9877d5bc_fk_Beer_ware`(`Warehouse_id`) USING BTREE,
  CONSTRAINT `Beer_material_invent_Warehouse_id_9877d5bc_fk_Beer_ware` FOREIGN KEY (`Warehouse_id`) REFERENCES `beer_warehouse` (`warehouse_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of beer_material_inventory
-- ----------------------------
INSERT INTO `beer_material_inventory` VALUES (1, 'barley', 'main', 12000, 1);
INSERT INTO `beer_material_inventory` VALUES (2, 'Oxidation of raw water', 'main', 9000, 4);
INSERT INTO `beer_material_inventory` VALUES (3, 'maize', 'main', 7850, 4);
INSERT INTO `beer_material_inventory` VALUES (4, 'wheat', 'main', 13510, 4);
INSERT INTO `beer_material_inventory` VALUES (5, 'ferment powder', 'assisted', 9846, 9);
INSERT INTO `beer_material_inventory` VALUES (6, 'malt', 'main', 7349, 9);
INSERT INTO `beer_material_inventory` VALUES (7, 'yeast', 'assisted', 11000, 9);
INSERT INTO `beer_material_inventory` VALUES (8, 'hops', 'main', 10000, 10);
INSERT INTO `beer_material_inventory` VALUES (9, 'brewing water', 'assisted', 9500, 10);

-- ----------------------------
-- Table structure for beer_orders
-- ----------------------------
DROP TABLE IF EXISTS `beer_orders`;
CREATE TABLE `beer_orders`  (
  `Order_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Order_Date` date NOT NULL,
  `Product_Case` int(11) NOT NULL,
  `Description` varchar(250) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Delivery_Date` date NOT NULL,
  `Customer_id` int(11) NOT NULL,
  `Product_id` int(11) NOT NULL,
  `ResponsibleMan_id` int(11) NOT NULL,
  PRIMARY KEY (`Order_Id`) USING BTREE,
  INDEX `Beer_orders_Customer_id_3de727fe_fk_Beer_customers_Customer_Id`(`Customer_id`) USING BTREE,
  INDEX `Beer_orders_Product_id_8e4143c2_fk_Beer_prod`(`Product_id`) USING BTREE,
  INDEX `Beer_orders_ResponsibleMan_id_99198a67_fk_Beer_staff_WorkNum`(`ResponsibleMan_id`) USING BTREE,
  CONSTRAINT `Beer_orders_Customer_id_3de727fe_fk_Beer_customers_Customer_Id` FOREIGN KEY (`Customer_id`) REFERENCES `beer_customers` (`customer_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Beer_orders_Product_id_8e4143c2_fk_Beer_prod` FOREIGN KEY (`Product_id`) REFERENCES `beer_product_inventory` (`product_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Beer_orders_ResponsibleMan_id_99198a67_fk_Beer_staff_WorkNum` FOREIGN KEY (`ResponsibleMan_id`) REFERENCES `beer_staff` (`worknum`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 201805001 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of beer_orders
-- ----------------------------
INSERT INTO `beer_orders` VALUES (201801001, '2018-01-26', 300, '', '2018-01-28', 20180001, 1, 1001);
INSERT INTO `beer_orders` VALUES (201801002, '2018-01-30', 500, '', '2018-02-01', 20180002, 2, 1040);
INSERT INTO `beer_orders` VALUES (201802001, '2018-02-08', 200, 'pls reach at 2-6 p.m.', '2018-02-09', 20180003, 1, 1040);
INSERT INTO `beer_orders` VALUES (201802002, '2018-02-15', 150, '', '2018-02-17', 20180004, 3, 1001);
INSERT INTO `beer_orders` VALUES (201803001, '2018-03-06', 100, '', '2018-03-09', 20180005, 4, 1040);
INSERT INTO `beer_orders` VALUES (201803002, '2018-03-14', 200, '', '2018-03-16', 20180006, 2, 1042);
INSERT INTO `beer_orders` VALUES (201803003, '2018-03-20', 200, 'please sent during 8-12 a.m.', '2018-03-22', 20180001, 3, 1001);
INSERT INTO `beer_orders` VALUES (201804001, '2018-04-05', 500, '', '2018-04-06', 20180002, 4, 1040);
INSERT INTO `beer_orders` VALUES (201804002, '2018-04-15', 800, '', '2018-04-17', 20180006, 2, 1042);
INSERT INTO `beer_orders` VALUES (201805001, '2018-05-02', 400, '', '2018-05-04', 20180007, 1, 1040);

-- ----------------------------
-- Table structure for beer_procurement
-- ----------------------------
DROP TABLE IF EXISTS `beer_procurement`;
CREATE TABLE `beer_procurement`  (
  `Purchase_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Purchase_Date` date NOT NULL,
  `Purchase_Quantity` int(11) NOT NULL,
  `Material_id` int(11) NOT NULL,
  `ResponsibleStaff_id` int(11) NOT NULL,
  `Supplier_id` int(11) NOT NULL,
  PRIMARY KEY (`Purchase_Id`) USING BTREE,
  INDEX `Beer_procurement_Material_id_e72e954a_fk_Beer_mate`(`Material_id`) USING BTREE,
  INDEX `Beer_procurement_ResponsibleStaff_id_a7609861_fk_Beer_staf`(`ResponsibleStaff_id`) USING BTREE,
  INDEX `Beer_procurement_Supplier_id_24379f34_fk_Beer_supp`(`Supplier_id`) USING BTREE,
  CONSTRAINT `Beer_procurement_Material_id_e72e954a_fk_Beer_mate` FOREIGN KEY (`Material_id`) REFERENCES `beer_material_inventory` (`material_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Beer_procurement_ResponsibleStaff_id_a7609861_fk_Beer_staf` FOREIGN KEY (`ResponsibleStaff_id`) REFERENCES `beer_staff` (`worknum`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Beer_procurement_Supplier_id_24379f34_fk_Beer_supp` FOREIGN KEY (`Supplier_id`) REFERENCES `beer_suppliers` (`supplier_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 201812 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of beer_procurement
-- ----------------------------
INSERT INTO `beer_procurement` VALUES (201801, '2018-01-02', 1500, 1, 1025, 1);
INSERT INTO `beer_procurement` VALUES (201802, '2018-01-03', 2000, 2, 1035, 2);
INSERT INTO `beer_procurement` VALUES (201803, '2018-01-04', 2500, 3, 1025, 3);
INSERT INTO `beer_procurement` VALUES (201804, '2018-01-05', 5000, 4, 1035, 4);
INSERT INTO `beer_procurement` VALUES (201805, '2018-01-08', 4000, 5, 1025, 5);
INSERT INTO `beer_procurement` VALUES (201806, '2018-01-09', 2000, 6, 1035, 6);
INSERT INTO `beer_procurement` VALUES (201807, '2018-01-10', 3000, 7, 1025, 7);
INSERT INTO `beer_procurement` VALUES (201808, '2018-01-11', 3500, 8, 1035, 8);
INSERT INTO `beer_procurement` VALUES (201809, '2018-01-12', 5000, 9, 1025, 9);
INSERT INTO `beer_procurement` VALUES (201810, '2018-12-23', 50, 1, 1001, 1);
INSERT INTO `beer_procurement` VALUES (201811, '2018-12-23', 50, 1, 1001, 1);
INSERT INTO `beer_procurement` VALUES (201812, '2018-12-23', 5000, 1, 1001, 1);

-- ----------------------------
-- Table structure for beer_product_inventory
-- ----------------------------
DROP TABLE IF EXISTS `beer_product_inventory`;
CREATE TABLE `beer_product_inventory`  (
  `Product_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Pro_Category` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Surplus` int(11) NOT NULL,
  `Warehouse_id` int(11) NOT NULL,
  PRIMARY KEY (`Product_Id`) USING BTREE,
  INDEX `Beer_product_invento_Warehouse_id_d861e38a_fk_Beer_ware`(`Warehouse_id`) USING BTREE,
  CONSTRAINT `Beer_product_invento_Warehouse_id_d861e38a_fk_Beer_ware` FOREIGN KEY (`Warehouse_id`) REFERENCES `beer_warehouse` (`warehouse_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of beer_product_inventory
-- ----------------------------
INSERT INTO `beer_product_inventory` VALUES (1, 'draft beer', 2000, 3);
INSERT INTO `beer_product_inventory` VALUES (2, 'mixed beer', 1480, 5);
INSERT INTO `beer_product_inventory` VALUES (3, 'fresh beer', 3000, 6);
INSERT INTO `beer_product_inventory` VALUES (4, 'pasteurized beer', 5000, 7);

-- ----------------------------
-- Table structure for beer_production_activity
-- ----------------------------
DROP TABLE IF EXISTS `beer_production_activity`;
CREATE TABLE `beer_production_activity`  (
  `Activity_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Act_Date` date NOT NULL,
  `Act_Quantity` int(11) NOT NULL,
  `ActResponStaff_id` int(11) NOT NULL,
  `Product_id` int(11) NOT NULL,
  `Warehouse_id` int(11) NOT NULL,
  PRIMARY KEY (`Activity_Id`) USING BTREE,
  INDEX `Beer_production_acti_ActResponStaff_id_dcd2fd83_fk_Beer_staf`(`ActResponStaff_id`) USING BTREE,
  INDEX `Beer_production_acti_Product_id_b777e65f_fk_Beer_prod`(`Product_id`) USING BTREE,
  INDEX `Beer_production_acti_Warehouse_id_b60ae27a_fk_Beer_ware`(`Warehouse_id`) USING BTREE,
  CONSTRAINT `Beer_production_acti_ActResponStaff_id_dcd2fd83_fk_Beer_staf` FOREIGN KEY (`ActResponStaff_id`) REFERENCES `beer_staff` (`worknum`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Beer_production_acti_Product_id_b777e65f_fk_Beer_prod` FOREIGN KEY (`Product_id`) REFERENCES `beer_product_inventory` (`product_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Beer_production_acti_Warehouse_id_b60ae27a_fk_Beer_ware` FOREIGN KEY (`Warehouse_id`) REFERENCES `beer_warehouse` (`warehouse_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2018012 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of beer_production_activity
-- ----------------------------
INSERT INTO `beer_production_activity` VALUES (2018001, '2018-02-08', 1000, 1030, 1, 3);
INSERT INTO `beer_production_activity` VALUES (2018002, '2018-02-13', 500, 1010, 2, 5);
INSERT INTO `beer_production_activity` VALUES (2018003, '2018-02-16', 500, 1025, 3, 6);
INSERT INTO `beer_production_activity` VALUES (2018004, '2018-02-22', 1000, 1035, 4, 7);
INSERT INTO `beer_production_activity` VALUES (2018005, '2018-03-02', 1500, 1030, 1, 3);
INSERT INTO `beer_production_activity` VALUES (2018006, '2018-03-17', 600, 1010, 2, 5);
INSERT INTO `beer_production_activity` VALUES (2018007, '2018-03-21', 800, 1025, 3, 6);
INSERT INTO `beer_production_activity` VALUES (2018008, '2018-03-26', 500, 1035, 4, 7);
INSERT INTO `beer_production_activity` VALUES (2018011, '2018-12-23', 100, 1001, 1, 1);
INSERT INTO `beer_production_activity` VALUES (2018012, '2018-12-23', 1, 1001, 1, 1);

-- ----------------------------
-- Table structure for beer_staff
-- ----------------------------
DROP TABLE IF EXISTS `beer_staff`;
CREATE TABLE `beer_staff`  (
  `WorkNum` int(11) NOT NULL AUTO_INCREMENT,
  `Staff_Name` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Department` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Staff_Gender` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`WorkNum`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1042 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of beer_staff
-- ----------------------------
INSERT INTO `beer_staff` VALUES (1001, 'wedon', 'Sales&Marketing', 'Male');
INSERT INTO `beer_staff` VALUES (1003, 'jocelyn', 'Finance', 'Female');
INSERT INTO `beer_staff` VALUES (1010, 'chase', 'Quality Control', 'Female');
INSERT INTO `beer_staff` VALUES (1025, 'mike', 'Procurement', 'Male');
INSERT INTO `beer_staff` VALUES (1027, 'christina', 'Finance', 'Female');
INSERT INTO `beer_staff` VALUES (1030, 'jon', 'Quality Control', 'Male');
INSERT INTO `beer_staff` VALUES (1031, 'joseph', 'Finance', 'Male');
INSERT INTO `beer_staff` VALUES (1035, 'ian', 'Procurement', 'Male');
INSERT INTO `beer_staff` VALUES (1040, 'robert', 'Sales&Marketing', 'Male');
INSERT INTO `beer_staff` VALUES (1042, 'becky', 'Sales&Marketing', 'Female');

-- ----------------------------
-- Table structure for beer_suppliers
-- ----------------------------
DROP TABLE IF EXISTS `beer_suppliers`;
CREATE TABLE `beer_suppliers`  (
  `Supplier_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Supplier_Name` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Liaison_Name` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Liaison_Number` int(11) NOT NULL,
  `Material_id` int(11) NOT NULL,
  PRIMARY KEY (`Supplier_Id`) USING BTREE,
  INDEX `Beer_suppliers_Material_id_0578acb5_fk_Beer_mate`(`Material_id`) USING BTREE,
  CONSTRAINT `Beer_suppliers_Material_id_0578acb5_fk_Beer_mate` FOREIGN KEY (`Material_id`) REFERENCES `beer_material_inventory` (`material_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of beer_suppliers
-- ----------------------------
INSERT INTO `beer_suppliers` VALUES (1, 'ANI', 'Zhang', 13873923, 1);
INSERT INTO `beer_suppliers` VALUES (2, 'deo', 'Wang', 13888009, 2);
INSERT INTO `beer_suppliers` VALUES (3, 'sss', 'Liang', 15932740, 3);
INSERT INTO `beer_suppliers` VALUES (4, 'dfe', 'Sun', 18639209, 4);
INSERT INTO `beer_suppliers` VALUES (5, 'gr', 'Wu', 18666329, 5);
INSERT INTO `beer_suppliers` VALUES (6, 'dw', 'Liu', 18638200, 6);
INSERT INTO `beer_suppliers` VALUES (7, 'dewa', 'Zheng', 17332199, 7);
INSERT INTO `beer_suppliers` VALUES (8, 'fre', 'Xu', 13808284, 8);
INSERT INTO `beer_suppliers` VALUES (9, 'dw', 'Chen', 15136976, 9);

-- ----------------------------
-- Table structure for beer_warehouse
-- ----------------------------
DROP TABLE IF EXISTS `beer_warehouse`;
CREATE TABLE `beer_warehouse`  (
  `Warehouse_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Storage_Type` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Warehouse_Location` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `PeopleInCharge_id` int(11) NOT NULL,
  PRIMARY KEY (`Warehouse_Id`) USING BTREE,
  INDEX `Beer_warehouse_PeopleInCharge_id_e359cf84_fk_Beer_staff_WorkNum`(`PeopleInCharge_id`) USING BTREE,
  CONSTRAINT `Beer_warehouse_PeopleInCharge_id_e359cf84_fk_Beer_staff_WorkNum` FOREIGN KEY (`PeopleInCharge_id`) REFERENCES `beer_staff` (`worknum`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of beer_warehouse
-- ----------------------------
INSERT INTO `beer_warehouse` VALUES (1, 'Material', 'X area', 1001);
INSERT INTO `beer_warehouse` VALUES (2, 'Equipment', 'X area', 1010);
INSERT INTO `beer_warehouse` VALUES (3, 'Product', 'Y area', 1030);
INSERT INTO `beer_warehouse` VALUES (4, 'Material', 'Y area', 1001);
INSERT INTO `beer_warehouse` VALUES (5, 'Product', 'X area', 1010);
INSERT INTO `beer_warehouse` VALUES (6, 'Product', 'Z area', 1025);
INSERT INTO `beer_warehouse` VALUES (7, 'Product', 'Z area', 1035);
INSERT INTO `beer_warehouse` VALUES (8, 'Equipment', 'Z area', 1035);
INSERT INTO `beer_warehouse` VALUES (9, 'Material', 'Z area', 1042);
INSERT INTO `beer_warehouse` VALUES (10, 'Material', 'Z area', 1042);

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (12, 'Beer', 'administrators');
INSERT INTO `django_content_type` VALUES (9, 'Beer', 'customers');
INSERT INTO `django_content_type` VALUES (11, 'Beer', 'equipments');
INSERT INTO `django_content_type` VALUES (17, 'Beer', 'maintenances');
INSERT INTO `django_content_type` VALUES (7, 'Beer', 'material_inventory');
INSERT INTO `django_content_type` VALUES (13, 'Beer', 'orders');
INSERT INTO `django_content_type` VALUES (14, 'Beer', 'procurement');
INSERT INTO `django_content_type` VALUES (8, 'Beer', 'production_activity');
INSERT INTO `django_content_type` VALUES (10, 'Beer', 'product_inventory');
INSERT INTO `django_content_type` VALUES (16, 'Beer', 'staff');
INSERT INTO `django_content_type` VALUES (18, 'Beer', 'suppliers');
INSERT INTO `django_content_type` VALUES (15, 'Beer', 'warehouse');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'Beer', '0001_initial', '2018-12-23 04:30:04.950000');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0001_initial', '2018-12-23 04:30:05.026000');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2018-12-23 04:30:06.042000');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0001_initial', '2018-12-23 04:30:06.271000');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0002_logentry_remove_auto_add', '2018-12-23 04:30:06.284000');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2018-12-23 04:30:06.453000');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2018-12-23 04:30:06.622000');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2018-12-23 04:30:06.767000');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2018-12-23 04:30:06.781000');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2018-12-23 04:30:06.876000');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2018-12-23 04:30:06.881000');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2018-12-23 04:30:06.894000');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2018-12-23 04:30:06.996000');
INSERT INTO `django_migrations` VALUES (14, 'sessions', '0001_initial', '2018-12-23 04:30:07.068000');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

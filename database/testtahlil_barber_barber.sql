-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: testtahlil
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `barber_barber`
--

DROP TABLE IF EXISTS `barber_barber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `barber_barber` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `BarberShop` varchar(255) NOT NULL,
  `Owner` varchar(255) NOT NULL,
  `Parvaneh` varchar(10) NOT NULL,
  `phone_Number` varchar(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `rate` double NOT NULL,
  `user_id` int NOT NULL,
  `area` varchar(255) NOT NULL DEFAULT 'areax',
  `background` varchar(100) NOT NULL DEFAULT 'default_profile.png',
  `logo` varchar(100) NOT NULL DEFAULT 'default_profile.png',
  PRIMARY KEY (`id`),
  UNIQUE KEY `Parvaneh` (`Parvaneh`),
  UNIQUE KEY `phone_Number` (`phone_Number`),
  UNIQUE KEY `Barber_barber_BarberShop_db673b7d_uniq` (`BarberShop`),
  KEY `Barber_barber_user_id_70914d2d` (`user_id`),
  CONSTRAINT `Barber_barber_user_id_70914d2d_fk_Auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `barber_barber`
--

LOCK TABLES `barber_barber` WRITE;
/*!40000 ALTER TABLE `barber_barber` DISABLE KEYS */;
INSERT INTO `barber_barber` VALUES (1,'barbershop1','owner1','123','09912240419','address1',1,1,'area1','download_1.png','images_4.jpg'),(2,'barbershop2','owner2','12345','09912240404','address3',1,3,'area2','Barber/backg/download_52y0bH4.jpg','Barber/Logo/1600w-BY9c16sBnxE.webp'),(3,'barb3','owner3','3143413','09912240403','address3',1,4,'area3','Barber/backg/images_21_YpiExtA.jpg','Barber/Logo/download_1_yLD4cYe.jpg'),(4,'Ullrich-Wiegand','Hill Gummer','3436078620','4083970991','579 Acker Junction',3,7,'areax','default_profile.png','default_profile.png'),(5,'Ziemann and Sons','Brade Bowra','5189621122','8347193490','42169 Havey Place',3,8,'areax','default_profile.png','default_profile.png'),(6,'Conn LLC','Peri Tollet','9544322949','7555992001','52 International Crossing',4,9,'areax','default_profile.png','default_profile.png'),(7,'Batz-Predovic','Carlee Flescher','6081769281','9049445489','1 Declaration Park',1,10,'areax','default_profile.png','default_profile.png'),(8,'Kunze-Feest','Kristy Andreaccio','9018408487','8255323543','72623 Sunnyside Court',1.5,11,'areax','default_profile.png','default_profile.png'),(9,'Block-Turcotte','Lamar Applebee','7585340026','6132770535','5 Bluestem Park',3.5,12,'areax','default_profile.png','default_profile.png'),(10,'Crooks, Jenkins and Willms','Keeley Meas','3064981726','4783897994','59 Kennedy Lane',5,13,'areax','default_profile.png','default_profile.png'),(11,'Murazik LLC','Charmian Ropkes','1155804669','8889659610','59182 Declaration Center',4,14,'areax','default_profile.png','default_profile.png'),(12,'Graham, Schneider and Vandervort','Cathrin Duran','5127806933','7804619855','1 Hazelcrest Alley',2.8,15,'areax','default_profile.png','default_profile.png'),(13,'Hoeger and Sons','Ray Whissell','9632359734','7599238569','06 Steensland Junction',4,16,'areax','default_profile.png','default_profile.png'),(14,'Little Inc','Monica Holborn','9063448627','3923859485','3367 Burning Wood Park',4,17,'areax','default_profile.png','default_profile.png'),(15,'Stoltenberg Inc','Elwira Reddle','5928688296','6712490570','25 Cottonwood Hill',3.3,18,'areax','default_profile.png','default_profile.png'),(16,'Reilly LLC','Halie Aguilar','9841001610','7196966546','9394 Hudson Trail',3.8,19,'areax','default_profile.png','default_profile.png'),(17,'Nienow, Lowe and Veum','Bartie Barlthrop','2921442735','1662429939','90 Jackson Park',1.5,20,'areax','default_profile.png','default_profile.png'),(18,'Schaefer-Legros','Lonnard Daniells','1163072205','4177714393','7 Luster Terrace',1,21,'areax','default_profile.png','default_profile.png'),(19,'Borer, Price and Mueller','Forrest Redemile','9219221548','5513829808','4 Heffernan Drive',2,22,'areax','default_profile.png','default_profile.png'),(20,'Paucek and Sons','Finlay McGaughey','1174494826','9045055018','6 Kensington Crossing',1,23,'areax','default_profile.png','default_profile.png'),(21,'Hamill, Cronin and Macejkovic','Dunn Duffield','3112322586','5331448364','764 Swallow Lane',3.2,24,'areax','default_profile.png','default_profile.png'),(22,'Beahan-Mueller','Grenville Turgoose','4165357701','1476994163','34 Forest Dale Avenue',3,25,'areax','default_profile.png','default_profile.png'),(23,'Reichert-Robel','Hershel Lonsdale','7067563417','2344804927','07720 Shoshone Park',1,26,'areax','default_profile.png','default_profile.png'),(24,'O\'Reilly-Harvey','Klarika McLafferty','2904671601','8104140221','009 Troy Park',1,27,'areax','default_profile.png','default_profile.png'),(25,'Johns and Sons','Hilliary Cowern','1618080889','5202357679','71 Claremont Point',3,28,'areax','default_profile.png','default_profile.png'),(26,'Ernser Inc','Lissi Poley','4933370106','8766396303','3 Fieldstone Circle',4,29,'areax','default_profile.png','default_profile.png'),(27,'Hegmann-Raynor','Stearne Jaukovic','6993672968','9871536831','113 Hayes Alley',4,30,'areax','default_profile.png','default_profile.png');
/*!40000 ALTER TABLE `barber_barber` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-17 16:34:15

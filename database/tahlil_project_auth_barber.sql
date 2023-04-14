-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: tahlil_project
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
-- Table structure for table `auth_barber`
--

DROP TABLE IF EXISTS `auth_barber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_barber` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL DEFAULT '0',
  `BarberShop` varchar(255) NOT NULL,
  `Owner` varchar(255) NOT NULL,
  `Parvaneh` varchar(10) NOT NULL,
  `phone_Number` varchar(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL DEFAULT 'barb',
  PRIMARY KEY (`id`),
  UNIQUE KEY `Parvaneh` (`Parvaneh`),
  UNIQUE KEY `phone_Number` (`phone_Number`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `password` (`password`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_barber`
--

LOCK TABLES `auth_barber` WRITE;
/*!40000 ALTER TABLE `auth_barber` DISABLE KEYS */;
INSERT INTO `auth_barber` VALUES (1,NULL,0,'barb1','owner1','12345','09912240401','barb1@domain.com','address1','pbkdf2_sha256$390000$kQV9yAJbzmWI5joyKsZjmh$ULTlnbD3VMnAMccMBLUcb3t3nl4ePpfBIcIiuwZ28Hg='),(2,NULL,0,'barb2','owner2','123456','09912240402','barb2@domain.com','address2','pbkdf2_sha256$390000$WIWSqOLKkOjayBK3WsxO86$cELB6tMZQi67w0j/NEEXBK9zewA+3eLAbW2ljwsvd1s='),(3,NULL,0,'barb3','owner3','1234567','09912240403','barb3@domain.com','address3','pbkdf2_sha256$390000$vNI8Nql7kvtMM5jRL6Y2Ii$Bs1hcgAKefeYHTCegRyVcw+mwR4y87qUUPP13AIOuS4='),(4,NULL,0,'Kunde, Beier and Pacocha','Evangelin Libermore','1696727736','7603016838','elibermore3@canalblog.com','9910 Wayridge Alley','barb4'),(5,NULL,0,'Jenkins Inc','Bamby Fear','7841321583','3391328573','bfear4@mtv.com','0 Utah Alley','barb5'),(6,NULL,0,'Runolfsson, Johnson and Herzog','Bibi Gilderoy','4329137402','6051355536','bgilderoy5@nature.com','04667 Pine View Junction','barb6'),(7,NULL,0,'Ullrich-Wiegand','Hill Gummer','3436078620','4083970991','hgummer6@4shared.com','579 Acker Junction','barb7'),(8,NULL,0,'Ziemann and Sons','Brade Bowra','5189621122','8347193490','bbowra7@ycombinator.com','42169 Havey Place','barb8'),(9,NULL,0,'Conn LLC','Peri Tollet','9544322949','7555992001','ptollet8@furl.net','52 International Crossing','barb9'),(10,NULL,0,'Batz-Predovic','Carlee Flescher','6081769281','9049445489','cflescher9@trellian.com','1 Declaration Park','barb10'),(11,NULL,0,'Kunze-Feest','Kristy Andreaccio','9018408487','8255323543','kandreaccioa@lycos.com','72623 Sunnyside Court','barb11'),(12,NULL,0,'Block-Turcotte','Lamar Applebee','7585340026','6132770535','lapplebeeb@fastcompany.com','5 Bluestem Park','barb12'),(13,NULL,0,'Crooks, Jenkins and Willms','Keeley Meas','3064981726','4783897994','kmeasc@ox.ac.uk','59 Kennedy Lane','barb13'),(14,NULL,0,'Murazik LLC','Charmian Ropkes','1155804669','8889659610','cropkesd@canalblog.com','59182 Declaration Center','barb14'),(15,NULL,0,'Graham, Schneider and Vandervort','Cathrin Duran','5127806933','7804619855','cdurane@histats.com','1 Hazelcrest Alley','barb15'),(16,NULL,0,'Hoeger and Sons','Ray Whissell','9632359734','7599238569','rwhissellf@github.io','06 Steensland Junction','barb16'),(17,NULL,0,'Little Inc','Monica Holborn','9063448627','3923859485','mholborng@yellowpages.com','3367 Burning Wood Park','barb17'),(18,NULL,0,'Stoltenberg Inc','Elwira Reddle','5928688296','6712490570','ereddleh@google.com.br','25 Cottonwood Hill','barb18'),(19,NULL,0,'Reilly LLC','Halie Aguilar','9841001610','7196966546','haguilari@github.io','9394 Hudson Trail','barb19'),(20,NULL,0,'Nienow, Lowe and Veum','Bartie Barlthrop','2921442735','1662429939','bbarlthropj@simplemachines.org','90 Jackson Park','barb20'),(21,NULL,0,'Schaefer-Legros','Lonnard Daniells','1163072205','4177714393','ldaniellsk@tiny.cc','7 Luster Terrace','barb21'),(22,NULL,0,'Borer, Price and Mueller','Forrest Redemile','9219221548','5513829808','fredemilel@google.pl','4 Heffernan Drive','barb22'),(23,NULL,0,'Paucek and Sons','Finlay McGaughey','1174494826','9045055018','fmcgaugheym@bbc.co.uk','6 Kensington Crossing','barb23'),(24,NULL,0,'Hamill, Cronin and Macejkovic','Dunn Duffield','3112322586','5331448364','dduffieldn@sphinn.com','764 Swallow Lane','barb24'),(25,NULL,0,'Beahan-Mueller','Grenville Turgoose','4165357701','1476994163','gturgooseo@virginia.edu','34 Forest Dale Avenue','barb25'),(26,NULL,0,'Reichert-Robel','Hershel Lonsdale','7067563417','2344804927','hlonsdalep@unicef.org','07720 Shoshone Park','barb26'),(27,NULL,0,'O\'Reilly-Harvey','Klarika McLafferty','2904671601','8104140221','kmclaffertyq@hugedomains.com','009 Troy Park','barb27'),(28,NULL,0,'Johns and Sons','Hilliary Cowern','1618080889','5202357679','hcowernr@ucla.edu','71 Claremont Point','barb28'),(29,NULL,0,'Ernser Inc','Lissi Poley','4933370106','8766396303','lpoleys@ucsd.edu','3 Fieldstone Circle','barb29'),(30,NULL,0,'Hegmann-Raynor','Stearne Jaukovic','6993672968','9871536831','sjaukovict@topsy.com','113 Hayes Alley','barb30');
/*!40000 ALTER TABLE `auth_barber` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-10 23:39:47

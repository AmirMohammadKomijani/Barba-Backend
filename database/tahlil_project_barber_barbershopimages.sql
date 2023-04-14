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
-- Table structure for table `barber_barbershopimages`
--

DROP TABLE IF EXISTS `barber_barbershopimages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `barber_barbershopimages` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `background` varchar(100) NOT NULL,
  `logo` varchar(100) NOT NULL,
  `barbershop_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Barber_barbershopima_barbershop_id_8f429589_fk_Barber_ba` (`barbershop_id`),
  CONSTRAINT `Barber_barbershopima_barbershop_id_8f429589_fk_Barber_ba` FOREIGN KEY (`barbershop_id`) REFERENCES `barber_barber` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `barber_barbershopimages`
--

LOCK TABLES `barber_barbershopimages` WRITE;
/*!40000 ALTER TABLE `barber_barbershopimages` DISABLE KEYS */;
INSERT INTO `barber_barbershopimages` VALUES (1,'Barber/backg/BarberShop_eMBvoyV.jpg','Barber/Logo/images_4_uZzyCTj.jpg',1),(6,'Barber/backg/download_1mFadMJ.jpg','Barber/Logo/images_5.jpg',2),(7,'Barber/backg/BarberShop_fouRLwp.jpg','Barber/Logo/images_2.jpg',3),(8,'Barber/backg/images_1_KdxheQz.jpg','Barber/Logo/images_HSpBODO.png',4),(9,'Barber/backg/images_2.jpg','Barber/Logo/images_1.jpg',5),(10,'Barber/backg/images_7.jpg','Barber/Logo/images_86OWvAK.png',6),(12,'Barber/backg/images_8.jpg','Barber/Logo/download_1_dVpBzhr.png',7),(13,'Barber/backg/images_9.jpg','Barber/Logo/images_1.png',8),(14,'Barber/backg/images_12.jpg','Barber/Logo/images_3.jpg',9),(15,'Barber/backg/images_13.jpg','Barber/Logo/images_2.png',10),(16,'Barber/backg/images_11.jpg','Barber/Logo/images_4_AAx7sg5.jpg',11),(17,'Barber/backg/images_14.jpg','Barber/Logo/download.png',12),(18,'Barber/backg/images_1_y1ysvph.jpg','Barber/Logo/images_5_6rofT7l.jpg',13),(19,'Barber/backg/images_9_wZTKea0.jpg','Barber/Logo/images_nWAUI1n.png',14),(20,'Barber/backg/images_zBaNnOy.jpg','Barber/Logo/images_18.jpg',15),(21,'Barber/backg/images_13_awlCiUu.jpg','Barber/Logo/images_6.jpg',16),(22,'Barber/backg/images_1_GU4DvoA.jpg','Barber/Logo/images_8hMA7bg.png',17),(23,'Barber/backg/images_16.jpg','Barber/Logo/images_NMXzZx8.png',18),(24,'Barber/backg/images_5.png','Barber/Logo/images_18_dBJXtOv.jpg',19),(25,'Barber/backg/images_15.jpg','Barber/Logo/images_3.png',20),(26,'Barber/backg/images_9_DNCZVMv.jpg','Barber/Logo/download_kibvlWm.png',21),(27,'Barber/backg/images_1_kYz1fjc.jpg','Barber/Logo/images_18_OFhY2nu.jpg',22),(28,'Barber/backg/images_14_D8DW2MR.jpg','Barber/Logo/download_1_BMdn360.png',23),(29,'Barber/backg/images_10_bLET5IZ.jpg','Barber/Logo/images_4.png',24),(30,'Barber/backg/images_3.jpg','Barber/Logo/images_7.png',25),(31,'Barber/backg/images_10.png','Barber/Logo/images_23.jpg',26),(32,'Barber/backg/images_20.jpg','Barber/Logo/images_22.jpg',27),(33,'Barber/backg/images_21.jpg','Barber/Logo/images_8.png',28),(34,'Barber/backg/images_19.jpg','Barber/Logo/images_4_Yafru25.jpg',29),(35,'Barber/backg/images_16_LKN6fYI.jpg','Barber/Logo/images_15.jpg',30);
/*!40000 ALTER TABLE `barber_barbershopimages` ENABLE KEYS */;
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

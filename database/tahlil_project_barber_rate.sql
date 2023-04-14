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
-- Table structure for table `barber_rate`
--

DROP TABLE IF EXISTS `barber_rate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `barber_rate` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `stars` int NOT NULL,
  `barbershop_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Barber_rate_barbershop_id_84e7ca9f_fk_Barber_barber_id` (`barbershop_id`),
  CONSTRAINT `Barber_rate_barbershop_id_84e7ca9f_fk_Barber_barber_id` FOREIGN KEY (`barbershop_id`) REFERENCES `barber_barber` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `barber_rate`
--

LOCK TABLES `barber_rate` WRITE;
/*!40000 ALTER TABLE `barber_rate` DISABLE KEYS */;
INSERT INTO `barber_rate` VALUES (1,2,1),(2,4,3),(3,5,2),(4,4,1),(5,2,3),(6,3,2),(7,5,1),(8,2,2),(9,3,3),(10,4,1),(11,5,18),(12,1,8),(13,4,9),(14,3,15),(15,1,8),(18,4,15),(19,4,24),(20,2,19),(21,4,15),(23,4,17),(24,5,30),(25,2,28),(26,3,30),(27,5,8),(30,2,11),(31,3,25),(35,1,11),(36,5,24),(37,4,4),(38,2,3),(40,3,4),(41,5,1),(42,4,5),(44,4,5),(47,2,15),(48,5,19),(49,5,29),(50,2,16),(51,5,8),(53,1,24),(56,1,23),(57,1,6),(58,4,14),(59,1,15),(61,1,24),(62,3,6),(64,2,22),(67,1,18),(69,4,28),(71,3,7),(74,2,1),(75,5,13),(77,2,12),(78,1,20),(79,5,19),(80,3,19),(82,5,12),(83,5,24),(84,5,16),(85,2,20),(86,3,29),(87,5,6),(88,5,16),(89,1,21),(90,4,18);
/*!40000 ALTER TABLE `barber_rate` ENABLE KEYS */;
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

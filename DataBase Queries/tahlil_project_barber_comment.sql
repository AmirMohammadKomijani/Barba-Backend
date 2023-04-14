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
-- Table structure for table `barber_comment`
--

DROP TABLE IF EXISTS `barber_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `barber_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `body` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `barber_id` bigint NOT NULL,
  `customer_id` bigint NOT NULL,
  `parent_comment_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Barber_comment_barber_id_935d8dea_fk_Auth_barber_id` (`barber_id`),
  KEY `Barber_comment_customer_id_d1c9240b_fk_Auth_customer_id` (`customer_id`),
  KEY `Barber_comment_parent_comment_id_8a180bc5_fk_Barber_comment_id` (`parent_comment_id`),
  CONSTRAINT `Barber_comment_barber_id_935d8dea_fk_Auth_barber_id` FOREIGN KEY (`barber_id`) REFERENCES `auth_barber` (`id`),
  CONSTRAINT `Barber_comment_customer_id_d1c9240b_fk_Auth_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `auth_customer` (`id`),
  CONSTRAINT `Barber_comment_parent_comment_id_8a180bc5_fk_Barber_comment_id` FOREIGN KEY (`parent_comment_id`) REFERENCES `barber_comment` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `barber_comment`
--

LOCK TABLES `barber_comment` WRITE;
/*!40000 ALTER TABLE `barber_comment` DISABLE KEYS */;
INSERT INTO `barber_comment` VALUES (1,'avalin commente man','2023-04-09 15:21:55.319853',1,1,NULL),(2,'dovomin commente man','2023-04-09 15:22:39.404131',3,1,NULL),(3,'3rd cmnt','2023-04-09 15:24:29.298822',1,1,NULL),(4,'dfa fa f s df asdf','2023-04-09 18:55:47.499907',2,2,2),(5,'dassadasdasd','2023-04-10 12:59:11.141938',1,1,NULL),(6,'dassadasdasd','2023-04-10 13:47:28.174909',1,1,NULL),(7,'dassadasdasd','2023-04-10 13:55:40.457136',1,1,NULL),(8,'dassadasdasd','2023-04-10 13:56:39.790141',1,1,NULL),(9,'dassadasdasd','2023-04-10 13:56:56.588184',3,1,6),(10,'wtf','2023-04-10 14:13:15.313057',2,2,NULL),(11,'wtf2','2023-04-10 14:13:33.979294',2,1,1);
/*!40000 ALTER TABLE `barber_comment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-11 11:27:59

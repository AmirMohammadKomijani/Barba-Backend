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
-- Table structure for table `auth_customer`
--

DROP TABLE IF EXISTS `auth_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_customer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `phone_Number` varchar(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `password` varchar(255) NOT NULL,
  `profile_picture` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone_Number` (`phone_Number`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `password` (`password`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_customer`
--

LOCK TABLES `auth_customer` WRITE;
/*!40000 ALTER TABLE `auth_customer` DISABLE KEYS */;
INSERT INTO `auth_customer` VALUES (1,NULL,0,'ZZZZZ','ZZZZZZZZZZ','09123456111','aa@aa.aabz','M','pbkdf2_sha256$600000$uer0Queixf48jHamQprVIX$22gThV2JXpvoeYF5SEQnTCT+LCHE6B4yaJGXwEYlydE=','profile_pictures/1600w-BY9c16sBnxE.webp'),(2,NULL,0,'kkkkkkkkk','kkkkkkkkkkkk','0912345688','aa@aa.aa','M','pbkdf2_sha256$600000$ahM44y9uL1h8KqEnMhM8At$wHZs4utPV9xRiDCdOmMz2KgYkOYh76gZAr5hAN5+LOU=','/default_profile.png'),(3,NULL,0,'ppppppppppp','pppppppppp','0912555','pp@pp.pp','M','pbkdf2_sha256$390000$NfcwtBLm65r9AyR8J4faE9$sKi+J5lNwOkppTqFtRwSlxDfdygUchfVODjY9AUE/GA=','/default_profile.png');
/*!40000 ALTER TABLE `auth_customer` ENABLE KEYS */;
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

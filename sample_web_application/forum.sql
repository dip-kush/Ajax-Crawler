-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 17, 2015 at 04:06 PM
-- Server version: 5.6.16
-- PHP Version: 5.5.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `forum`
--

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `feedback` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=146 ;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`id`, `name`, `feedback`) VALUES
(25, 'vishal', ' hello'),
(26, 'vishal', ' hello'),
(27, 'vishal', ' hello'),
(28, 'vishal', ' hello'),
(29, 'vishal', ' hello'),
(30, 'vishal', ' hello'),
(31, 'vishal', ' hello'),
(32, 'vishal', ' hello'),
(33, 'vishal', ' hello'),
(34, 'vishal', ' hello'),
(35, 'vishal', ' hello'),
(36, 'vishal', ' hello'),
(37, 'vishal', ' hello'),
(38, 'vishal', ' hello'),
(39, 'vishal', ' hello'),
(40, 'vishal', ' hello'),
(41, 'vishal', ' hello'),
(42, 'vishal', ' hello'),
(43, 'vishal', ' hello'),
(44, 'vishal', ' hello'),
(45, 'vishal', ' hello'),
(46, 'vishal', ' hello'),
(47, 'vishal', ' hello'),
(48, 'vishal', ' hello'),
(49, 'vishal', ' hello'),
(50, 'vishal', ' hello'),
(51, 'vishal', ' hello'),
(52, 'vishal', ' hello'),
(53, 'vishal', ' hello'),
(54, 'vishal', ' hello'),
(55, 'vishal', ' hello'),
(56, 'fd', ' '),
(57, 'vishal', ' hello'),
(58, 'vishal', ' hello'),
(59, 'vishal', ' hello'),
(60, 'vishal', ' hello'),
(61, 'vishal', ' hello'),
(62, 'vishal', ' hello'),
(63, 'vishal', ' hello'),
(64, 'vishal', ' hello'),
(65, 'vishal', ' hello'),
(66, 'vishal', ' hello'),
(67, 'vishal', ' hello'),
(68, 'vishal', ' hello'),
(69, 'vishal', ' hello'),
(70, 'vishal', ' hello'),
(71, 'vishal', ' hello'),
(72, 'vishal', ' hello'),
(73, 'vishal', ' hello'),
(74, 'vishal', ' hello'),
(75, 'vishal', ' hello'),
(76, 'vishal', ' hello'),
(77, 'vishal', ' hello'),
(78, 'vishal', ' hello'),
(79, 'vishal', ' hello'),
(80, 'vishal', ' hello'),
(81, 'vishal', ' hello'),
(82, 'vishal', ' hello'),
(83, 'vishal', ' hello'),
(84, 'vishalvishal', ' hellohello'),
(85, 'vishal', ' hello'),
(86, 'vishal', ' hello'),
(87, 'vishal', ' hello'),
(88, 'vishal', ' hello'),
(89, 'vishal', ' hello'),
(90, 'vishal', ' hello'),
(91, 'vishal', ' hello'),
(92, 'vishal', ' hello'),
(93, 'vishal', ' hello'),
(94, 'vishal', ' hello'),
(95, 'vishal', ' hello'),
(96, 'vishal', ' hello'),
(97, 'vishal', ' hello'),
(98, 'fdf', ' fdf'),
(99, 'vishal', ' hello'),
(100, 'vishal', ' hello'),
(101, 'vishal', ' hello'),
(102, 'vishal', ' hello'),
(103, 'vishal', ' hello'),
(104, 'vishal', ' hello'),
(105, 'vishal', ' hello'),
(106, 'vishal', ' hello'),
(107, 'vishal', ' hello'),
(108, 'vishal', ' hello'),
(109, 'vishal', ' hello'),
(110, 'vishal', ' hello'),
(111, 'vishal', ' hello'),
(112, 'vishal', ' hello'),
(113, 'fdf', 'fdf '),
(114, 'vishal', ' hello'),
(115, 'vishal', ' hello'),
(116, 'vishal', ' hello'),
(117, 'vishal', ' hello'),
(118, 'vishal', ' hello'),
(119, 'vishal', ' hello'),
(120, 'vishal', ' hello'),
(121, 'vishal', ' hello'),
(122, 'vishal', ' hello'),
(123, 'vishal', ' hello'),
(124, 'vishal', ' hello'),
(125, 'vishal', ' hello'),
(126, 'vishal', ' hello'),
(127, 'vishal', ' hello'),
(128, 'vishal', ' hello'),
(129, 'vishal', ' hello'),
(130, 'vishal', ' hello'),
(131, 'vishal', ' hello'),
(132, 'vishal', ' hello'),
(133, 'vishal', ' hello'),
(134, 'vishal', ' hello'),
(135, 'vishal', ' hello'),
(136, 'vishal', ' hello'),
(137, 'vishal', ' hello'),
(138, 'vishal', ' hello'),
(139, 'vishal', ' hello'),
(140, 'vishal', ' hello'),
(141, 'vishal', ' hello'),
(142, 'vishal', ' hello'),
(143, 'vishal', 'somehtin\r\n '),
(144, 'anythin', 'antyi '),
(145, 'vishal', ' hello');

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE IF NOT EXISTS `members` (
  `Memberid` int(10) NOT NULL AUTO_INCREMENT,
  `Username` varchar(20) NOT NULL,
  `Email` varchar(20) NOT NULL,
  `Password` varchar(10) NOT NULL,
  `Activation` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`Memberid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`Memberid`, `Username`, `Email`, `Password`, `Activation`) VALUES
(21, 'dipkush', 'dip.kush', 'dkool', NULL),
(22, 'Vinay Sharma', 'vinaysharma@gmail', 'vinaykool', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `submit`
--

CREATE TABLE IF NOT EXISTS `submit` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=117 ;

--
-- Dumping data for table `submit`
--

INSERT INTO `submit` (`id`, `name`) VALUES
(9, 'vishal'),
(10, 'vishal'),
(11, 'vishal'),
(12, 'vishal'),
(13, 'vishal'),
(14, 'vishal'),
(15, 'vishal'),
(16, 'vishal'),
(17, 'vishal'),
(18, 'vishal'),
(19, 'vishal'),
(20, 'vishal'),
(21, 'vishal'),
(22, 'vishal'),
(23, 'vishal'),
(24, 'vishal'),
(25, 'vishal'),
(26, 'vishal'),
(27, 'vishal'),
(28, 'vishal'),
(29, 'vishal'),
(30, 'vishal'),
(31, 'vishal'),
(32, 'vishal'),
(33, 'vishal'),
(34, 'vishal'),
(35, 'vishal'),
(36, 'vishal'),
(37, 'vishal'),
(38, 'vishal'),
(39, 'vishal'),
(40, 'vishal'),
(41, 'vishal'),
(42, 'vishal'),
(43, 'vishal'),
(44, 'vishal'),
(45, 'vishal'),
(46, 'vishal'),
(47, 'vishal'),
(48, 'vishal'),
(49, 'vishal'),
(50, 'vishal'),
(51, 'vishal'),
(52, 'vishal'),
(53, 'vishal'),
(54, 'vishal'),
(55, 'vishal'),
(56, 'vishal'),
(57, 'vishal'),
(58, 'vishal'),
(59, 'fdf'),
(60, 'vishal'),
(61, 'vishal'),
(62, 'vishal'),
(63, 'vishal'),
(64, 'vishal'),
(65, 'vishal'),
(66, 'vishal'),
(67, 'vishal'),
(68, 'vishal'),
(69, 'vishal'),
(70, 'vishal'),
(71, 'vishal'),
(72, 'vishal'),
(73, 'vishal'),
(74, 'vishal'),
(75, 'fd'),
(76, 'vishal'),
(77, 'vishal'),
(78, 'vishal'),
(79, 'vishal'),
(80, 'vishal'),
(81, 'vishal'),
(82, 'vishal'),
(83, 'vishal'),
(84, 'fdf'),
(85, 'fd'),
(86, 'vishal'),
(87, 'vishal'),
(88, 'vishal'),
(89, 'vishal'),
(90, 'vishal'),
(91, 'vishal'),
(92, 'vishal'),
(93, 'vishal'),
(94, 'vishal'),
(95, 'vishal'),
(96, 'vishal'),
(97, 'vishal'),
(98, 'vishal'),
(99, 'vishal'),
(100, 'vishal'),
(101, 'vishal'),
(102, 'vishal'),
(103, 'vishal'),
(104, 'vishal'),
(105, 'vishal'),
(106, 'vishal'),
(107, 'vishal'),
(108, 'vishal'),
(109, 'vishal'),
(110, 'vishal'),
(111, 'vishal'),
(112, 'vishal'),
(113, 'vishal'),
(114, 'anythin'),
(115, 'dfdd'),
(116, 'vishal');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

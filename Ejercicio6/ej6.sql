-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema ejercicio6
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ejercicio6
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ejercicio6` DEFAULT CHARACTER SET utf8 ;
USE `ejercicio6` ;

-- -----------------------------------------------------
-- Table `ejercicio6`.`region`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ejercicio6`.`region` (
  `region_id` INT NOT NULL,
  `nombre` VARCHAR(300) NOT NULL,
  PRIMARY KEY (`region_id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ejercicio6`.`pais`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ejercicio6`.`comuna` (
  `comuna_id` INT NOT NULL,
  `region_id` INT NOT NULL,
  `nombre` VARCHAR(300) NOT NULL,
  `latitud` VARCHAR(300) NOT NULL,
  `longitud` VARCHAR(300) NOT NULL,
  PRIMARY KEY (`comuna_id`))
ENGINE = InnoDB;



-- -----------------------------------------------------
-- Data for table `ejercicio6`.`region`
-- -----------------------------------------------------
START TRANSACTION;
USE `ejercicio6`;
INSERT INTO region(region_id,nombre) VALUES (1,'Arica y Parinacota');
INSERT INTO region(region_id,nombre) VALUES (2,'Tarapacá');
INSERT INTO region(region_id,nombre) VALUES (3,'Antofagasta');
INSERT INTO region(region_id,nombre) VALUES (4,'Atacama');
INSERT INTO region(region_id,nombre) VALUES (5,'Coquimbo');
INSERT INTO region(region_id,nombre) VALUES (6,'Valparaiso');
INSERT INTO region(region_id,nombre) VALUES (7,'Metropolitana de Santiago');
INSERT INTO region(region_id,nombre) VALUES (8,'Libertador General Bernardo O''Higgins');
INSERT INTO region(region_id,nombre) VALUES (9,'Maule');
INSERT INTO region(region_id,nombre) VALUES (10,'Biobío');
INSERT INTO region(region_id,nombre) VALUES (11,'La Araucanía');
INSERT INTO region(region_id,nombre) VALUES (12,'Los Ríos');
INSERT INTO region(region_id,nombre) VALUES (13,'Los Lagos');
INSERT INTO region(region_id,nombre) VALUES (14,'Aisén del General Carlos Ibáñez del Campo');
INSERT INTO region(region_id,nombre) VALUES (15,'Magallanes y de la Antártica Chilena');

COMMIT;


-- -----------------------------------------------------
-- Data for table `ejercicio6`.`espacio_encargo`
-- -----------------------------------------------------
START TRANSACTION;
USE `ejercicio6`;
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (1,1,'Arica',-18.4707,-70.2945);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (2,1,'Camarones',-18.9191,-69.4532);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (3,1,'General Lagos',-17.7863,-69.5452);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (4,1,'Putre',-18.2052,-69.4946);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (5,2,'Alto Hospicio',-20.2418,-70.0762);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (6,2,'Iquique',-20.2474,-70.1187);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (7,2,'Camiña',-19.2855,-69.4074);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (8,2,'Colchane',-19.3585,-68.7207);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (9,2,'Huara',-19.9617,-69.8691);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (10,2,'Pica',-20.489,-69.3225);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (11,2,'Pozo Almonte',-20.2791,-69.7609);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (12,3,'Antofagasta',-23.6279,-70.3884);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (13,3,'Mejillones',-23.0918,-70.4713);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (14,3,'Sierra Gorda',-22.8964,-69.22);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (15,3,'Taltal',-25.3617,-70.466);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (16,3,'Calama',-22.4692,-68.8974);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (17,3,'Ollague',-21.1947,-68.2992);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (18,3,'San Pedro de Atacama',-22.9085,-68.1356);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (19,3,'María Elena',-22.3501,-69.6565);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (20,3,'Tocopilla',-22.0871,-70.1924);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (21,4,'Chañaral',-26.3588,-70.5793);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (22,4,'Diego de Almagro',-26.3699,-69.9809);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (23,4,'Caldera',-27.0715,-70.817);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (24,4,'Copiapó',-27.3785,-70.3159);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (25,4,'Tierra Amarilla',-27.5673,-70.2154);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (26,4,'Alto del Carmen',-28.8183,-70.3968);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (27,4,'Freirina',-28.5618,-71.0896);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (28,4,'Huasco',-28.4665,-71.2216);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (29,4,'Vallenar',-28.6113,-70.7266);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (30,5,'Canela',-31.4502,-71.5606);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (31,5,'Illapel',-31.5777,-71.1642);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (32,5,'Los Vilos',-31.9172,-71.5014);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (33,5,'Salamanca',-31.8024,-70.9259);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (34,5,'Andacollo',-30.2274,-71.0571);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (35,5,'Coquimbo',-29.9737,-71.3156);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (36,5,'La Higuera',-28.9939,-70.379);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (37,5,'La Serena',-29.9063,-71.2346);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (39,5,'Vicuña',-30.0258,-70.695);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (40,5,'Combarbalá',-31.1422,-71.0127);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (41,5,'Monte Patria',-30.7177,-70.9729);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (42,5,'Ovalle',-30.5999,-71.1941);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (43,5,'Punitaqui',-30.8355,-71.2746);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (44,5,'Río Hurtado',-30.3834,-70.8295);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (45,6,'Isla de Pascua',-27.156,-109.435);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (46,6,'Calle Larga',-32.8599,-70.6264);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (47,6,'Los Andes',-32.8261,-70.6012);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (48,6,'Rinconada',-35.4499,-72.2658);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (49,6,'San Esteban',-35.8673,-72.4348);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (50,6,'La Ligua',-32.4551,-71.2428);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (51,6,'Papudo',-32.5037,-71.4328);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (52,6,'Petorca',-32.2454,-70.9183);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (53,6,'Zapallar',-32.556,-71.4466);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (54,6,'Hijuelas',-32.8213,-71.1259);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (55,6,'La Calera',-32.7862,-71.2009);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (56,6,'La Cruz',-32.8339,-71.23);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (57,6,'Limache',-33.0043,-71.2566);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (58,6,'Nogales',-32.7097,-71.2118);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (59,6,'Olmué',-33.0038,-71.162);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (60,6,'Quillota',-32.8849,-71.2536);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (61,6,'Algarrobo',-33.3665,-71.6665);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (62,6,'Cartagena',-33.5402,-71.5987);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (63,6,'El Quisco',-33.4086,-71.6865);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (64,6,'El Tabo',-33.4662,-71.6414);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (65,6,'San Antonio',-33.5789,-71.5974);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (66,6,'Santo Domingo',-33.6645,-71.626);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (67,6,'Catemu',-32.7704,-70.9572);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (68,6,'Llaillay',-32.8163,-70.952);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (69,6,'Panquehue',-32.7742,-70.8377);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (70,6,'Putaendo',-32.6256,-70.715);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (71,6,'San Felipe',-32.7462,-70.7065);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (72,6,'Santa María',-37.825,-73.1947);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (73,6,'Casablanca',-33.3072,-71.409);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (74,6,'Concón',-32.9299,-71.521);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (75,6,'Juan Fernández',-33.6364,-78.8318);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (76,6,'Puchuncaví',-32.7216,-71.3796);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (77,6,'Quilpué',-33.0491,-71.438);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (78,6,'Quintero',-32.7888,-71.5244);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (79,6,'Valparaíso',-33.0547,-71.6157);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (80,6,'Villa Alemana',-33.0478,-71.3687);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (82,7,'Colina',-33.2102,-70.6692);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (83,7,'Lampa',-33.2883,-70.872);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (84,7,'Tiltil',-33.0806,-70.9243);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (85,7,'Pirque',-33.6692,-70.5684);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (86,7,'Puente Alto',-33.5869,-70.5671);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (87,7,'San José de Maipo',-33.6404,-70.3314);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (88,7,'Buin',-33.7303,-70.7464);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (89,7,'Calera de Tango',-33.6221,-70.783);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (90,7,'Paine',-33.8234,-70.7343);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (91,7,'San Bernardo',-33.5695,-70.7376);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (92,7,'Alhué',-34.0383,-71.1112);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (93,7,'Curacaví',-33.4067,-71.1284);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (94,7,'María Pinto',-33.5327,-71.1342);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (95,7,'Melipilla',-33.6886,-71.2139);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (96,7,'San Pedro',-33.9497,-71.433);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (97,7,'Cerrillos',-33.4978,-70.7164);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (98,7,'Cerro Navia',-33.4232,-70.7403);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (99,7,'Conchalí',-33.3837,-70.6749);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (100,7,'El Bosque',-33.5657,-70.6728);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (101,7,'Estación Central',-33.466,-70.7034);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (102,7,'Huechuraba',-33.3655,-70.6505);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (103,7,'Independencia',-33.4137,-70.6658);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (104,7,'La Cisterna',-33.5257,-70.6606);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (105,7,'La Granja',-33.5361,-70.6239);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (106,7,'La Florida',-33.5363,-70.5822);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (107,7,'La Pintana',-33.5659,-70.6321);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (108,7,'La Reina',-33.449,-70.5503);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (109,7,'Las Condes',-33.4119,-70.5685);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (110,7,'Lo Barnechea',-33.3534,-70.5086);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (111,7,'Lo Espejo',-33.5171,-70.6901);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (112,7,'Lo Prado',-33.4257,-70.7501);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (113,7,'Macul',-33.4895,-70.5968);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (114,7,'Maipú',-33.5114,-70.7696);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (115,7,'Ñuñoa',-33.4506,-70.5907);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (116,7,'Pedro Aguirre Cerda',-33.4931,-70.6761);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (117,7,'Peñalolén',-33.4841,-70.5573);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (118,7,'Providencia',-33.434,-70.6105);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (119,7,'Pudahuel',-33.4458,-70.7653);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (120,7,'Quilicura',-33.3612,-70.7319);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (121,7,'Quinta Normal',-33.4246,-70.7019);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (122,7,'Recoleta',-33.3974,-70.6431);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (123,7,'Renca',-33.4034,-70.7213);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (124,7,'San Miguel',-33.5007,-70.6514);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (125,7,'San Joaquín',-33.4975,-70.6287);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (126,7,'San Ramón',-33.4274,-70.4843);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (127,7,'Santiago',-33.4624,-70.6491);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (128,7,'Vitacura',-33.3867,-70.5688);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (129,7,'El Monte',-33.6936,-71.0118);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (130,7,'Isla de Maipo',-33.7509,-70.8983);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (131,7,'Padre Hurtado',-33.5719,-70.8068);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (132,7,'Peñaflor',-33.5985,-70.8734);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (133,7,'Talagante',-33.6844,-70.9248);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (134,8,'Codegua',-34.0561,-70.6633);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (135,8,'Coínco',-34.2682,-70.955);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (136,8,'Coltauco',-34.3107,-71.0988);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (137,8,'Doñihue',-34.226,-70.9633);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (138,8,'Graneros',-34.0373,-70.7034);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (139,8,'Las Cabras',-34.2675,-71.3166);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (140,8,'Machalí',-34.1817,-70.6521);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (141,8,'Malloa',-34.4487,-70.9271);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (142,8,'Mostazal',-33.9779,-70.6874);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (143,8,'Olivar',-34.2079,-70.7885);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (144,8,'Peumo',-36.5738,-72.3381);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (145,8,'Pichidegua',-34.3693,-71.302);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (146,8,'Quinta de Tilcoco',-34.3547,-70.9791);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (147,8,'Rancagua',-34.1732,-70.731);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (148,8,'Rengo',-34.4108,-70.8639);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (149,8,'Requínoa',-34.2762,-70.808);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (150,8,'San Vicente de Tagua Tagua',-34.442,-71.0778);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (151,8,'La Estrella',-34.1971,-71.6678);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (152,8,'Litueche',-34.1011,-71.7094);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (153,8,'Marchihue',-34.3923,-71.626);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (154,8,'Navidad',-33.9829,-71.822);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (156,8,'Pichilemu',-34.3922,-71.9999);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (157,8,'Chépica',-30.9969,-70.8342);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (158,8,'Chimbarongo',-34.7088,-71.0398);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (159,8,'Lolol',-34.7361,-71.5889);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (160,8,'Nancagua',-34.6518,-71.1991);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (161,8,'Palmilla',-34.5441,-71.3676);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (162,8,'Peralillo',-34.4516,-71.5318);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (163,8,'Placilla',-26.1221,-70.2201);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (164,8,'Pumanque',-34.6226,-71.662);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (165,8,'San Fernando',-34.5829,-70.9926);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (166,8,'Santa Cruz',-34.6494,-71.375);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (167,9,'Cauquenes',-35.9802,-72.327);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (168,9,'Chanco',-35.7154,-72.5123);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (169,9,'Pelluhue',-35.856,-72.6031);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (170,9,'Curicó',-34.9878,-71.2281);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (171,9,'Hualañé',-34.9665,-71.8113);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (172,9,'Licantén',-34.9947,-72.0278);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (173,9,'Molina',-35.1037,-71.2808);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (174,9,'Rauco',-34.9299,-71.3878);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (175,9,'Romeral',-34.9631,-71.0961);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (176,9,'Sagrada Familia',-35.04,-71.4083);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (177,9,'Teno',-34.8715,-71.1527);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (178,9,'Vichuquén',-34.9012,-71.9943);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (179,9,'Colbún',-35.7263,-71.4156);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (180,9,'Linares',-35.8499,-71.5848);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (181,9,'Longaví',-35.9783,-71.6977);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (182,9,'Parral',-36.135,-71.8278);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (183,9,'Retiro',-36.0426,-71.7794);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (184,9,'San Javier',-35.6158,-71.7312);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (185,9,'Villa Alegre',-37.37,-73.5054);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (186,9,'Yerbas Buenas',-29.5223,-71.2211);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (187,9,'Constitución',-35.3427,-72.3978);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (188,9,'Curepto',-35.1066,-71.9943);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (189,9,'Empedrado',-35.6342,-72.2742);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (190,9,'Maule',-35.4794,-71.6842);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (191,9,'Pelarco',-35.3887,-71.4266);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (192,9,'Pencahue',-35.3537,-71.8315);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (193,9,'Río Claro',-35.2458,-71.2885);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (194,9,'San Clemente',-35.5462,-71.4905);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (195,9,'San Rafael',-35.3038,-71.4684);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (196,9,'Talca',-35.4299,-71.6555);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (197,10,'Arauco',-37.2599,-73.3093);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (198,10,'Cañete',-37.83,-73.3671);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (199,10,'Contulmo',-37.9982,-73.2629);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (200,10,'Curanilahue',-37.487,-73.3175);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (201,10,'Lebu',-37.6197,-73.6359);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (202,10,'Los Álamos',-37.6267,-73.497);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (203,10,'Tirúa',-38.3762,-73.4789);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (204,10,'Alto Biobío',-37.9726,-71.3473);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (205,10,'Antuco',-37.3465,-71.6614);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (206,10,'Cabrero',-37.0496,-72.4002);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (207,10,'Laja',-37.282,-72.7167);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (208,10,'Los Ángeles',-37.4648,-72.3541);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (209,10,'Mulchén',-37.725,-72.2456);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (210,10,'Nacimiento',-37.5012,-72.6866);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (211,10,'Negrete',-37.5881,-72.5392);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (212,10,'Quilaco',-37.6775,-71.9681);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (213,10,'Quilleco',-37.4537,-71.9744);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (214,10,'San Rosendo',-37.2561,-72.7204);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (215,10,'Santa Bárbara',-37.6657,-71.992);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (216,10,'Tucapel',-37.2905,-71.9328);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (217,10,'Yumbel',-37.0822,-72.5761);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (218,10,'Chiguayante',-36.9529,-72.9996);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (219,10,'Concepción',-36.8201,-73.0595);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (220,10,'Coronel',-37.0011,-73.1532);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (221,10,'Florida',-36.8354,-72.682);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (222,10,'Hualpén',-36.7935,-73.0973);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (223,10,'Hualqui',-36.9734,-72.9295);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (224,10,'Lota',-37.1014,-73.153);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (225,10,'Penco',-36.7575,-72.9568);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (226,10,'San Pedro de La Paz',-36.8527,-73.1306);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (227,10,'Santa Juana',-37.1987,-72.9369);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (228,10,'Talcahuano',-36.7433,-73.104);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (229,10,'Tomé',-36.6081,-72.9349);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (230,10,'Bulnes',-36.736,-72.2852);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (231,10,'Chillán',-36.613,-72.0961);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (232,10,'Chillán Viejo',-36.6377,-72.1484);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (233,10,'Cobquecura',-36.1285,-72.7823);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (234,10,'Coelemu',-36.5111,-72.7007);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (235,10,'Coihueco',-36.6849,-71.7899);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (236,10,'El Carmen',-37.6982,-71.7692);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (237,10,'Ninhue',-36.3804,-72.3935);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (238,10,'Ñiquen',-36.3218,-71.8591);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (239,10,'Pemuco',-36.9966,-72.0466);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (240,10,'Pinto',-36.8263,-71.6815);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (241,10,'Portezuelo',-36.5374,-72.4523);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (242,10,'Quillón',-36.7474,-72.4847);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (243,10,'Quirihue',-36.2941,-72.5324);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (244,10,'Ránquil',-36.6311,-72.5281);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (245,10,'San Carlos',-36.4167,-71.951);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (246,10,'San Fabián',-36.5657,-71.482);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (247,10,'San Ignacio',-36.8068,-72.0201);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (248,10,'San Nicolás',-36.5338,-72.2132);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (249,10,'Treguaco',-36.4038,-72.7551);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (250,10,'Yungay',-37.1104,-71.9952);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (251,11,'Carahue',-38.739,-73.1746);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (252,11,'Cholchol',-38.6067,-72.8429);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (253,11,'Cunco',-38.9264,-72.0387);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (254,11,'Curarrehue',-39.3513,-71.5718);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (255,11,'Freire',-38.9286,-72.6102);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (256,11,'Galvarino',-38.4596,-72.8027);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (257,11,'Gorbea',-39.2095,-72.6738);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (258,11,'Lautaro',-38.5323,-72.4223);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (259,11,'Loncoche',-39.3592,-72.6247);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (260,11,'Melipeuco',-38.8357,-71.7198);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (261,11,'Nueva Imperial',-38.7579,-72.9453);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (262,11,'Padre Las Casas',-38.7728,-72.586);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (263,11,'Perquenco',-38.4152,-72.3882);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (264,11,'Pitrufquén',-38.9899,-72.636);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (265,11,'Pucón',-39.2936,-71.9646);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (266,11,'Saavedra',-38.7908,-73.3927);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (267,11,'Temuco',-38.7357,-72.6193);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (268,11,'Teodoro Schmidt',-38.9674,-73.0382);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (269,11,'Toltén',-39.194,-73.1726);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (271,11,'Villarrica',-39.2969,-72.2297);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (272,11,'Angol',-37.7948,-72.7254);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (273,11,'Collipulli',-37.9486,-72.4365);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (274,11,'Curacautín',-38.4344,-71.8793);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (275,11,'Ercilla',-38.0806,-72.3769);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (276,11,'Lonquimay',-38.4431,-71.3439);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (277,11,'Los Sauces',-37.9709,-72.8396);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (278,11,'Lumaco',-38.18,-72.9197);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (279,11,'Purén',-38.0744,-73.0241);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (280,11,'Renaico',-37.6826,-72.5826);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (281,11,'Traiguén',-38.2451,-72.7345);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (282,11,'Victoria',-38.2383,-72.3315);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (283,12,'Corral',-39.8781,-73.432);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (284,12,'Lanco',-39.4579,-72.7641);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (285,12,'Los Lagos',-39.8613,-72.8137);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (286,12,'Máfil',-39.6491,-72.9386);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (287,12,'Mariquina',-39.5275,-73.0236);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (288,12,'Paillaco',-40.0799,-72.8686);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (289,12,'Panguipulli',-39.6443,-72.3276);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (290,12,'Valdivia',-39.8781,-73.432);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (291,12,'Futrono',-40.1295,-72.3806);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (292,12,'La Unión',-40.2825,-73.0789);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (293,12,'Lago Ranco',-40.3269,-72.4422);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (294,12,'Río Bueno',-40.3531,-72.9455);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (295,13,'Ancud',-41.8791,-73.8166);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (296,13,'Castro',-42.4663,-73.7704);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (297,13,'Chonchi',-42.6525,-73.7579);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (298,13,'Curaco de Vélez',-42.4393,-73.6004);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (299,13,'Dalcahue',-42.3705,-73.6418);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (300,13,'Puqueldón',-42.6028,-73.6728);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (301,13,'Queilén',-42.8812,-73.4826);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (302,13,'Quemchi',-42.1395,-73.4624);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (303,13,'Quellón',-43.1138,-73.6363);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (304,13,'Quinchao',-42.4967,-73.4409);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (305,13,'Calbuco',-41.7635,-73.1535);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (306,13,'Cochamó',-41.5152,-72.3273);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (307,13,'Fresia',-41.1672,-73.3962);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (308,13,'Frutillar',-41.1211,-73.0508);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (309,13,'Llanquihue',-41.2518,-73.0245);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (310,13,'Los Muermos',-41.4324,-73.5273);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (311,13,'Maullín',-41.6363,-73.5836);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (312,13,'Puerto Montt',-41.4544,-72.9388);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (313,13,'Puerto Varas',-41.3214,-72.9793);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (314,13,'Osorno',-40.5788,-73.1419);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (316,13,'Purranque',-40.9257,-73.1373);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (317,13,'Puyehue',-40.6808,-72.5819);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (318,13,'Río Negro',-40.8043,-73.1999);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (319,13,'San Juan de la Costa',-40.5564,-73.5645);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (320,13,'San Pablo',-36.9638,-72.8093);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (321,13,'Chaitén',-42.9204,-72.7027);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (322,13,'Futaleufú',-43.1845,-71.8685);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (323,13,'Hualaihué',-41.9565,-72.5866);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (324,13,'Palena',-43.6257,-71.801);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (326,14,'Cisnes',-44.7093,-72.6796);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (327,14,'Guaitecas',-43.8915,-73.7787);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (328,14,'Cochrane',-47.3096,-72.618);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (329,14,'O''higgins',-48.454,-72.574);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (330,14,'Tortel',-47.7983,-73.5319);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (331,14,'Coihaique',-45.5799,-72.0531);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (332,14,'Lago Verde',-44.2417,-71.8512);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (333,14,'Chile Chico',-46.5557,-71.722);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (334,14,'Río Ibáñez',-46.2271,-72.8027);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (336,15,'Cabo de Hornos',-54.9388,-68.1517);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (337,15,'Laguna Blanca',-52.4272,-71.4149);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (338,15,'Punta Arenas',-53.1522,-70.9194);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (339,15,'Río Verde',-52.7272,-71.4337);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (340,15,'San Gregorio',-52.3723,-69.6564);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (341,15,'Porvenir',-53.3033,-70.2913);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (342,15,'Primavera',-52.7667,-69.2987);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (343,15,'Timaukel',-54.0564,-68.8272);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (344,15,'Natales',-51.7263,-72.5062);
INSERT INTO comuna(comuna_id,region_id,nombre,latitud,longitud) VALUES (345,15,'Torres del Paine',-51.0342,-73.016);

COMMIT;


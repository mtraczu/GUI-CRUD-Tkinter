CREATE DATABASE IF NOT EXISTS Vehicles;

USE Vehicles;

CREATE TABLE IF NOT EXISTS cars (
    ID INT PRIMARY KEY,
    Brand VARCHAR(50),
    Model VARCHAR(50),
    ProductionYear INT,
    Color VARCHAR(50)
);

INSERT INTO cars (ID, Brand, Model, ProductionYear, Color) VALUES
    (1, 'Ford', 'Focus', 2019, 'Red'),
    (2, 'Toyota', 'Corolla', 2018, 'Blue'),
    (3, 'Honda', 'Civic', 2020, 'Silver'),
    (4, 'BMW', 'X5', 2017, 'Black'),
    (5, 'Audi', 'A4', 2021, 'White'),
    (6, 'Mercedes', 'C-Class', 2016, 'Black'),
    (7, 'Volkswagen', 'Golf', 2019, 'Gray'),
    (8, 'Chevrolet', 'Camaro', 2022, 'Red'),
    (9, 'Nissan', 'Sentra', 2015, 'Silver'),
    (10, 'Hyundai', 'Tucson', 2020, 'White'),
    (11, 'Kia', 'Sportage', 2017, 'Black'),
    (12, 'Subaru', 'Impreza', 2018, 'Blue'),
    (13, 'Mazda', 'CX-5', 2021, 'Red'),
    (14, 'Volvo', 'XC90', 2019, 'Silver'),
    (15, 'Lexus', 'RX', 2020, 'White'),
    (16, 'Tesla', 'Model 3', 2022, 'Black'),
    (17, 'Jaguar', 'F-Type', 2017, 'Red'),
    (18, 'Land Rover', 'Discovery', 2018, 'Green'),
    (19, 'Fiat', '500', 2021, 'Yellow'),
    (20, 'Peugeot', '308', 2019, 'Silver');
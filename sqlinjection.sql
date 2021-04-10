/*Creation of the table*/

CREATE TABLE Nidoking (Lv INTEGER, Move TEXT, Category TEXT);

INSERT INTO Nidoking values(1, "Megahorn", "Physical");
INSERT INTO Nidoking values(1, "Peck", "Physical");
INSERT INTO Nidoking values(1, "Focus Energy", "Status");
INSERT INTO Nidoking values(1, "Double Kick", "Physical");
INSERT INTO Nidoking values(1, "Poison Sting", "Physical");
INSERT INTO Nidoking values(23, "Chip Away", "Physical");
INSERT INTO Nidoking values(35, "Thrash", "Physical");
INSERT INTO Nidoking values(43, "Earth Power", "Special");
INSERT INTO Nidoking values(58, "Megahorn", "Physical");

/*This is what we would want the query to look like*/
/*The hacker has input into the Category, but he wants to be able to see
the whole moveset, so he runs a SQL Injection in Category to access the rest*/
SELECT * FROM Nidoking WHERE Category = 'Physical' AND Lv > 50;

/*Starting from here*/

/*Now, the hacker can see all the Physical moves without having to worry
about the level cap just by editing the string*/
SELECT * FROM Nidoking WHERE Category = 'Physical'; --' AND Lv > 50;

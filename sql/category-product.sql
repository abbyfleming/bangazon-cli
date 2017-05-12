
-- Delete if exists
DELETE FROM Product;
DELETE FROM Category;


DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Category;


-- Create Category
CREATE TABLE Category (
	category_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
);


-- Create Product
CREATE TABLE Product (
	product_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	price INTEGER UNSIGNED NOT NULL,
	quantity INTEGER NOT NULL,
	category_id INTEGER NOT NULL,
	FOREIGN KEY (category_id) REFERENCES Category(category_id)

);


-- Add categories
INSERT INTO Category VALUES (null, "Pots");
INSERT INTO Category VALUES (null, "Succulent");
INSERT INTO Category VALUES (null, "Cactus");

-- Add Products
INSERT INTO Product VALUES 
	(null, "Terracota Pots", "Our mini terracotta pots add fun and flair to all events", 1.40, 20, 1);
INSERT INTO Product VALUES 
	(null, "Mercury Votives", "Looking for the PERFECT favor, gift or décor for your event.", 1.80, 20, 1);
INSERT INTO Product VALUES
	(null, "Glass Votives", "These votives add an elegant look to any event.", 1.70, 20, 1);


INSERT INTO Product VALUES
	(null, "Rosette Leaf Starters", "Place in the shade and wait a few weeks.", 2.70, 50, 2);
INSERT INTO Product VALUES
	(null, "Aloe - Crosby's Prolific", "Large rosette shaped Echeveria types", 2.70, 50, 2);

INSERT INTO Product VALUES
	(null, "San Pedro Trichocereus", "Fast-growing columnar cactus", 15, 25, 3);
INSERT INTO Product VALUES
	(null, "Glow Cactus", "Neon oranges, reds, pinks, and yellows!", 4.50, 10, 3);



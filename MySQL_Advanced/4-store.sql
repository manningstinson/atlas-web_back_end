-- 4-store.sql

-- Drop the trigger if it exists
DROP TRIGGER IF EXISTS update_item_quantity;

-- Create the trigger
DELIMITER //

CREATE TRIGGER update_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the quantity in the items table based on the order
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END //

DELIMITER ;

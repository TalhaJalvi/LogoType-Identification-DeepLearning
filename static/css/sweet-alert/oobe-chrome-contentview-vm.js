eld 'col' doesn't have a default
value
 
In all other cases, if a NOT NULL column without a DEFAULT
value is not referenced, an empty value will be inserted
(for example, 0 for INTEGER columns and '' for CHAR
columns). See NULL Values in MariaDB:Inserting for examples.
 
If a NOT NULL column having a DEFAULT value is not
ref
CREATE DATABASE IF NOT EXISTS testing_btree;

USE testing_btree;

CREATE TABLE IF NOT EXISTS test_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    int_column INT,
    float_column FLOAT,
    string_column VARCHAR(255),
    date_column DATE
);

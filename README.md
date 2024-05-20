# B+ Tree with MySQL Integration

This repository contains a Python implementation of a B+ Tree index structure that integrates with a MySQL database. The implementation supports various MySQL data types and provides basic operations such as INSERT, UPDATE, DELETE, and SHOW.

## Files

1. **BPlusTreeMySQL.py**
    - This script connects to a MySQL database and manages a B+ Tree index. It supports the following operations:
        - INSERT: Insert data items into the index.
        - UPDATE: Update existing items in the index.
        - DELETE: Delete items from the index.
        - SHOW: Display the current status of the index structure.

2. **setup_schema.sql**
    - This SQL file creates the necessary schema and table for the MySQL database. Run this file before running the Python script to set up the database.

3. **test_BPlusTreeMySQL.py**
    - This file contains unit tests for the INSERT, UPDATE, DELETE, and SHOW operations. It ensures that the operations work correctly for various MySQL data types.

## Setup

### Prerequisites

- MySQL server installed and running.
- MySQL user with necessary permissions to create databases and tables.
- Python 3.x installed.
- MySQL Connector for Python installed (`mysql-connector-python`).

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/BPlusTreeMySQL.git
    cd BPlusTreeMySQL
    ```

2. Install the required Python package:
    ```bash
    pip install mysql-connector-python
    ```

3. Set up the MySQL database:
    - Open the `setup_schema.sql` file and update the database name if necessary.
    - Run the SQL file to create the schema and table:
      ```bash
      mysql -u your_username -p < setup_schema.sql
      ```

## Usage

1. Run the Python script for interactive operations:
    ```bash
    python BPlusTreeMySQL.py
    ```

    Follow the on-screen prompts to perform operations:
    - INSERT: `INSERT <int> <float> <string> <date>`
    - DELETE: `DELETE <int>`
    - UPDATE: `UPDATE <old_int> <new_int> <float> <string> <date>`
    - SHOW: `SHOW`

2. Run the unit tests to verify the operations:
    ```bash
    python -m unittest test_BPlusTreeMySQL.py
    ```

## Example Commands

- Insert an entry:
    ```bash
    INSERT 10 10.5 "test1" "2024-05-20"
    ```
- Delete an entry:
    ```bash
    DELETE 10
    ```
- Update an entry:
    ```bash
    UPDATE 10 15 15.5 "test_updated" "2024-05-23"
    ```
- Show the B+ Tree structure:
    ```bash
    SHOW
    ```



# B+ Tree Implementation

This repository contains an implementation of a B+ Tree in Python. The B+ Tree supports various operations such as insert, delete, update, and show. These operations can be performed interactively via the command line.

## Requirements

- Python 3.6 or higher

## Setup

To run this project, clone the repository and navigate into the project directory:

```bash
git clone https://github.com/sanketsh4h/csc675_extracred_btree.git
cd csc675_extracred_btree
```

## Usage

To start the program, run the following command in your terminal:

```bash
python BPlusTree.py <order>
```

Where `<order>` is the order of the B+ Tree you wish to create. The order must be a positive integer.

### Available Commands

- `INSERT <value>`: Inserts a value into the B+ Tree.
- `DELETE <value>`: Deletes a value from the B+ Tree.
- `UPDATE <old_value> <new_value>`: Updates an existing value in the B+ Tree with a new one.
- `SHOW`: Displays the current structure of the B+ Tree.
- `exit`: Exits the application.

### Command Examples

1. **Creating the B+ Tree**

   Start the B+ Tree application with an order of 3:
   ```bash
   python BPlusTree.py 3
   ```

2. **Inserting Values**

   Insert a value into the B+ Tree:
   ```plaintext
   Enter command: INSERT 10
   ```

3. **Deleting Values**

   Delete a value from the B+ Tree:
   ```plaintext
   Enter command: DELETE 10
   ```

4. **Updating Values**

   Update an existing value in the B+ Tree:
   ```plaintext
   Enter command: UPDATE 10 15
   ```

5. **Showing the Tree**

   Display the current structure of the B+ Tree:
   ```plaintext
   Enter command: SHOW
   ```

6. **Exiting the Program**

   Exit the application:
   ```plaintext
   Enter command: exit
   ```

# CHAR vs VARCHAR in Relational Databases

This page outlines the key differences between `CHAR` and `VARCHAR` data types used in relational databases like MySQL. These types are commonly used for storing string data but behave differently in terms of storage, performance, and usage.

---

## Overview

`CHAR` and `VARCHAR` are both used to store character strings, but they differ in how the data is stored and handled. Choosing the correct type is important for performance and storage efficiency.

---

## Key Differences

| Feature               | CHAR                          | VARCHAR                            |
|----------------------|-------------------------------|-------------------------------------|
| **Storage Type**     | Fixed-length                  | Variable-length                     |
| **Length Padding**   | Pads with spaces to full length | No padding                          |
| **Performance**      | Slightly faster for fixed-size fields | More efficient for variable-length text |
| **Storage Efficiency** | Wastes space for short values | More compact for short/variable data |
| **Max Length (MySQL)** | Up to 255 characters (before MySQL 5.0.3) / 255 bytes | Up to 65,535 bytes (row size limit applies) |
| **Trailing Spaces**  | Trailing spaces are removed during comparison | Trailing spaces are preserved       |

---

## Use Cases

- Use **CHAR** when:
  - All values have the same length (e.g., fixed-length codes like country codes, gender).
  - You prioritise slightly better performance over storage.

- Use **VARCHAR** when:
  - Data length varies significantly (e.g., names, addresses, descriptions).
  - You want to minimise storage space.

---

## Example

Creating a table with both types:

```sql
CREATE TABLE employees (
  emp_code CHAR(5),
  emp_name VARCHAR(100)
);

[Back](https://github.com/hmislk/hmis/wiki)

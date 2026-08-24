# Library Management System - UML Class Diagram

## Problem Statement

Design a simple **Library Management System** using a UML class diagram.

## Requirements

- A `Library` has multiple `Books`.
- Each `Book` has:
  - `title`
  - `author`
  - `isAvailable`
- A `Library` has multiple `Members`.
- A `Member` can borrow a book.
- A `Member` can return a book.
- A `Book` can conceptually exist independently of a `Library`.
- There are two types of members:
  - `StudentMember`
  - `TeacherMember`
- Both `StudentMember` and `TeacherMember` are types of `Member`.

## Task

### 1. Identify the Classes

Identify the classes required to model the system.

Example:

```text
Library
Book
```

### 2. Define Attributes and Methods

Add the necessary attributes and methods to each class using UML notation.
Example format:


|       Book        |
---------------------
| - title: str      |
| - author: str     |

| + borrow(): void  |


The above is only an example of the UML format. Determine the appropriate attributes and methods based on the requirements.

### 3. Identify the Relationships
Identify and represent the appropriate relationships between the classes.
Consider the following UML relationships where applicable:
- Association
- Aggregation
- Composition
- Inheritance / Generalization
- Realization
- Dependency
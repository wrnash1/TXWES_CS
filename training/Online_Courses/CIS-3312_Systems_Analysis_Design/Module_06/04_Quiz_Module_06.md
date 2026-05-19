# Quiz: Module 06 - Data Modeling (ERD)
## Course: CIS-3312_Systems_Analysis_Design (IIBA Entry Certificate in Business Analysis (ECBA))

---

### Question 1
How must a many-to-many (M:N) relationship between two database entities be resolved in relational database design?

*   A) Using a direct foreign key link
*   B) Creating an associative (junction) entity that links both tables using 1:N relationships
*   C) Combining both tables
*   D) Deleting one of the entities

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
Relational engines do not support direct M:N tables; an associative entity maps many-to-many links through two one-to-many relations.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    Direct keys only map 1:1 or 1:N linkages.

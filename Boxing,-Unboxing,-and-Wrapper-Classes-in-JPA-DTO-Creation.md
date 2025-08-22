## Overview

When creating Data Transfer Objects (DTOs) in JPA, it is important to understand the concepts of **boxing**, **unboxing**, and **wrapper classes**. These concepts come into play whenever you are dealing with primitive types (e.g., `int`, `double`) and their corresponding object types (e.g., `Integer`, `Double`). Proper handling ensures type safety, prevents `NullPointerException`s, and improves compatibility with JPA queries.

---

## Wrapper Classes

In Java, every primitive type has a corresponding **wrapper class** in the `java.lang` package:

| Primitive | Wrapper Class |
| --------- | ------------- |
| `boolean` | `Boolean`     |
| `byte`    | `Byte`        |
| `char`    | `Character`   |
| `short`   | `Short`       |
| `int`     | `Integer`     |
| `long`    | `Long`        |
| `float`   | `Float`       |
| `double`  | `Double`      |

Wrapper classes allow primitives to be treated as objects, which is essential when working with **collections**, **generics**, or **JPA DTO constructors**, because JPA cannot directly map primitive types to `null`.

---

## Boxing

**Boxing** is the automatic conversion of a primitive type into its corresponding wrapper class.
Example:

```java
int value = 10;
Integer boxedValue = value; // boxing
```

---

## Unboxing

**Unboxing** is the reverse process — converting a wrapper class object back into its primitive type.
Example:

```java
Integer boxedValue = 10;
int unboxedValue = boxedValue; // unboxing
```

---

## Why Wrapper Classes Are Preferred in JPA DTOs

When constructing DTOs using JPQL or Criteria queries, wrapper classes are preferred over primitives for several reasons:

1. **Null Safety**

   * Primitives cannot hold `null`.
   * JPA often returns `null` for missing values in projections.
   * Using a primitive (e.g., `int`) can cause a `NullPointerException`.

   ```java
   // Risky: will throw NPE if db column is null
   public DTO(int count) { ... }

   // Safe: can accept null
   public DTO(Integer count) { ... }
   ```

2. **Optional Values in Queries**
   Wrapper classes make it easy to represent optional fields (e.g., a bill discount may or may not exist).

3. **Consistency in Calculations**
   Wrapper classes integrate better with methods like `BigDecimal.valueOf()` and can be checked for null before calculations.

4. **JPQL Constructor Expressions**
   JPQL requires wrapper classes when instantiating DTOs with possible `null` values.

   ```java
   String jpql = "SELECT new com.divudi.dto.SaleSummaryDTO("
               + " b.id, "
               + " COALESCE(b.total, 0) ) "
               + "FROM Bill b";
   ```

---

## Best Practices for DTO Creation

1. **Always use Wrapper Types in DTOs**

   ```java
   public class LabIncomeReportDTO {
       private Long billId;     // not long
       private BigDecimal total; // not double
       private Integer count;    // not int
   }
   ```

2. **Use `COALESCE` in JPQL**
   Prevents `null` values from causing runtime issues.

   ```java
   SELECT new com.divudi.dto.LabIncomeReportDTO(
       b.id,
       COALESCE(b.netTotal, 0.0),
       COALESCE(b.discount, 0.0)
   )
   FROM Bill b
   ```

3. **Guard Against Nulls in Controller Code**
   Always check for `null` when doing calculations.

   ```java
   BigDecimal safeTotal = dto.getTotal() != null ? dto.getTotal() : BigDecimal.ZERO;
   ```

4. **Prefer `BigDecimal` for Monetary Values**
   Avoid `double` or `float` in financial calculations to prevent rounding errors.

---

## Example: DTO Constructor with Wrapper Classes

```java
public class LabIncomeReportDTO {
    private Long billId;
    private String billNumber;
    private Date billDate;
    private String patientName;
    private BigDecimal netTotal;
    private BigDecimal discount;

    public LabIncomeReportDTO(Long billId, String billNumber, Date billDate,
                              String patientName, BigDecimal netTotal, BigDecimal discount) {
        this.billId = billId;
        this.billNumber = billNumber;
        this.billDate = billDate;
        this.patientName = patientName;
        this.netTotal = netTotal != null ? netTotal : BigDecimal.ZERO;
        this.discount = discount != null ? discount : BigDecimal.ZERO;
    }
}
```

---

## Conclusion

Using wrapper classes with careful attention to boxing and unboxing is critical for stable and null-safe JPA DTO creation. Always avoid primitives in DTOs, use `COALESCE` in JPQL queries, and handle nulls defensively in code.

This practice ensures your HMIS DTOs are robust, performant, and safe against runtime errors.

[Back](https://github.com/hmislk/hmis/wiki/Code-Concepts-for-Developers)

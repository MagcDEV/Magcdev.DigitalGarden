---
title: Records
draft: false
tags:
  - Dotnet
  - CSharp
  - Programming
---

# Records in C#

Records are reference types (like classes) but designed specifically for immutable data models with value-based equality semantics.

## Key Differences Between Records and Classes

1. **Value-based equality**: Records compare based on property values, not references
2. **Immutability**: Records are immutable by default
3. **Concise syntax**: Shorter ways to define data-only types
4. **Built-in functionality**: Auto-generated ToString(), Equals(), GetHashCode(), etc.

## Examples

### Basic Record vs Class

```csharp 
// Record - concise, immutable by default
public record Person(string FirstName, string LastName, int Age);

// Equivalent class would require much more code
public class PersonClass
{
    public string FirstName { get; init; } // Using init to be immutable
    public string LastName { get; init; }
    public int Age { get; init; }
    
    // Would need to manually implement:
    // - Equality members
    // - ToString()
    // - GetHashCode()
    // - Constructor
}

// Usage
var record1 = new Person("John", "Doe", 30);
var record2 = new Person("John", "Doe", 30);
Console.WriteLine(record1 == record2);  // True - value equality!

var class1 = new PersonClass { FirstName = "John", LastName = "Doe", Age = 30 };
var class2 = new PersonClass { FirstName = "John", LastName = "Doe", Age = 30 };
Console.WriteLine(class1 == class2);  // False - reference equality!
``` 

### Non-destructive Mutation with "with"

```csharp 
// Records support non-destructive mutation with "with" expressions
var john = new Person("John", "Doe", 30);
var olderJohn = john with { Age = 31 };  // Creates a new record, original unchanged

Console.WriteLine(john);      // Person { FirstName = John, LastName = Doe, Age = 30 }
Console.WriteLine(olderJohn); // Person { FirstName = John, LastName = Doe, Age = 31 }
``` 

### Practical Use Cases

```csharp
// 1. Data Transfer Objects (DTOs)
public record UserDto(int Id, string Username, string Email);

// 2. Domain events in event-sourcing
public record OrderPlaced(Guid OrderId, DateTime PlacedOn, decimal Amount);

// 3. Immutable configuration
public record DatabaseConfig(string ConnectionString, int Timeout, bool UsePooling);

// 4. API responses
public record ApiResponse<T>(bool Success, T Data, string ErrorMessage = null);

// 5. Nominal record style (C# 10+)
public record Product
{
    public string Name { get; init; }
    public decimal Price { get; init; }
    public string Category { get; init; }
}
```
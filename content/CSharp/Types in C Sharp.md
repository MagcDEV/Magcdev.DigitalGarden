---
title: Types in C#
draft: false
tags:
  - Dotnet
  - CSharp
  - Programming
---
 Value types directly contain their data and are stored in the stack. When you assign a value type to another variable a copy of the value is made.

Examples of value types:
- Numeric types: `int`, `float`, `double`, `decimal`
- `bool`
- `char` 
- Structs
- Enums

## Reference Types

Reference types store a reference (memory address) to the data, with the actual data stored on the heap. When you assign a reference type, only the reference is copied.

Examples of reference types:
- Classes
- Interfaces
- Arrays
- Delegates
- `string` (though it has special immutable behavior)
- `object`

## Key Differences

Here's a practical example demonstrating the difference:
```csharp
// Value type example
int x = 10;
int y = x;  // Creates a copy of the value
y = 20;     // Only changes y, not x
Console.WriteLine($"x: {x}, y: {y}");  // Output: x: 10, y: 20

// Reference type example
class Person { public string Name; }

Person person1 = new Person { Name = "Alice" };
Person person2 = person1;  // Both variables reference the same object
person2.Name = "Bob";      // Changes affect both variables
Console.WriteLine($"person1.Name: {person1.Name}, person2.Name: {person2.Name}");  // Output: person1.Name: Bob, person2.Name: Bob
```

## Heap vs Stack in C#

## Stack
- Fast, fixed-size memory region managed with LIFO (Last-In, First-Out) access pattern
- Automatically managed by the runtime (allocation/deallocation happens when variables go in/out of scope)
- Stores value types and references to objects (not the objects themselves)
- Each thread has its own stack
- Limited in size (typically a few MB)
- Better performance for small, short-lived data

## Heap
- Larger, dynamic memory region for objects with variable lifetimes
- Memory managed by the Garbage Collector
- Stores actual objects (reference type instances)
- Shared across all threads in the application
- Much larger capacity than the stack
- Slightly slower access than stack

## Example

```csharp
public void MemoryExample()
{
    // STACK:
    int x = 10;              // Value type - stored entirely on stack
    bool flag = true;        // Value type - stored entirely on stack
    double pi = 3.14;        // Value type - stored entirely on stack
    
    // HEAP:
    string message = "Hello"; // Reference type - reference on stack, actual string on heap
    List<int> numbers = new List<int> { 1, 2, 3 }; // Reference on stack, list object on heap
    
    // Value type within a reference type:
    numbers.Add(42);         // 42 is boxed and stored on the heap as part of the List
    
    // Reference on stack, Person object on heap
    Person person = new Person { Name = "Alice", Age = 30 };
    
    // Local reference variable on stack points to existing heap object
    Person anotherRef = person;
}

class Person 
{
    public string Name;  // Reference to string (on heap)
    public int Age;      // Value type (stored in the Person object on heap)
}
```

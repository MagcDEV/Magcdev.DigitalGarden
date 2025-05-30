### Single Responsibility Principle

"A class should have only one reason to change"
### Open / Closed Principle

Classes should be open for extensions but closed for modification.
### Liskov Substitution Principle

A child class should be able to do everything its parent class can do, without breaking the parent's behavior expectations.
### Interface Segregation Principle

"Clients should not be forced to depend on interfaces they do not use", this means that large interfaces should be broken down into smaller, more specific interfaces.
### Dependency Inversion Principle

"High-level modules should not depend on low-level modules. Both should depend on abstractions (interfaces)"

"Abstraction should not depend on details. Details (concrete implementations) should depend on abstractions"

The principle aims to decouple modules by introducing an abstraction layer between them. Instead of high-level component directly instantiating or calling a low-level component. both interact through an interface or abstract class defined by the high-level component (or in a shared abstraction layer).
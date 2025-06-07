---
title: Head First Design Patterns Summary
draft: false
tags:
---
## Chapter 1

### **Identify the aspects of your application vary and separate them from what stays the same.**

This is the principle of  [[Encapsulation]] take the part that vary and encapsulate them, so that later you can alter or extend the parts that vary without affecting those that don't.

### **Program to an interface, not an implementation.**

Your code should depend on interfaces not on specific implementations to achieve this we use [[Dependency Inversion]].

```csharp

using System;

// 1. Define the Abstraction (the "Interface")
public interface IDataSaver
{
    void SaveData(string data);
}

// 2. Create Concrete Implementations
public class SqlDataSaver : IDataSaver // Implements the interface
{
    private string _connectionString;
    public SqlDataSaver(string connectionString) {
        _connectionString = connectionString;
         Console.WriteLine($"SqlDataSaver: Initialized with connection string: {_connectionString}");
    }

    public void SaveData(string data) {
        Console.WriteLine($"SqlDataSaver: Saving '{data}' to SQL Database.");
        // ... actual database interaction code ...
    }
}

public class FileDataSaver : IDataSaver // Implements the SAME interface
{
    private string _filePath;
    public FileDataSaver(string filePath) {
        _filePath = filePath;
         Console.WriteLine($"FileDataSaver: Initialized with file path: {_filePath}");
     }

    public void SaveData(string data) {
        Console.WriteLine($"FileDataSaver: Saving '{data}' to file '{_filePath}'.");
        // ... actual file writing code ...
    }
}

// 3. Application Service depends on the INTERFACE
public class OrderService
{
    // --- LOOSE COUPLING --- depends on the abstraction
    private readonly IDataSaver _dataSaver;

    // The specific implementation is injected (Dependency Injection is common here)
    public OrderService(IDataSaver dataSaver)
    {
        this._dataSaver = dataSaver; // Receives ANY object that IS an IDataSaver
    }

    public void PlaceOrder(string orderData)
    {
        Console.WriteLine("OrderService: Placing order.");
        // ... order processing logic ...

        // Calling the method via the INTERFACE reference
        // Doesn't care if it's SqlDataSaver or FileDataSaver!
        this._dataSaver.SaveData($"Order: {orderData}");

        Console.WriteLine("OrderService: Order placed and saved.");
    }
}

public class TestApp
{
    public static void Main(string[] args)
    {
        Console.WriteLine("--- Using SQL Saver ---");
        // Create the specific implementation we want to use right now
        IDataSaver sqlSaver = new SqlDataSaver("Server=myServer;Database=myDataBase;...");
        // Inject it into the service
        OrderService sqlOrderService = new OrderService(sqlSaver);
        sqlOrderService.PlaceOrder("123-ABC-SQL");

        Console.WriteLine("\n--- Using File Saver ---");
         // Create a DIFFERENT implementation
        IDataSaver fileSaver = new FileDataSaver("orders.txt");
         // Inject the OTHER implementation - OrderService code doesn't change!
        OrderService fileOrderService = new OrderService(fileSaver);
        fileOrderService.PlaceOrder("456-DEF-FILE");
    }
}
/* Output:
--- Using SQL Saver ---
SqlDataSaver: Initialized with connection string: Server=myServer;Database=myDataBase;...
OrderService: Placing order.
SqlDataSaver: Saving 'Order: 123-ABC-SQL' to SQL Database.
OrderService: Order placed and saved.

--- Using File Saver ---
FileDataSaver: Initialized with file path: orders.txt
OrderService: Placing order.
FileDataSaver: Saving 'Order: 456-DEF-FILE' to file 'orders.txt'.
OrderService: Order placed and saved.
*/
```

### **Favor composition over inheritance**

When you are designing your classes and need to reuse functionality or extend behavior, you should lean toward using composition (building classes by including instances of other classes) rather than inheritance (deriving a new class from an existing base class).

**Inheritance** models an "is-a" relationship. A Dog is an Animal. A Savings Account is an Account. The derived class (subclass) inherits members from the base class (superclass) and can be treated polymorphically as an instance of the base class.

**Composition** models a "has-a" or "uses-a" relationship. A Car has an Engine. An OrderProcessor uses a PaymentGateway. One class holds a reference (an instance) to another class and delegates tasks to it.

### The Strategy Pattern

Defines a family of algorithms, encapsulates each one, and makes then interchangeable. Strategy lets the algorithm vary independently from clients that use it.

---

## Chapter 2

The Observer pattern defines a one-to-many dependency between objects so that when on object (the subject or observable) changes its state, all its dependents (the observers) are notified and updated automatically.

##### Problem it solves

it addresses the issue of needing to maintain consistency between related objects without making then tightly coupled. Imagine you have and object whose state is interesting to other objects. You want these other objects to be updated whenever this state changes, but you don't want the primary object to know about the concrete classes of these depended objects. This promotes loose coupling, which is a cornerstone of good software design.

#### Advantages

- Loose Coupling
- Dynamic Relationships
- Broadcast Communication
- Reusability
- Improved Modularity

#### Disadvantages

- Unexpected Updates
- Memory Leaks
- Notification Overhead
- Order of Notification
- Subject State management
- Potential for "God" Subjects

### Example

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

// --- 1. Define the Observer Interface ---
// This interface will be implemented by all observers.
public interface IObserver
{
    // Method called by the Subject to notify the observer of a change.
    void Update(ISubject subject);
}

// --- 2. Define the Subject Interface ---
// This interface will be implemented by the subject.
public interface ISubject
{
    // Registers an observer.
    void Attach(IObserver observer);

    // Unregisters an observer.
    void Detach(IObserver observer);

    // Notifies all registered observers of a change.
    void Notify();
}

// --- 3. Concrete Subject Implementation ---
// This is the class whose state changes will trigger notifications.
public class Product : ISubject
{
    // A list to store all registered observers.
    private List<IObserver> _observers = new List<IObserver>();

    private string _productName;
    private decimal _price;

    public string ProductName => _productName;

    // Property for the price. When the price is set, observers are notified.
    public decimal Price
    {
        get { return _price; }
        set
        {
            if (_price != value)
            {
                _price = value;
                Console.WriteLine($"\n--- Product '{_productName}' price changed to ${_price:C} ---");
                // Notify all observers about the price change.
                Notify();
            }
        }
    }

    public Product(string productName, decimal initialPrice)
    {
        _productName = productName;
        _price = initialPrice;
        Console.WriteLine($"Product '{_productName}' created with initial price: ${_price:C}");
    }

    // Method to register an observer.
    public void Attach(IObserver observer)
    {
        Console.WriteLine($"Subject: Attached an observer to '{_productName}'.");
        this._observers.Add(observer);
    }

    // Method to unregister an observer.
    public void Detach(IObserver observer)
    {
        this._observers.Remove(observer);
        Console.WriteLine($"Subject: Detached an observer from '{_productName}'.");
    }

    // Method to notify all observers.
    // It iterates through the list of observers and calls their Update method.
    public void Notify()
    {
        Console.WriteLine($"Subject '{_productName}': Notifying observers...");
        foreach (var observer in _observers)
        {
            observer.Update(this);
        }
    }

    // A business logic method that might change the state
    public void ChangePrice(decimal newPrice)
    {
        this.Price = newPrice; // Setting the Price property will trigger Notify()
    }
}

// --- 4. Concrete Observer Implementations ---
// These classes implement the IObserver interface and react to notifications.

public class Customer : IObserver
{
    private string _customerName;
    private Product _observedProduct; // Reference to the subject to pull state if needed

    public Customer(string name)
    {
        _customerName = name;
    }

    // The Update method is called by the Subject when its state changes.
    public void Update(ISubject subject)
    {
        if (subject is Product product)
        {
            _observedProduct = product; // Keep a reference if needed later
            Console.WriteLine($"Hey {_customerName}! The price of '{product.ProductName}' has changed to ${product.Price:C}.");
            // Here, the observer could have more complex logic, like deciding to buy or sell.
        }
    }

    // Method for the customer to subscribe to a product
    public void SubscribeToProduct(Product product)
    {
        Console.WriteLine($"Customer '{_customerName}' is subscribing to product '{product.ProductName}'.");
        product.Attach(this);
        _observedProduct = product; // Store a reference to the product being observed
    }

    // Method for the customer to unsubscribe from a product
    public void UnsubscribeFromProduct(Product product)
    {
        Console.WriteLine($"Customer '{_customerName}' is unsubscribing from product '{product.ProductName}'.");
        product.Detach(this);
        if (_observedProduct == product)
        {
            _observedProduct = null;
        }
    }
}

public class InventoryManager : IObserver
{
    private string _managerName;

    public InventoryManager(string name)
    {
        _managerName = name;
    }

    public void Update(ISubject subject)
    {
        if (subject is Product product)
        {
            Console.WriteLine($"Inventory Manager {_managerName}: Notified! Product '{product.ProductName}' price is now ${product.Price:C}. Adjusting stock levels or reordering strategies might be needed.");
        }
    }

    public void MonitorProduct(Product product)
    {
        Console.WriteLine($"Inventory Manager '{_managerName}' is now monitoring product '{product.ProductName}'.");
        product.Attach(this);
    }
}


// --- 5. Demonstration ---
public class ObserverPatternDemo
{
    public static void Main(string[] args)
    {
        // Create a subject (Product)
        Product laptop = new Product("SuperDell Laptop", 1200.00m);
        Product mouse = new Product("LogiTech Mouse", 25.00m);

        Console.WriteLine("\n--- Initial Setup Complete ---\n");

        // Create observers (Customers and an Inventory Manager)
        Customer alice = new Customer("Alice");
        Customer bob = new Customer("Bob");
        InventoryManager charlie = new InventoryManager("Charlie");

        // Observers subscribe to subjects
        alice.SubscribeToProduct(laptop);
        bob.SubscribeToProduct(laptop);
        bob.SubscribeToProduct(mouse); // Bob is interested in both laptop and mouse
        charlie.MonitorProduct(laptop); // Inventory manager monitors the laptop

        Console.WriteLine("\n--- Subscriptions Complete ---\n");

        // Change the state of the subject (laptop price)
        // This will trigger notifications to Alice, Bob, and Charlie.
        laptop.ChangePrice(1150.00m);

        // Change the state of another subject (mouse price)
        // This will trigger a notification only to Bob.
        mouse.ChangePrice(22.50m);

        // Bob decides he's no longer interested in the laptop
        bob.UnsubscribeFromProduct(laptop);

        Console.WriteLine("\n--- Bob Unsubscribed from Laptop ---\n");

        // Change laptop price again. Only Alice and Charlie should be notified.
        laptop.ChangePrice(1100.00m);

        Console.ReadLine();
    }
}
```

## Chapter 3

The Decorator pattern is a structural pattern uset to dynamically add new behavior or responsibilities to objects without modifying their existing code. It´s a flexible alternative to subclassing for extending functionality.

##### Key Concepts

- Component: The interface or abstract class definig the operations.
- ConcreteComponent: The core class that implements the Component.
- Decorator: An abstract class that implements the Component interface and has a reference to a Component object.
- ConcreteDecorator: Extends the Decorator and adds new behavior.

This pattern is usefull to follow the Open/Closed solid principle an to add responsabilities to individual objects and not to entire class.

##### Example

1. Component Interface

```csharp
public interface ICoffee
{
    string GetDescription();
    double GetCost();
}
```

2. ConcreteComponent

```csharp
public class SimpleCoffee : ICoffee
{
    public string GetDescription() => "Simple Coffee";
    public double GetCost() => 5.0;
}
```

3. Decorator Base Class

```csharp
public abstract class CoffeeDecorator : ICoffee
{
    protected ICoffee _coffee;

    public CoffeeDecorator(ICoffee coffee)
    {
        _coffee = coffee;
    }

    public virtual string GetDescription() => _coffee.GetDescription();
    public virtual double GetCost() => _coffee.GetCost();
}
```

4. ConcreteDecorators

```csharp
public class MilkDecorator : CoffeeDecorator
{
    public MilkDecorator(ICoffee coffee) : base(coffee) { }

    public override string GetDescription() => _coffee.GetDescription() + ", Milk";
    public override double GetCost() => _coffee.GetCost() + 1.5;
}

public class SugarDecorator : CoffeeDecorator
{
    public SugarDecorator(ICoffee coffee) : base(coffee) { }

    public override string GetDescription() => _coffee.GetDescription() + ", Sugar";
    public override double GetCost() => _coffee.GetCost() + 0.5;
}
```

5. Usage

```csharp
class Program
{
    static void Main()
    {
        ICoffee coffee = new SimpleCoffee();
        Console.WriteLine($"{coffee.GetDescription()} - ${coffee.GetCost()}");

        coffee = new MilkDecorator(coffee);
        coffee = new SugarDecorator(coffee);

        Console.WriteLine($"{coffee.GetDescription()} - ${coffee.GetCost()}");
    }
}
```

🖨️ Output
Simple Coffee - $5.0
Simple Coffee, Milk, Sugar - $7.0
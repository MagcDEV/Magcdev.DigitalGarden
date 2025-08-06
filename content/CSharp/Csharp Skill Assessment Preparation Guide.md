---
title: Example Title
draft: false
tags:
  - CSharp
  - Dotnet
  - Programming
---
## Create Classes and Objects in C#

Classes are blueprints for objects. Objects are instances of classes.

```csharp
public class Car
{
	// Properties
	public string Make {get; set;}
	public string Model {get; set;}
	public int Year {get; set;}

	// Constructor
	public Car(string make, string model, int year)
	{
		Make = make;
		Model = model;
		Year = year;
	}
	// Method
	public void StartEngine()
	{
		Console.WriteLine($"{Make} {Model} engine started!");
	}
}

// Creating objects
class Program
{
	static void Main()
	{
		Car myCar = new Car("Toyota", "Camry", 2003)
		myCar.StartEngine(); // Output: Toyota Camry engine started!

		// Object initializer syntax
		Car anotherCar = new Car("Audi", "zz", 2023)
		{
			Year = 2024; // properties can be overrriden after construction
		};
	}
}
```

## Basic Data Types and Variables

C# has value types (stored on stack) and reference types (stored on heap).

```csharp
class DataTypesDemo
{
	static void Main()
	{
		// Value Types
		int integer = 32;
		double floatingPoint = 3.14159
		decimal money = 19.99m;
		bool isActive = true;
		char letter = 'A';
		DateTime date = DateTime.Now;

		// Reference types
		string text = "Hello World";
		int[] numbers = {1, 2, 3, 4};
		object anything = "can hold any type";

		// nullable types
		int? nullableInt = null;
		nullableInt = 34;

		// type Inference
		var inferredInt = 100; // copiler determines type
		var inferredString = "Text";

		// constanst
		const double PI = 3.14159;

		// Enums
		enum Status {Active, Inactive, Penging};
		Status currentStatus = Status.Active;
	}
}
```

## Class Hierarchies and Polymorphism

Inheritance allows classes to inherit properties and methods from base classes.

```csharp
// Base class
public abstract class Animal
{
	public string Name {get; set;}
	public int Age {get; set;}

	public Animal(string name, int age)
	{
		Name = name;
		Age = age;
	}

	// Abstract method - must be implemented by derived classes
	public abstract void MakeSoung();

	// Virtual method - can be overridden
	public virtual void Move()
	{
		Console.WriteLine($"{Name} is moving");
	}
}

// Derived classes
public class Dog : Animal
{
	public string Breed {get; set;}

	public Dog(string name, int age, string breed) : base(name, age)
	{
		Breed = breed;
	}

	public override void MakeSound()
	{
		Console.WriteLine($"{Name} says: Woof!");
	}

	public override void Move()
	{
		Console.WriteLine($"{Name} is running");
	}
}

public class Cat : Animal
{
	public Cat(string name, int age) : Base(name, age) { }

	public override void MakeSound()
	{
		Console.WriteLine($"{Name} says: Meow!");
	}
}

// Polymorphism in action
class Program
{
	static void Main()
	{
		List<Animal> animals = new List<Animal>
		{
			new Dog("Rex", 5, "Labrador),
			new Cat("Whiskers", 3)
		};

		foreach(Animal animal in animals)
		{
			animal.MoakeSound(); // Polymorphic call
			animal.Move();
		}
	}
}
```

## LINQ - Join, Aggregate, and Group

LINQ (Language Integrated Query) provides powerful data querying capabilities.

```csharp
public class Product
{
	public int Id {get; set;}
	public string Name {get; set;}
	public decimal Price {get; set;}
	public int CategoryId {get; set;}
}

public class Category
{
	public int Id {get; set;}
	public string Name {get; set;}
}

class LinqDemo
{
	 static void Main()
	 {
		var products = new List<Product>
		{
			new Product {Id = 1, Name = "Laptop", Price = 999.99m, CategoryId = 1},
			new Product {Id = 2, Name = "Mouse", Price = 25.99m, CategoryId = 1},
			new Product {Id = 3, Name = "Shirt", Price = 29.99m, CategoryId = 2},
			new Product {Id = 4, Name = "Pants", Price = 49.99m, CategoryId = 2},
		} 

		var categories = new List<Category>
		{
			new Category {Id = 1, Name = "Electronics"},
			new Category {Id = 2, Name = "Clothing"}
		}

		// JOIN
		var productWithCategory = from p in products
								  join c in categories on p.CategoryId equals c.Id
								  select new
								  {
									ProductName = p.Name,
									CategoryName = c.Name,
									Price = p.Price
								  };
		
		// Method syntax for join
		var joinMethod = product.Join(categories,
			p => p.CategoryId,
			c => c.Id,
			(p, c) => new {p.Name, Category = c.Name, p.Price});

		// AGGREGATE
		decimal totalPrice = products.Aggregate(0m, (total, p) => total + p.Price);
		string concatenated = products.Aggregate("Products: "
		, (current, p) => current + p.Name + ", ");

		// Built-in aggregates
		decimal sum = products.Sum(p => p.Price);
		decimal average = products.Average(p => p.Price);
		int count = products.Count();
		decimal min = products.Min(p => p.Price);
		decimal max = products.Max(p => p.Price);

		// GROUP
		var groupedByCategory = from p in products
								group p by p.CategoryId into g
								select new
								{
									CategoryId = g.Key,
									Products = g.ToList(),
									TotalPrice = g.Sum(p => p.Price)
								};

		// Method syntax for grouping
		var gruopMethod = products.GroupBy(p => p.CategoryId)
								  .Select(g => new
								  {
									  CategoryId = g.Key,
									  Count = g.Count(),
									  AveragePrice = g.Average(p => p.Price)
								  });
	 }
}
```
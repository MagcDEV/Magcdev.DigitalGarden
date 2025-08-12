---
title: Csharp Skill Assessment Preparation Guide
draft: false
tags:
  - CSharp
  - Dotnet
  - Programming
---
## 1. Create Classes and Objects in C#

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

## 2. Basic Data Types and Variables

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

## 3. Class Hierarchies and Polymorphism

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

## 4. LINQ - Join, Aggregate, and Group

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

## 5. Combining Collection Types

Different collection types ca be combined to solve specific problems.

```csharp
class CollectionsCombination
{
	static void Main()
	{
		// Dictionary with List as value
		var studentCourses = new Dictionary<string, List<string>>
		{
			["John"] = new List<string> {"Math", "Physics", "Chemistry"},
			["Jane"] = new List<string> {"Biology", "Chemistry"},
			["John"] = new List<string> {"Math", "Computer Science"}
		};

		// HashSet for unique values with fast lookup
		var uniqueCourses = new HashSet<string>();
		foreach(var courses in studentCourses.Values)
		{
			uniqueCourses.UnionWith(courses);
		}

		// Queue with custom objects
		var taskQueue = new Queue<(string task, int priority)>
		taskQueue.Enqueue(("Process Order", 1));
		taskQueue.Enqueue(("Send email", 2));

		// Stack with Dictionary
		var history = new Stack<Dictionary<string, object>>();
		history.Push(new Dictionary<string, object>
		{
			["Action"] = "create",
			["Timestamp"] = DateTime.Now,
		});

		// List of Tuples
		var coordinates = new List<(double x, double y, double z)>
		{
			(1.0, 2.0, 3.0),
			(4.0, 5.0, 6.0)
		};

		// Nested collections for matrix
		var matrix = new List<List<int>>
		{
			new List<int> {1, 2, 3},
			new List<int> {4, 5, 6},
			new List<int> {7, 8, 9}
		};
	}
}
```


## 6. Interfaces for Loosely Coupled Code

Interfaces define contracts that classes must implement.
```csharp
// Define interfaces
public interface ILogger
{
	void Log(string message);
	void LogError(string error);
}

public interface IDataRepository<T>
{
	T GetById(int id);
	IEnumerable<T> GetAll();
	void Add(T entity);
	void Update(T entity);
	void Delete(int id);
}

// Implementations
public class ConsoleLogger : ILogger
{
	public void Log(string message)
	{
		Console.WriteLine($"[INFO] {DateTime.Now}: {message}");
	}
	
	public void LogError(string error)
	{
		Console.WriteLine($"[ERROR] {DateTime.Now}: {error}");
	}
}

public class FileLogger : ILogger
{
	private string _filePath;

	public FileLogger(string filePath)
	{
		_filePath = filePath; 
	}

	public void Log(string message)
	{
		File.AppendAllText(_filePath, $"[INFO] {DateTime.Now}: {message}\n");
	}
	
	public void LogError(string error)
	{
		File.AppendAllText(_filePath, $"[ERROR] {DateTime.Now}: {error}\n");
	}
}

// Service using dependency injection
public class OrderService
{
	private readonly ILogger _logger;
	private readonly IDataRepository<Order> _repository; 

	public OrderService(ILogger logger, IDataRepository<Order> repository)
	{
		_logger = logger;
		_repository = repository;
	}

	public void ProcessOrder(Order order)
	{
		try
		{
			_repository.Add(order);
			_logger.Log($"Order {order.Id} processed successfully");
		}
		catch(Exception ex)
		{
			_logger.LogError($"Failed to process order: {ex.Message}");
		}
	}
}

public class Order
{
	public int Id {get; set;};
	public string Description {get; set;};
}

```

## 7. Record Types

Records provide a concise way to  create immutable data types.
```csharp
// Record declaration
public record Person(string FirstName, string LastName, int Age);


// Record with additional members
public record Employee(string FirstName, string LastName, int Age, string Department) : Person(FirstName, LastName, Age)
{
	public decimal Salary {get; init;}
	public string GetFullName() => $"{FirsName} {LastName}";
}

// Record struct (value type)
public record struct Point(double X, double Y);

// Mutable record
public record MutablePerson
{
	public string FirstName {get; set;}
	public string LastName {get; set;}
}

class RecordDemo
{
	static void Main()
	{
		// Creating records
		var person1 = new Person("John", "Doe", 30)
		var person2 = new Person("John", "Doe", 30)

		// Value equality (not reference equality)
		Console.Writeline(person1 == person2); // True

		// With-expressions for non-destructive mutation
		var person3 = person1 with {Age = 31};

		// Deconstruction
		var (firstName, lastName, age) = person1;

		// ToString() is automatically implemented
		Console.WriteLine(person1); // Person {FirstName = John, LastName = Doe, Age = 30}

		// Record inheritance 
		var employee = new Employee("Jane", "Smith", 25, "IT") {Salary = 7500m};
	}
}
```

## 8. LINQ - Filter, Map, and Sort

LINQ provides powerful methods for data manipulation.
```csharp
public class Student
{

	public int Id {get; set;}
	public string Name {get; set;}
	public int Age {get; set;}
	public double GPA {get; set;}
	public string Major {get; set;}
}

class LinqOperations
{
	static void Main()
	{
		var students = new List<Student>
		{
			new Student {Id = 1, Name = "Alice", Age = 20, GPA = 3.2, Major = "Computer Science"};
			new Student {Id = 2, Name = "Miguel", Age = 20, GPA = 3.2, Major = "Computer Science"};
			new Student {Id = 3, Name = "Alberto", Age = 20, GPA = 3.2, Major = "Computer Science"};
			new Student {Id = 4, Name = "Maicol", Age = 20, GPA = 3.2, Major = "Computer Science"};
		}

		// FILTER (Where)
		var csStudents = students.Where(s => s.Major == "Computer Science");
		var highGPA = students.Where(s => s.GPA > 3);
		var complexFilter= students.Where(s => s.Major == "Computer Science" && 
		s.GPA > 3);
		
		// MAP (Select)
		var names = students.Select(s => s.Name);
		var studentInfo = students.Select(s => new
		{
			s.Name,
			s.GPA,
			IsHonors = s.GPA > 3.7
		});

		// SelectMany (flattening)
		// allCourses will be a IEnumerble<string> with the courses
		/*
		CS101
		MATH201
		MATH301
		PHYS101
		*/
		var courses = new List<(int StudentId, List<string> Courses)>
		{
			(1, new List<string> {"CS101", "MATH201"}),
			(1, new List<string> {"MATH301", "PHYS101"})
		}
		var allCourses = courses.SelectMany(s => s.Courses);

		// SORT (OrderBy, ThenBy)
		var sortedByGPA = students.OrderBy(s => s.GPA);
		var sortedByGPADesc = studens.OrderByDescending(s => s.GPA);
		var multiSort = students.OrderBy(s => s.Major).ThenByDescending(s => s.GPA);

		// Combining operations
		var result = students
			.Where(s => s.Age >= 20)
			.OrderByDescending(s => s.GPA)
			.Select(s => new {s.Name, s.GPA, s.Major})
			.Take(3);

		// Query syntax alternative
		var querySyntax = from s in students
						where s.GPA >= 3.5
						orderBy s.Name
						select new {s.Name, s.GPA};
	}
}

```

## 9 Generics

Generics allow you to write type-safe, reusable code.
```csharp

```

## 10. Action and Func

Delegates that represent methods with specific signatures.
```cshapr

```

## 11. Fundamental Type Constructs

Understanding the basic building blocks of C# types.
```csharp

```

## 12. Extension Methods
Extension methods allow you to add methods to existing types.
```csharp

```

## 13. Events and Delegates

Events and delegates enable event-driven programming.
```csharp

```
## 14. Exception Handling

Proper exception handling ensures  robust applications.
```csharp

```
## 15. Working with Null Values

C# provides various techniques to  handle null values safely.
```csharp

```
## 16. Asynchronous Programming

Async/await pattern  for efficient asynchronous operations.
```csharp

```
## 17. Working with Dates and Times

DateTime and DateTimeOffset handling in .NET.
```csharp

```
## 18. Map-Based Collections (Dictionary, etc.)

Key-value pair collections for efficient lookups.
```csharp

```
## 19. List-Based Collections

Working with ordered collections.
```csharp

```
## 20. Basic C# Application Constructs

Understanding the fundamental building  blocks of C# applications.
```csharp

```


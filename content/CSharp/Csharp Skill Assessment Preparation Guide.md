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
public class GenericRepository<T> where T : class
{
	private List<T> _items = new List<T>();

	public void Add(T item) 
	{
		_item.Add(item);
	}

	public T Get(int index)
	{
		return _items[index];
	}

	public IEnumerable<T> GetAll()
	{
		return _item;
	}
}

public class Utilities
{
	public static void Swap<T>(ref T a, ref T b)
	{
		T temp = a;
		a = b;
		b = temp;
	}

	public static T Max<T>(T a, T b) where T : IComparable<T>
	{
		return a.CompareTo(b) > 0 ? a : b;
	}
}

// Generic Interface
public interface ICache<IKey, TValue>
{
	void Add(Tkey key, TValue value);
	TValue Get(TKey key);
	bool Contains(TKey key);
}

// Implementation with multimple type parameters
public class MemoryCache<Tkey, TValue> : ICache<TKey, TValue>
{
	private Dictionary<TKey, TValue> _cache = new Dictionary<TKey, TValue>();

	public void Add(TKey key, TValue value)
	{
		_cache[key] = value;
	}

	public TValue Get(TKey key)
	{
		return _cache.TryGetValue(key, out TValue value) ? value : default(TValue);
	}

	public bool Contains(Tkey key)
	{
		return _cache.Contains(key);
	}
}

// Generic constrains
public class AdvancedRepository<T> where T : class, new()
{
	public T CreateNew()
	{
		return new T(); // possible because of new() constraint
	}
}

// Multiple constraints
public interface IEntity
{
	int Id {get; set;}
}

public class EntityRepository<T> where T : class, IEntity, new()
{
	public T FindById(int id, List<T> items)
	{
		return items.FirstOrdefault(item => item.Id == id);
	}
}

```

## 10. Delegates, Action and Func

A delegate is a type that represents a reference to a method with a specific signature. Is like pointer in C/C++, but safe and object oriented.

### Why Action and Func?

Before they where created if you wanted to pass methods as parameters you have to declare your own delegates, for example

```csharp
public delegate int MyDelegate(int x, int y);
```

This works but it is verbose and repetitive so .NET introduced the generic delegates predefined:

- Action for methods that return void
- Func for method that return some T generic value

```csharp
class DelegatesDemo
{
	static void Main()
	{
		// Action: represent void methods
		Action<strings> print = Console.WriteLine();
		print("Hello World");

		Action<int, int> printSum = (a, b) => Console.WriteLine($"Sum:{a + b}");
		printSum(5, 3);

		// Func: represents methods with return values
		Func<int, int, int> add = (a, b) => a + b;
		int result = add(10, 20);

		Func<string, bool> isLongString = s => s.Length > 10;
		bool isLong = isLongString("Hello");

		// Using with methods
		ProcessData(GetData, TransformData, SaveData);

		// Using with LINQ
		var numbers = new List<int> {1, 2, 3, 4, 5};
		Func<int, bool> isEven = n => n % 2 == 0;
		var evenNumbers = numbers.Where(isEven);

		// Chaining functions
		Func<int, int> doubleIt = x => x * 2;
		Func<int, int> addTen = x => x + 10;
		Func<int, int> combined = x => addTen(doubleIt(x));

		// Predicate (special case of Func<T, bool>)
		Predicate<string> isEmpty = string.IsNullOrEmpty;

		// Using in higher-order functions
		var transformed = Transform(numbers, x => x * x);
	}

	static List<T> GetData<T>() where T : new()
	{
		return new List<T> {new T(), new T() };
	}

	static void TransformData<T>(List<T> data, Action<T> transformer)
	{
		foreach (var item in data)
		{
			transformer(item);
		}
	}

	static void SaveData<T>(List<T> data)
	{
		Console.WriteLine($"Saved {data.Count} items");
	}

	static void ProcessData<T>(Func<List<T>> getData,
							   Action<List<T>, Action<T>> transform,
							   Action<List<T>> save) where T : new()
	{
		var data = getData();
		transform(data, item => Console.WriteLine($"Processing {item}"));
		save(data);
	}

	static List<TResult> Transform<T, TResult>(List<T> source, Func<T, TResult> selector)
	{
		var result = new List<TResult>();
		foreach (var item in source)
		{
			result.Add(selector(item));
		}
		return result;
	}
}
```

## 11. Fundamental Type Constructs

Understanding the basic building blocks of C# types.
```csharp
// Structs (Value Types)
public struct Point3D
{
	public double X {get; set;}
	public double Y {get; set;}
	public double Z {get; set;}

	public Point3D(double x, double y, double z)
	{
		X = x;
		Y = y;
		Z = z;
	}

	public double DistanceFromOrigin()
	{
		return Math.Sqrt(X * X + Y * Y + Z * Z);
	}
}

// Enums
public enum DayOfWeek
{
	Monday = 1,
	Tuesday = 2,
	Wednesday = 3,
	Thursday = 4,
	Friday = 5,
	Saturday = 6,
	Sunday = 7
}

[Flags]
public enum FilePermisssions
{
	None = 0,
	Read = 1,
	Write = 2,
	Execute = 3,
	All = Read | Write | Execute
}

class TypeConstructsDemo
{
	static void Main()
	{
		// Value Types vs Reference Types
		Point3D point1 = new Point3D(1, 2, 3);
		Point3D point2 = point1; // Copy by value 
		point2.X = 5;
		Console.WriteLine(point1.X); // Still 1

		// Boxing and Unboxing
		int value = 42;
		object boxed = value; // boxing
		int unboxed = (int)boxed;

		// Tuples
		var tuple = (Name: "John", Age: 30, IsActive: true);
		Console.WriteLine($"{tuple.Name} is {tuple.Age} years old");

		// tuple deconstruction
		var (name, age, isActive) = tuple;

		// ValueTuple return type
		var result = GetMinMax(new[] {1, 5, 3, 9, 2});
		Console.WriteLine($"Min: {result.Min}, Max: {result.Max}");

		// Enum operatinos
		DayOfWeek today = DayOfWeek.Wednesdat;
		int dayNumber = (int)today;

		FilePermisions permissions = FilePermissions.Read | FilePermissions.Write;
		bool canRead = (permissions & FilePermissions.Read) == FilePermissions.Read;

		// Anonymous types
		var anonymous = new {Name = "Alice", Score = 95};	
		Console.WriteLine(anonymous.Name);

		dynamic dynamicVar = 10;
		dynamicVar = "Now I'm a string";
		dynamicVar = new {Property = "Dynamic object"};
	}

	static (int Min, int Max) GetMinMax(int[] numbers)
	{
		return (numbers.Min(), numbers.Max());
	}
}

```

## 12. Extension Methods
Extension methods allow you to add methods to existing types.
```csharp
// Extension methods must be in static class
public static class StringExtensions
{
	public static bool IsPalindrome(this string str)
	{
		if (s == null) return false;
		int i = 0, j = s.Length - 1;
		while(i < j)
		{
			if (s[i] != s[j]) return false;
			i++;
			j--;
		}
		return true;
	}
}

// Usage
using myNamespace; // where StringExtensions lives
string t = "level";
bool pal = t.IsPalindrome(); // calls StringExtensions.IsPalindrome(t);
```

## 13. Events and Delegates

Events and delegates enable event-driven programming.

Delegate: a type that represent a reference to a method (or multiple methods). It describes a method signature (parameter types and return type). Example: 

```csharp
delegate void MyHandler(int x);
```

Event: a language construct (build on top of delegates) that exposes a publisher/subscriber pattern, this construct exposes a delegate to  other classes in a controlled way. External code can subscribe (+=) and unsubscribe (-=) handlers, but only the declaring class can raise (invoke) the event.

Think of a delegate as a type-safe function pointer.

Basic Example:
```csharp
using System;

public delegate int MathOp(int x, int y);

class Program
{
	// Methods that match the MathOp signature
	static int Add(int a, int b) => a + b;
	static int Multiply(int a, int b) => a * b;

	static void Main()
	{
		// Create a delegate instance that points to Add
		MathOpe op = Add;
		Console.WriteLine(op(2, 3)); // Calls Add(2,3) => 5

		// Reassing the delegate to point to Multiply
		op = Multiply;
		Console.WriteLine(op(2,3)); // Calls Multiply(2,3) => 6

		// Multicast delegates: attach multiple methods
		op = Add;
		op += Multiply; // op now contains Add then Multiply

		// When you invoke a multicast delegate both methods run in order.
		// The return valur of the delgate invocation is the result from the last method
		int result = op(2,3);
		Console.WriteLine("Multicast result: " + result);

		foreach (var d in op.GetInvocationList())
		{
			var methodResult = (int)d.DynamicInvoke(2,3);
			Console.WriteLine("Individual invocation result: " + methodResult);
		}
	}
}
```

### Using Func and Action
Func and Action are predefined generic delegates
```csharp
class Program
{
	static void Main()
	{
		// Func<int, int, int> represents a method that takes two ints and returns an int
		Func<int, int, int> add = (a, b) => a + b;
		Console.WriteLine(add(3,4)); // 7

		// Action<string> represent a method that takes a string and returns void
		Action<string> greet = name => Console.WriteLine("Hello, " + name);
		greet("Alice"); // prints "Hello, Alice"
	}
}
```

### What is a Event?
An event is a special wrapper around a delegate that provides publish/subscribe semantics, the publisher exposes the event; subscribers attach handlers using +=, only the declaring class (or code inside it) can raise (invoke) the event. Subscribers cannot invoke directly -- this enforces encapsulation

#### Simple Event With EventHandler

```csharp
// Publisher
public class Alarm
{
	// Standard .NET delegate for events with no data: EventHandler
	public event EventHandler AlarmRaised;

	// protected virtual method to allow derived tyeps to eoverrride raise behavior
	protected virtual void OnAlarmRaised()
	{
		// Dave invocatin: use null-conditional operator to avoid race conditions
		AlarmRaised?.Invoke(this, EventArgs.Empty);
	}

	public void Raise()
	{
		Console.WriteLine("Publisher: Raising alarm...");
		OnAlarmRaised(); // Only publisher calls OnAlarmRaised to trigger the event
	}
}

// Subscriber
class Program
{
	static void Main()
	{
		var alarm = new Alarm();

		// Subscribe: attach a handler ot the event
		alarm.AlarmRaised += AlarmHandler;

		// Raised the event
		alarm.Raise();

		// Unsubscribe
		alarm.AlarmRaised -= AlarmHandler;
	}

	// Matches the EventHandler signature: void Handler(object sender, EventArgs e)
	static voind AlarmHandler(object sender, EventArgs e)
	{
		Console.WriteLine("Subscriber: Alarm received.");
	}
}
```

#### Simple Event With EventHandler with args

```csharp
// Custom EventArgs carryin event-specifc data.
// Make properties read-only and provide a constructor to set them.
public sealed class  AlarmEventArgs: EventArgs
{
	public int Level {get;}

	public string Message {get;}

	public AlarmEventArgs(int level, string message)
	{
		Level = level;
		Message = message ?? string.Empty;
	}
}

// Publisher
public class Alarm
{
	// Declare an event using the generic EventHandler<TEventArgs>.
	// Subscribers will receive AlarmEvnetArgs with each invocation.
	public event EventHandler<AlarmEventArgs> AlarmRaised;

	// Protected virtual method to allow derived classes to alter raising behavior.
	// It accepts AlarmEventArgs so even callers an supply custom data.
	protected virtual void OnAlarmRaised(AlarmEventArgs e)
	{
		// Safe invocation using the null-conditional operator
		// If thre are no subscribers, nothing happens.
		AlarmRaised?.Invoke(this, e);
	}

	// Public API to trigger the alarm; constructs the event args and raises the event.
	public void Raise(int level, string message)
	{
		Console.WriteLine("Publicher: Raising alarm...")
		var args = new AlarmEventArgs(level,message); // construct a custom EventArgs object
		OnAlarmRaised(args); // only the published raises the event
	}
}

// Subscriber
class Program
{
	static void Main()
	{
		// Subscribe a named method
		alarm.AlarmRaised += AlarmHandler;

		// subcribe an inline lambda handler (also receives AlarmEventArgs)
		alarm.AlarmRaised += (sender, e) =>
		{
			Console.WriteLine("Lambda subscriber: Alarm received. Level={e.Level}, Message='{e.Message}'");
		}

		// Raise the event with custom data, it will trigger both handlers because both are subscribed o the alarm event
		alarm.Raise(2, "Temperature above threshold");

		// Umsubscrive the named handler
		alarm.AlarmRaised -= AlarmHandler;

		// Raise again; only the lambda subscriber will run now
		alarm.Raise(5, "Critical failure");
	}

	// This method matches EventHandler<AlarmEventArgs> signature
	// voit Handler(object sender, AlarmeventArgs e)
	static void AlarmHandler(object sender, AlarmEventArgs s)
	{
		// We can read custom data  from e (Level and Messsage)
		Console.WriteLine("Subscriber: Alarm received. Level={e.Level}, Message='{e.Message}'");
	}
}
```

#### Remember this:
- Publisher: declares the event and raises it (calls Event?.Invoke(...)).
- Subscriber: provides handler(s) and attaches them with +=. Those handlers contain the logic executed when the event fires.
## 14. Exception Handling

Proper exception handling ensures  robust applications.
```csharp
// Custom exception
public class InsufficientFoundsException : Exception
{
	public decimal RequestedAmount {get;}
	public decimal AvailableAmount {get;}

	public InsufficientFundsException(decimal requested, decimal available)
		: base($"Insufficient funds. Requested: ${requested}, Available: ${available}");
	{
		RequestedAmount = requested;
		AvailableAmount = available;
	}
}

public class BankAccount
{
	private decimal _balance;

	public decimal Balance => _balance;

	public void Deposit(decimal amount)
	{
		if(amount <= 0)
		{
			throw new ArgumentException("Deposit amount must be positive",
				nameof(amount));
		}

		_balance += amount;
	}

	public void Withdraw(decimal amount)
	{
		if(amount <= 0)
		{
			throw new ArgumentException("Withdrawal amount must be positive",
				nameof(amount));
		}

		if(amount > _balance)
		{
			throw new InsufficientFundsException(amount, _balance);
		}
		
		_balance -= amount;
	}
}
```
## 15. Working with Null Values

C# provides various techniques to  handle null values safely.

For reference types  (classes, interfaces, delegates, arrays), a variable can point to an obbject  or to null (no object). For value types (int, bool, struct), variables normally always have a value. to allow "no value" for a value type you use Nullable or the shorthand T? (for example int?). 

```csharp
// Example A: NullReferenceException
class A
{
	public string Name; // default is null (for reference field)
}

class Program
{
	static void Main()
	{
		A a = new A();  // a is not null, but a.Name is null
		// The next line throws NullReferenceException at runtime:
		Console.WriteLine(a.Name.Length);
	}
}
```

```csharp
int? maybe = null;

// Check if it has value:
if (maybe.HasValue)
{
	Console.WriteLine(maybe.Value);
} else
{
	Console.WriteLine("No value (null)");
}

// Safe access with GetValueOrDefault;
int v = maybe.GetValueOrDefault(0); // returns 0 if maybe is null

// Null-coalescing with ??:
int v2 = maybe ?? 42; // if maybe is null use 42
Console.WriteLine(v2); // prints 42

// Assing a value only if a variable is null
string s = null;
s ??= "filled";
Console.Writeline(s); // "filled"
```

Null conditional operator (?) and null-conditional indexer (?[])
```csharp
string? maybe = null;
int? len = maybe?.Length;  // len is null (int?)
Console.WriteLine(len ?? 0);

string?[] arr = null;
int? count = arr?.Length;  // arr?.Length is null if arr is null
```

Combining ?. with ?? to produce non-null values
```csharp
string? maybeName = null;
int length = maybeName?.Length ?? 0; // safe: use 0 when maybeName is null
```


C# 8 introduced nullable reference types as compiler annotations the compiler warns you when you use a possible-null reference without handling it. Example:

```csharp
string? maybeNull = null; // allowed: nullable reference
string notNull = maybeNull; // WARNING: possible null assignment
```

```csharp
string? maybe = GetValue();
Console.WriteLine(maybe!.Length); // suppresses compiler warning; may still throw at runtime if maybe is null
```

## 16. Asynchronous Programming

Async/await pattern  for efficient asynchronous operations. It lets you perform work without blocking the calling thread (important for responsive UIs and scalable servers). 

The main building blocks are:
```csharp
// Task / Task<T>, async/await, and cooperative cancellation (CancellationToken).
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


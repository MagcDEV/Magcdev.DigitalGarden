## Lifetime of the services
#### AddTransient:
A new instance of the service is created every time it´s requested
#### AddScoped:
A new instance is created once per "scope". In ASP.NET Core, a scope typically means per HTTP request.
### AddSingleton:
Only one instance of the service is created for the entire lifetime of the application. This instance is shared across all request and scopes.

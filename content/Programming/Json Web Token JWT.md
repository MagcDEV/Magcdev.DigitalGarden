---
title: Json Web Token JWT
draft: false
tags:
  - Programming
  - Authentication
  - Authorization
---

# Understanding JSON Web Tokens (JWT)

JSON Web Tokens (JWT) are a compact, self-contained way to securely transmit information between parties as a JSON object. They consist of three parts:

1. **Header** - Contains token type and algorithm information
2. **Payload** - Contains claims (user data and metadata) 
3. **Signature** - Verifies the token's integrity

JWTs work by:
- Being generated on the server when authentication succeeds
- Getting signed with a secret key
- Being sent to the client who stores it
- Being included in subsequent request headers
- Getting validated on each request without needing to query a database

We use C# to create a little controller class **IdentityController.cs** to create a JWT to use for authorization and authentication.
## Line-by-Line Explanation of IdentityController.cs

```cs
using System.IdentityModel.Tokens.Jwt;    // Core JWT library
using System.Security.Claims;             // For working with claims
using System.Text;                        // For byte encoding
using System.Text.Json;                   // For JSON processing
using Microsoft.AspNetCore.Mvc;           // For API controller functionality
using Microsoft.IdentityModel.Tokens;     // For security token handling
```

These are the necessary imports for JWT processing and API controller functionality.

```cs
namespace Identity.Api.Controllers;

[ApiController]
public class IdentityController : ControllerBase
{
```

Defines the controller class with the `ApiController` attribute.

```cs
    private const string TokenSecret = "ForTheLoveOfGodStoreAndLoadThisSecurely";
    private static readonly TimeSpan TokenLifetime = TimeSpan.FromHours(8);
```

Defines the signing key (which should be stored securely, not hardcoded) and token expiration time.

```cs
    [HttpPost("token")]
    public IActionResult GenerateToken([FromBody] TokenGenerationRequest request)
    {
```

Creates an endpoint at POST `/token` that accepts a JSON request body.

```cs
        var tokenHandler = new JwtSecurityTokenHandler();
        var key = Encoding.UTF8.GetBytes(TokenSecret);
```

Initializes the JWT handler and converts the secret to bytes for signing.

```cs
        var claims = new List<Claim>
        {
            new(JwtRegisteredClaimNames.Jti, Guid.NewGuid().ToString()),  // Unique token ID
            new(JwtRegisteredClaimNames.Sub, request.Email),              // Subject (user)
            new(JwtRegisteredClaimNames.Email, request.Email),            // Email
            new("userid", request.UserId.ToString()),                     // Custom user ID claim
        };
```

Creates a list of standard claims to include in the token.

```cs
        foreach (var claimPair in request.CustomClaims)
        {
            var jsonElement = (JsonElement)claimPair.Value;
            var valueType = jsonElement.ValueKind switch
            {
                JsonValueKind.True => ClaimValueTypes.Boolean,
                JsonValueKind.False => ClaimValueTypes.Boolean,
                JsonValueKind.Number => ClaimValueTypes.Double,
                _ => ClaimValueTypes.String,
            };

            var claim = new Claim(claimPair.Key, claimPair.Value.ToString()!, valueType);
            claims.Add(claim);
        }
```

Processes any custom claims provided in the request, determining the correct data type for each.

```cs
        var tokenDescriptor = new SecurityTokenDescriptor
        {
            Subject = new ClaimsIdentity(claims),  // Claims about the user
            Expires = DateTime.UtcNow.Add(TokenLifetime), // When token expires
            Issuer = "https://id.magcdev.com", // Who issued the token
            Audience = "https://movies.magcdev.com", // Who the token is for
            SigningCredentials = new SigningCredentials(
                new SymmetricSecurityKey(key),   // Key for signing
                SecurityAlgorithms.HmacSha256Signature // Signing algorithm
            ),
        };
```

Creates a descriptor with all token parameters.

```cs
        var token = tokenHandler.CreateToken(tokenDescriptor);
        var jwt = tokenHandler.WriteToken(token);
        return Ok(jwt);
    }
}
```

Creates the JWT token, converts it to a string, and returns it in the HTTP response.

This is the token request model:

```json
{
    "userid": "d85b3b3e-3b7b-4b3b-8b3b-3b7b3b7b3b7b",
    "email": "manuel@gmail.com",
    "customClaims": {
        "admin": true,
        "trusted_member": true
    }
}
```

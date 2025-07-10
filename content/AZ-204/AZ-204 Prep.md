---
title: AZ-204 Prep
draft: false
tags:
  - example-tag
---

### What is Azure?
 Azure is a suite of online services for building, hosting, and delivering applications, operating from Microsoft's global data centers.

### Key Computing Services:
- Virtual Machines: are a service known as infrastructure-as-a-Service because they are traditional IT infrastructure components that are offered as a service for this reason they are the most logical way to perform a lift-and-shift operation.
- App Services
- Azure Kubernetes Service
- Azure Functions
- Azure Container Instances: Containers are somewhat like virtual machines except they don't include the operating system. This make it easy to deploy them because they are very lightweight compared to virtual machines. 

### Storage Options:
- Blob Storage
- File Storage
- Data Lake Storage Gen2

### Relational Databases
- SQL Database
- Azure Database for MySQL
- Azure Database for MariaDB
- Azure Database for PostgreSQL

### No-SQL
- Cosmos DB
- Azure Cache for Redis

### Networking Features
- Virtual Networks (VNets)
- VNet Peering
- VPN
- Azure ExpressRoute
- Azure Traffic Manager: provide a load balancing for VMs or web apps that are distributed across multiple regions.

### Azure Migrate

### Entra ID

### Azure DevOps

### Azure Content Delivery Network

### IoT services
- Azure IoT Central
- IoT Hub
- Azure Sphere: it provides its own certified chips, operating system, and security service to increase the security for IoT devices.

### Data Analytics Services
- Azure Databricks
- Synapse Analytics
- HDInsight (Apache Spark)

### Azure logic Apps

### Azure Monitor

### Microsoft Defender for Cloud
- Scores: for example a secure score int Microsoft defender indicates the general security health of your Azure resources. The more secure your environment is, the higher the percentage score will be.
- Azure Policy: Defender is connected to Azure Policy this allows you to create compliance requirements for accounts and resources within you Azure account.

### Deployment automation
- Azure Resource Manager Templates
- Blueprints

### Access to Azure
- Portal
- CLI
- PowerShell
- SDK
- Mobile app
- Cloud Shell

### Azure accounts
- Billing accounts
- Subscriptions
- Resource Groups

### High availability

## Azure App Service

### Pricing Tiers

- Free and Shared: offer limited resources and shared VMs, suitable for development and testing.
- Basic: Provides dedicated VMs with more resources.
- Standard: Adds autoscaling capabilities.
- Premium: Offers Enhanced resources and up to 30 VM instances.
- Isolated: provides a private virtual network with up to 100 VM instances.

Multiples apps can share a services plan, but excessive apps may lead to performance issues, which can be mitigated by **scaling out** (adding more VM instances) or **scaling up** (switching to a higher tier).

### Scaling

- Scaling up resources involves switching to a higher pricing tire, but it´s not dynamic for varying usage patterns.
- Scaling out/in adds or removes virtual machines based on app demand, available on Basic plans and higher.
- Autoscaling, which automates scaling without manual intervention, is available on Standard plans and higher.
- **Azure Monitor**: Manages autoscaling allowing users to set scale conditions and rules bases on metrics like CPU and memory usage.
- Users can defines rules for scaling out/in, set metrics, and determine actions like adding or removing VM instances.
- A "cool down" period prevents rapid scaling changes, allowing metrics to stabilize.
- Multiple rules can be set, with scale-out rules taking precedence over scale-in rules to ensure resource availability.
- Autoscaling can also be scheduled, allowing scaling to a specific instance count at set times or days.
- Users can combine metric-based and schedule-bases scaling without conflicts by setting them for different times.

### Using Deployment Slots in Azure App

- Deployment slots allow for testing new app version in environments similar to production before going live.
- By default, apps have a "Production" slot, but additional slots like "testing" and "staging" can be created
- Cloning the production slot to a staging slot helps maintain similar configurations, enhancing testing validity.
- New app versions are uploaded to the staging slot, not cloned, and require the "az webapp deployment source".
- After testing, the staging slot can be swapper with the production slot, transferring app versions and settings, except for slot-specific settings.
- Slot-specific settings, like separate  test databases, remain with their respective slots during swaps.
- Swapping slots minimizes downtime by allowing VM instances to warm up and provides an easy rollback option if issues arises.
- The "swap with preview" options allows testing with production settings before completing a swap, enhancing safety.
- "Auto swap" can automate deployments as part of a DevOps process, but staging slots allow for app warm-up before production.
- Custom warm-up configurations can be sets for apps needing initialization before serving user requests.
- More than two slots can be used for complex configurations, such as development, testing, staging, and production.
- Canary testing is supported by directing a small percentage of traffic to non-production slots to minimize deployment risks.
- The number of slots available depends on the App Service Plan tier, with Standard supporting up to 5 slots and Premium/Isolated up to 20.
---
- **Auto Swap**: As soon as an application is deployed to a slot it automatically swaps into a target slot. This is not the same as deploying directly to the target because the application gets a warm start, and the previous release of the target slot is preserved if a rollback is required.
- **Swap**: The most basic swap type that requires you to manually trigger the swap operation.
- **Swap with preview**: This type is similar to a regular swap but allows you to preview the swap before completing it. Because each slot maintains its own configuration and application settings, the web app may not behave exactly as it did in the originating slot, and that is a good thing.
---

Application Insights is an application performance management (APM) service. Some of the features of Application Insights include the ability to:

- Find and diagnose performance issues
- Find and diagnose runtime exceptions
- Monitor and alert on application health
- Analyze customer usage
- Create custom key performance indicator (KPI) dashboards
---

### Deploying Code from GitHub to Azure App Service
This file contains URLs from the demos in Cloud Academy's _Deploying Code from GitHub to Azure App Service_ course.  

#### Create a resource group
```
az group create --name webapprg --location westus
```

#### Create an App Service Plan
```
az appservice plan create --name asplan --resource-group webapprg --location westus --sku F1
```

#### Create a webapp
```
az webapp create --name <app_name> --resource-group webapprg --plan asplan
```

#### Deploy an app from GitHub to Azure App Service
```
az webapp deployment source config --repo-url https://github.com/Azure-Samples/html-docs-hello-world --branch master --manual-integration --name <app_name> --resource-group webapprg
```

#### URL of webapp
https://<app_name>.azurewebsites.net

---

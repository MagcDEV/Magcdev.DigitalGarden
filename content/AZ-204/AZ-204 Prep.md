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
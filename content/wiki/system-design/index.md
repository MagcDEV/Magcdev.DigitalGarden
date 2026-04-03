---
title: "System Design"
tags:
  - wiki
  - system-design
---

# System Design

## Fundamentals

- [[wiki/system-design/scalability|Scalability (Horizontal vs Vertical)]]
- [[wiki/system-design/cap-theorem|CAP Theorem]]
- [[wiki/system-design/consistency-patterns|Consistency Patterns]]
- [[wiki/system-design/availability-patterns|Availability Patterns]]
- [[wiki/system-design/load-balancing|Load Balancing]]
- [[wiki/system-design/caching|Caching Strategies]]
- [[wiki/system-design/cdn|Content Delivery Networks]]
- [[wiki/system-design/dns|DNS & Domain Resolution]]

## Data Layer

- [[wiki/system-design/sql-vs-nosql|SQL vs NoSQL]]
- [[wiki/system-design/database-sharding|Database Sharding]]
- [[wiki/system-design/replication|Database Replication]]
- [[wiki/system-design/indexing|Indexing Strategies]]
- [[wiki/system-design/data-partitioning|Data Partitioning]]

## Communication

- [[wiki/system-design/rest-vs-grpc|REST vs gRPC vs GraphQL]]
- [[wiki/system-design/message-queues|Message Queues (Kafka, RabbitMQ)]]
- [[wiki/system-design/websockets|WebSockets & Real-Time Communication]]
- [[wiki/system-design/api-gateway|API Gateway Pattern]]

## Infrastructure

- [[wiki/system-design/microservices|Microservices Architecture]]
- [[wiki/system-design/rate-limiting|Rate Limiting]]
- [[wiki/system-design/circuit-breaker|Circuit Breaker Pattern]]
- [[wiki/system-design/observability|Observability (Logs, Metrics, Traces)]]
- [[wiki/system-design/containers|Containers & Orchestration]]

## Classic Design Problems

- [[wiki/system-design/url-shortener|Design: URL Shortener]]
- [[wiki/system-design/rate-limiter-design|Design: Rate Limiter]]
- [[wiki/system-design/chat-system|Design: Chat System]]
- [[wiki/system-design/news-feed|Design: News Feed]]
- [[wiki/system-design/notification-system|Design: Notification System]]
- [[wiki/system-design/distributed-cache|Design: Distributed Cache]]
- [[wiki/system-design/search-autocomplete|Design: Search Autocomplete]]

## Framework

> [!tip] System Design Interview Framework
> 1. **Clarify requirements** (functional + non-functional)
> 2. **Back-of-envelope estimation** (QPS, storage, bandwidth)
> 3. **High-level design** (API + data model + architecture diagram)
> 4. **Deep dive** (pick 2-3 components to detail)
> 5. **Bottlenecks & trade-offs** (what breaks at 10x scale?)

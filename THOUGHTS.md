## 1. How do you prevent duplicate readings?

Duplicate readings are prevented using a database-level unique constraint on the combination of (device, timestamp).  
In addition, during data ingestion, `get_or_create()` is used so that if a reading for the same device and timestamp already exists, it will not be inserted again.  
This makes the import process idempotent and safe to run multiple times.

---

## 2. How does your code fetch the latest reading per device?

Readings are stored with a timestamp and queried in descending order using `order_by('-timestamp')`.  
The latest reading is obtained by selecting the first record from the ordered queryset.  
This ensures the most recent reading is returned regardless of insertion order.

---

## 3. What happens if readings are inserted out of order?

Out-of-order inserts do not affect correctness because ordering is handled at query time.  
Even if older readings are inserted after newer ones, queries explicitly sort by timestamp, ensuring accurate results when fetching the latest or historical data.

---

## 4. What part of your solution would break first at large scale?

The database layer would become the first bottleneck.  
SQLite is not designed for high write throughput or large datasets, and querying large time-series data without proper indexing or partitioning would degrade performance.

---

## 5. What is the best way to handle the timeseries data?

For large-scale production systems, a time-series optimized database such as PostgreSQL with TimescaleDB or partitioned tables should be used.  
These systems support efficient range queries, indexing by time, and better storage optimization for time-series data.

---

## 6. If this Django project were deployed using Docker, which components would you place in separate containers and why?

I would separate the Django application, database, and background worker into different containers.  
This allows independent scaling, better isolation, and easier maintenance.  
Each component can be updated or scaled without affecting others.

---

## 7. Why is Django’s runserver not suitable for production usage?

Django’s runserver is intended only for development.  
It is single-threaded, not optimized for performance, lacks robust security features, and cannot handle high traffic reliably.  
Production environments require servers like Gunicorn or uWSGI.

---

## 8. How would you manage environment variables in a Docker-based deployment?

Environment variables would be managed using `.env` files, Docker environment variables, or secret management tools.  
Sensitive information such as secret keys and database credentials should never be hardcoded in the codebase.

---

## 9. What problems does Docker solve compared to running Django directly on a virtual machine?

Docker ensures consistency across environments, simplifies dependency management, and improves deployment reliability.  
It allows applications to run the same way in development, testing, and production, reducing “it works on my machine” issues.

---

## 10. Which part of this system would you scale first under increased load, and why?

The database would be scaled first because it handles all read and write operations.  
As data volume grows, database performance becomes critical for API response times and overall system stability.

---

## 11. What kind of tasks in this project would be suitable to run using Celery, and why?

Tasks such as bulk CSV imports, data aggregation, report generation, and cleanup jobs are suitable for Celery.  
These tasks are time-consuming and can be processed asynchronously without blocking API responses.

---

## 12. Which tasks should NOT be handled by Celery?

Simple request-response logic, validation, and lightweight database queries should not be handled by Celery.  
These operations should remain synchronous to keep the application logic simple and predictable.

---

## 13. What happens if a Celery task fails halfway through execution?

If a Celery task fails, it can be retried automatically based on configuration or marked as failed.  
Proper error handling and idempotent task design help ensure partial failures do not corrupt data.

---

## 14. Where would task results or progress be stored, if needed?

Task results or progress can be stored in a result backend such as Redis or a database.  
This allows tracking task status, progress updates, and debugging failed tasks if required.

---

## 15. How does Celery improve scalability compared to running everything inside Django views?

Celery moves long-running and resource-intensive tasks out of the request-response cycle.  
This keeps Django views fast, improves user experience, and allows background tasks to scale independently using worker processes.

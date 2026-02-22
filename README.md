
🚀 CodeForge: Polyglot DSA Practice Platform
A high-performance microservices platform for practicing Data Structures and Algorithms. The system supports multiple languages (Java, Python, JavaScript) using a distributed worker architecture powered by Apache Kafka.
🏗️ Project Architecture
Main Backend: Spring Boot (API Gateway, User & Problem Management, PostgreSQL).
Message Broker: Apache Kafka (KRaft mode) for task distribution.
Workers:
Java Worker: Spring Boot service for executing Java code.
Python Worker: Dockerized Python runtime for script execution.
Node Worker: Node.js environment for JavaScript execution.
🛠️ Prerequisites
Docker Desktop (Installed and running)
Postman (For API testing)
🚀 Getting Started
1. Build and Start the Entire Cluster
This command builds the images for all workers and the backend, then starts them in the background.
powershell
docker-compose up --build -d
Use code with caution.

2. Verify Services are Running
Check the status of all 5 containers (Kafka, Backend, 3 Workers):
powershell
docker-compose ps
Use code with caution.

3. View Live Logs (Highly Recommended)
Watch the communication between the Main Backend and the Workers in real-time:
powershell
docker-compose logs -f
Use code with caution.

🧪 Testing the API
Use Postman to send a code submission.
Endpoint: POST http://localhost:8080/api/submissions/run
Body (JSON):
json
{
  "problemId": "YOUR_PROBLEM_UUID",
  "language": "PYTHON",
  "code": "print('Hello from the Python Worker!')"
}
Use code with caution.

🛑 Management Commands
Stop All Services
Stops the containers but keeps the images and data.
powershell
docker-compose stop
Use code with caution.

Stop and Remove Everything
Stops the containers and removes the internal Docker network. Use this for a clean reset.
powershell
docker-compose down
Use code with caution.

Restart a Specific Worker
If you change code in only the Python worker, you can restart just that container:
powershell
docker-compose up --build -d python-worker
Use code with caution.

📁 Project Structure
text
CODE_FORGE_BACKEND/
├── code_forge_backend/   # Main Spring Boot API
├── java-worker/          # Java Execution Service
├── node_worker/          # JavaScript Execution Service
├── python_worker/        # Python Execution Service
└── docker-compose.yml    # System Orchestrator
Use code with caution.

Pro-Tip: After running docker-compose up, wait about 30 seconds for Kafka to show as (healthy) in Docker Desktop before sending your first request.
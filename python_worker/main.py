import json
import subprocess
from kafka import KafkaConsumer

# 1. Configure Kafka Consumer
consumer = KafkaConsumer(
    'python-tasks',
    bootstrap_servers=['kafka:9092'], # Connects to the 'kafka' service in docker-compose
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Python Worker is ready and waiting for code...")

for message in consumer:
    task = message.value
    code = task.get('code')
    print(f"Executing: {task.get('title')}")

    # 2. Write code to a temporary file
    with open("solution.py", "w") as f:
        f.write(code)

    # 3. Run the code and capture output
    try:
        result = subprocess.run(
            ["python", "solution.py"], 
            capture_output=True, 
            text=True, 
            timeout=5
        )
        print("Output:", result.stdout if result.stdout else result.stderr)
    except subprocess.TimeoutExpired:
        print("Error: Time Limit Exceeded")

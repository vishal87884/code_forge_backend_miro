const { Kafka } = require('kafkajs');

// Configure Kafka connection to use the Docker service name 'kafka'
const kafka = new Kafka({
  clientId: 'node-worker',
  brokers: [process.env.KAFKA_BROKER || 'kafka:9092']
});

const consumer = kafka.consumer({ groupId: 'node-group' });

const run = async () => {
  await consumer.connect();
  // Subscribe to the JavaScript tasks topic
  await consumer.subscribe({ topic: 'js-tasks', fromBeginning: true });

  await consumer.run({
    eachMessage: async ({ message }) => {
      const payload = JSON.parse(message.value.toString());
      console.log(`[node-worker] Received Task: ${payload.title}`);
      
      // Add your safe code execution logic here (e.g., using 'vm' module)
      console.log("Code to run:", payload.code);
    },
  });
};

run().catch(e => console.error(`[node-worker] Error: ${e.message}`, e));

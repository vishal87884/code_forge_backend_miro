package code.forge.java.worker;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@SpringBootApplication
public class JavaWorkerApplication {
    public static void main(String[] args) {
        SpringApplication.run(JavaWorkerApplication.class, args);
    }
}

@Service
class CodeExecutionService {
    @KafkaListener(topics = "java-tasks", groupId = "java-worker-group")
    public void listen(String message) {
        System.out.println("Received Java Code: " + message);
        // TODO: Compile and Execute logic
    }
}

import csv


questions_answers = [
    ["What is monolithic architecture?", "An architecture where all components of an application are in a single codebase."],
    ["What is microservices architecture?", "An architecture where an application is divided into small, independent services."],
    ["What is a key advantage of microservices?", "Scalability and independent deployment of services."],
    ["What is a major drawback of monolithic architecture?", "Difficulty in scaling and updating specific parts of the system."],
    ["How are services in microservices architecture communicated?", "Via APIs, often using REST or messaging queues."],
    ["What is a common challenge with microservices?", "Managing inter-service communication and data consistency."],
    ["What is the deployment model for monolithic architecture?", "A single deployable unit."],
    ["How do microservices handle failures?", "Using strategies like retries, circuit breakers, and service isolation."],
    ["What is an example of a tool used to orchestrate microservices?", "Kubernetes or Docker Swarm."],
    ["Which architecture is better suited for small applications?", "Monolithic architecture due to its simplicity."],
]

# Creating the CSV file
csv_file_path = "D:/csv file creator/SDA qs.csv"
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["question", "answer"])
    writer.writerows(questions_answers)

csv_file_path

from locust import HttpUser, task, between
import uuid

class MyUser(HttpUser):
    host = "http://k8s-default-webingre-99128f9312-1530015987.ap-south-1.elb.amazonaws.com"
    wait_time = between(1, 3)

    @task
    def generate_text(self):
        # Generate a unique prompt for each request
        unique_prompt = f"AI is better than Full Stack {uuid.uuid4()}"
        form_data = {
            "prompt": unique_prompt
        }
        self.client.post("/generate-text", data=form_data)

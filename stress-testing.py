from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # You can adjust the wait time as needed

    @task
    def generate_text(self):
        url = "/generate?inp_text=AI%20is%20better%20than%20Full%20Stack"

        # make a POST request to the API
        self.client.post(url)


     
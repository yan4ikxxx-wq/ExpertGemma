import json
import time

class Gemma4Config:
    def __init__(self, mode="coding"):
        self.model_id = "gemma-4-26b-a4b-it"
        self.target_rpm = 15
        self.last_request_time = 0

        # Dynamic mode selection based on expert feedback
        if mode == "coding":
            self.temperature = 0.2  # High determinism for logic
            self.top_p = 0.90
        else:
            self.temperature = 0.7  # Balanced for general tasks
            self.top_p = 0.95

        self.top_k = 40
        self.max_output_tokens = 4096

    def _rate_limit(self):
        """Simple implementation of the RPM logic."""
        elapsed = time.time() - self.last_request_time
        wait_time = 60 / self.target_rpm
        if elapsed < wait_time:
            time.sleep(wait_time - elapsed)
        self.last_request_time = time.time()

    def generate_payload(self, user_query, system_context=""):
        self._rate_limit()  # Active use of RPM setting

        prompt = f"<|system|>\n{system_context}\n<|user|>\n{user_query}\n<|thought|>\n"

        return {
            "model": self.model_id,
            "contents": [{"parts": [{"text": prompt}]}],
            "generation_config": {
                "temperature": self.temperature,
                "top_p": self.top_p,
                "top_k": self.top_k,
                "max_output_tokens": self.max_output_tokens
            }
        }

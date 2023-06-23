from cog import BasePredictor, Input
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

device = "cuda"

class Predictor(BasePredictor):
    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""
        base_model = "WizardLM/WizardCoder-15B-V1.0"
        self.tokenizer = AutoTokenizer.from_pretrained(base_model, cache_dir="cache")
        self.model = AutoModelForCausalLM.from_pretrained(base_model, device_map="auto", load_in_4bit=True, cache_dir="cache")
        self.model.config.pad_token_id = self.tokenizer.pad_token_id

    def predict(self,
        prompt: str = Input(description="Instruction for the model"),
        max_new_tokens: int = Input(description="max tokens to generate", default=48),
        temperature: float = Input(description="0.1 to 2.5 temperature", default=0.2),
    ) -> str:    
        inputs = self.tokenizer.encode(prompt, return_tensors="pt").to(device)
        outputs = self.model.generate(
            inputs, max_new_tokens=max_new_tokens, temperature=temperature
        )
        output = self.tokenizer.decode(outputs[0])
        print(output)

        return output
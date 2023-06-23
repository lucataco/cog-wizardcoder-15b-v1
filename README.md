# WizardCoder COG

Attempt at quantized cog for [WizardLM/WizardCoder-15B-V1.0](https://huggingface.co/WizardLM/WizardCoder-15B-V1.0).

## Run

`cog build -t wizardcoder`

`docker run -d -p 5000:5000 --gpus all wizardcoder`

## Test

### Input

`curl http://localhost:5000/predictions -X POST -H 'Content-Type: application/json' -d '{"input": {"prompt":"//Python function that determines if a given number x is prime"}}'`

### Output

`{"input":{"prompt":"//Python function that determines if a given number x is prime","max_new_tokens":48,"temperature":0.2},"output":"//Python function that determines if a given number x is prime or not.\r\ndef is_prime(x):\r\n    if x < 2:\r\n        return False\r\n    for i in range(2, int(x**0.5) + 1):\r\n        if x % i ==","id":null,"version":null,"created_at":null,"started_at":"2023-06-23T21:50:57.768717+00:00","completed_at":"2023-06-23T21:51:09.981636+00:00","logs":"//Python function that determines if a given number x is prime or not.\ndef is_prime(x):\nif x < 2:\nreturn False\nfor i in range(2, int(x**0.5) + 1):\nif x % i ==\n","error":null,"status":"succeeded","metrics":{"predict_time":12.212919},"webhook":null,"webhook_events_filter":["logs","completed","start","output"],"output_file_prefix":null}`

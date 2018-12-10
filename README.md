# Pourover Coffee Micro Service
- Docker compatible
- Required
  - Flask
  - flask_restful

## Ratio override
pourover.py --ratio ##

## Usage
`curl -X POST http://127.0.0.1:5000/pourover?coffee=20`

`{"water grams": 400, "coffee grams": 20}`

`curl -X POST http://127.0.0.1:5000/pourover?water=20`

`{"water grams": 591.4, "coffee grams": 29.57}` 

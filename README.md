# HDLTestAI

HDLTestAI is an AI-powered tool that automatically generates SystemVerilog testbenches for Verilog and SystemVerilog modules using the OpenAI API.

The tool reads a hardware design file, sends the module to an LLM with verification-specific instructions, and saves the generated testbench as a new SystemVerilog file.

---

## Features

- Generate SystemVerilog testbenches using AI
- Supports Verilog (`.v`) and SystemVerilog (`.sv`) source files
- Automatically validates the input file
- Automatically creates an output directory for generated testbenches
- Saves generated testbenches with descriptive filenames
- Uses the OpenAI Python SDK
- Securely loads the API key from an environment variable

---

## Project Structure

```
hdl-test-ai/
│
├── designs/                   # Input Verilog/SystemVerilog modules
├── generated_testbenches/     # AI-generated testbenches
├── testbenches/               # Hand-written reference testbenches
├── generate_testbench.py      # AI testbench generator
├── run_test.py                # Compile and run simulations
├── .gitignore
└── README.md
```

---

## Requirements

- Python 3.9+
- OpenAI Python SDK
- Icarus Verilog

Install Python dependencies:

```bash
pip install openai
```

Install Icarus Verilog:

https://bleyer.org/icarus/

---

## Setup

Create an OpenAI API key:

https://platform.openai.com/api-keys

Store the key as an environment variable named:

```
OPENAI_API_KEY
```

---

## Usage

Run the generator:

```bash
python generate_testbench.py
```

Enter the path to a Verilog or SystemVerilog design when prompted.

Example:

```
designs/adder.sv
```

The generated testbench will be saved in:

```
generated_testbenches/
```

Example output:

```
generated_testbenches/generated_adder_tb.sv
```

---

## Current Workflow

```
User selects HDL module
            │
            ▼
Validate file
            │
            ▼
Read module
            │
            ▼
Generate AI prompt
            │
            ▼
OpenAI API
            │
            ▼
Generate SystemVerilog testbench
            │
            ▼
Save generated testbench
```

---

## Example

Input:

```systemverilog
module adder(
    input logic [3:0] a,
    input logic [3:0] b,
    output logic [4:0] sum
);

assign sum = a + b;

endmodule
```

Output:

- Automatically generated SystemVerilog testbench
- Exhaustive input testing
- Pass/fail reporting
- Clock generation (when applicable)

---

## Technologies Used

- Python
- OpenAI API
- SystemVerilog
- Verilog
- Icarus Verilog
- Git
- GitHub

---

## License

This project is licensed under the MIT License.
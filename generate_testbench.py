from pathlib import Path
from openai import OpenAI

# Create OpenAI client
client = OpenAI()

# Ask user for filepath
user_input = input("Please enter the file path: ")

file_path = Path(user_input)

# Create output file
output_filename = "generated_" + file_path.stem + "_tb" + file_path.suffix

full_path = Path("generated_testbenches") / output_filename
full_path.parent.mkdir(parents=True, exist_ok=True)

if file_path.is_file():
    if  file_path.suffix == '.sv' or file_path.suffix == '.v':
        # Open the file for reading
        with open(file_path) as f:
            content = f.read()
    else:
        print("Please provide a Verilog or SystemVerilog source file.")
else:
    print("The file does not exist.")

system_role = "You are a senior verification engineer specializing in SystemVerilog testbench creation and debugging."

task_instructions = (
    "Generate a SystemVerilog testbench for the following module.\n"
    "Requirements:\n"
    "- Instantiate the DUT\n"
    "- Generate a clock\n"
    "- Apply all input combinations\n"
    "- Print pass/fail counts. If a test fails, specify which line and condition."
    "- Call $finish"
    "- Return only raw SystemVerilog code. Do not include Markdown. Do not use triple backticks. Do not include explanations or comments outside the code."
    "Module to test:\n"
)

prompt = f"""""

Instructions:
{task_instructions}

Module:
{content}
"""

response = client.responses.create(
    model = "gpt-4.1-mini",
    instructions = system_role,
    input = prompt  
)

full_path.write_text(response.output_text)
print(f"Saved generated testbench to:\n{full_path}")
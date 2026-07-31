import subprocess

adder_pieces = [
    "iverilog",
    "-g2012",
    "-o",
    "outputs/adder_tb",
    "designs/adder.sv",
    "testbenches/adder_tb.sv"
]

compilation = subprocess.run(adder_pieces, capture_output=True, text=True)

if compilation.returncode == 0:
    adder_run = [
        "vvp",
        "outputs/adder_tb"
    ]
    run = subprocess.run(adder_run, capture_output=True, text=True)
    if run.returncode == 0:
        if "Failed: 0" in run.stdout:
            print("All tests passed")
        else:
            print("Tests failed")
            print("STDOUT:", run.stdout)
    else:
        print("STDOUT:", run.stdout)
        print("STDERR:", run.stderr)
        print("Code:", run.returncode) 
else:
    print("STDOUT:", compilation.stdout)
    print("STDERR:", compilation.stderr)
    print("Code:", compilation.returncode)


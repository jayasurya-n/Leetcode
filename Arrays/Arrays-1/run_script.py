import sys,os
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_script.py <script_name.py>")
        return

    script_name = sys.argv[1]

    # Check if the script file exists
    if not os.path.isfile(script_name):
        print(f"Error: File '{script_name}' not found.")
        return

    # Read input from input.txt
    with open('input.txt', 'r') as infile:
        input_data = infile.read()

    # Execute the script and capture the output
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            input=input_data,
            text=True,
            capture_output=True,
            check=True
        )
        # Write the output to output.txt
        with open('output.txt', 'w') as outfile:
            outfile.write(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e.stderr}")

if __name__ == "__main__":
    main()

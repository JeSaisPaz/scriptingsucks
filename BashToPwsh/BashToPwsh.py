import re
import sys

def convert_line(line):
    stripped = line.strip()

    if stripped.startswith("#!") and "bash" in stripped:
        return None

    if stripped.startswith("#"):
        return stripped

    line = re.sub(r'\becho\b', 'Write-Output', line)

    line = re.sub(r'\bls\b', 'Get-ChildItem', line)

    line = re.sub(r'\bcd\b', 'Set-Location', line)

    line = re.sub(r'\$(\w+)', r'$env:\1', line)

    if re.match(r'\s*if\s+\[.*\];?\s*', line):
        line = re.sub(r'\s*if\s+\[(.*)\];?', r'if (\1) {', line)
        line = line.replace("=", "-eq").replace("!=", "-ne")

    elif re.match(r'\s*elif\s+\[.*\];?\s*', line):
        line = re.sub(r'\s*elif\s+\[(.*)\];?', r'} elseif (\1) {', line)
        line = line.replace("=", "-eq").replace("!=", "-ne")

    elif re.match(r'\s*else\s*', line):
        line = "} else {"

    elif re.match(r'\s*fi\s*', line):
        line = "}"

    elif re.match(r'\s*for\s+(\w+)\s+in\s+(.*);?\s*', line):
        match = re.match(r'\s*for\s+(\w+)\s+in\s+(.*);?', line)
        var, values = match.groups()
        values = values.strip().replace(";", "")
        line = f"foreach (${var} in {values}) {{"

    elif re.match(r'\s*done\s*', line):
        line = "}"

    return line.strip()


def bash_to_powershell(input_file, output_file):
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        for line in fin:
            converted = convert_line(line)
            if converted is not None:
                fout.write(converted + "\n")

    print(f"✅ Converted '{input_file}' to '{output_file}'")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bash_to_ps1.py input.sh output.ps1")
        sys.exit(1)

    bash_to_powershell(sys.argv[1], sys.argv[2])

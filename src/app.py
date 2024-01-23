from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

PACKAGES = {
    "Additional vCPU": {"vcpu": 1, "ram": 0},
    "Additional vRAM": {"vcpu": 0, "ram": 1},
    "Pool Small": {"vcpu": 8, "ram": 32},
    "Pool Medium": {"vcpu": 16, "ram": 64},
    "Pool Large": {"vcpu": 32, "ram": 128},
    "Pool XLarge": {"vcpu": 64, "ram": 256}
}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    vcpu_required = data.get('vcpu')
    ram_required = data.get('ram')
    result = calculate_packages(vcpu_required, ram_required)
    return jsonify(result)

def calculate_packages(vcpu, ram):
    result = {}
    total_vcpu = 0
    total_ram = 0
    # Sort the packages by 'vcpu' and 'ram' in descending order
    sorted_packages = sorted(PACKAGES.items(), key=lambda item: (-item[1]['vcpu'], -item[1]['ram']))
    
    for package_name, package_info in sorted_packages:
        while vcpu >= package_info['vcpu'] and ram >= package_info['ram']:
            vcpu -= package_info['vcpu']
            ram -= package_info['ram']
            total_vcpu += package_info['vcpu']
            total_ram += package_info['ram']
            result[package_name] = result.get(package_name, 0) + 1


    # Always show the total vcpu and ram
    result['Total vCPU'] = total_vcpu
    result['Total RAM'] = total_ram

    return result

@app.route('/package_calculator', methods=['GET'])
def package_calculator_form():
    return render_template('package_calculator.html', packages=PACKAGES)

@app.route('/package_calculator', methods=['POST'])
def package_calculator():
    data = request.get_json()
    total_vcpu = 0
    total_ram = 0
    for package_name, package_info in PACKAGES.items():
        count = int(data.get(package_name, 0))
        total_vcpu += count * package_info['vcpu']
        total_ram += count * package_info['ram']
    return jsonify({'total_vcpu': total_vcpu, 'total_ram': total_ram})

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
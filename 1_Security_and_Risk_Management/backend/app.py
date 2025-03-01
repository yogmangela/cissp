import json
import boto3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure boto3 client for LocalStack S3 service
s3 = boto3.client('s3', endpoint_url='http://localstack:4566')

def calculate_cvss(impact, exploitability):
    impact_scores = {"High": 10.0, "Medium": 7.0, "Low": 4.0}
    exploitability_scores = {"High": 2.0, "Medium": 1.5, "Low": 1.0}
    
    impact_score = impact_scores.get(impact, 0)
    exploitability_score = exploitability_scores.get(exploitability, 0)
    
    cvss_score = impact_score * exploitability_score
    return round(cvss_score, 1)

@app.route('/api/cvss', methods=['POST'])
def cvss():
    data = request.get_json()
    vulnerability_name = data.get("vulnerabilityName")
    impact = data.get("impact")
    exploitability = data.get("exploitability")

    if not vulnerability_name or not impact or not exploitability:
        return jsonify({"error": "Missing data"}), 400

    score = calculate_cvss(impact, exploitability)

    # Save the result to S3 (LocalStack)
    s3.put_object(
        Bucket="vulnerability-reports-bucket",
        Key=f"{vulnerability_name}_report.json",
        Body=json.dumps({"vulnerability_name": vulnerability_name, "cvss_score": score}),
    )

    return jsonify({"cvssScore": score})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
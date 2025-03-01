import React, { useState } from "react";

function App() {
  const [vulnerabilityName, setVulnerabilityName] = useState("");
  const [impact, setImpact] = useState("High");
  const [exploitability, setExploitability] = useState("High");
  const [cvssScore, setCvssScore] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch("http://localhost:5000/api/cvss", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        vulnerabilityName,
        impact,
        exploitability,
      }),
    });
    const data = await response.json();
    setCvssScore(data.cvssScore);
  };

  return (
    <div className="App">
      <h1>Risk Assessment Tool</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Vulnerability Name</label>
          <input
            type="text"
            value={vulnerabilityName}
            onChange={(e) => setVulnerabilityName(e.target.value)}
          />
        </div>
        <div>
          <label>Impact</label>
          <select value={impact} onChange={(e) => setImpact(e.target.value)}>
            <option value="High">High</option>
            <option value="Medium">Medium</option>
            <option value="Low">Low</option>
          </select>
        </div>
        <div>
          <label>Exploitability</label>
          <select
            value={exploitability}
            onChange={(e) => setExploitability(e.target.value)}
          >
            <option value="High">High</option>
            <option value="Medium">Medium</option>
            <option value="Low">Low</option>
          </select>
        </div>
        <button type="submit">Submit</button>
      </form>

      {cvssScore && (
        <div>
          <h2>CVSS Score: {cvssScore}</h2>
        </div>
      )}
    </div>
  );
}

export default App;
import axios from 'axios';
import React, { useState } from 'react';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    pain: 0,
    weightGain: 'None',
    cycleDelay: 'Regular',
    acne: 'None',
    polycysticOvaries: 0,
    excessiveHairGrowth: 'None',
    scalpHairLoss: 0,
    infertility: 0,
    darkSkinPatches: 0
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: isNaN(value) ? value : Number(value)
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://127.0.0.1:5001/predict', formData);
      setResult(res.data.result);
    } catch (error) {
      console.error("Prediction error:", error);
      setResult("Prediction failed. Check console.");
    }
  };

  return (
    <div className="container">
      <h1>PCOS Detection Model</h1>
      <form onSubmit={handleSubmit}>
        <label>Pain</label>
        <select name="pain" value={formData.pain} onChange={handleChange}>
          <option value={0}>No</option>
          <option value={1}>Yes</option>
        </select>

        <label>Weight Gain</label>
        <select name="weightGain" value={formData.weightGain} onChange={handleChange}>
          <option>None</option>
          <option>Mild</option>
          <option>Severe</option>
        </select>

        <label>Cycle Delay</label>
        <select name="cycleDelay" value={formData.cycleDelay} onChange={handleChange}>
          <option>Regular</option>
          <option>Irregular</option>
          <option>Absent</option>
        </select>

        <label>Acne</label>
        <select name="acne" value={formData.acne} onChange={handleChange}>
          <option>None</option>
          <option>Moderate</option>
          <option>Severe</option>
        </select>

        <label>Polycystic Ovaries</label>
        <select name="polycysticOvaries" value={formData.polycysticOvaries} onChange={handleChange}>
          <option value={0}>No</option>
          <option value={1}>Yes</option>
        </select>

        <label>Excessive Hair Growth</label>
        <select name="excessiveHairGrowth" value={formData.excessiveHairGrowth} onChange={handleChange}>
          <option>None</option>
          <option>Mild</option>
          <option>Severe</option>
        </select>

        <label>Scalp Hair Loss</label>
        <select name="scalpHairLoss" value={formData.scalpHairLoss} onChange={handleChange}>
          <option value={0}>No</option>
          <option value={1}>Yes</option>
        </select>

        <label>Infertility</label>
        <select name="infertility" value={formData.infertility} onChange={handleChange}>
          <option value={0}>No</option>
          <option value={1}>Yes</option>
        </select>

        <label>Dark Skin Patches</label>
        <select name="darkSkinPatches" value={formData.darkSkinPatches} onChange={handleChange}>
          <option value={0}>No</option>
          <option value={1}>Yes</option>
        </select>

        <button type="submit">Submit</button>
      </form>

      {result && <div className="result">{result}</div>}
    </div>
  );
}

export default App;
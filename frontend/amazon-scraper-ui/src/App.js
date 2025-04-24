import React, { useState, useEffect } from 'react';
import ProductTable from './components/ProductTable';
import './App.css';

const queries = [
  "wireless_headphones",
  "gaming_laptops",
  "smartphones_under_50000",
  "4K_LED_TVs",
  "bluetooth_speakers",
  "smart_watches_for_men",
  "dslr_cameras",
  "portable_hard_drives",
  "home_theater_systems",
  "tablet_for_students"
];

function App() {
  const [selectedQuery, setSelectedQuery] = useState(queries[0]);
  const [data, setData] = useState([]);

  useEffect(() => {
    import(`./data/${selectedQuery}.json`)
      .then((res) => setData(res.default))
      .catch((err) => console.error("Failed to load JSON:", err));
  }, [selectedQuery]);

  return (
    <div className="App">
      <h2>Amazon Scraper Results</h2>
      <select onChange={(e) => setSelectedQuery(e.target.value)} value={selectedQuery}>
        {queries.map((q, idx) => (
          <option key={idx} value={q}>{q.replaceAll("_", " ")}</option>
        ))}
      </select>
      <ProductTable data={data} />
    </div>
  );
}

export default App;

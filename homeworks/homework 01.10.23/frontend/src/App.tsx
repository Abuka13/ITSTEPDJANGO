import React from 'react';
import axios from "axios";
function App() {
  async function getData() {
    const response =  await axios.get("http://127.0.0.1:8000/api/")
    console.log("response:", response.data)
  }
  return (
    <div className="App">
      <header className="App-header">
        <button className={"btn btn-lg btn-outline-danger"} onClick={getData}>getData</button>
      </header>
    </div>
  );
}

export default App;

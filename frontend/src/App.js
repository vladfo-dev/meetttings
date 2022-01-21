import React from 'react';
import { ShowData } from './Components/ShowData';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <ShowData url="http://127.0.0.1:8000/api/ready" />
        <ShowData url='https://jsonplaceholder.typicode.com/posts/' method='POST' body={{id: 32}} />
      </header>
    </div>
  );
}

export default App;
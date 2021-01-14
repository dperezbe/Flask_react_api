import React from 'react';
import axios from 'axios';

function App() {

  const get_information = async () => {
    const url = '/api';
    const resultado = await axios.get(url);
    console.log(resultado.data)

  }

  get_information()

  return (
      <h1>Hola</h1>
  );
}

export default App;

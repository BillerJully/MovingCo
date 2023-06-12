import React, {useState} from 'react';


function App() {
  const [buttonclicks, setCount] = useState(0);
  function plus() {
    setCount(buttonclicks + 1)
    console.log(buttonclicks);
  }
  function minus() {
    setCount(buttonclicks - 1)
    console.log(buttonclicks);
  }
  return (
    <div className="App">
     <button onClick={plus}>Plus</button>
     <h1>{buttonclicks}</h1>
     <button onClick={minus}>Minus</button>
    </div>
  );
}

export default App;

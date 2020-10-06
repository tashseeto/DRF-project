import React from 'react';
import './App.css';

function App() {
  const [message, SetMessage] = React.useState("Javascript is so cool.");

  function handleClick() {
    SetMessage("my new message");
  }

  return (
    <div>
    <h1>{message}</h1>
    <button onClick={handleClick}>Update the message!</button>
    </div>
  );
}
export default App;

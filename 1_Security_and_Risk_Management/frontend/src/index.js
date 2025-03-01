import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';  // Optional, if you have custom styles
import App from './App';  // Your main React component
import reportWebVitals from './reportWebVitals';  // Optional, for performance metrics

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
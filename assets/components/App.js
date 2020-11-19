import React, { Component } from "react";
import HomePage from './HomePage';

class App extends Component {
    constructor(props) {
      super(props);
    }
  
    render() {
      return (
       <div className="container">
          <HomePage />
       </div>
      );
    }
}
  
export default App;
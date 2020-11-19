import React, { Component } from "react";
import HomePage from './HomePage';
import Library from './Library';

class App extends Component {
    constructor(props) {
      super(props);
    }
  
    render() {
      return (
       <div className="container">
          <HomePage />
          <Library />
       </div>
      );
    }
}
  
export default App;
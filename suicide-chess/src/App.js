import React, { Component } from 'react'
import Gamescene from './Gamescene/Gamescene'
import './App.css'

class App extends Component {
  render() {
    return (
      <div className="App">
        <h1>Suicide Chess</h1>
        <Gamescene roomID={this.props.roomID}/>
      </div>
    );
  }
}

export default App;

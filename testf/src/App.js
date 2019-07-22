import React, { Component } from 'react';
import io from 'socket.io-client'
const socket   = io.connect('http://localhost:5000')
class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      username:''
    }
  }

  setSocketListeners(){
    socket.on('test', (data)=>{
      console.log(data)
    })
  }
  componentDidMount(){
    this.setSocketListeners();
  }
  render() {
    return (
      <div className="App">
      <div>{this.state['username']}</div>
      </div>
    );
  }
}

export default App;

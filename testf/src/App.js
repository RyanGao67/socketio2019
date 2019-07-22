import React, { Component } from 'react';
import io from 'socket.io-client'
const socket   = io.connect('http://localhost:5000/test')
const socket2 = io.connect('http://localhost:5000/chat')
class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      username:''
    };
  }

  setSocketListeners = ()=>{
    console.log('locate me socket');
    socket.on('connect', ()=>{
      socket.emit('my event', {data:'I\'m connected!'})
    })
    socket2.on('my response', (data)=>{
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

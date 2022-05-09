import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

class Square extends React.Component {
  constructor(props){
    super(props);
    const isMine = Math.random() * 10 % 2
    if(isMine === 1){
      isMine = true
    }
    else {
      isMine = false
    }
    this.state = {
      isMine:isMine,
    }
  }
  render(){
    return (<button className='square' onClick={() => this.setState()}>

    </button>)
  }  
}

class Game extends React.Component {
  renderSquare(i){
    return <Square />
  }
  render(){
    return (
      <div className='Board'>
        <div className='boardRow'>
        {this.renderSquare(1)}
        {this.renderSquare(2)}
        {this.renderSquare(3)}
        </div>
        <div>
        {this.renderSquare(4)}
        {this.renderSquare(5)}
        {this.renderSquare(6)}
        </div>
        <div>
        {this.renderSquare(7)}
        {this.renderSquare(8)}
        {this.renderSquare(9)}
        </div>
      </div>
      )
  }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Game />);

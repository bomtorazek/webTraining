import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';

let style1 = {color : 'black', fontSize : '30px'};

function importAll(r) {
  let images = {};
  r.keys().map((item, index) => { images[item.replace('./', '')] = r(item); });
  return images;
}

function App() {
  const [imgInfo, setImgInfo] = useState([]) //  name, lbl from backend
  const [imgIdx, setImgIdx] = useState(0) // idx of frontend
  const [label, setLabel] = useState(0) // lbl of frontend
  const images = importAll(require.context('./catdog', false, /\.(png|jpe?g|svg)$/)) // pre-required images
  const length = Object.keys(images).length
  const label_dict = {0: "Cat", 1: "Dog"}
  const left = '<';
  const right = '>';

  useEffect(() => {
    axios.get(`http://localhost:8000/api/gt/${imgIdx}`)
      .then(res => {
        setImgInfo(res.data)
        setLabel(res.data[1])
      })
  }); // useEffect

  function setpostLabel(lbl){
    axios.post(`http://localhost:8000/api/gt/${imgIdx}/${lbl}`)
    .then(res => console.log(res))
    setLabel(lbl); 
    // should be lbl, not label, setLabel had better come later 
  }

  const exportLabel = () => {
    axios.put(`http://localhost:8000/api/gt`)
      .then(res => console.log(res))
  }

  console.log(imgIdx)
  return (
    <div className="App">
      <div className='table'>
        <div className='table-cell title left-justified' style={ style1 }>Labeling Tool</div>
        <button className='table-cell right-justified' onClick={ exportLabel} > Export </button>
      </div>
      <hr/>

      <div className='portrait'>
        <img src= { images[imgInfo[0]] } alt="cat or dog"/>
      </div>
      <hr/>

      <div> {imgInfo[0]} ({imgIdx+1}/{length}) </div>

      <button onClick={ () => setImgIdx((((imgIdx-1)%length)+length)%length) }> {left} </button>
      <button onClick={ () => setImgIdx((((imgIdx+1)%length)+length)%length) }> {right} </button>
      <hr/>

      <button onClick={ () => setpostLabel(0) }> Cat </button>
      <button onClick={ () => setpostLabel(1) }> Dog </button>
      <div> Label: {label_dict[label]} </div>
      <hr/>

    </div>
  );
}


export default App;

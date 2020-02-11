import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import CssBaseline from '@material-ui/core/CssBaseline';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';



function App() {
  return (
    <div className="App">
      <div className="fadeout" style={{ height: 200, textAlign: "center", width: "100%"}}>
        <h1 style={{paddingTop: 30, margin: 0, fontFamily: "Avenir Next", fontSize: 44, color: "white"}}> Hi, Sydney</h1>
        <h1 style={{paddingTop: 5, margin: 0, fontFamily: "FiraFlott", fontSize: 14, color: "black"}}> Tracking provided by Spé</h1>
        <div style={{marginTop: 20, marginLeft: 100, marginRight: 100}}>
          <div style={{float: "left", height: "60px", backgroundColor: "#9DBAC9", width: "300px"}}>
            <h1 style={{paddingTop: 5, margin: 0, fontFamily: "Avenir Next", fontSize: 14, color: "white"}}> Est. Date til Next Checkpoint</h1>
            <h1 style={{paddingTop: 3, margin: 0, fontFamily: "Arial Black", fontSize: 22, fontWeight: "bold", color: "white"}}> 21 NOVEMBER</h1>
          </div>
          <div style={{float: "right", height: "60px", backgroundColor: "#9DBAC9", width: "300px"}}>
            <h1 style={{paddingTop: 5, margin: 0, fontFamily: "Avenir Next", fontSize: 14, color: "white"}}> Token Credential</h1>
            <h1 style={{paddingTop: 3, margin: 0, fontFamily: "Arial Black", fontSize: 22, fontWeight: "bold", color: "white"}}> NL23094434</h1>
          </div>
        </div> 
      </div>
      <div className="timeline">
        <div className="container left">
          <div className="content">
            <h2>21/11/2015</h2>
            <p>Formal Discussion with Ad Board Representative </p>
          </div>
        </div>
        <div className="container right">
          <div className="content">
            <h2>04/11/2015</h2>
            <p>Opening of Formal Complaint</p>
          </div>
        </div>
        <div className="container left">
          <div className="content">
            <h2>03/11/2015</h2>
            <p>Verification of Allegation</p>
          </div>
        </div>
      </div>
    </div>
    
  );
}

export default App;

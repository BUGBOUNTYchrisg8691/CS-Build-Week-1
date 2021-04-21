import React from "react";
import { hot } from "react-hot-loader";

import { BoardSizeSelector } from "../Utils";
import { Board } from "../Board";

import "./App.css";

const App = () => {
  const [boardSize, setBoardSize] = React.useState(50);

  const handleChangeSize = (e) => {
    const { value } = e.target;
    setBoardSize(value);
  };

  const handleCellClick = (e, setter, value) => {
    setter(!value);
  };

  return (
    <div className="App">
      <h1>Conway's Game of Life</h1>
      <BoardSizeSelector
        boardSize={boardSize}
        handleChangeSize={handleChangeSize}
      />
      <Board boardSize={boardSize} handleCellClick={handleCellClick} />
    </div>
  );
};

export default hot(module)(App);

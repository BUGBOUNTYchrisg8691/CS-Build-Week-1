import React from "react";
import { hot } from "react-hot-loader";

import { BoardSizeSelector, PlayPauseButton, ResetButton } from "../Utils";
import { Board } from "../Board";

import "./App.css";

const App = () => {
  const [boardSize, setBoardSize] = React.useState(50);
  const [play, setPlay] = React.useState(false);

  const handleChangeSize = (e) => {
    const { value } = e.target;
    setBoardSize(value);
  };

  const handleCellClick = (setter, value) => {
    setter(!value);
  };

  const handleReset = () => {
    setBoardPattern(null);
  };

  return (
    <div className="App">
      <h1>Conway's Game of Life</h1>
      <div className="controls">
        <BoardSizeSelector
          boardSize={boardSize}
          handleChangeSize={handleChangeSize}
        />
        <PlayPauseButton play={play} setPlay={setPlay} />
        <ResetButton handleReset={handleReset} />
      </div>
      <Board boardSize={boardSize} handleCellClick={handleCellClick} />
    </div>
  );
};

export default hot(module)(App);

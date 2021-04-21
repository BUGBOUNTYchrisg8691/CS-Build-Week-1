import React from "react";
import { hot } from "react-hot-loader";

import { Cell } from "../Cell";

import "./Board.css";

const Board = (props) => {
  const { boardSize, handleCellClick } = props;

  const style = {
    border: "3px solid darkblue",
    margin: "0",
    display: "grid",
    width: "100%",
    gridTemplate: `repeat(${boardSize}, 1fr) / repeat(${boardSize}, 1fr)`,
  };

  return (
    <div className="board-container">
      <div className="board" style={style}>
        {Array(boardSize * boardSize)
          .fill(0)
          .map((_, i) => (
            <Cell value={false} handleCellClick={handleCellClick} />
          ))}
      </div>
    </div>
  );
};

export default hot(module)(Board);

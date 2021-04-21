import React from "react";
import { hot } from "react-hot-loader";

import { Cell } from "../Cell";

import "./Board.css";

const Board = (props) => {
  const { boardSize } = props;

  const style = {
    border: "2px solid darkblue",
    width: "inherit",
    height: "inherit",
    margin: "0 auto",
    display: "grid",
    gridTemplate: `repeat(${boardSize}, 1fr) / repeat(${boardSize}, 1fr)`,
  };

  return (
    <div className="board-container">
      <div className="board" style={style}>
        {Array(boardSize * boardSize)
          .fill(0)
          .map((_, i) => (
            <Cell value={i} handleCellClick={(e) => console.log(e)} />
          ))}
      </div>
    </div>
  );
};

export default hot(module)(Board);
